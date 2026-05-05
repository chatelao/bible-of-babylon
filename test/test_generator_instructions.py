import pytest
from src.models import (
    Program, Pattern, Instance, Parameter, Type, Assignment, Block,
    CallInstruction, AssignInstruction, ReturnInstruction, RawInstruction, Identifier
)
from src.generator import CodeGenerator

def test_render_instructions():
    pattern = Pattern(
        name="Function",
        parameters=[
            Parameter(name="syntax", type=Type(name="Block"))
        ]
    )

    instances = [
        Instance(
            name="MyFunc",
            pattern_name="Function",
            assignments=[
                Assignment(
                    name="syntax",
                    value=Block(instructions=[
                        CallInstruction(name="print", arguments=["hello"]),
                        AssignInstruction(target="x", value=10),
                        ReturnInstruction(value=Identifier(name="x")),
                        RawInstruction(snippet="exit(0);")
                    ])
                )
            ]
        )
    ]

    program = Program(patterns=[pattern], instances=instances)
    generator = CodeGenerator()
    output = generator.render_program(program)

    expected_body = "{ call print(hello); assign x = 10; return x; raw \"exit(0);\" }"
    assert expected_body in output

def test_render_nested_blocks():
    # Although the grammar currently doesn't explicitly support nested blocks
    # as first-class values in instructions (only in Value),
    # the ASG and generator can handle them if they appear in assignments.
    pattern = Pattern(
        name="ControlFlow",
        parameters=[
            Parameter(name="syntax", type=Type(name="Block"))
        ]
    )

    instances = [
        Instance(
            name="NestedTest",
            pattern_name="ControlFlow",
            assignments=[
                Assignment(
                    name="syntax",
                    value=Block(instructions=[
                        AssignInstruction(
                            target="inner",
                            value=Block(instructions=[
                                CallInstruction(name="log", arguments=["inner"])
                            ])
                        )
                    ])
                )
            ]
        )
    ]

    program = Program(patterns=[pattern], instances=instances)
    generator = CodeGenerator()
    output = generator.render_program(program)

    # Note: Identifier 'inner' in assign target doesn't use format_value yet in AssignInstruction
    # but the value does.
    expected_content = "{ assign inner = { call log(inner) } }"
    assert expected_content in output
