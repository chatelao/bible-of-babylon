import argparse
import sys
import os
from pathlib import Path
from antlr4 import CommonTokenStream, InputStream

# Add src/generated to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'generated')))

from SourcePatternsLexer import SourcePatternsLexer
from SourcePatternsParser import SourcePatternsParser
from .transformer import SourcePatternsTransformer
from .validator import Validator, ValidationError
from .generator import CodeGenerator

def main():
    parser = argparse.ArgumentParser(description="Transform Source Patterns DSL to reStructuredText.")
    parser.add_argument("input", help="Path to the input .patterns file")
    parser.add_argument("-o", "--output", help="Path to the output .rst file (defaults to stdout)")
    parser.add_argument("-t", "--title", help="Top-level title for the generated documentation")
    parser.add_argument("-p", "--pivot", help="Generate a pivot table for the specified language")
    parser.add_argument("-m", "--matrix", help="Generate a matrix table for the specified comma-separated languages")
    parser.add_argument("--csv", action="store_true", help="Output in CSV format (only for matrix)")

    args = parser.parse_args()

    input_path = Path(args.input)
    if not input_path.exists():
        print(f"Error: Input file '{args.input}' not found.", file=sys.stderr)
        sys.exit(1)

    content = input_path.read_text()

    # 1. Parsing
    input_stream = InputStream(content)
    lexer = SourcePatternsLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    sp_parser = SourcePatternsParser(token_stream)
    tree = sp_parser.program()

    # 2. Transformation
    transformer = SourcePatternsTransformer()
    program_asg = transformer.visit(tree)

    # 3. Validation
    validator = Validator()
    try:
        validator.validate(program_asg)
    except ValidationError as e:
        print(f"Validation Error:\n{e}", file=sys.stderr)
        sys.exit(1)

    # 4. Generation
    generator = CodeGenerator()
    if args.pivot:
        output_rst = generator.render_pivot_chapter(program_asg, args.pivot, title=args.title)
    elif args.matrix:
        langs = [l.strip() for l in args.matrix.split(",")]
        if args.csv:
            output_rst = generator.render_matrix_csv(program_asg, langs)
        else:
            output_rst = generator.render_matrix_chapter(program_asg, langs, title=args.title)
    else:
        output_rst = generator.render_program(program_asg, title=args.title)

    # 5. Output
    if args.output:
        output_path = Path(args.output)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(output_rst)
    else:
        print(output_rst)

if __name__ == "__main__":
    main()
