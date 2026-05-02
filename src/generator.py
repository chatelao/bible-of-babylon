from pathlib import Path
from jinja2 import Environment, FileSystemLoader, select_autoescape
from .models import Pattern, Program

class CodeGenerator:
    def __init__(self, template_dir=None):
        if template_dir is None:
            template_dir = Path(__file__).parent / 'templates'

        self.env = Environment(
            loader=FileSystemLoader(str(template_dir)),
            autoescape=select_autoescape()
        )

    def render_pattern(self, pattern: Pattern) -> str:
        template = self.env.get_template('pattern.rst.j2')
        return template.render(pattern=pattern)

    def render_program(self, program: Program) -> str:
        # For now, just render patterns
        results = []
        for pattern in program.patterns:
            results.append(self.render_pattern(pattern))
        return "\n\n".join(results)
