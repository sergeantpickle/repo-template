# Repository Template

An AI-primary repository template for projects where coding agents are expected to create, maintain, and hand off substantial portions of the codebase.

The template keeps durable project knowledge separate from active work, research, historical records, and release history. It is designed so a fresh agent can orient itself from the repository without depending on prior chat context.

## Starting a new project

1. Create a repository from this template.
2. Give the first agent the project goal and tell it to follow `AGENTS.md`.
3. The agent inventories the repository, replaces template placeholders, and builds `INDEX.md` from the actual project.
4. The agent creates architecture, product, reference, operations, and other deeper documentation only when the project actually needs them.
5. Non-trivial implementation work gets a task-scoped execution plan under `docs/plans/active/`.
6. Durable decisions are recorded under `docs/decisions/`; research evidence goes under `docs/research/`.
7. When work is complete, the execution plan moves to `docs/plans/completed/`.

## Repository knowledge model

- `AGENTS.md` — small, stable instructions and navigation for agents.
- `README.md` — human-facing project purpose, setup, and usage.
- `INDEX.md` — canonical map of the actual project.
- `docs/README.md` — index of deeper documentation.
- `docs/GOVERNANCE.md` — documentation authority, lifecycle, and conflict rules.
- `docs/PLANS.md` — execution-plan contract.
- `docs/architecture/` — architecture documents when the project needs them.
- `docs/decisions/` — durable architectural/product/engineering decisions.
- `docs/plans/active/` — living plans for substantial work.
- `docs/plans/completed/` — completed plans retained as engineering history.
- `docs/research/` — scoped investigations and evidence.
- `docs/handoffs/` — exceptional dated continuation snapshots.
- `docs/reference/` — durable technical reference.
- `docs/generated/` — generated documentation; never hand-edit.
- `docs/templates/` — templates for repository knowledge artifacts.

## Principle

Repository state is the memory. Chat history is not required for continuity.
