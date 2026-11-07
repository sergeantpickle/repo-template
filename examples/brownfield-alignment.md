# Example: Brownfield Alignment Without Rewriting the Repository

An existing project already has code, README, CI, several docs, and its own agent instructions. The goal is to align with the growth standard without forcing the project into the starter layout.

## 1. Review before alignment

From a checkout of the standard:

```bash
python scripts/audit_project.py /path/to/project --pre-alignment
```

Do not create `.repo-standard.json` yet. First inspect the heuristic findings and perform the contextual review from `docs/audit.md`.

## 2. Inventory existing owners

For each persistent organizational artifact, record:

- lifecycle;
- current responsibility;
- whether another artifact overlaps that responsibility;
- whether the artifact is still earning its maintenance cost.

Existing structures are evidence. Do not rename or replace them merely because the standard's examples use different filenames.

## 3. Repair clear routing failures

Example findings might include:

- README carrying active blockers;
- a global HANDOFF with several generations of finished work;
- independent AGENTS/CLAUDE copies that have drifted;
- a docs directory whose categories no longer match actual project responsibilities.

Prefer moving/deleting stale information over adding new structure.

## 4. Decide deviations

If an existing structure is healthy but differs from a recommended rule, record an explicit exception only when an actual audit finding/rule requires it. Do not create exceptions for harmless filename differences.

## 5. Add alignment state

Add `.repo-standard.json` with the source and last-aligned version and any justified exceptions.

Do not replace the project's README or AGENTS with files from `starter/`. The starter is for greenfield export.

## 6. Pin the auditor

If the project uses GitHub Actions, pin the standard action to the reviewed commit/tag corresponding to the last-aligned version. The pinned action should match the manifest version.

## 7. Re-run as an aligned project

```bash
python scripts/audit_project.py /path/to/project --strict --require-version-match
```

Heuristic warnings still require judgment. Strict mode means unresolved active warnings fail the check; it does not convert heuristics into facts.

## Result

The project keeps its own identity and structure. Alignment adds a governance reference and audit capability, not a second repository architecture.
