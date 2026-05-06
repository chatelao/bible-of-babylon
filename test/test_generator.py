import pytest
from src.models import Program, Pattern, Instance, Parameter, Type, Assignment
from src.generator import CodeGenerator

def test_render_pattern_only():
    pattern = Pattern(
        name="VarDec",
        parameters=[
            Parameter(name="name", type=Type(name="Identifier")),
            Parameter(name="type", type=Type(name="Type"))
        ]
    )
    program = Program(patterns=[pattern], instances=[])
    generator = CodeGenerator()
    output = generator.render_program(program)

    assert "VarDec" in output
    assert "------" in output
    assert "* name: Identifier" in output
    assert "* type: Type" in output

def test_render_program_with_title():
    pattern = Pattern(
        name="VarDec",
        parameters=[
            Parameter(name="name", type=Type(name="Identifier"))
        ]
    )
    program = Program(patterns=[pattern], instances=[])
    generator = CodeGenerator()
    output = generator.render_program(program, title="My Title")

    assert "My Title" in output
    assert "========" in output
    assert "VarDec" in output
    assert "------" in output

def test_render_instance_table():
    pattern = Pattern(
        name="VarDec",
        parameters=[
            Parameter(name="name", type=Type(name="Identifier")),
            Parameter(name="value", type=Type(name="Expression")),
            Parameter(name="syntax", type=Type(name="String"))
        ]
    )
    instances = [
        Instance(
            name="Python",
            pattern_name="VarDec",
            assignments=[
                Assignment(name="name", value="x"),
                Assignment(name="value", value=42),
                Assignment(name="syntax", value="x = 42")
            ]
        ),
        Instance(
            name="Java",
            pattern_name="VarDec",
            assignments=[
                Assignment(name="name", value="y"),
                Assignment(name="value", value=100)
            ]
        )
    ]
    program = Program(patterns=[pattern], instances=instances)
    generator = CodeGenerator()
    output = generator.render_program(program)

    assert ".. list-table:: VarDec Comparison" in output
    assert "* - Language" in output
    assert "  - Syntax" in output
    assert "* - Python" in output
    assert "  - ::\n\n           x = 42" in output
    assert "* - Java" in output
    assert "  - N/A" in output

    # These should NOT be in the table anymore
    assert "  - name" not in output
    assert "  - value" not in output
