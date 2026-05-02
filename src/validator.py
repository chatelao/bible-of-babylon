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
        self.patterns = {}

    def validate(self, program: Program):
        """
        Validates the entire program.

        Args:
            program: The Program ASG object to validate.

        Raises:
            ValidationError: If any validation errors are found.
        """
        self.errors = []
        self.patterns = {p.name: p for p in program.patterns}

        for instance in program.instances:
            self._validate_instance(instance)

        if self.errors:
            raise ValidationError("\n".join(self.errors))

    def _validate_instance(self, instance: AnonymousInstance):
        """Validates an instance or anonymous instance."""
        pattern = self.patterns.get(instance.pattern_name)
        name_part = f" '{instance.name}'" if isinstance(instance, Instance) else ""

        if not pattern:
            self.errors.append(f"Pattern '{instance.pattern_name}' not found for instance{name_part}.")
        else:
            # Validate mandatory parameter assignment
            assigned_names = {a.name for a in instance.assignments}
            for param in pattern.parameters:
                if param.name not in assigned_names:
                    self.errors.append(
                        f"Missing mandatory parameter '{param.name}' for instance{name_part} of pattern '{pattern.name}'."
                    )

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
