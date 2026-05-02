# Roadmap

## Phase 1: Foundation
- [x] Create project structure and initial documentation (`CONCEPT.md`, `GEMINI.md`, `DESIGN.md`) <!-- 2024-05-24, issue #1 -->
- [x] Setup `src/install.sh` for development environment <!-- 2026-05-01, issue #2 -->
- [x] Setup `test/install.sh` <!-- 2026-05-01, issue #3.1 -->
- [x] Setup CI/CD workflow <!-- 2024-05-24, issue #3.2 -->

## Phase 2: Transpiler Development
- [ ] Define DSL for Source Patterns <!-- issue #4 -->
    - [x] 4.1 Define DSL requirements and syntax draft <!-- 2026-05-01, issue #4.1 -->
    - [x] 4.2 Validate DSL draft with example patterns <!-- 2026-05-01, issue #4.2 -->
    - [x] 4.3 Finalize DSL specification <!-- 2026-05-01, issue #4.3 -->
- [ ] Implement ANTLR4 grammar for the DSL <!-- issue #5 -->
    - [x] 5.1 Define Lexer rules for identifiers, literals, and keywords <!-- 2026-05-01, issue #5.1 -->
    - [x] 5.2 Define Parser rules for pattern definitions, instances, and metadata <!-- 2026-05-01, issue #5.2 -->
    - [x] 5.3 Define Parser rules for blocks, instructions, and collections <!-- 2026-05-01, issue #5.3 -->
    - [x] 5.4 Implement grammar verification tests <!-- 2026-05-01, issue #5.4 -->
- [ ] Design the Intermediate Representation (IR) / ASG <!-- issue #6 -->
    - [x] 6.1 Define the ASG object model in Python <!-- 2026-05-01, issue #6.1 -->
    - [ ] 6.2 Implement CST to ASG transformation logic <!-- issue #6.2 -->
        - [ ] 6.2.1 Implement base Visitor for CST to ASG transformation <!-- issue #6.2.1 -->
        - [ ] 6.2.2 Implement transformation for Pattern definitions <!-- issue #6.2.2 -->
        - [ ] 6.2.3 Implement transformation for Instance definitions <!-- issue #6.2.3 -->
    - [ ] 6.3 Implement ASG validation (e.g., parameter type checking) <!-- issue #6.3 -->
- [ ] Implement Jinja2 generators for reStructuredText <!-- issue #7 -->
    - [ ] 7.1 Setup Jinja2 environment and base reST templates <!-- issue #7.1 -->
    - [ ] 7.2 Implement generator logic for Programming Language patterns <!-- issue #7.2 -->
    - [ ] 7.3 Implement generator logic for Data Format patterns <!-- issue #7.3 -->

## Phase 3: Content Creation
- [ ] Populate Programming Language patterns <!-- issue #8 -->
    - [ ] 8.1 Variable declaration <!-- issue #8.1 -->
    - [ ] 8.2 Control flow (if/else, loops) <!-- issue #8.2 -->
    - [ ] 8.3 Function/Procedure definition <!-- issue #8.3 -->
    - [ ] 8.4 Error handling <!-- issue #8.4 -->
    - [ ] 8.5 Concurrency models <!-- issue #8.5 -->
- [ ] Populate Data Format patterns <!-- issue #9 -->
    - [ ] 9.1 Basic data types (Strings, Numbers, Booleans) <!-- issue #9.1 -->
    - [ ] 9.2 Nested structures (Objects/Maps, Arrays/Lists) <!-- issue #9.2 -->
    - [ ] 9.3 Metadata/Attributes <!-- issue #9.3 -->
    - [ ] 9.4 Comments support <!-- issue #9.4 -->
    - [ ] 9.5 Schema validation <!-- issue #9.5 -->

## Phase 4: Publication
- [ ] Configure ReadTheDocs integration <!-- issue #10 -->
- [ ] Final review and polish of the comparative book <!-- issue #11 -->
