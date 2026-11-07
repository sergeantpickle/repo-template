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

When this repository is newly created from the template, the first agent must build the project index from the repository itself rather than merely filling placeholders.

1. Inventory the full repository tree and identify source, tests, configuration, infrastructure, scripts, generated files, entry points, external integrations, and release/deployment surfaces.
2. Read the files that define actual behavior: manifests, package/build configuration, application entry points, schemas, CI workflows, tests, and existing documentation.
3. Replace template placeholders in `README.md`, `ARCHITECTURE.md`, and `docs/README.md`.
4. Make `docs/README.md` the canonical project index. It must tell a fresh agent what exists, where it lives, which documents are authoritative, and which validation commands establish correctness.
5. Create deeper documentation only when supported by the repository or required for the first planned work. Do not manufacture speculative architecture.
6. Remove unused placeholder directories/files after evaluating whether the project needs them.
7. Establish executable validation commands and record them in the project index.
8. Before substantial implementation, create the first execution plan in `docs/plans/active/`.
9. Run repository knowledge checks and resolve stale template markers before declaring initialization complete.

The initialized repository must explain itself to a fresh agent without requiring prior conversation context.

## Project index requirements

The project index at `docs/README.md` must include, when applicable:

- repository map and major directories;
- runtime/application entry points;
- important modules, packages, services, or subsystems;
- test layout and exact validation commands;
- build/package/dependency configuration;
- CI/CD and deployment/release surfaces;
- persistence, schemas, protocols, APIs, or external integrations;
- architecture and decision-document links;
- active execution plans;
- generated artifacts and how to regenerate them;
- known constraints that materially affect implementation.

Every entry should point to the canonical file or directory. Prefer links and concise descriptions over duplicated prose.

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
- `docs/README.md` still maps the repository accurately;
- no stale template text or contradictory documentation was introduced.
