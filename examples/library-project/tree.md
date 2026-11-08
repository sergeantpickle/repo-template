# Library or SDK Project

A reusable library has a public interface and external consumers. Its repository should make the package boundary, compatibility expectations, tests, examples, and release process easy to find.

This example uses a Python-style package layout. The same responsibilities apply to libraries in other languages, with their native source and package conventions.

## Example tree

```text
library/
├── AGENTS.md                         # Contributor guidance, boundaries, and exact checks
├── README.md                         # What consumers install and how they get started
├── pyproject.toml                    # Package metadata, dependencies, and tool configuration
├── CHANGELOG.md                      # Consumer-facing release history, if releases warrant it
├── .github/
│   └── workflows/
│       ├── ci.yml                    # Supported-version tests and quality checks
│       └── release.yml               # Publishing workflow, if the package is published here
├── src/
│   └── library_name/
│       ├── __init__.py               # Deliberate public exports
│       ├── client.py                 # Main public client or entry point
│       ├── types.py                  # Public types and contracts
│       └── internal/                 # Implementation not promised as public API
├── tests/
│   ├── test_client.py                # Public behavior and contract tests
│   ├── test_types.py                 # Type and serialization behavior
│   └── fixtures/                     # Reusable test inputs
├── examples/
│   ├── quickstart.py                 # Small, runnable consumer example
│   └── advanced_usage.py             # More involved integration example
├── docs/
│   ├── getting-started.md            # Consumer setup and first use
│   └── api/                          # Expanded API reference, when the surface is broad
└── benchmarks/
    └── README.md                     # Performance methodology, only if performance is a promise
```

## Notes

- **`src/library_name/`** is the importable package. Keep the public surface deliberate; internal modules should not accidentally become compatibility promises.
- **`README.md`** is for consumers. It should answer what the library does, how to install it, and how to perform the common task.
- **`tests/`** should protect public behavior and compatibility, not only implementation details. A test matrix for supported language/runtime versions may be more valuable than a large internal test taxonomy.
- **`examples/`** contains runnable examples that help consumers understand the library. It is not a place for scratch scripts or duplicate test fixtures.
- **`docs/api/`** is useful when the public API is too large for the README. Generated reference should identify its source and generation method.
- **`CHANGELOG.md`** helps when downstream users need to understand breaking changes and upgrade paths. A small internal library may rely on Git history instead.
- **`release.yml`** belongs only when this repository actually publishes the package. Publishing credentials and approval boundaries should be handled by the release environment.
- **`benchmarks/`** earns a directory when performance is a supported contract or a recurring engineering concern. Otherwise keep a focused benchmark near the code or omit it.

## What changes as the library grows

Several packages may justify a monorepo layout. Multiple public API areas may justify separate API documentation. Complex compatibility promises may justify a support matrix and migration guides. None of those are required simply because the project is called an SDK.

## Related patterns

- [Growing project](../growing-project/tree.md) for durable decisions and architecture.
- [Monorepo](../monorepo/tree.md) when several packages evolve together.
- [Repeatable workflows](../repeatable-workflows/tree.md) for reusable release or compatibility procedures.
