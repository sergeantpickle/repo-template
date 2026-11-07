# Changelog

This changelog records changes to the Repository Growth Standard itself. It is not a development log or handoff record.

## 0.1.0 - 2026-11-07

Initial draft standard.

### Standard model

- Defined canonical information ownership, explicit information lifecycles, progressive structural growth, evidence-based promotion, retirement, and mechanical enforcement.
- Added stable rule IDs and a machine-readable `rules.json` catalog with required/recommended/advisory levels and mechanical/heuristic/manual detection classes.
- Defined upstream adoption by semantic version rather than copying the full guide into every project.
- Defined explicit exceptions that reference known rule IDs and remain visible in audit output.

### Routing and growth

- Defined README, agent-instruction, changelog, active-work, durable-doc, decision, research, and Git/history jurisdictions.
- Treated permanent root HANDOFF/NOTES/LOG buckets as review smells rather than mandatory artifacts.
- Added Level 0-5 coordination triggers, including regression/removal when complexity disappears.
- Added optional project-map guidance so repositories do not maintain a duplicate tree unless semantic navigation repeatedly earns it.

### Examples

- Added recovery guidance for README/HANDOFF/CHANGELOG contamination.
- Added a seed-to-mature trajectory showing structure appearing only after triggers.
- Added a starting-at-twenty-files example demonstrating that file count is not maturity.
- Added project-map/index examples and restraint cases where the correct action is no new structure.

### Tooling

- Added `scripts/audit_project.py` with text/JSON output, strict mode, visible exceptions, structured manifest validation, routing heuristics, and instruction-copy drift warnings.
- Added `scripts/check_latest.py` to compare a project's adopted version with upstream `VERSION` without auto-adoption.
- Added a composite GitHub Action for pinned downstream audits and optional upstream version checks.
- Added focused unit tests and standard self-validation.

### Removed from the original scaffold

- Mandatory speculative architecture, plans, decisions, research, handoff, operations, quality, reference, generated-doc, and template directories.
- A permanent project-wide handoff requirement.
- The assumption that an upstream template is copied once and then evolves independently from its descendants.
