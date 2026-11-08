# Growing Project

A project has acquired durable technical knowledge that agents and contributors repeatedly need. The code remains the source of implementation truth; the documents explain context that is not obvious from the code alone.

## Example tree

```text
project/
├── AGENTS.md                     # Cross-project agent instructions and doc routing
├── README.md                     # Project purpose and normal use
├── src/
├── tests/
└── docs/
    ├── architecture.md           # Current system boundaries and major data flows
    ├── operations.md              # Non-obvious deploy, recovery, or maintenance steps
    └── decisions/
        ├── 001-storage-model.md   # Rationale for a durable storage choice
        └── 002-auth-boundary.md   # Rationale for a durable security boundary
```

## Notes

- **Root `AGENTS.md`** stays a short map: explain what each document owns and when to read it. Do not copy the full documents into the instructions.
- **`docs/architecture.md`** describes the current system, not a history of every design conversation.
- **`docs/operations.md`** exists when routine operation depends on non-obvious knowledge that is not discoverable from deployment configuration or scripts.
- **`docs/decisions/`** is appropriate when multiple decisions have independent rationales and lifecycles. For one decision, start with a section in an existing document or a single decision file before creating a directory.

## Active work stays bounded

The tree does not prescribe a permanent `plans/` or `handoff/` directory. A substantial task can live in the issue tracker, pull request, change proposal, or a bounded work record the project already uses. The work record closes or retires when the task ends.

## When to grow

Split documentation by domain when different areas evolve independently or have different audiences. Add a project map when semantic relationships become difficult to reconstruct.

See [scoped instructions](../scoped-instructions/tree.md) and [semantic project map](../semantic-project-map/tree.md).
