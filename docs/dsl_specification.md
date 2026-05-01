# DSL Specification: Source Patterns

This document defines the requirements and initial syntax draft for the Domain-Specific Language (DSL) used to define source patterns in the comparative book project.

## 1. Requirements

- **Semantic Intent**: The DSL must capture the *what* (the meaning of the pattern) rather than the *how* (the syntax of a specific language).
- **Structure**: It should be easy to define patterns with parameters (e.g., variable name, type, value).
- **Extensibility**: It must allow adding new pattern types and properties without breaking existing definitions.
- **Parseability**: The syntax must be compatible with ANTLR4 for generating a parser.
- **Readability**: It should be human-readable to facilitate contributions.

## 2. Syntax Draft (v0.1)

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

## 3. Metadata

Patterns and instances can include metadata such as descriptions and notes.

```
pattern VariableDeclaration {
    meta description: "The act of naming a value and optionally specifying its type."
    parameter name: Identifier
    ...
}
```

## 4. Next Steps

- [ ] Validate this syntax against more complex patterns (e.g., Concurrency).
- [ ] Refine the list of built-in types (Identifier, Type, Expression, etc.).
- [ ] Implement the ANTLR4 grammar based on this specification.
