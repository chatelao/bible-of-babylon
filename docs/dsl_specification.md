# DSL Specification: Source Patterns

This document defines the requirements and initial syntax draft for the Domain-Specific Language (DSL) used to define source patterns in the comparative book project.

## 1. Requirements

- **Semantic Intent**: The DSL must capture the *what* (the meaning of the pattern) rather than the *how* (the syntax of a specific language).
- **Structure**: It should be easy to define patterns with parameters (e.g., variable name, type, value).
- **Extensibility**: It must allow adding new pattern types and properties without breaking existing definitions.
- **Parseability**: The syntax must be compatible with ANTLR4 for generating a parser.
- **Readability**: It should be human-readable to facilitate contributions.

## 2. Syntax (v0.2)

The DSL uses a block-based structure.

### Pattern Definition
A pattern definition describes the structure of a common programming or data concept.

```
pattern VariableDeclaration {
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
- **Expression**: A value or simple operation (often represented as a string literal for simplicity in v0.2).
- **Block**: A collection of logical steps (see below).
- **List<T>**: A collection of items of type T.

### Blocks and Instructions
Blocks are used for control flow or procedural patterns. They contain instructions rather than raw code.

```
instance CheckBalance of IfElse {
    then_branch = {
        call charge_fee(0)
    }
}
```

### Anonymous Instances and Collections
Used for nesting complex structures.

```
instance UserProfile of DataMap {
    entries = [
        instance of MapEntry { key = "id", value = 1 },
        instance of MapEntry { key = "active", value = true }
    ]
}
```

## 3. Metadata

Patterns and instances can include metadata such as descriptions and notes.

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

---
*Evaluated on 2026-05-01*
