# Example: Recovering from README / HANDOFF / CHANGELOG Sprawl

## Starting state

The project has three long-lived Markdown files:

- `README.md` — setup plus current progress, old release notes, blockers, and debugging discoveries;
- `HANDOFF.md` — hundreds of lines covering completed features, current tasks, architecture observations, and old next steps;
- `CHANGELOG.md` — a short release history mixed with attempted fixes and session notes.

The problem is not that one file is long and another is short. The problem is that all three have overlapping jurisdiction.

## Step 1 — classify by lifecycle

For every meaningful section, classify it as:

- current project truth;
- active bounded work;
- release-facing history;
- durable rationale/reference;
- raw historical chronology;
- disposable exploration.

Do not choose a destination until the lifecycle is known.

## Step 2 — restore canonical owners

README keeps project purpose, setup, and normal usage.

CHANGELOG keeps notable shipped changes appropriate to the project's users/release consumers.

Current progress, validation state, blockers, and next action move into the active task artifact.

Durable non-obvious system knowledge moves only if it is still useful and expensive to rediscover.

Raw chronology stays in Git/issues/PRs. Disposable debugging notes are deleted.

## Step 3 — retire the global handoff

Once useful content has been promoted or routed, remove `HANDOFF.md` unless it has a newly defined bounded responsibility.

Do not replace it with a more complicated global handoff framework.

## Step 4 — add enforcement only after recurrence

If agents later put active state into README again, add a routing reminder or a heuristic audit check. If the mistake repeats and becomes mechanically detectable with acceptable false positives, strengthen the check.

The recovery goal is restored jurisdiction, not maximum documentation.
