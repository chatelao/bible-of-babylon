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
    - [ ] 5.1 Define Lexer rules for identifiers, literals, and keywords <!-- issue #5.1 -->
    - [ ] 5.2 Define Parser rules for pattern definitions, instances, and metadata <!-- issue #5.2 -->
    - [ ] 5.3 Define Parser rules for blocks, instructions, and collections <!-- issue #5.3 -->
    - [ ] 5.4 Implement grammar verification tests <!-- issue #5.4 -->
- [ ] Design the Intermediate Representation (IR) / ASG <!-- issue #6 -->
    - [ ] 6.1 Define the ASG object model in Python <!-- issue #6.1 -->
    - [ ] 6.2 Implement CST to ASG transformation logic <!-- issue #6.2 -->
    - [ ] 6.3 Implement ASG validation (e.g., parameter type checking) <!-- issue #6.3 -->
- [ ] Implement Jinja2 generators for reStructuredText <!-- issue #7 -->
    - [ ] 7.1 Setup Jinja2 environment and base reST templates <!-- issue #7.1 -->
    - [ ] 7.2 Implement generator logic for Programming Language patterns <!-- issue #7.2 -->
    - [ ] 7.3 Implement generator logic for Data Format patterns <!-- issue #7.3 -->

## Phase 3: Content Creation
- [ ] Populate Programming Language patterns (Variables, Control Flow, etc.) <!-- issue #8 -->
- [ ] Populate Data Format patterns (JSON, XML, YAML, etc.) <!-- issue #9 -->

## Phase 4: Publication
- [ ] Configure ReadTheDocs integration <!-- issue #10 -->
- [ ] Final review and polish of the comparative book <!-- issue #11 -->
