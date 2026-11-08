# Agent Reference

A field guide for AI agents that build and maintain other repositories. Use these structures as references, not as a scaffold to copy wholesale.

## How to use this reference

1. Identify the project's shape and the coordination problem.
2. Find the closest tree below.
3. Open its linked `examples/<pattern>/tree.md` for the full annotated tree and notes.
4. Keep only paths that solve a real need.
5. Revisit the structure when the work or its boundaries change.

A project can combine patterns, begin at any point, or stay simpler than every example.

## This reference repository

```text
repo-template/
├── AGENTS.md                         # Structural reference and agent instructions
├── README.md                         # Human entry point
├── docs/
│   ├── growth.md                     # How and when structure evolves
│   ├── information.md                # Information ownership and lifecycles
│   ├── agent-context.md              # Instructions, skills, and agents
│   ├── audit.md                      # Checkpoints and contextual reviews
│   └── research.md                   # Observed patterns and sources
└── examples/
    ├── README.md                     # Example index
    └── <pattern>/tree.md             # Annotated structure and path notes
```

## Project structure references

### Small project

```text
project/
├── AGENTS.md                 # Shared agent context, when needed
├── README.md                 # Purpose, setup, and normal use
├── src/                      # Implementation
└── tests/                    # Behavior checks
```

See [seed-project](examples/seed-project/tree.md).

### Application or product

```text
product/
├── AGENTS.md
├── README.md
├── app/                      # Routes and user-facing screens
├── server/                   # Server behavior, if separate
├── db/                       # Schema and migrations, if owned here
├── tests/
└── docs/                     # Architecture or operations, when useful
```

See [application-project](examples/application-project/tree.md).

### Reusable library or SDK

```text
library/
├── AGENTS.md
├── README.md                 # Consumer quick start and public promises
├── src/library_name/         # Importable public package
├── tests/
├── examples/                 # Consumer usage
└── docs/                     # API guide, when the surface warrants it
```

See [library-project](examples/library-project/tree.md).

### Durable project knowledge

```text
project/
├── AGENTS.md                 # Map to deeper project context
├── README.md
├── src/
├── tests/
└── docs/
    ├── architecture.md
    ├── operations.md
    └── decisions/
```

See [growing-project](examples/growing-project/tree.md).

### Distinct domains and scoped instructions

```text
project/
├── AGENTS.md                 # Repository-wide rules
└── src/
    ├── api/AGENTS.md          # API-only contracts and checks
    ├── billing/AGENTS.md      # Billing-only invariants and checks
    └── shared/                # Root rules remain sufficient
```

See [scoped-instructions](examples/scoped-instructions/tree.md).

### Monorepo or workspace

```text
workspace/
├── AGENTS.md                 # Workspace-wide boundaries and navigation
├── apps/
│   ├── web/AGENTS.md          # Local rules only if they differ
│   └── admin/
├── services/
│   └── api/AGENTS.md
├── packages/
│   ├── contracts/
│   └── ui/
└── docs/architecture.md      # Cross-workspace relationships
```

See [monorepo](examples/monorepo/tree.md).

### Agent-first project

```text
agent-first-project/
├── AGENTS.md                 # Shared entry point and work boundaries
├── CLAUDE.md                 # Tool-specific entry, if required
├── src/
├── tests/
├── evals/                    # Agent behavior evaluations, when needed
├── .agents/skills/           # Shared skill source, if supported
├── .claude/rules/            # Claude-specific scoped rules
├── .claude/agents/           # Claude-specific specialists
└── .claude/skills -> ../.agents/skills/  # Optional verified alias
└── docs/
    ├── design-docs/
    └── exec-plans/           # Active/completed work, when needed
```

See [agent-first-project](examples/agent-first-project/tree.md).

### Research or data project

```text
research/
├── AGENTS.md                 # Data and reproducibility boundaries
├── README.md                 # Question, sources, reproduction steps
├── src/                      # Reusable analysis code
├── tests/
├── notebooks/                # Exploration and narrative analysis
├── data/                     # Provenance and staged inputs
├── experiments/
└── reports/                  # Published findings and figures
```

See [research-project](examples/research-project/tree.md).

## Cross-cutting structure patterns

### Repeatable procedures

```text
.agents/skills/<name>/
├── SKILL.md                  # Trigger and procedure
├── references/               # On-demand detail
├── scripts/                  # Deterministic helpers, if useful
└── assets/                   # Stable templates or fixtures, if needed
```

See [repeatable-workflows](examples/repeatable-workflows/tree.md). Use the location recognized by the project's actual agent tools.

### Semantic project map

```text
docs/
├── project-map.md            # Ownership, entry points, dependencies
└── architecture/
    ├── request-flow.md
    └── event-flow.md
```

See [semantic-project-map](examples/semantic-project-map/tree.md). A map should explain relationships that paths alone cannot.

### Organization-scale coordination

```text
engineering/
├── catalog/
│   ├── services.yaml
│   ├── ownership.yaml
│   └── dependencies.yaml
├── docs/platform-map.md
└── standards/
```

See [organization-scale](examples/organization-scale/tree.md). This is a separate engineering knowledge surface, not a folder every project needs.

## Keep the examples useful

- Every example lives in `examples/<pattern>/tree.md` and includes a directory tree with inline path notes.
- The notes explain responsibility, why a path exists, when it earns its place, and what can be omitted.
- Keep trees representative, not exhaustive. Do not invent files to make them look complete.
- Update [examples/README.md](examples/README.md) and this file when adding, renaming, or removing an example.

## Working principles

- Understand the project before proposing its structure.
- Give persistent artifacts clear responsibilities and audiences.
- Prefer an existing owner over a new category.
- Scope instructions where behavior differs; do not mirror every directory.
- Treat examples as adaptable patterns, never checklists.
- Preserve useful information when reorganizing; retire structure when its purpose disappears.

Read [growth](docs/growth.md), [information ownership](docs/information.md), and [agent context](docs/agent-context.md) when those topics matter. For a full review, follow [the audit guide](docs/audit.md).
