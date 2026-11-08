# Organization Scale

Many teams own independently evolving services or repositories. Local README and AGENTS files are no longer enough to answer cross-cutting questions about ownership, dependencies, standards, and change impact.

This example represents a central engineering catalog repository, not a folder every application should copy.

## Example tree

```text
engineering/
├── catalog/
│   ├── services.yaml          # Service identity, lifecycle, and canonical owner
│   ├── ownership.yaml         # Team ownership when not maintained elsewhere
│   └── dependencies.yaml      # Cross-service dependency relationships
├── docs/
│   ├── platform-map.md        # System-wide domains and major flows
│   └── service-lifecycle.md   # Shared expectations for service ownership
├── standards/
│   ├── security.md            # Organization-wide security expectations
│   └── operations.md          # Shared operational requirements
└── CODEOWNERS                 # Review routing for this repository, if useful
```

## Notes

- **`catalog/services.yaml`** makes services discoverable by stable identity and lifecycle.
- **`catalog/ownership.yaml`** exists only if there is no better authoritative owner source. Do not maintain team ownership independently in a catalog, service manifest, and CODEOWNERS file.
- **`catalog/dependencies.yaml`** records cross-repository relationships when they cannot be reliably derived from source manifests.
- **`docs/platform-map.md`** explains the system at a level that individual repositories cannot.
- **`standards/`** holds shared guidance with a real cross-team audience and an owner responsible for keeping it current.
- **`CODEOWNERS`** routes review in GitHub. It is not automatically the full ownership registry.

## When this earns its cost

Use organization-level catalogs when there are many independently changing components, ownership is hard to infer, cross-team changes routinely require coordination, or local repository views cannot answer system-wide questions.

Do not introduce this structure because a company has many employees or because a catalog product is available. The topology itself must be a demonstrated coordination problem.

See [the monorepo example](../monorepo/tree.md) for a repository that still fits within local ownership.
