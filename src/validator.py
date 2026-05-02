from typing import List, Set, Any
from .models import (
    Program, Instance, AnonymousInstance, Assignment, Block,
    Instruction, AssignInstruction, ReturnInstruction, CallInstruction,
    ListLiteral
)

class ValidationError(Exception):
    """Exception raised for errors in ASG validation."""
    pass

class Validator:
    """Validates the Abstract Semantic Graph (ASG) for semantic correctness."""

    def __init__(self):
        self.errors: List[str] = []
        self.pattern_names: Set[str] = set()

    def validate(self, program: Program):
        """
        Validates the entire program.

        Args:
            program: The Program ASG object to validate.

        Raises:
            ValidationError: If any validation errors are found.
        """
        self.errors = []
        self.pattern_names = {p.name for p in program.patterns}

        for instance in program.instances:
            self._validate_instance(instance)

        if self.errors:
            raise ValidationError("\n".join(self.errors))

    def _validate_instance(self, instance: AnonymousInstance):
        """Validates an instance or anonymous instance."""
        if instance.pattern_name not in self.pattern_names:
            name_part = f" '{instance.name}'" if isinstance(instance, Instance) else ""
            self.errors.append(f"Pattern '{instance.pattern_name}' not found for instance{name_part}.")

        for assignment in instance.assignments:
            self._validate_value(assignment.value)

    def _validate_value(self, value: Any):
        """Recursively validates values for nested instances."""
        if isinstance(value, AnonymousInstance):
            self._validate_instance(value)
        elif isinstance(value, ListLiteral):
            for element in value.elements:
                self._validate_value(element)
        elif isinstance(value, Block):
            for instruction in value.instructions:
                self._validate_instruction(instruction)

    def _validate_instruction(self, instruction: Instruction):
        """Validates instructions that might contain nested instances."""
        if isinstance(instruction, AssignInstruction):
            self._validate_value(instruction.value)
        elif isinstance(instruction, ReturnInstruction):
            self._validate_value(instruction.value)
        elif isinstance(instruction, CallInstruction):
            for arg in instruction.arguments:
                self._validate_value(arg)
