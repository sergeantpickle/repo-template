# Agent Reference

This repository is a field guide for AI agents that build and maintain other repositories. It is not a scaffold to copy wholesale. Use the structural references below to understand common shapes, then adapt them to the project's actual work.

## How to use this reference

1. Identify the kind of project and the coordination problem you are solving.
2. Find the closest structure reference below.
3. Open the linked `examples/<pattern>/tree.md` for the complete annotated tree and path-by-path notes.
4. Keep only the parts that solve a real need in the target project.
5. Revisit the structure when responsibilities, domains, or working practices change.

The trees are illustrative reference layouts, not maturity levels or mandatory checklists. A project can start at any pattern, combine patterns, or remain simpler.

## This reference repository

```text
repo-template/
├── AGENTS.md                         # This guide: reference trees and agent instructions
├── README.md                         # Human entry point and quick orientation
├── docs/
│   ├── growth.md                     # When and why a repository should evolve
│   ├── information.md                # Information ownership and lifecycles
│   ├── agent-context.md              # Root/scoped instructions, skills, and agents
│   ├── audit.md                      # Checkpoints and contextual repository reviews
│   └── research.md                   # Observed patterns and source notes
└── examples/
    ├── README.md                     # Example index and selection guide
    ├── seed-project/tree.md
    ├── application-project/tree.md
    ├── library-project/tree.md
    ├── growing-project/tree.md
    ├── scoped-instructions/tree.md
    ├── monorepo/tree.md
    ├── agent-first-project/tree.md
    ├── research-project/tree.md
    ├── repeatable-workflows/tree.md
    ├── semantic-project-map/tree.md
    └── organization-scale/tree.md
```

The example tree files are the detailed references. Each explains what the paths own, why they appear, and what should stay optional.

## Repository structure references

### 1. Small project

Start with the project's actual implementation and the smallest useful human and agent entry points.

```text
project/
├── AGENTS.md                 # Shared agent instructions, when agents need them
├── README.md                 # Purpose, setup, and normal use
├── src/                      # Actual implementation
└── tests/                    # Checks for promised behavior
```

See [examples/seed-project/tree.md](examples/seed-project/tree.md) for notes and growth signals.

### 2. Application or product

A single application may have a UI, server-side behavior, data access, migrations, and multiple kinds of tests. Keep those responsibilities visible without introducing layers the application does not need.

```text
product/
├── AGENTS.md                 # Project-wide agent orientation and boundaries
├── README.md                 # Product purpose, setup, and usage
├── app/                      # User-facing routes and screens
├── server/                   # Server-side behavior and integrations, if separate
├── db/                       # Schema and migrations, when the app owns a database
├── tests/                    # Unit, integration, and end-to-end checks as needed
└── docs/
    ├── architecture.md       # Important system boundaries and flows
    └── operations.md         # Non-obvious operation and recovery procedures
```

See [examples/application-project/tree.md](examples/application-project/tree.md) for a fuller annotated application layout.

### 3. Reusable library or SDK

A library is organized around its public package, compatibility promises, tests, and examples that show how consumers use it.

```text
library/
├── AGENTS.md                 # Contributor and agent guidance
├── README.md                 # Installation, quick start, and public promises
├── src/
│   └── library_name/         # Importable package
├── tests/                    # Tests of public and internal behavior
├── examples/                 # Small consumer-facing usage examples
└── docs/
    └── api/                  # Expanded API reference, when warranted
```

See [examples/library-project/tree.md](examples/library-project/tree.md) for package layout, release material, and optional directories.

### 4. Project with durable knowledge

When architecture, operations, or decisions become expensive to reconstruct, give each kind of knowledge a clear owner.

```text
project/
├── AGENTS.md                 # Short map to relevant project guidance
├── README.md                 # Purpose and normal use
├── src/
├── tests/
└── docs/
    ├── architecture.md       # Current system shape
    ├── operations.md         # Operational knowledge, if non-obvious
    └── decisions/            # Durable rationale, when several decisions exist
```

See [examples/growing-project/tree.md](examples/growing-project/tree.md).

### 5. Scoped instructions and distinct domains

Use nested instruction files only where local conventions, commands, validation, or safety boundaries genuinely differ.

```text
project/
├── AGENTS.md                 # Rules that apply across the repository
└── src/
    ├── api/
    │   └── AGENTS.md         # API-specific contracts and validation
    ├── billing/
    │   └── AGENTS.md         # Billing invariants and local checks
    └── shared/               # No local instructions while root rules suffice
```

See [examples/scoped-instructions/tree.md](examples/scoped-instructions/tree.md). Check the target agent's discovery and precedence rules before relying on nested instructions.

### 6. Monorepo or multi-application workspace

Keep shared workspace guidance at the root. Give independently evolving applications, services, or packages local instructions only when their needs diverge.

```text
workspace/
├── AGENTS.md                 # Workspace-wide conventions and navigation
├── README.md                 # Workspace purpose and entry points
├── apps/
│   ├── web/
│   │   └── AGENTS.md         # Web-specific conventions, if distinct
│   └── admin/
├── services/
│   └── api/
│       └── AGENTS.md         # API contracts and service-specific checks
├── packages/
│   ├── contracts/            # Shared API and event contracts
│   └── ui/                   # Shared interface components
└── docs/
    └── architecture.md       # Cross-workspace boundaries and dependencies
```

See [examples/monorepo/tree.md](examples/monorepo/tree.md) for ownership and workspace notes.

### 7. Agent-first project or harness

When agents do a substantial share of the work, the repository may need explicit agent instructions, reusable procedures, evaluations, and durable plans. These are earned capabilities, not a default installation.

```text
agent-first-project/
├── AGENTS.md                 # Shared entry point and work boundaries
├── CLAUDE.md                 # Thin tool-specific entry, only if required
├── ARCHITECTURE.md           # System map, when the code needs one
├── src/
├── tests/
├── evals/                    # Agent behavior evaluations, when needed
├── .agents/
│   └── skills/               # Portable/on-demand procedures, if supported
├── .claude/
│   ├── rules/                # Claude-specific scoped rules, if used
│   └── agents/               # Claude-specific specialist agents, if useful
└── docs/
    ├── design-docs/
    └── exec-plans/
        ├── active/
        └── completed/
```

See [examples/agent-first-project/tree.md](examples/agent-first-project/tree.md). Do not create every directory just because an agent platform supports it; tool-specific paths and loading behavior differ.

### 8. Research or data project

Research projects often need to distinguish reusable analysis code, exploratory notebooks, data provenance, experiments, and generated outputs.

```text
research-project/
├── AGENTS.md                 # Reproduction, data, and research boundaries
├── README.md                 # Research question and how to reproduce results
├── src/                      # Reusable analysis and pipeline code
├── tests/                    # Tests for transformations and calculations
├── notebooks/                # Exploratory work and narrative analysis
├── data/
│   ├── README.md             # Provenance, access, and storage instructions
│   ├── raw/                  # Original inputs; often stored externally
│   └── processed/            # Derived data, usually reproducible
├── experiments/              # Configurations and tracked experiment results
└── reports/                  # Published figures and analysis outputs
```

See [examples/research-project/tree.md](examples/research-project/tree.md) for data-handling and reproducibility notes.

### 9. Repeatable agent workflows

Package a procedure when it recurs and its branching, validation, or supporting assets are worth maintaining separately from root instructions.

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

See [examples/repeatable-workflows/tree.md](examples/repeatable-workflows/tree.md). Use the skill location recognized by the project's actual tools.

### 10. Semantic project map

A map is useful when it explains ownership, entry points, dependency direction, or data flow that a directory listing cannot show.

```text
project/
├── README.md
└── docs/
    ├── project-map.md          # Semantic ownership and navigation
    └── architecture/
        ├── request-flow.md     # Important request path
        └── event-flow.md       # Important event relationships
```

See [examples/semantic-project-map/tree.md](examples/semantic-project-map/tree.md).

### 11. Organization-scale coordination

A central catalog becomes useful when many independently changing repositories or services make ownership and dependencies difficult to discover locally.

```text
engineering/
├── catalog/
│   ├── services.yaml           # Service identity and lifecycle
│   ├── ownership.yaml          # Ownership, only if no better source exists
│   └── dependencies.yaml       # Cross-service relationships
├── docs/
│   └── platform-map.md         # System-wide architecture
└── standards/
    ├── security.md
    └── operations.md
```

See [examples/organization-scale/tree.md](examples/organization-scale/tree.md). This is a separate engineering knowledge surface, not a folder to add to every application.

## How to maintain the examples

- Every example lives in `examples/<pattern>/tree.md` and contains a real Markdown directory tree plus notes for the paths shown.
- Explain what each important path owns, why it appears, when it is useful, and what can be omitted.
- Keep trees representative rather than exhaustive. Do not invent files just to make a tree look complete.
- When adding, renaming, or removing an example, update [examples/README.md](examples/README.md) and the relevant section above.
- Keep the reference-repository tree near the top of this file synchronized with the actual tree.

## Working principles

- Understand the project before proposing its structure.
- Give every persistent artifact a clear responsibility and audience.
- Prefer an existing owner over a new category.
- Let domain boundaries, not directory counts, determine instruction scope.
- Keep root instructions concise enough to orient; route detailed context to the right documents.
- Treat examples as adaptable patterns, never checklists.
- Preserve useful information when reorganizing and update references.
- Retire structure when the responsibility that justified it disappears.

For deeper reasoning, read [growth](docs/growth.md), [information ownership](docs/information.md), and [agent context](docs/agent-context.md). For a repository review, follow [the audit guide](docs/audit.md).
