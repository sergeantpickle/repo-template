# Seed Project

A small but real project with one coherent area of work. This is the starting point when there is no demonstrated need for additional documentation or agent infrastructure.

## Example tree

```text
project/
├── AGENTS.md             # Project-wide instructions for coding agents
├── README.md             # Purpose, setup, and normal use for people
├── src/                  # The implementation
└── tests/                # Tests for behavior the project promises
```

## Notes

- **`AGENTS.md`** belongs at the root when agents need durable project-wide context: boundaries, non-obvious conventions, exact commands, and validation expectations. It is not required for a project that does not use coding agents.
- **`README.md`** explains what the project is, how to get started, and how to use it. Keep task progress and session history elsewhere.
- **`src/`** and **`tests/`** represent the project's actual implementation and verification. Their internal organization follows the language and project type.

## Why this is enough

The project has one coherent context and its code is the best source for most implementation details. There is no need to create empty `docs/`, `plans/`, `decisions/`, `skills/`, `agents/`, or `architecture/` directories just because a larger project might use them.

A project may have configuration, deployment, or generated files from day one. Their presence does not automatically imply a need for more documentation.

## When to grow

Add a durable document when a non-obvious fact becomes expensive or risky to reconstruct. Add scoped instructions when a domain develops rules that do not apply to the rest of the project. Add a persistent work record when a task must survive context changes.

See [growing project](../growing-project/tree.md) and [scoped instructions](../scoped-instructions/tree.md).
