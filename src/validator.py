from typing import List, Set, Any
from .models import (
    Program, Instance, AnonymousInstance, Assignment, Block,
    Instruction, AssignInstruction, ReturnInstruction, CallInstruction,
    ListLiteral, Type
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
        full_name = f"instance{name_part}"

        if not pattern:
            self.errors.append(f"Pattern '{instance.pattern_name}' not found for {full_name}.")
        else:
            params_by_name = {p.name: p for p in pattern.parameters}
            assigned_names = {a.name for a in instance.assignments}

            # Check for unknown parameters and type consistency
            for assignment in instance.assignments:
                if assignment.name not in params_by_name:
                    self.errors.append(f"Unknown parameter '{assignment.name}' for {full_name} of pattern '{pattern.name}'.")
                else:
                    param = params_by_name[assignment.name]
                    self._check_type(assignment.value, param.type, full_name, assignment.name)

            # Validate mandatory parameter assignment
            for param in pattern.parameters:
                if param.name not in assigned_names:
                    self.errors.append(
                        f"Missing mandatory parameter '{param.name}' for {full_name} of pattern '{pattern.name}'."
                    )

        for assignment in instance.assignments:
            self._validate_value(assignment.value)

    def _check_type(self, value: Any, expected_type: Type, context: str, param_name: str, in_list: bool = False):
        """Checks if a value matches the expected type."""
        location = "in list for " if in_list else "for "

        if expected_type.name == "String":
            if not isinstance(value, str):
                self.errors.append(f"Type mismatch {location}parameter '{param_name}' in {context}. Expected 'String', got '{type(value).__name__}'.")
        elif expected_type.name == "Number":
            if not isinstance(value, (int, float)):
                self.errors.append(f"Type mismatch {location}parameter '{param_name}' in {context}. Expected 'Number', got '{type(value).__name__}'.")
        elif expected_type.name == "List":
            if not isinstance(value, ListLiteral):
                self.errors.append(f"Type mismatch {location}parameter '{param_name}' in {context}. Expected 'List', got '{type(value).__name__}'.")
            elif expected_type.inner_type:
                for element in value.elements:
                    self._check_type(element, expected_type.inner_type, context, param_name, in_list=True)
        elif expected_type.name == "Block":
            if not isinstance(value, Block):
                self.errors.append(f"Type mismatch {location}parameter '{param_name}' in {context}. Expected 'Block', got '{type(value).__name__}'.")
        else:
            # Assume it's a pattern name
            if not isinstance(value, AnonymousInstance) or value.pattern_name != expected_type.name:
                actual = f"instance of '{value.pattern_name}'" if isinstance(value, AnonymousInstance) else type(value).__name__
                self.errors.append(f"Type mismatch {location}parameter '{param_name}' in {context}. Expected '{expected_type.name}', got {actual}.")

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
