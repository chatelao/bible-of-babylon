from src.models import Program, Instance, Assignment, Pattern, Parameter, Type
from src.generator import CodeGenerator

def test_render_pivot_table():
    pattern = Pattern(name="Var", parameters=[Parameter(name="syntax", type=Type(name="String"))])
    instance = Instance(name="SQLVar", pattern_name="Var", assignments=[Assignment(name="syntax", value="DECLARE @x")])
    program = Program(patterns=[pattern], instances=[instance])

    generator = CodeGenerator()
    output = generator.render_pivot_table(program, "SQL")

    assert "SQL Pivot Table" in output
    assert "Var" in output
    assert "DECLARE @x" in output

def test_render_pivot_chapter():
    pattern = Pattern(name="Var", parameters=[Parameter(name="syntax", type=Type(name="String"))])
    instance = Instance(name="SQLVar", pattern_name="Var", assignments=[Assignment(name="syntax", value="DECLARE @x")])
    program = Program(patterns=[pattern], instances=[instance])

    generator = CodeGenerator()
    output = generator.render_pivot_chapter(program, "SQL", title="My Title")

    assert "My Title" in output
    assert "SQL Pivot Table" in output

def test_pivot_collision_filtering():
    pattern = Pattern(name="Var", parameters=[Parameter(name="syntax", type=Type(name="String"))])
    # CSSVar starts with C, but CSS is a longer match
    c_instance = Instance(name="CVar", pattern_name="Var", assignments=[Assignment(name="syntax", value="int x")])
    css_instance = Instance(name="CSSVar", pattern_name="Var", assignments=[Assignment(name="syntax", value="--x")])
    program = Program(patterns=[pattern], instances=[c_instance, css_instance])

    generator = CodeGenerator()

    # Requesting "C" should ONLY give CVar, not CSSVar
    c_output = generator.render_pivot_table(program, "C")
    assert "int x" in c_output
    assert "--x" not in c_output

    # Requesting "CSS" should ONLY give CSSVar
    css_output = generator.render_pivot_table(program, "CSS")
    assert "--x" in css_output
    assert "int x" not in css_output
