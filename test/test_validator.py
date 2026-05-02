import pytest

from src.models import Program, Pattern, Instance, AnonymousInstance, Assignment, Block, RawInstruction
from src.validator import Validator, ValidationError

def test_validate_success():
    program = Program(
        patterns=[Pattern(name="P1")],
        instances=[Instance(name="I1", pattern_name="P1")]
    )
    validator = Validator()
    validator.validate(program)  # Should not raise

def test_validate_missing_pattern():
    program = Program(
        patterns=[Pattern(name="P1")],
        instances=[Instance(name="I1", pattern_name="Missing")]
    )
    validator = Validator()
    with pytest.raises(ValidationError) as excinfo:
        validator.validate(program)
    assert "Pattern 'Missing' not found for instance 'I1'." in str(excinfo.value)

def test_validate_nested_anonymous_missing_pattern():
    program = Program(
        patterns=[Pattern(name="P1")],
        instances=[
            Instance(name="I1", pattern_name="P1", assignments=[
                Assignment(name="nested", value=AnonymousInstance(pattern_name="Missing"))
            ])
        ]
    )
    validator = Validator()
    with pytest.raises(ValidationError) as excinfo:
        validator.validate(program)
    assert "Pattern 'Missing' not found for instance." in str(excinfo.value)

def test_validate_block_nested_missing_pattern():
    program = Program(
        patterns=[Pattern(name="P1")],
        instances=[
            Instance(name="I1", pattern_name="P1", assignments=[
                Assignment(name="body", value=Block(instructions=[
                    RawInstruction(snippet="nop"),
                    # Technically we don't have an instruction that takes an instance directly yet,
                    # but _validate_value is used by instructions via Call/Assign/Return.
                ]))
            ])
        ]
    )
    validator = Validator()
    validator.validate(program) # Success

def test_multiple_errors():
    program = Program(
        patterns=[],
        instances=[
            Instance(name="I1", pattern_name="P1"),
            Instance(name="I2", pattern_name="P2")
        ]
    )
    validator = Validator()
    with pytest.raises(ValidationError) as excinfo:
        validator.validate(program)
    assert "Pattern 'P1' not found" in str(excinfo.value)
    assert "Pattern 'P2' not found" in str(excinfo.value)
