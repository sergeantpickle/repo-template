# Semantic Project Map

A repository has enough moving parts that an agent cannot reliably infer ownership, data flow, or change impact from filenames alone. A map adds relationships rather than repeating the directory listing.

## Example tree

```text
project/
├── AGENTS.md
├── README.md
├── src/
│   ├── gateway/
│   ├── billing/
│   └── notifications/
└── docs/
    ├── project-map.md           # Ownership, entry points, dependencies, and boundaries
    └── architecture/
        ├── request-flow.md      # How a request crosses the system
        └── event-flow.md        # Which components publish and consume events
```

## Notes

- **`docs/project-map.md`** answers navigation questions that the directory tree cannot: who owns a capability, where execution starts, what depends on what, and where validation differs.
- **`docs/architecture/request-flow.md`** and **`event-flow.md`** explain specific flows that are important enough to understand independently.
- **`README.md`** points readers to the map when it is useful; it does not duplicate the map.
- **`AGENTS.md`** routes agents to the map before structural or cross-domain changes.

## What makes a map useful

A useful map explains semantic relationships and links to authoritative code, configuration, or documentation. It does not try to list every file or duplicate package manifests.

Start with a short section in README or an existing architecture document. Give the map its own file only when it has enough content and an independent update responsibility.

See [the growing-project example](../growing-project/tree.md) for a smaller documentation layout.
