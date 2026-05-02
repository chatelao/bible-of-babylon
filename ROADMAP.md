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
        - [x] 6.2.1 Implement base Visitor for CST to ASG transformation <!-- 2026-05-02, issue #6.2.1 -->
        - [x] 6.2.2 Implement transformation for Pattern definitions <!-- 2026-05-02, issue #6.2.2 -->
        - [x] 6.2.3 Implement transformation for Instance definitions <!-- 2026-05-02, issue #6.2.3 -->
    - [ ] 6.3 Implement ASG validation <!-- issue #6.3 -->
        - [x] 6.3.1 Validate pattern existence for instances <!-- 2026-05-02, issue #6.3.1 -->
        - [x] 6.3.2 Validate mandatory parameter assignment <!-- 2026-05-02, issue #6.3.2 -->
        - [ ] 6.3.3 Validate type consistency for assignments <!-- issue #6.3.3 -->
- [ ] Implement Jinja2 generators for reStructuredText <!-- issue #7 -->
    - [x] 7.1 Setup Jinja2 environment and base reST templates <!-- 2026-05-02, issue #7.1 -->
    - [ ] 7.2 Implement generator logic for Pattern instances (tables) <!-- issue #7.2 -->
        - [ ] 7.2.1 Implement reST table rendering for basic assignments <!-- issue #7.2.1 -->
        - [ ] 7.2.2 Implement reST rendering for nested instances and lists <!-- issue #7.2.2 -->
    - [ ] 7.3 Implement generator logic for Instructions (blocks) <!-- issue #7.3 -->
        - [ ] 7.3.1 Implement reST rendering for call, assign, and return instructions <!-- issue #7.3.1 -->
        - [ ] 7.3.2 Implement reST rendering for raw snippets and nested blocks <!-- issue #7.3.2 -->

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
