# Quick Examples

These examples are non-normative. They demonstrate application of the standard; they do not create requirements.

Longer trajectories live under `examples/`.

## README contamination

Observed: README contains setup, current progress, unfinished TODOs, prior release summaries, blockers, and next-agent instructions.

Action: keep purpose/setup/normal usage in README; route shipped history to changelog when useful; route active state to the bounded work artifact; promote only durable non-obvious discoveries; delete obsolete debugging narrative.

Growth: none. The first fix is jurisdiction, not another category.

## HANDOFF.md becomes enormous

Observed: a permanent HANDOFF covers several completed features, old blockers, architecture notes, release notes, and current work.

Action: move current continuation state into the active work owner, promote durable knowledge, leave raw history to Git/issues/PRs, and retire the handoff when it no longer has a bounded transfer purpose.

Growth: persistent task state may be justified; a larger handoff framework is not.

## CHANGELOG becomes a development diary

Observed: changelog contains attempted fixes, abandoned approaches, blockers, TODOs, and session summaries.

Action: retain notable shipped changes only. Route active state elsewhere.

Growth: none.

## One architecture discussion occurs

Wrong response: create an architecture directory, index, ADR framework, and architecture-review workflow.

Better response: keep the task-level choice in active work. Promote only if it later becomes a durable non-obvious boundary.

## A decision keeps being rediscovered

Observed: several agents independently question the same technology choice and repeatedly reconstruct the same constraints.

Action: create one decision record. Link to it instead of repeating the rationale.

Growth: one decision file first; a decisions directory only after multiple independent decisions justify it.

## Rule graduates into enforcement

Observed: agents repeatedly forget to regenerate derived clients after schema changes.

Progression: fix task -> concise durable rule if needed -> deterministic stale-generation check -> shrink redundant prose once enforcement is reliable.

## A document reaches 500 lines

Wrong response: split solely because of size.

Better response: split only if it now contains independently evolving responsibilities or retrieval paths.

Size is pressure, not jurisdiction.

## Starting at twenty files

File count does not determine maturity. A project can begin with source, tests, CI, deployment, and generated files while still needing only README, scoped agent rules, and the standard adoption manifest.

See `../examples/starting-at-twenty.md`.

## Detailed trajectories

- `../examples/seed-to-mature.md`
- `../examples/starting-at-twenty.md`
- `../examples/recovering-from-sprawl.md`
- `../examples/project-map.md`
- `../examples/organization-scale.md`
