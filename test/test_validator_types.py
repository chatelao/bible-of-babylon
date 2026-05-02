import pytest
from src.models import (
    Program, Pattern, Instance, AnonymousInstance, Assignment,
    Parameter, Type, ListLiteral, Identifier
)
from src.validator import Validator, ValidationError

def test_validate_unknown_parameter():
    program = Program(
        patterns=[Pattern(name="P1", parameters=[Parameter(name="p1", type=Type(name="String"))])],
        instances=[
            Instance(name="I1", pattern_name="P1", assignments=[
                Assignment(name="p1", value="val"),
                Assignment(name="unknown", value="val")
            ])
        ]
    )
    validator = Validator()
    with pytest.raises(ValidationError) as excinfo:
        validator.validate(program)
    assert "Unknown parameter 'unknown' for instance 'I1' of pattern 'P1'." in str(excinfo.value)

def test_validate_type_mismatch_basic():
    program = Program(
        patterns=[Pattern(name="P1", parameters=[Parameter(name="p1", type=Type(name="String"))])],
        instances=[
            Instance(name="I1", pattern_name="P1", assignments=[
                Assignment(name="p1", value=123)
            ])
        ]
    )
    validator = Validator()
    with pytest.raises(ValidationError) as excinfo:
        validator.validate(program)
    assert "Type mismatch for parameter 'p1' in instance 'I1'. Expected 'String', got 'int'." in str(excinfo.value)

def test_validate_type_mismatch_list():
    program = Program(
        patterns=[
            Pattern(name="P1", parameters=[
                Parameter(name="list_param", type=Type(name="List", inner_type=Type(name="String")))
            ])
        ],
        instances=[
            Instance(name="I1", pattern_name="P1", assignments=[
                Assignment(name="list_param", value=ListLiteral(elements=["a", 1, "c"]))
            ])
        ]
    )
    validator = Validator()
    with pytest.raises(ValidationError) as excinfo:
        validator.validate(program)
    assert "Type mismatch in list for parameter 'list_param' in instance 'I1'. Expected 'String', got 'int'." in str(excinfo.value)

def test_validate_type_mismatch_nested_instance():
    program = Program(
        patterns=[
            Pattern(name="Inner", parameters=[Parameter(name="ip", type=Type(name="String"))]),
            Pattern(name="Outer", parameters=[Parameter(name="op", type=Type(name="Inner"))])
        ],
        instances=[
            Instance(name="I1", pattern_name="Outer", assignments=[
                Assignment(name="op", value=AnonymousInstance(pattern_name="WrongPattern"))
            ])
        ]
    )
    validator = Validator()
    with pytest.raises(ValidationError) as excinfo:
        validator.validate(program)
    assert "Type mismatch for parameter 'op' in instance 'I1'. Expected 'Inner', got instance of 'WrongPattern'." in str(excinfo.value)

def test_validate_type_consistency_success():
    program = Program(
        patterns=[
            Pattern(name="Inner", parameters=[Parameter(name="ip", type=Type(name="String"))]),
            Pattern(name="Outer", parameters=[
                Parameter(name="p_str", type=Type(name="String")),
                Parameter(name="p_num", type=Type(name="Number")),
                Parameter(name="p_list", type=Type(name="List", inner_type=Type(name="Number"))),
                Parameter(name="p_inst", type=Type(name="Inner"))
            ])
        ],
        instances=[
            Instance(name="I1", pattern_name="Outer", assignments=[
                Assignment(name="p_str", value="hello"),
                Assignment(name="p_num", value=42.5),
                Assignment(name="p_list", value=ListLiteral(elements=[1, 2, 3])),
                Assignment(name="p_inst", value=AnonymousInstance(
                    pattern_name="Inner",
                    assignments=[Assignment(name="ip", value="inner_val")]
                ))
            ])
        ]
    )
    validator = Validator()
    validator.validate(program) # Should pass
