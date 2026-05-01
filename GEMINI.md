# Goal
Create a comprehensive book of most popular prorgramming languages and data structures 
by simply comparing the most often used patterns.

# Areas to compare
## Programming 
### Pogramming languages
- SQL, C, XQuery, Java, Rust, Erlang, Lisp, Bash, Cmd, PowerShell, CSS
- (not yet) : https://madnight.github.io/githut/#/pull_requests/2024/1

### Pogramming patterns
- <tbd>

## Data
### Data format types
- Fixlength, csv, XML, json, yaml, toml

### Data format patterns
- <tbd>

# Structure
- `CONCEPT.md`: Business Cases with 1:N Use Cases each as well as a High-level business architecture
- `DESIGN.md` : Detailed design of the book mostly using tables
- `ROADMAP.md`: Task the progress of the  development, organized by chapters, 
- `TECHNICAL_DEBTS.md`: Log of architectural or implementation debts.
- `/specifications/`: External documentation and manuals converted to reStructuredText.
- `/docs/`: External documentation and manuals converted to reStructuredText.
- `/test/`: Test suite, verifications of the syntax of all files.

# HOWTO
- Use readthedocs.org to produce the documentation
- Use reStructuredText  to document everything not markdown
- Keep `src/install.sh` to install all tools and dependencies.
- For every decision evaluate three options and archiv the discarded ones in a compressed way
  in an appendix of the documentation.

# Testing Locally & with Github Action Workflow
- Maintain a CI/CD pipeline that runs on every commit and every push.
- Use `test/install.sh` to install testing-specific dependencies.
- Verify the syntax and rendering on every task and ever steps.
- Add caching to the Github action workflows to speed up builds.

# ROADMAP rules
- Split big tasks into multiple and/or subtasks if not  modest, feasible and reasonable in one go.
- Add an intermediate usecase, architecture or design tasks if direct implementation is risky.
- Mark Tasks are  as completed with a timestamp and the corresponding issue id when closed.
