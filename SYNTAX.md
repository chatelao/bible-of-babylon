# Concept: Improved Syntax Highlighting

## Overview
Currently, the "Bible of Babylon" uses generic reStructuredText literal blocks (`::`) for all code snippets. This results in no syntax highlighting or very limited highlighting based on Sphinx's default guesser. To improve the developer experience, we need to implement language-specific syntax highlighting across all comparison tables and pivot chapters.

## Technical Approach

### 1. Language Mapping
The transpiler must maintain a mapping between the internal instance names (e.g., "Java", "Python") and Pygments-compatible lexer names.

| Internal Name | Pygments Lexer |
|---------------|----------------|
| SQL           | `sql`          |
| C             | `c`            |
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
| Prolog        | `prolog`       |
| JSON          | `json`         |
| XML           | `xml`          |
| YAML          | `yaml`         |
| TOML          | `toml`         |
| CSV           | `text`         |
| Fixlength     | `text`         |

### 2. Implementation Strategy

#### A. Template Modernization
Update `instance_table.rst.j2` and `pivot_table.rst.j2` to use the `.. code-block:: <lexer>` directive instead of `::`.

**Example (Internal Pivot Table Logic):**
```rst
   * - VariableDeclaration
     - .. code-block:: c

           int x = 42;
```

#### B. Generator Logic
The `CodeGenerator` class in `src/generator.py` should be enhanced to:
1.  Detect the target language of an instance or pivot page.
2.  Pass the correct `lexer` name to the Jinja2 context.
3.  Modify `format_table_cell` to accept an optional `lexer` parameter.

#### C. Pivot Chapter Optimization
For language-specific pivot chapters, we can use the `.. highlight:: <lang>` directive at the top of the file. This sets the default language for all subsequent literal blocks (`::`), allowing us to keep the table generation logic simple while still getting highlighting.

## Appendix: Decision Evaluation

### Mixed-Language Highlighting Options

| Option | Description | Pros | Cons | Status |
|---|---|---|---|---|
| **A: Default Highlighting** | Use `.. highlight:: none` or let Sphinx guess. | No changes needed to templates. | Poor visual quality; inconsistent highlighting. | Discarded |
| **B: Per-Cell Directives** | Wrap every code snippet in a specific `.. code-block:: <lang>`. | Precise highlighting for every cell; works in all tables. | Increases generated file size; more complex Jinja2 logic. | **Completed** |
| **C: Language-Specific Pages Only** | Only highlight on Pivot chapters using `.. highlight::`. | Simple implementation; clean pivot chapters. | Comparison tables (the core of the project) remain unhighlighted. | Discarded |

### Lexer Selection for Assembly

| Option | Description | Pros | Cons | Status |
|---|---|---|---|---|
| **A: Generic `asm`** | Use the standard Pygments `asm` lexer. | Simple; broad compatibility. | May not capture dialect-specific keywords (e.g., RISC-V vs x86). | **Completed** (for RISC-V) |
| **B: Dialect-Specific** | Use `nasm`, `gas`, etc. | Better highlighting for specific dialects. | Requires mapping internal names to specific dialects. | **Completed** (for x86) |
| **C: Custom Lexer** | Write a custom Pygments lexer for the project. | Perfect highlighting. | High maintenance overhead; overkill for documentation. | Discarded |

---
*Evaluated on 2026-05-24. Implemented on 2026-05-24.*
