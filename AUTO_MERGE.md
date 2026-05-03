# Automated Merge and Iteration Workflow (BC 3)

This project uses an automated workflow to speed up development by automatically merging successful Pull Requests and re-opening the associated tasks for the next iteration.

## How it works

The workflow is triggered whenever the **CI** workflow completes successfully for a Pull Request targeting the `main` branch.

### 1. Label Detection
The workflow looks for specific "Iteration Labels" on either the **Pull Request** or its **linked Issue**.

*   **`Auto-Repeat`**: Merges the PR and duplicates the associated issue for another iteration. This continues indefinitely.
*   **`Auto-Repeat-X`** (e.g., `Auto-Repeat-5`): Merges the PR and duplicates the issue, but decrements the counter in the label (e.g., to `Auto-Repeat-4`). The process stops when the counter reaches 0.

### 2. PR Merging
If an iteration label is found, the workflow attempts to merge the Pull Request using the `--merge` strategy.

### 3. Issue Duplication
After a successful merge, the workflow identifies the associated issue. It then creates a **new issue** with the same title and description, and applies the next iteration label (either `Auto-Repeat` or the decremented `Auto-Repeat-X`).

## Troubleshooting: Why didn't my PR merge?

If your PR was not merged automatically even though CI passed, check the following:

1.  **Label Missing**: Ensure the `Auto-Repeat` or `Auto-Repeat-X` label is present on either the PR or the linked Issue.
2.  **Issue Link**: The workflow must be able to find the associated issue. It looks for:
    *   Official GitHub "Linked Issues" (e.g., using "Closes #123" in the description).
    *   Any `#123` reference in the PR title or body.
3.  **Branch Protection**: If the `main` branch has protection rules (e.g., "Require status checks to pass before merging" or "Require a pull request before merging"), the `GITHUB_TOKEN` used by the workflow must have permission to bypass these, or the requirements must be met.
4.  **Conflicts**: If the PR has merge conflicts, it cannot be merged automatically.
5.  **Draft Status**: The PR must not be in "Draft" status.

## Configuration

The workflow logic is defined in [`.github/workflows/auto_repeat.yml`](.github/workflows/auto_repeat.yml).
