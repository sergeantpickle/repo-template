# Scoped Instructions

A project has distinct areas with different conventions, validation commands, or safety boundaries. Nested instructions keep local rules close to the work they govern.

## Example tree

```text
project/
├── AGENTS.md                 # Rules shared by the whole repository
└── src/
    ├── api/
    │   ├── AGENTS.md         # API contracts, routing, and API-specific checks
    │   └── ...
    ├── billing/
    │   ├── AGENTS.md         # Financial invariants and billing test commands
    │   └── ...
    └── shared/
        └── ...               # Uses root rules; no local file without a real need
```

## Notes

- **Root `AGENTS.md`** owns rules that apply across the repository: project purpose, global boundaries, common commands, and links to deeper context.
- **`src/api/AGENTS.md`** exists because API work has distinct contracts and validation. It should contain only the local differences and point back to shared guidance.
- **`src/billing/AGENTS.md`** exists because billing has special correctness or safety constraints that do not apply everywhere.
- **`src/shared/`** deliberately has no nested instruction file. A directory is not a reason to add one.

Codex and GitHub Copilot support nested AGENTS.md files, but discovery and precedence differ across agent harnesses. Check the target tool's current behavior before relying on inherited instructions. Some tools use their own rule files or path-matching configuration.

## Common mistake

Do not mirror the source tree with an AGENTS.md in every folder. That produces repeated, contradictory, or low-value instructions. Scope follows differences in responsibility, not directory depth.

See [the monorepo example](../monorepo/tree.md) for several independently evolving applications and services.
