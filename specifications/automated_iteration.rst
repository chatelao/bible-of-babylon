==========================================
Automated Iteration Workflow Specification
==========================================

Overview
========

The Automated Iteration Workflow is designed to increase development velocity by automating repetitive tasks associated with incremental content creation and bug fixing (Business Case 3). It enables a "continuous refinement" loop where successful pull requests are automatically merged and their corresponding tasks are re-opened for the next iteration.

Workflow Logic
==============

The workflow is triggered upon the successful completion of a CI/CD pipeline for a pull request. It checks for specific labels to determine if and how to proceed with automation.

Label: ``Auto-Repeat``
----------------------

* **Action**: If CI/CD passes, the pull request is automatically merged.
* **Refinement**: The associated issue is duplicated.
* **Continuity**: The duplicated issue retains the ``Auto-Repeat`` label.
* **Termination**: The loop continues indefinitely until a CI/CD failure occurs or the label is manually removed.

Label: ``Auto-Repeat-X`` (e.g., ``Auto-Repeat-10``) [Planned]
-------------------------------------------------------------

* **Note**: This is a planned enhancement to the MVP.
* **Action**: If CI/CD passes, the pull request is automatically merged.
* **Refinement**: The associated issue is duplicated.
* **Continuity**: The counter ``X`` is decremented by 1 in the duplicated issue's label (e.g., ``Auto-Repeat-10`` becomes ``Auto-Repeat-9``).
* **Termination**:
    * If the decremented counter is greater than 0, the new label (e.g., ``Auto-Repeat-9``) is applied to the duplicated issue.
    * If the counter reaches 0, no ``Auto-Repeat`` or ``Auto-Repeat-X`` label is applied to the new issue, effectively stopping the automated loop.

Appendix: Decision Evaluation
=============================

Triggering Strategy Options
---------------------------

.. list-table::
   :widths: 20 40 20 20 10
   :header-rows: 1

   * - Option
     - Description
     - Pros
     - Cons
     - Status
   * - **A: Label-based**
     - Using GitHub Labels (``Auto-Repeat``, ``Auto-Repeat-X``) to trigger the workflow.
     - Highly visible; easy to manage via UI; native GitHub feature.
     - Can clutter the labels list if not managed.
     - **Selected**
   * - - B: PR-comment-based
     - Triggering based on a specific command in a PR comment (e.g., ``/auto-iterate``).
     - Less visual clutter; explicitly triggered by a user action.
     - Harder to track status at a glance across multiple PRs.
     - Discarded
   * - - C: Branch-naming-convention-based
     - Triggering based on a prefix in the branch name (e.g., ``auto/feature-x``).
     - Zero configuration after branch creation.
     - Inflexible; requires branch renaming to change behavior.
     - Discarded

---
*Evaluated on 2024-05-24*
