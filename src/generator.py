from pathlib import Path
from typing import List, Dict, Any
from jinja2 import Environment, FileSystemLoader, select_autoescape
from .models import (
    Pattern, Program, Instance, AnonymousInstance, Block, ListLiteral, Identifier,
    CallInstruction, AssignInstruction, ReturnInstruction, RawInstruction
)

def format_table_cell(value: Any, is_code: bool = False) -> str:
    str_value = str(value)
    if str_value != "N/A":
        str_value = str_value.rstrip()

    if is_code and str_value != "N/A":
        if "\n" in str_value:
            return "::\n" + "\n".join(f"    {line}" for line in str_value.splitlines())
        return f"``{str_value}``"

    if isinstance(value, str) and "\n" in str_value:
        lines = str_value.splitlines()
        return "\n".join(f"| {line}" if line.strip() else "|" for line in lines)
    return str_value

def format_value(value) -> str:
    if isinstance(value, str):
        return value
    if isinstance(value, (int, float)):
        return str(value)
    if isinstance(value, Identifier):
        return value.name
    if isinstance(value, ListLiteral):
        elements = [format_value(e) for e in value.elements]
        return f"[{', '.join(elements)}]"
    if isinstance(value, AnonymousInstance):
        assignments = [f"{a.name}={format_value(a.value)}" for a in value.assignments]
        return f"{value.pattern_name}({', '.join(assignments)})"
    if isinstance(value, Block):
        instructions = [format_value(i) for i in value.instructions]
        return f"{{ {'; '.join(instructions)} }}"
    if isinstance(value, CallInstruction):
        args = [format_value(a) for a in value.arguments]
        return f"call {value.name}({', '.join(args)})"
    if isinstance(value, AssignInstruction):
        return f"assign {value.target} = {format_value(value.value)}"
    if isinstance(value, ReturnInstruction):
        return f"return {format_value(value.value)}"
    if isinstance(value, RawInstruction):
        return f'raw "{value.snippet}"'
    return str(value)

class CodeGenerator:
    def __init__(self, template_dir=None):
        if template_dir is None:
            template_dir = Path(__file__).parent / 'templates'

        self.env = Environment(
            loader=FileSystemLoader(str(template_dir)),
            autoescape=select_autoescape()
        )
        self.env.filters['format_value'] = format_value
        self.env.filters['format_table_cell'] = format_table_cell

    def render_pattern(self, pattern: Pattern) -> str:
        template = self.env.get_template('pattern.rst.j2')
        return template.render(pattern=pattern)

    def render_instance_table(self, pattern: Pattern, instances: List[Instance]) -> str:
        syntax_params = {"syntax", "single_line", "multi_line", "string_val", "number_val", "boolean_val"}

        display_parameters = [p for p in pattern.parameters if p.name in syntax_params]
        notes_param = next((p for p in pattern.parameters if p.name == "notes"), None)
        if notes_param:
            display_parameters.append(notes_param)

        template = self.env.get_template('instance_table.rst.j2')
        return template.render(
            pattern=pattern,
            instances=instances,
            display_parameters=display_parameters
        )

    def render_program(self, program: Program, title: str = None) -> str:
        results = []

        if title:
            results.append(f"{title}\n{'=' * len(title)}")

        # Map pattern name to pattern object
        patterns_map = {p.name: p for p in program.patterns}

        # Group instances by pattern
        instances_by_pattern: Dict[str, List[Instance]] = {}
        for instance in program.instances:
            if instance.pattern_name not in instances_by_pattern:
                instances_by_pattern[instance.pattern_name] = []
            instances_by_pattern[instance.pattern_name].append(instance)

        # Render each pattern and its instances
        for pattern_name, pattern in patterns_map.items():
            results.append(self.render_pattern(pattern))

            if pattern_name in instances_by_pattern:
                results.append(self.render_instance_table(pattern, instances_by_pattern[pattern_name]))

        return "\n\n".join(results)

    def render_pivot_table(self, program: Program, language: str) -> str:
        syntax_params = ["syntax", "multi_line", "string_val", "number_val", "boolean_val", "notes"]

        # List of all known languages from DESIGN.md to avoid prefix collisions (e.g., C vs CSS)
        all_languages = [
            "SQL", "C", "XQuery", "Java", "Rust", "Erlang", "Lisp", "Bash", "Cmd",
            "PowerShell", "Python", "CSS", "CUDA", "x86 Assembler"
        ]

        pivot_data = []
        for instance in program.instances:
            # First, check if any OTHER language matches the instance name better
            other_matches = [lang for lang in all_languages if lang.lower() != language.lower()
                             and instance.name.lower().startswith(lang.lower())]

            # If the requested language matches the prefix
            if instance.name.lower().startswith(language.lower()):
                # Ensure no OTHER language is a longer (better) match
                is_best_match = True
                for other in other_matches:
                    if len(other) > len(language):
                        is_best_match = False
                        break

                if not is_best_match:
                    continue

                assignments = {a.name: a.value for a in instance.assignments}

                # Merge single_line into syntax if syntax is missing or N/A
                if assignments.get("syntax", "N/A") == "N/A" and "single_line" in assignments:
                    assignments["syntax"] = assignments["single_line"]

                pivot_data.append({
                    "pattern_name": instance.pattern_name,
                    "assignments": assignments
                })

        if not pivot_data:
            return f"No data found for language: {language}"

        template = self.env.get_template('pivot_table.rst.j2')
        return template.render(
            language=language,
            display_parameters=syntax_params,
            pivot_data=pivot_data
        )

    def render_pivot_chapter(self, program: Program, language: str, title: str = None) -> str:
        results = []
        if not title:
            title = f"{language} Pivot View"

        results.append(f"{title}\n{'=' * len(title)}")
        results.append(self.render_pivot_table(program, language))

        return "\n\n".join(results)
