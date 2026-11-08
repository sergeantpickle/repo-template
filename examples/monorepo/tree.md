# Monorepo

A repository contains multiple applications, services, or shared packages that can evolve independently. The root file describes the whole workspace; local instructions appear only where teams or components need different guidance.

## Example tree

```text
workspace/
├── AGENTS.md                  # Workspace-wide boundaries and navigation
├── README.md                  # What the workspace contains and how to start
├── apps/
│   ├── web/
│   │   ├── AGENTS.md          # Web app commands, UI conventions, browser checks
│   │   └── src/
│   └── admin/
│       └── src/               # Uses root guidance until local rules diverge
├── services/
│   └── api/
│       ├── AGENTS.md          # Service contracts, migrations, API validation
│       └── src/
└── packages/
    ├── contracts/             # Shared API and event contracts
    └── ui/                    # Shared interface components
```

## Notes

- **Root `AGENTS.md`** explains workspace-wide commands, dependency boundaries, shared conventions, and where domain-specific instructions live.
- **`apps/web/AGENTS.md`** captures browser/UI-specific validation and local conventions that do not apply to the API.
- **`services/api/AGENTS.md`** captures service-specific commands, API contracts, data migrations, and operational constraints.
- **`apps/admin/`** inherits root guidance because its conventions still match the workspace defaults.
- **`packages/contracts/`** and **`packages/ui/`** do not receive nested instructions automatically. Add them only if the packages have independent rules, owners, or validation.

## Keep the workspace navigable

Use package manifests and workspace configuration as the source of truth for package membership and dependencies. Add a semantic map only when the relationships are not clear from those sources.

A monorepo is not automatically an organization-scale platform. Start with local ownership and interfaces; add catalogs and cross-repository governance only when local structure no longer answers the coordination questions.

See [semantic project map](../semantic-project-map/tree.md) and [organization scale](../organization-scale/tree.md).
