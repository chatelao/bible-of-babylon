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

    assert "Pattern: VarDec" in output
    assert "* name: Identifier" in output
    assert "* type: Type" in output

def test_render_instance_table():
    pattern = Pattern(
        name="VarDec",
        parameters=[
            Parameter(name="name", type=Type(name="Identifier")),
            Parameter(name="value", type=Type(name="Expression"))
        ]
    )
    instances = [
        Instance(
            name="Python",
            pattern_name="VarDec",
            assignments=[
                Assignment(name="name", value="x"),
                Assignment(name="value", value=42)
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
    assert "* - Instance" in output
    assert "  - name" in output
    assert "  - value" in output
    assert "* - Python" in output
    assert "  - x" in output
    assert "  - 42" in output
    assert "* - Java" in output
    assert "  - y" in output
    assert "  - 100" in output
