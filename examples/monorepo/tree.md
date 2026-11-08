# Monorepo

A repository contains multiple applications, services, or shared packages that are developed and released together or coordinated through a common workspace. The root explains the whole workspace; local instructions appear only where a component's needs differ.

## Example tree

```text
workspace/
├── AGENTS.md                         # Workspace-wide boundaries, commands, and navigation
├── README.md                         # What lives here and how to work across the workspace
├── workspace manifest                # Actual package/workspace definition for the toolchain
├── .github/
│   └── workflows/
│       └── ci.yml                    # Shared CI entry point, if CI is used
├── apps/
│   ├── web/
│   │   ├── AGENTS.md                 # Web-only conventions and browser validation, if distinct
│   │   ├── src/
│   │   └── tests/
│   └── admin/
│       ├── src/
│       └── tests/
├── services/
│   └── api/
│       ├── AGENTS.md                 # API contracts, migrations, and service-specific checks
│       ├── src/
│       └── tests/
├── packages/
│   ├── contracts/                   # Shared API, event, or schema contracts
│   └── ui/                          # Shared interface components
├── infra/                           # Shared infrastructure definitions, when centrally owned
└── docs/
    └── architecture.md              # Cross-workspace dependency direction and important flows
```

## Notes

- **Root `AGENTS.md`** describes workspace-level commands, package boundaries, shared conventions, and navigation. It should not contain every package's local instructions.
- **Workspace manifest** is the actual source of truth for package membership and dependency relationships. Use the language/toolchain's native workspace file rather than inventing a second catalog.
- **`apps/`** groups independently runnable user-facing applications. They may share packages but should not reach into each other's private implementation.
- **`services/`** groups independently deployable or operational services. A service gets local instructions when its contracts, validation, or operations differ from workspace defaults.
- **`packages/`** contains reusable libraries, contracts, or components. Shared code should have a clear owner and public interface; avoid making packages a dumping ground for cross-app imports.
- **Nested `AGENTS.md`** belongs only in areas with genuinely different commands, conventions, safety boundaries, or validation. `apps/admin/` deliberately has none while root guidance is sufficient.
- **`infra/`** belongs when infrastructure is managed as part of this workspace. A separate platform repository may be the better owner.
- **`docs/architecture.md`** explains dependency direction and cross-service flows that cannot be inferred reliably from the workspace manifest.

## Keep the workspace navigable

Use package manifests and workspace configuration as the source of truth for package membership and dependencies. Add a semantic map only when the relationships are not clear from those sources.

A monorepo is not automatically an organization-scale platform. Start with local ownership and interfaces; add catalogs and cross-repository governance only when local structure no longer answers the coordination questions.

See [semantic project map](../semantic-project-map/tree.md) and [organization scale](../organization-scale/tree.md).
