# Bible of Babylon

[![Documentation Status](https://readthedocs.org/projects/bible-of-babylon/badge/?version=latest)](https://bible-of-babylon.readthedocs.io/en/latest/?badge=latest)

Bible of Babylon is a comprehensive comparative guide designed for developers and data engineers. It provides structured comparisons of common patterns across various programming languages and data formats.

## 📖 Documentation

The full documentation, including detailed comparison tables for programming patterns and data formats, is hosted on Read the Docs:

- **Official Documentation**: [https://bible-of-babylon.readthedocs.io/](https://bible-of-babylon.readthedocs.io/)
- **Read the Docs Project Page**: [https://readthedocs.org/projects/bible-of-babylon/](https://readthedocs.org/projects/bible-of-babylon/)

## 🚀 Key Concepts

- **Polyglot Developer Onboarding**: Accelerating the transition between programming languages by comparing syntax and patterns.
- **Data Format Interoperability**: Understanding how data structures map across different formats like JSON, XML, YAML, and TOML.
- **Automated Refinement**: Using a pattern-driven transpilation pipeline to ensure consistency and maintainability.

## 📁 Project Structure

- `patterns/`: Domain-specific definitions of programming and data patterns using a custom DSL.
- `src/`: The transpiler engine (ANTLR4 and Jinja2) that generates documentation from patterns.
- `docs/`: Sphinx documentation source, including generated reStructuredText tables.
- `specifications/`: Formal specifications for the DSL and automated workflows.
- `test/`: Verification suite for grammar, transformation, and documentation consistency.

## 📜 License

This project is licensed under the GNU Affero General Public License v3.0 - see the [LICENSE](LICENSE) file for details.
