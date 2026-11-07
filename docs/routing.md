# Information Routing

This document is normative.

The first routing question is not "which file is convenient?" It is **what lifecycle does this information have, and which artifact owns that lifecycle?**

## Common owners

| Artifact | Canonical responsibility | Must not silently become |
| --- | --- | --- |
| `README.md` | Project purpose, setup, normal usage, essential human-facing entry points | Handoff, blocker list, work log, release diary, debugging notebook |
| `AGENTS.md` | Broad non-derivable agent rules, exact commands, boundaries, routing cues for its scope | Active task state, repository encyclopedia, historical narrative |
| `CHANGELOG.md` | Notable shipped changes for release consumers, when the project has an audience for release history | Development diary, TODO list, blocker list, handoff |
| Active work artifact | Objective, scope, progress, discoveries, validation state, blockers, exact next action for one bounded body of work | Permanent project policy or current-system reference |
| Durable technical doc | Current non-obvious behavior, contracts, operations, or reference that is expensive/risky to rediscover | Planned future behavior presented as shipped truth |
| Decision record | Rationale for a durable non-obvious choice where credible alternatives existed | Every implementation choice or general meeting notes |
| Research artifact | Evidence/experiments that must survive the task because reproduction is expensive or consequential | Ordinary scratchpad |
| Git / issue / PR | Raw chronology, diffs, discussion, review, provenance | Canonical current project documentation |

A project does not need every artifact in this table.

## README routing — RGS-ROUTE-README-001

README owns introduction and normal usage. If it starts accumulating "current state", "next steps", blockers, implementation progress, or old session summaries, classify and move that information instead of accepting the new responsibility by precedent.

## Changelog routing — RGS-ROUTE-CHANGELOG-001

CHANGELOG owns shipped change history when release history is useful. Attempted fixes, abandoned approaches, unfinished work, and session summaries belong elsewhere or nowhere durable.

## Active work

The active work artifact normally owns continuation state. That includes the information a future agent needs to resume the bounded task.

The project may use a Markdown plan, an issue, an OpenSpec change, or another system. The standard cares about the ownership boundary, not the filename.

## Handoffs — RGS-ROUTE-HANDOFF-001

A permanent repository-wide `HANDOFF.md` is a growth smell because its natural scope is unbounded.

Create a separate handoff only when a real transfer boundary is not already represented by the active work system. Give it a bounded scope and a retirement condition.

## Generic buckets — RGS-ROUTE-BUCKET-001

Generic `NOTES.md` and `LOG.md` files easily accumulate unrelated lifecycles.

Before creating or appending to one, classify the content:

- current system truth -> durable documentation;
- active discovery -> active work artifact;
- durable rationale -> decision record;
- shipped release history -> changelog;
- raw chronology -> Git/issues/PRs;
- reproducible consequential investigation -> research artifact;
- disposable exploration -> do not persist.

## Project maps / indexes

A project map is optional. It earns existence when semantic relationships, ownership, entry points, or validation paths are repeatedly expensive to reconstruct from the repository itself.

A map that merely restates the tree creates another freshness obligation without adding knowledge.

See `examples/project-map.md`.

## Duplication

Do not solve discoverability by copying paragraphs into several documents. Improve navigation or add a concise link.

When a coding tool requires its own instruction surface, make tool-specific differences explicit. Prefer adapters, generation, symlinks/imports, or drift checks when supported.
