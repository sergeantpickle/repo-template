# Agent Reference

This repository is a field guide for AI agents that build and maintain other repositories. It is not a scaffold to copy wholesale. Use its structures as reference patterns, then shape the project around its real work.

## How to use this reference

1. Identify the kind of project and the coordination problem you are solving.
2. Find the closest structural pattern below.
3. Open that example's `tree.md` for the annotated directory layout and notes.
4. Keep only the parts that solve a real need in the target project.
5. Revisit the structure when responsibilities, domains, or working practices change.

The trees are examples, not maturity levels or mandatory checklists. A project can start at any pattern, combine patterns, or remain simpler.

## This reference repository

```text
repo-template/
├── AGENTS.md                    # This navigation map and structural reference
├── README.md                    # Human entry point and purpose
├── docs/
│   ├── growth.md                # When repository structure should evolve
│   ├── information.md           # Where different kinds of information belong
│   ├── agent-context.md         # Root and scoped instructions, skills, agents
│   ├── audit.md                 # Lightweight checkpoints and full reviews
│   └── research.md              # Observations and sources behind the guidance
└── examples/
    ├── README.md                # Pattern index and selection guide
    ├── seed-project/tree.md
    ├── growing-project/tree.md
    ├── scoped-instructions/tree.md
    ├── monorepo/tree.md
    ├── repeatable-workflows/tree.md
    ├── semantic-project-map/tree.md
    └── organization-scale/tree.md
```

Read the relevant guide; open an example when you need to see the actual folders and files together.

## Structural patterns

### 1. A simple project

Start with a small root: a human README, one project-wide agent instruction file, and the source and tests the project actually needs.

```text
project/
├── AGENTS.md
├── README.md
├── src/
└── tests/
```

Annotated tree, file responsibilities, and growth signals: [examples/seed-project/tree.md](examples/seed-project/tree.md).

### 2. A project with durable knowledge

Add documentation when important architecture, operational knowledge, or decisions become expensive to reconstruct. Keep active task state in the project's existing issue, pull-request, or planning system.

```text
project/
├── AGENTS.md
├── README.md
├── src/
├── tests/
└── docs/
    ├── architecture.md
    ├── operations.md
    └── decisions/
```

See [examples/growing-project/tree.md](examples/growing-project/tree.md).

### 3. Distinct domains with different instructions

Use nested `AGENTS.md` files when a domain has rules, commands, boundaries, or validation that do not apply elsewhere. Do not add one to every directory.

```text
project/
├── AGENTS.md
└── src/
    ├── api/
    │   └── AGENTS.md
    ├── billing/
    │   └── AGENTS.md
    └── shared/
```

See [examples/scoped-instructions/tree.md](examples/scoped-instructions/tree.md).

### 4. A multi-application repository

Keep repository-wide guidance at the root and give independently evolving applications or services their own context where it differs. Shared packages keep their own guidance only when they have distinct contracts or conventions.

```text
workspace/
├── AGENTS.md
├── apps/
│   ├── web/
│   │   └── AGENTS.md
│   └── admin/
├── services/
│   └── api/
│       └── AGENTS.md
└── packages/
    ├── contracts/
    └── ui/
```

See [examples/monorepo/tree.md](examples/monorepo/tree.md).

### 5. Repeated procedures

A skill or equivalent on-demand procedure earns a place when a workflow recurs and its steps, branching, validation, or supporting assets are worth maintaining separately. Use the location supported by the project's agent harness.

```text
project/
├── AGENTS.md
└── .agents/
    └── skills/
        └── release/
            ├── SKILL.md
            ├── references/
            └── scripts/
```

See [examples/repeatable-workflows/tree.md](examples/repeatable-workflows/tree.md).

### 6. A project map with semantic value

A map is useful when it explains ownership, dependencies, entry points, or data flow that cannot be understood from a plain directory listing.

```text
project/
├── README.md
└── docs/
    ├── project-map.md
    └── architecture/
        └── request-flow.md
```

See [examples/semantic-project-map/tree.md](examples/semantic-project-map/tree.md).

### 7. Organization-scale coordination

Catalogs, ownership metadata, dependency maps, and shared policy become useful when many independently changing components or repositories make the overall system difficult to understand.

```text
engineering/
├── catalog/
│   ├── services.yaml
│   └── ownership.yaml
├── docs/
│   └── architecture/
│       └── dependency-map.md
└── CODEOWNERS
```

See [examples/organization-scale/tree.md](examples/organization-scale/tree.md).

## Maintaining this reference

- Every example pattern lives in `examples/<pattern>/tree.md` and includes an annotated tree, notes for the paths shown, when the pattern fits, and what should remain optional.
- When adding, renaming, or removing an example, update `examples/README.md` and the corresponding tree reference in this file.
- Keep the repository tree above accurate when the guide's own structure changes.
- Keep research claims linked to sources and recheck fast-changing agent-harness behavior before presenting it as current.

## Working principles

- Understand the project before proposing its structure.
- Give each persistent document or directory a clear responsibility.
- Prefer an existing owner over a new category.
- Let domain boundaries, not directory counts, determine instruction scope.
- Keep root instructions concise and route to deeper context when needed.
- Treat example trees as patterns to adapt, never as a checklist to reproduce.
- Preserve useful information when reorganizing; update links and references.
- Retire structure when the responsibility that justified it disappears.

For deeper reasoning, read [growth](docs/growth.md), [information ownership](docs/information.md), and [agent context](docs/agent-context.md). For a repository review, follow [the audit guide](docs/audit.md).
