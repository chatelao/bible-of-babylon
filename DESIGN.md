# Design

## Book Structure

The comparative book is divided into two main parts: Programming Languages and Data Formats.

### Part I: Programming Languages
This section compares languages based on common programming patterns.

**Languages:**
- SQL
- C
- XQuery
- Java
- Rust
- Erlang
- Lisp
- Bash
- Cmd
- PowerShell
- Python
- CSS
- CUDA
- x86 Assembler

**Patterns to be compared:**
- Variable declaration
- Control flow (if/else, loops)
- Function/Procedure definition
- Error handling
- Concurrency models
- Module/Package Import
- Constants

### Part II: Data Formats
This section compares data structures and serialization formats.

**Formats:**
- Fixlength
- CSV
- XML
- JSON
- YAML
- TOML

**Patterns to be compared:**
- Basic data types (Strings, Numbers, Booleans)
- Nested structures (Objects/Maps, Arrays/Lists)
- Metadata/Attributes
- Comments support
- Schema validation

## Presentation Design: Comparison Tables

Each pattern will be presented using a standardized table format to ensure consistency across the book.

### Table Layout Example

| Language/Format | Pattern Implementation | Notes |
|-----------------|------------------------|-------|
| Java            | `int x = 5;`           | Strongly typed |
| Python          | `x = 5`                | Dynamically typed |
| Rust            | `let x = 5;`           | Immutable by default |

## Technical Architecture: Transpiler Pipeline

The book is generated using a custom transpilation pipeline to ensure consistency and maintainability.

### 1. Source Patterns
Patterns are defined in a domain-specific format (DSL) that describes the semantic intent of a pattern.

### 2. ANTLR4 Parser
An ANTLR4 grammar parses the source patterns into a concrete syntax tree (CST).

### 3. Abstract Semantic Graph (ASG) / Intermediate Representation (IR)
The CST is transformed into an ASG. This representation is language-agnostic and captures the core logic and parameters of the pattern.

### 4. Jinja2 Generators
Target-specific Jinja2 templates consume the IR to produce reStructuredText (reST) snippets for each language or format.

### 5. Final Assembly
The generated reST snippets are aggregated into the final documentation structure for ReadTheDocs.

## Automated Iteration Workflow

To support automated bulk tasks, the repository implements a GitHub Actions workflow that automatically merges PRs and duplicates their associated issues based on labels.

### Workflow Logic

- **Label `Auto-Repeat`**:
    - If CI/CD passes, the PR is automatically merged.
    - The associated issue is duplicated.
    - The duplicate issue retains the `Auto-Repeat` label, enabling an infinite loop until a CI/CD failure occurs.

- **Label `Auto-Repeat-X` (e.g., `Auto-Repeat-10`) [Planned Enhancement]**:
    - If CI/CD passes, the PR is automatically merged.
    - The associated issue is duplicated.
    - The counter `X` is decremented in the new issue's label (e.g., `Auto-Repeat-9`).
    - If the counter reaches 0, the `Auto-Repeat` or `Auto-Repeat-X` label is removed from the new issue, stopping the loop.

## Appendix: Decision Evaluation

### Automation Implementation Options

| Option | Description | Pros | Cons | Status |
|---|---|---|---|---|
| **A: GitHub CLI in Bash** | Using `gh` commands within a standard Bash script in a workflow. | Native integration; no extra dependencies; easy to debug; fast execution. | Limited to what `gh` CLI provides. | **Selected** |
| **B: GitHub Script** | Using the `actions/github-script` (JavaScript) for complex logic. | Full access to GitHub API via Octokit; powerful for complex data manipulation. | Requires JavaScript knowledge; slightly more overhead than pure Bash for simple tasks. | Discarded |
| **C: Custom Python Action** | Writing a dedicated Python script and using it as a composite action. | Consistent with the rest of the codebase (Python); highly testable. | More boilerplate; slower to run due to environment setup; overkill for simple CLI tasks. | Discarded |

### Presentation Layout Options

| Option | Description | Pros | Cons | Status |
|---|---|---|---|---|
| **A: Markdown Tables** | Standard GitHub-flavored Markdown tables. | Simple; native support in most editors; readable in raw form. | Limited styling; hard to manage very wide tables (many languages). | **Selected** |
| **B: Sphinx Grid Tables** | reStructuredText grid tables. | More flexible than Markdown; better support for multi-line cells. | Harder to write/read in raw text; requires reST knowledge for contributors. | Discarded |
| **C: Interactive Tabs** | Using `sphinx-tabs` to switch between languages. | Saves vertical space; clean look; good for long code snippets. | Requires JavaScript; hard to compare two languages at a glance. | Discarded |

### Environment Setup Options

| Option | Description | Pros | Cons | Status |
|---|---|---|---|---|
| **A: Manual Installation** | Manually downloading ANTLR4 JAR and setting up CLASSPATH. | Direct control over versions. | Error-prone; hard to automate; manual path management. | Discarded |
| **B: Python-based Tooling** | Using `pip` to install `jinja2` and `antlr4-tools`. | Easy to automate; handles ANTLR4 environment setup; standard tooling. | Depends on Python/pip. | **Selected** |
| **C: System Packages** | Using `apt-get` to install `antlr4` and `python3-jinja2`. | Standard system packages. | May be outdated; requires sudo; inconsistent across OS. | Discarded |

### Testing Framework Options

| Option | Description | Pros | Cons | Status |
|---|---|---|---|---|
| **A: pytest** | A mature, full-featured Python testing tool. | Simple syntax; powerful fixtures; extensive plugin ecosystem. | Slightly more complex than `unittest` for very simple cases. | **Selected** |
| **B: unittest** | Built-in Python testing library. | No extra dependencies; part of standard library. | More boilerplate; less flexible than `pytest`. | Discarded |
| **C: nose2** | Successor to `nose`, based on `unittest`. | Extends `unittest` with plugins. | Less active development compared to `pytest`. | Discarded |

---
*Evaluated on 2026-05-01*
