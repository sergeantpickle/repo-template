# Agent Instructions

This repository is the upstream Repository Growth Standard. It is not a normal project scaffold.

## Read first

For changes to this repository, read:

1. `README.md` for the role of the repository.
2. `STANDARD.md` for normative rules.
3. `docs/evidence.md` when changing guidance that depends on current agent behavior or tooling.
4. The relevant document under `docs/` for the area being changed.

## Change discipline

- Keep normative rules in `STANDARD.md` or a document it explicitly delegates to.
- Keep examples non-normative. An example demonstrates judgment; it does not create a requirement.
- Do not add a new permanent category, directory, or workflow because it might be useful someday. Apply the growth triggers in `docs/growth.md` first.
- Prefer one file before a directory. Split only when independent responsibilities, lifecycles, or retrieval needs justify it.
- Do not duplicate rules across documents. Link to the canonical owner.
- When a rule can be checked deterministically and repeated violations justify the cost, prefer tooling over additional prose.
- Treat model- and tool-specific advice as fast-moving. Verify current sources before changing it.

## Versioning

Any normative change must update `VERSION` and `CHANGELOG.md` in the same change:

- MAJOR: incompatible governance, routing, or adoption semantics.
- MINOR: a new normative rule, lifecycle, or materially expanded requirement.
- PATCH: clarification, example, evidence refresh, or tooling change that does not alter normative meaning.

## Validation

Run:

```bash
python scripts/check_standard.py
```

When changing project-audit behavior, also exercise:

```bash
python scripts/audit_project.py starter
```
