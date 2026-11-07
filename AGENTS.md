# AGENTS.md

This repository is designed for AI-primary development.

## Start here

Before making changes:

1. Read `README.md`.
2. Read `docs/README.md`.
3. Read `docs/GOVERNANCE.md`.
4. Read `ARCHITECTURE.md` when architecture is relevant.
5. Read the active plan under `docs/plans/active/` when one exists.

Do not treat chat history as canonical project memory. Durable context belongs in the repository.

## Project initialization

When this repository is newly created from the template:

1. Replace template placeholders with project-specific content.
2. Build `docs/README.md` into the canonical project index.
3. Create only the documentation categories the project actually needs.
4. Remove unused placeholder files once their purpose has been evaluated.
5. Establish executable validation commands and record them in the project index.
6. Create the first execution plan before substantial implementation begins.

The initialized repository must explain itself to a fresh agent without requiring prior conversation context.

## Working rules

- Keep this file short and stable.
- Prefer links to canonical repository docs over duplicating their contents here.
- For substantial or multi-step work, create or update a task-scoped plan in `docs/plans/active/`.
- Put durable decisions in `docs/decisions/`, not in plans or handoffs.
- Put investigation evidence in `docs/research/`.
- Use handoffs only for a real continuation boundary; they are snapshots, not canonical truth.
- When completed, move execution plans to `docs/plans/completed/`.
- Update relevant documentation in the same change as behavior.
- Convert recurring rules into tests, linters, scripts, schemas, or CI checks whenever practical.
- Do not hand-edit generated documentation.

## Before declaring work complete

Verify:

- acceptance criteria are satisfied;
- relevant tests/checks pass;
- active plans reflect the actual state;
- durable decisions and architecture docs are updated where needed;
- no stale template text or contradictory documentation was introduced.
