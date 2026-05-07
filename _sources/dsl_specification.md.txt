# DSL Specification: Source Patterns

This document defines the requirements and syntax for the Domain-Specific Language (DSL) used to define source patterns in the comparative book project.

## 1. Requirements

- **Semantic Intent**: The DSL must capture the *what* (the meaning of the pattern) rather than the *how* (the syntax of a specific language).
- **Structure**: It should be easy to define patterns with parameters (e.g., variable name, type, value).
- **Extensibility**: It must allow adding new pattern types and properties without breaking existing definitions.
- **Parseability**: The syntax must be compatible with ANTLR4 for generating a parser.
- **Readability**: It should be human-readable to facilitate contributions.

## 2. Syntax (v1.0)

The DSL uses a block-based structure.

### Pattern Definition
A pattern definition describes the structure of a common programming or data concept.

```
pattern VariableDeclaration {
    meta description: "Declares a variable."
    parameter name: Identifier
    parameter type: Type
    parameter initial_value: Expression
}
```

### Pattern Instance
An instance provides the specific values for a pattern to be compared across languages.

```
instance VarDec1 of VariableDeclaration {
    name = "x"
    type = "Integer"
    initial_value = 42
}
```

### Types
- **Identifier**: A standard name (e.g., variable or function name).
- **Type**: A logical type name (e.g., "Integer", "String").
- **Expression**: A value or simple operation (represented as a string literal or number).
- **Block**: A sequence of instructions enclosed in `{}`.
- **List<T>**: A collection of items of type T, represented by `[]`.

### Blocks and Instructions
Blocks are used for control flow or procedural patterns. They contain a sequence of instructions.

```
instance CheckBalance of IfElse {
    then_branch = {
        call charge_fee(0)
    }
}
```

#### Supported Instructions:
- `call <name>(<args>)`: Invokes a function or procedure.
- `assign <target> = <expression>`: Assigns a value to a variable.
- `return <expression>`: Returns a value.
- `raw "<snippet>"`: Fallback for language-specific code that doesn't fit the DSL model.

### Anonymous Instances and Collections
Used for nesting complex structures without requiring a top-level name for every sub-component.

```
instance UserProfile of DataMap {
    entries = [
        instance of MapEntry { key = "id", value = 1 },
        instance of MapEntry { key = "active", value = true }
    ]
}
```

## 3. Metadata

Patterns and instances can include metadata such as descriptions and notes using the `meta` keyword.

```
pattern VariableDeclaration {
    meta description: "The act of naming a value and optionally specifying its type."
    parameter name: Identifier
    ...
}
```

## Appendix: Decision Evaluation

### Code Block Representation Options

| Option | Description | Pros | Cons | Status |
|---|---|---|---|---|
| **A: Opaque Strings** | Represent blocks as single string literals. | Extremely simple to parse. | No semantic validation; generator must do all the heavy lifting. | Discarded |
| **B: Structural Blocks** | Define a set of logical instructions (call, assign, return) inside `{}`. | Captures semantic intent; allows structured transformation. | Increases grammar complexity. | **Selected** |
| **C: External References** | Link to external snippets in files. | Keeps DSL clean. | Fragmented source; harder to maintain. | Discarded |

### Instruction Set for Structural Blocks

| Option | Description | Pros | Cons | Status |
|---|---|---|---|---|
| **A: Minimal Set** | Only `call`, `assign`, `return`. | Simple to implement; covers 90% of cases. | Might lack expressiveness for complex patterns. | Discarded |
| **B: Extended Set** | `call`, `assign`, `return` + `raw`. | High flexibility; `raw` provides an escape hatch. | `raw` might be overused, defeating the purpose of the DSL. | **Selected** |
| **C: Full AST** | Replicate a full programming language AST. | Can represent anything. | Extremely complex to design and implement. | Discarded |

---
*Evaluated on 2026-05-01*
