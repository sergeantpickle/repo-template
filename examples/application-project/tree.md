# Application Project

A single product repository with a user-facing application, server-side behavior, persistent data, and automated verification. This is a representative full-stack layout, not a framework prescription.

## Example tree

```text
product/
├── AGENTS.md                         # Project-wide agent context and working boundaries
├── README.md                         # What the product does, setup, and normal use
├── package.json                      # Or pyproject.toml / equivalent project manifest
├── .env.example                      # Names and safe placeholders for required settings
├── .github/
│   └── workflows/
│       └── ci.yml                    # Build and verification workflow, if CI is used
├── app/
│   ├── routes/                       # User-facing routes or page handlers
│   ├── components/                   # Reusable UI components
│   └── styles/                       # Application-level styling
├── server/
│   ├── domain/                       # Core business rules, when domain logic warrants separation
│   ├── services/                     # Application use cases
│   └── adapters/                     # Database, email, payment, and external-system integrations
├── db/
│   ├── schema/                       # Database schema or model definitions
│   └── migrations/                   # Ordered schema changes
├── tests/
│   ├── unit/                         # Isolated behavior
│   ├── integration/                  # Database and service boundaries
│   └── e2e/                          # Important end-to-end user journeys
└── docs/
    ├── architecture.md               # Important components, boundaries, and data flow
    └── operations.md                 # Deployment, recovery, and maintenance procedures
```

## Notes

- **Root `AGENTS.md`** holds project-wide conventions, exact commands, architecture boundaries, and links to deeper guidance. Add nested instruction files only when part of the application has meaningfully different rules.
- **Project manifest** names the real language and framework tooling. The example uses `package.json`; Python, Rust, Go, and other projects use their own manifests.
- **`app/`** is a common route-oriented web application shape. A CLI, desktop app, service, or mobile application will organize its entry points differently.
- **`server/`** is useful when server-side responsibilities have enough complexity to separate. A small application may keep handlers and business logic together.
- **`domain/`, `services/`, and `adapters/`** are boundaries, not mandatory layers. Do not create empty layers or move every function into a named architectural pattern.
- **`db/`** belongs when the application owns persistent schema and migrations. Use the database tool's normal migration location if it already defines one.
- **`tests/unit`, `integration`, and `e2e`** distinguish different verification costs and boundaries. A project can begin with one test directory and split only when the suite needs it.
- **`docs/architecture.md`** earns its place when system relationships are not obvious from code. **`docs/operations.md`** earns its place when operators need non-obvious recovery or maintenance knowledge.
- **`.env.example`** documents configuration names and safe placeholders. Never put secrets or live credentials in the repository.

## What to omit at first

A simple application may need only a README, one instruction file, its source, tests, and project configuration. Add domain layers, end-to-end tests, architecture docs, deployment docs, and migration directories when the application actually has those responsibilities.

## Related patterns

- [Seed project](../seed-project/tree.md) for a smaller starting point.
- [Growing project](../growing-project/tree.md) for durable knowledge.
- [Monorepo](../monorepo/tree.md) when the application becomes one of several independently evolving components.
