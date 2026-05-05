from pathlib import Path
from typing import List, Dict
from jinja2 import Environment, FileSystemLoader, select_autoescape
from .models import (
    Pattern, Program, Instance, AnonymousInstance, Block, ListLiteral, Identifier,
    CallInstruction, AssignInstruction, ReturnInstruction, RawInstruction
)

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

    def render_pattern(self, pattern: Pattern) -> str:
        template = self.env.get_template('pattern.rst.j2')
        return template.render(pattern=pattern)

    def render_instance_table(self, pattern: Pattern, instances: List[Instance]) -> str:
        template = self.env.get_template('instance_table.rst.j2')
        return template.render(pattern=pattern, instances=instances)

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
