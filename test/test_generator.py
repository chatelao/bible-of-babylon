import pytest
from src.models import Pattern, Metadata, Parameter, Type
from src.generator import CodeGenerator

def test_render_pattern():
    pattern = Pattern(
        name="VarDecl",
        metadata=[Metadata(key="description", value="Variable")],
        parameters=[
            Parameter(name="name", type=Type(name="Identifier")),
            Parameter(name="type", type=Type(name="List", inner_type=Type(name="String")))
        ]
    )

    generator = CodeGenerator()
    output = generator.render_pattern(pattern)

    assert "Pattern: VarDecl" in output
    assert ":description: Variable" in output
    assert "* name: Identifier" in output
    assert "* type: List<String>" in output

def test_generator_initialization():
    generator = CodeGenerator()
    assert generator.env is not None
    assert "pattern.rst.j2" in generator.env.list_templates()
