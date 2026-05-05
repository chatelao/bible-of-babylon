import pytest
from src.models import Program, Pattern, Instance, Parameter, Type, Assignment, AnonymousInstance, ListLiteral, Identifier
from src.generator import CodeGenerator

def test_render_nested_list_and_instance():
    pattern = Pattern(
        name="DataMap",
        parameters=[
            Parameter(name="syntax", type=Type(name="List", inner_type=Type(name="MapEntry")))
        ]
    )

    map_entry_pattern = Pattern(
        name="MapEntry",
        parameters=[
            Parameter(name="key", type=Type(name="String")),
            Parameter(name="value", type=Type(name="Expression"))
        ]
    )

    instances = [
        Instance(
            name="UserProfile",
            pattern_name="DataMap",
            assignments=[
                Assignment(
                    name="syntax",
                    value=ListLiteral(elements=[
                        AnonymousInstance(
                            pattern_name="MapEntry",
                            assignments=[
                                Assignment(name="key", value="id"),
                                Assignment(name="value", value=1)
                            ]
                        ),
                        AnonymousInstance(
                            pattern_name="MapEntry",
                            assignments=[
                                Assignment(name="key", value="active"),
                                Assignment(name="value", value=True)
                            ]
                        )
                    ])
                )
            ]
        )
    ]

    program = Program(patterns=[pattern, map_entry_pattern], instances=instances)
    generator = CodeGenerator()
    output = generator.render_program(program)

    assert "UserProfile" in output
    # Current output for AnonymousInstance is "instance of MapEntry"
    # Current output for ListLiteral is "[instance of MapEntry, instance of MapEntry]"
    assert "[MapEntry(key=id, value=1), MapEntry(key=active, value=True)]" in output
