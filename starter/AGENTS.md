# Agent Instructions

This project follows the Repository Growth Standard. `.repo-standard.json` records the upstream source and the version this project last aligned to.

For ordinary code work, use the project's code, tests, configuration, and local instructions. Do not fetch the upstream standard on every task.

When consulting upstream, use the `source` and `version` recorded in `.repo-standard.json`. The latest **released** upstream standard is the alignment target. A newer release is not applied silently, but being behind is known governance drift to review rather than a permanently separate policy line.

Treat `.repo-standard.json` as governance state. Do not change its `source`, `version`, or exceptions as incidental cleanup; changes follow the adoption/exception process in the upstream standard.

Consult upstream before:

- changing repository-wide instruction or documentation structure;
- creating or splitting a permanent work/document category;
- resolving routing drift such as README, changelog, notes, or handoff contamination;
- adding a new repository-level enforcement layer;
- deliberately auditing repository organization;
- aligning to a newer released standard.

## Project-specific rules

Add only non-derivable rules, exact validation commands, boundaries, and conventions that materially improve work in this project.

Do not store active task state, release history, or a general repository encyclopedia here.
