import pytest
from src.models import (
    Program, Pattern, Instance, Metadata, Parameter, Type,
    Assignment, Block, CallInstruction, AssignInstruction,
    ReturnInstruction, RawInstruction, ListLiteral, AnonymousInstance
)

def test_pattern_creation():
    meta = Metadata(key="description", value="Test pattern")
    param = Parameter(name="var", type=Type(name="Identifier"))
    pattern = Pattern(name="TestPattern", metadata=[meta], parameters=[param])

    assert pattern.name == "TestPattern"
    assert len(pattern.metadata) == 1
    assert pattern.metadata[0].key == "description"
    assert len(pattern.parameters) == 1
    assert pattern.parameters[0].name == "var"

def test_instance_creation():
    assign = Assignment(name="x", value=42)
    instance = Instance(
        name="test_inst",
        pattern_name="TestPattern",
        assignments=[assign]
    )

    assert instance.name == "test_inst"
    assert instance.pattern_name == "TestPattern"
    assert len(instance.assignments) == 1
    assert instance.assignments[0].name == "x"
    assert instance.assignments[0].value == 42

def test_block_and_instructions():
    instructions = [
        AssignInstruction(target="x", value=10),
        CallInstruction(name="print", arguments=["x"]),
        ReturnInstruction(value="x"),
        RawInstruction(snippet="exit(0);")
    ]
    block = Block(instructions=instructions)

    assert len(block.instructions) == 4
    assert isinstance(block.instructions[0], AssignInstruction)
    assert isinstance(block.instructions[1], CallInstruction)
    assert isinstance(block.instructions[2], ReturnInstruction)
    assert isinstance(block.instructions[3], RawInstruction)

def test_nested_structures():
    # Test ListLiteral and AnonymousInstance
    anon = AnonymousInstance(
        pattern_name="MapEntry",
        assignments=[Assignment(name="key", value="id"), Assignment(name="value", value=1)]
    )
    list_lit = ListLiteral(elements=[anon])

    instance = Instance(
        name="UserProfile",
        pattern_name="DataMap",
        assignments=[Assignment(name="entries", value=list_lit)]
    )

    assert instance.name == "UserProfile"
    assert isinstance(instance.assignments[0].value, ListLiteral)
    assert isinstance(instance.assignments[0].value.elements[0], AnonymousInstance)
    assert instance.assignments[0].value.elements[0].pattern_name == "MapEntry"

def test_type_nesting():
    inner = Type(name="Integer")
    outer = Type(name="List", inner_type=inner)

    assert outer.name == "List"
    assert outer.inner_type.name == "Integer"
