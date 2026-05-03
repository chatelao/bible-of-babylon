import pytest
from antlr4 import CommonTokenStream, InputStream
import sys
import os

# Add src and src/generated to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src', 'generated')))

from SourcePatternsLexer import SourcePatternsLexer
from SourcePatternsParser import SourcePatternsParser
from src.transformer import SourcePatternsTransformer
from src.models import Program, Pattern, Instance, AnonymousInstance, Metadata, Type, Parameter, Assignment, Identifier, Block, CallInstruction, ListLiteral

def transform_snippet(snippet):
    input_stream = InputStream(snippet)
    lexer = SourcePatternsLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = SourcePatternsParser(token_stream)
    tree = parser.program()

    transformer = SourcePatternsTransformer()
    return transformer.visit(tree)

def test_transform_metadata_and_params():
    snippet = """
    pattern VarDecl {
        meta description: "Variable"
        parameter name: Identifier
        parameter type: Type
    }
    """
    program = transform_snippet(snippet)
    assert len(program.patterns) == 1
    pattern = program.patterns[0]
    assert pattern.name == "VarDecl"
    assert len(pattern.metadata) == 1
    assert pattern.metadata[0].key == "description"
    assert pattern.metadata[0].value == "Variable"
    assert len(pattern.parameters) == 2
    assert pattern.parameters[0].name == "name"
    assert pattern.parameters[0].type.name == "Identifier"
    assert pattern.parameters[1].name == "type"
    assert pattern.parameters[1].type.name == "Type"

def test_transform_instance():
    snippet = """
    instance MyVar of VarDecl {
        name = "x"
        type = "int"
    }
    """
    program = transform_snippet(snippet)
    assert len(program.instances) == 1
    instance = program.instances[0]
    assert instance.name == "MyVar"
    assert instance.pattern_name == "VarDecl"
    assert len(instance.assignments) == 2
    assert instance.assignments[0].name == "name"
    assert instance.assignments[0].value == "x"
    assert instance.assignments[1].name == "type"
    assert instance.assignments[1].value == "int"

def test_transform_complex_values():
    snippet = """
    instance Complex of Data {
        list = [1, 2, "three"]
        nested = instance of Inner { key = "val" }
        id = some_id
    }
    """
    program = transform_snippet(snippet)
    instance = program.instances[0]

    # ListLiteral
    list_val = next(a.value for a in instance.assignments if a.name == "list")
    assert isinstance(list_val, ListLiteral)
    assert list_val.elements == [1, 2, "three"]

    # AnonymousInstance
    nested_val = next(a.value for a in instance.assignments if a.name == "nested")
    assert isinstance(nested_val, AnonymousInstance)
    assert nested_val.pattern_name == "Inner"
    assert nested_val.assignments[0].name == "key"
    assert nested_val.assignments[0].value == "val"

    # Identifier
    id_val = next(a.value for a in instance.assignments if a.name == "id")
    assert isinstance(id_val, Identifier)
    assert id_val.name == "some_id"

def test_transform_block():
    snippet = """
    instance MyFunc of Function {
        body = {
            call print("hello")
            assign x = 10
            return x
            raw "exit(0);"
        }
    }
    """
    program = transform_snippet(snippet)
    instance = program.instances[0]
    body = instance.assignments[0].value
    assert isinstance(body, Block)
    assert len(body.instructions) == 4
    assert isinstance(body.instructions[0], CallInstruction)
    assert body.instructions[0].name == "print"
    assert body.instructions[0].arguments == ["hello"]
    assert body.instructions[3].snippet == "exit(0);"

def test_list_type():
    snippet = """
    pattern P {
        parameter items: List<String>
    }
    """
    program = transform_snippet(snippet)
    param = program.patterns[0].parameters[0]
    assert param.type.name == "List"
    assert param.type.inner_type.name == "String"
