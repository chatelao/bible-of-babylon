# Concept

## Business Cases

### BC 1: Language-Agnostic Pattern Reference
Provide a centralized resource for developers to quickly find equivalent syntax and patterns across various programming languages.

#### Use Case 1.1: Syntax Migration
A Java developer is transitioning to Rust and needs to understand how Java's `try-catch` blocks map to Rust's `Result` type and `match` patterns.

#### Use Case 1.2: Polyglot Education
A student learning functional programming wants to compare recursion and list manipulation patterns between Erlang and Lisp.

### BC 2: Data Format Interoperability
Enable architects and data engineers to make informed decisions about data storage and transmission formats by comparing their structures and constraints.

#### Use Case 2.1: Configuration Format Selection
A systems engineer is choosing between YAML and TOML for a new project's configuration and wants to compare their handling of nested structures and readability.

#### Use Case 2.2: Legacy Data Transformation
A developer needs to migrate a legacy system using fixed-length records to a modern JSON-based API and needs a clear mapping of data patterns.

## High-level Business Architecture

The system follows a pipeline from raw specifications to a generated, hosted book:

1.  **Specification Ingestion**: Official language specifications and data format manuals are collected and converted into `/specifications/` (reStructuredText) or `/docs/` (Markdown).
2.  **Transpiler Engine**:
    *   **ANTLR4 Grammars**: Parse the source specifications into Abstract Syntax Trees (AST).
    *   **ASG/IR Logic**: Transform ASTs into an Abstract Semantic Graph (ASG) or Intermediate Representation (IR) to extract common patterns.
    *   **Jinja2 Templates**: Render the extracted patterns into a consistent comparison format (tables, code blocks).
3.  **Documentation Generation**: The rendered content is compiled using Sphinx/ReadTheDocs to produce a web-accessible book.
4.  **CI/CD Pipeline**: Automated verification and deployment via GitHub Actions ensures every change is tested and reflected in the live documentation.

## Appendix: Decisions

As per `GEMINI.md`, every major decision evaluates three options. Discarded options are archived here.

### D1: Documentation Format
*   **Option 1: Markdown** - Widely used, but limited for complex technical documentation. (Used for some parts)
*   **Option 2: reStructuredText (Selected)** - Powerful, natively supported by Sphinx/ReadTheDocs, better for structured technical books.
*   **Option 3: AsciiDoc** - Very powerful but less integrated with the standard ReadTheDocs/Python ecosystem than rST.

### D2: Transpiler Implementation
*   **Option 1: Manual Regex/String Parsing** - Too fragile for complex language specs. (Discarded)
*   **Option 2: ANTLR4 (Selected)** - Robust parser generator with wide language support and strong tree-walking capabilities.
*   **Option 3: Custom Recursive Descent Parser** - High maintenance and time-consuming to implement for multiple languages. (Discarded)

### D3: Template Engine
*   **Option 1: Mako** - Fast, but syntax can be complex. (Discarded)
*   **Option 2: Jinja2 (Selected)** - Industry standard for Python, clean syntax, well-documented, and easily extensible.
*   **Option 3: String.Template** - Too basic for the logic required in documentation generation. (Discarded)
