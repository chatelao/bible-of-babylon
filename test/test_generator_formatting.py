import pytest
from src.models import Program, Pattern, Instance, Parameter, Type, Assignment
from src.generator import CodeGenerator, format_table_cell

def test_format_table_cell_basic():
    assert format_table_cell("hello") == "hello"
    assert format_table_cell(42) == "42"

def test_format_table_cell_code():
    assert format_table_cell("hello", is_code=True) == "``hello``"
    assert format_table_cell(42, is_code=True) == "``42``"

def test_format_table_cell_multiline():
    val = "line 1\nline 2"
    expected = "| line 1\n| line 2"
    assert format_table_cell(val) == expected

def test_format_table_cell_multiline_code():
    val = "line 1\nline 2"
    expected = "| ``line 1``\n| ``line 2``"
    assert format_table_cell(val, is_code=True) == expected

def test_render_syntax_column_as_code():
    pattern = Pattern(
        name="TestPattern",
        parameters=[
            Parameter(name="syntax", type=Type(name="String")),
            Parameter(name="notes", type=Type(name="String"))
        ]
    )
    instances = [
        Instance(
            name="TestInstance",
            pattern_name="TestPattern",
            assignments=[
                Assignment(name="syntax", value="code_here"),
                Assignment(name="notes", value="some notes")
            ]
        )
    ]
    program = Program(patterns=[pattern], instances=instances)
    generator = CodeGenerator()
    output = generator.render_program(program)

    assert "  - ``code_here``" in output
    assert "  - some notes" in output

def test_render_multiline_syntax_column_as_code():
    pattern = Pattern(
        name="TestPattern",
        parameters=[
            Parameter(name="syntax", type=Type(name="String"))
        ]
    )
    instances = [
        Instance(
            name="TestInstance",
            pattern_name="TestPattern",
            assignments=[
                Assignment(name="syntax", value="line 1\nline 2")
            ]
        )
    ]
    program = Program(patterns=[pattern], instances=instances)
    generator = CodeGenerator()
    output = generator.render_program(program)

    assert "  - | ``line 1``" in output
    assert "    | ``line 2``" in output
