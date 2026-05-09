# Concept: Syntax Highlighting

## Overview
The "Bible of Babylon" implements language-specific syntax highlighting across all comparison tables, pivot chapters, and generated Excel matrices. This provides a rich developer experience by visually distinguishing code constructs across the 30+ supported programming languages and data formats.

## Technical Approach

### 1. Language Mapping
The transpiler maintains a mapping between internal instance names and Pygments-compatible lexer names in `src/generator.py`.

| Internal Name | Pygments Lexer |
|---------------|----------------|
| SQL           | `sql`          |
| C             | `c`            |
| Cpp           | `cpp`          |
| XQuery        | `xquery`       |
| Java          | `java`         |
| Rust          | `rust`         |
| Erlang        | `erlang`       |
| Lisp          | `common-lisp`  |
| Bash          | `bash`         |
| Cmd           | `doscon`       |
| PowerShell    | `powershell`   |
| Python        | `python`       |
| PHP           | `php`          |
| CSS           | `css`          |
| CUDA          | `cpp`          |
| x86 Assembler | `nasm`         |
| RISC-V Assembler| `asm`        |
| ARM AArch64 Assembler | `asm`  |
| Prolog        | `prolog`       |
| Java Bytecode | `jasmin`       |
| OCaml/Camel   | `ocaml`        |
| Go            | `go`           |
| Haskell       | `haskell`      |
| TypeScript    | `typescript`   |
| Tcl           | `tcl`          |
| COBOL         | `cobol`        |
| Fortran       | `fortran`      |
| C#            | `csharp`       |
| Swift         | `swift`        |
| Kotlin        | `kotlin`       |
| GraphQL       | `graphql`      |
| SPARQL        | `sparql`       |
| Overpass Turbo| `text`         |
| JSON          | `json`         |
| XML           | `xml`          |
| YAML          | `yaml`         |
| TOML          | `toml`         |
| CSV           | `text`         |
| Fixlength     | `text`         |

### 2. Implementation Strategy

#### A. Template Modernization
The `instance_table.rst.j2` and `pivot_table.rst.j2` templates use the `.. code-block:: <lexer>` directive. This is applied via the `format_table_cell` filter which accepts a `lexer` parameter.

#### B. Generator Logic
The `CodeGenerator` class in `src/generator.py` detects the target language of an instance or pivot page using a longest-match strategy and passes the correct `lexer` name to the Jinja2 context via the `get_lexer` filter.

#### C. Pivot Chapter Optimization
For language-specific pivot chapters, the generator ensures that all code snippets are wrapped in the appropriate `.. code-block::` directive, providing consistent highlighting.

#### D. Excel Highlighting
The `CodeGenerator.render_matrix_excel` method uses Pygments to tokenize code snippets. It then maps these tokens to an RTD-inspired color palette and applies them using `openpyxl.cell.rich_text.CellRichText`. This ensures that syntax highlighting is preserved even in the downloadable spreadsheet formats.

## Appendix: Decision Evaluation

### Mixed-Language Highlighting Options

| Option | Description | Pros | Cons | Status |
|---|---|---|---|---|
| **A: Default Highlighting** | Use `.. highlight:: none` or let Sphinx guess. | No changes needed to templates. | Poor visual quality; inconsistent highlighting. | Discarded |
| **B: Per-Cell Directives** | Wrap every code snippet in a specific `.. code-block:: <lang>`. | Precise highlighting for every cell; works in all tables. | Increases generated file size; more complex Jinja2 logic. | **Completed** |
| **C: Language-Specific Pages Only** | Only highlight on Pivot chapters using `.. highlight::`. | Simple implementation; clean pivot chapters. | Comparison tables remain unhighlighted. | Discarded |

### Lexer Selection for Assembly

| Option | Description | Pros | Cons | Status |
|---|---|---|---|---|
| **A: Generic `asm`** | Use the standard Pygments `asm` lexer. | Simple; broad compatibility. | May not capture dialect-specific keywords. | **Completed** (for RISC-V/ARM) |
| **B: Dialect-Specific** | Use `nasm`, `gas`, etc. | Better highlighting for specific dialects. | Requires mapping internal names to specific dialects. | **Completed** (for x86) |
| **C: Custom Lexer** | Write a custom Pygments lexer for the project. | Perfect highlighting. | High maintenance overhead. | Discarded |

### Excel Highlighting Options

| Option | Description | Pros | Cons | Status |
|---|---|---|---|---|
| **A: Plain Text** | No highlighting in Excel. | Simplest implementation; small file size. | Poor readability compared to web docs. | Discarded |
| **B: Rich Text (Pygments)** | Tokenize with Pygments and apply colors via `openpyxl`. | Consistent look and feel with web docs; excellent readability. | Complex implementation; slightly larger file sizes. | **Completed** |
| **C: Conditional Formatting** | Use Excel's built-in conditional formatting. | Small file size; native Excel feature. | Extremely limited for syntax highlighting; hard to implement for many languages. | Discarded |

---
*Last updated on 2026-05-09.*
