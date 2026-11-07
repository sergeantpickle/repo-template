# Information Routing

This document defines common artifact jurisdictions. A project does not need every artifact listed here.

The governing test is: **what lifecycle does this information have, and which existing artifact already owns that lifecycle?**

## Common owners

| Artifact | Owns | Must not become |
| --- | --- | --- |
| `README.md` | Project purpose, setup, normal usage, essential user/developer entry points | Handoff, work log, release diary, debugging notebook |
| `AGENTS.md` | Broad, non-derivable agent rules, exact commands, boundaries, routing cues | Repository encyclopedia, task state, historical narrative |
| `CHANGELOG.md` | Notable shipped changes, normally organized by release/version | Development log, TODO list, blocker list, handoff |
| Active work artifact | Objective, scope, progress, discoveries, validation state, blockers, next action for one bounded body of work | Permanent repository policy or system reference |
| Durable technical documentation | Current system behavior, contracts, operations, or non-obvious reference that is expensive to rediscover | Planned future behavior presented as current truth |
| Decision record | Rationale for a durable, non-obvious choice where credible alternatives existed | General meeting notes or every implementation choice |
| Research artifact | Evidence, experiments, and sources that must survive the task because reproduction is expensive or consequential | Scratchpad for ordinary exploration |
| Git history / issue / PR | Raw chronology, discussion, review, diffs, and provenance | Current project documentation |

## Handoffs

A permanent repository-wide `HANDOFF.md` is high-risk because its natural responsibility is unbounded.

For work that spans sessions or agents, the active work artifact should normally contain the continuation state: completed work, remaining work, validation, blockers, and the exact next action.

Create a separate handoff only when there is a real continuation boundary not already represented by the work artifact. Scope it to that boundary and retire it when it no longer has continuing value.

## Notes and logs

Generic `NOTES.md` and `LOG.md` files are ambiguous owners. They tend to accumulate unrelated lifecycles.

Before creating one, classify the information:

- current system truth → durable documentation;
- active task discovery → active work artifact;
- durable rationale → decision record;
- release-facing history → changelog;
- raw chronology → Git/issues/PRs;
- reproducible investigation evidence → research artifact;
- disposable exploration → do not persist it.

## Routing decision

Before writing durable information:

1. Identify its lifecycle: current truth, active work, history, evidence, or rule.
2. Find the existing canonical owner for that lifecycle.
3. If an owner exists, update it or link to it.
4. If no owner exists, apply `docs/growth.md` before creating a new persistent artifact.
5. If the information can be regenerated cheaply and safely, prefer regeneration over storage.

## Duplication

Do not solve discoverability by copying the same paragraph into multiple documents.

Improve navigation, add a concise link, or add a small routing cue. If a tool requires a duplicate instruction file, prefer symlinks, generated files, imports, or drift checks where the toolchain supports them.
