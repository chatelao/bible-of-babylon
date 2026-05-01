# Technical Debts

## Documentation
- [ ] reStructuredText conversion: Some external docs in `/specifications/` and `/docs/` might still be in their original formats.

## Architecture
- [ ] Jinja2 Template duplication: Risk of duplication between different language templates if shared patterns are not properly identified.
- [ ] DSL Complexity: The initial DSL might be too simple to capture complex language features (e.g., Rust's ownership or Erlang's actor model).

## Implementation
- [ ] Missing initial templates: Basic templates for all target languages/formats need to be created.
