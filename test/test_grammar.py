import pytest
from antlr4 import CommonTokenStream, InputStream, DiagnosticErrorListener
from antlr4.error.ErrorListener import ErrorListener
import sys
import os

# Add src/generated/src to sys.path to import the generated parser
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src', 'generated', 'src')))

from SourcePatternsLexer import SourcePatternsLexer
from SourcePatternsParser import SourcePatternsParser

class ExceptionErrorListener(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        raise Exception(f"Syntax error at line {line}, column {column}: {msg}")

def parse_snippet(snippet):
    input_stream = InputStream(snippet)
    lexer = SourcePatternsLexer(input_stream)
    # Remove default console error listeners
    lexer.removeErrorListeners()
    lexer.addErrorListener(ExceptionErrorListener())

    token_stream = CommonTokenStream(lexer)
    parser = SourcePatternsParser(token_stream)
    parser.removeErrorListeners()
    parser.addErrorListener(ExceptionErrorListener())

    return parser.program()

@pytest.mark.parametrize("snippet", [
    # Control Flow (If/Else)
    r"""
    pattern IfElse {
        parameter condition: Expression
        parameter then_branch: Block
        parameter else_branch: Block
    }

    instance CheckBalance of IfElse {
        condition = "balance > 100"
        then_branch = {
            call charge_fee(0)
        }
        else_branch = {
            call charge_fee(10)
        }
    }
    """,
    # Concurrency (Message Passing)
    r"""
    pattern MessageSend {
        parameter target: Identifier
        parameter payload: Expression
    }

    instance NotifyUser of MessageSend {
        target = "user_service"
        payload = "registration_complete"
    }
    """,
    # Nested Data Structures (Object/Map)
    r"""
    pattern DataMap {
        parameter entries: List<MapEntry>
    }

    pattern MapEntry {
        parameter key: String
        parameter value: Expression
    }

    instance UserProfile of DataMap {
        entries = [
            instance of MapEntry { key = "id", value = 1 },
            instance of MapEntry { key = "active", value = true }
        ]
    }
    """,
    # Metadata support
    r"""
    pattern VariableDeclaration {
        meta description: "Declares a variable."
        parameter name: Identifier
        parameter type: Type
        parameter initial_value: Expression
    }
    """,
    # Instructions in blocks
    r"""
    instance ComplexBlock of Something {
        body = {
            assign x = 5
            call print(x)
            return x
            raw "printf(\"done\");"
        }
    }
    """
])
def test_valid_snippets(snippet):
    try:
        parse_snippet(snippet)
    except Exception as e:
        pytest.fail(f"Parser failed on valid snippet: {e}")

@pytest.mark.parametrize("snippet", [
    # Missing pattern name
    "pattern { }",
    # Missing of keyword in instance
    "instance MyInstance MyPattern { }",
    # Invalid keyword
    "notakeyword X { }",
    # Malformed block
    "instance X of Y { body = { call missing_paren } }",
])
def test_invalid_snippets(snippet):
    with pytest.raises(Exception):
        parse_snippet(snippet)
