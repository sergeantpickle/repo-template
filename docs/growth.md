# Growth Model

Repository maturity is triggered by coordination needs, not by team size, line count, or age.

A one-person repository can legitimately need advanced controls. A large repository can remain structurally simple when responsibilities stay clear.

## Level 0 — Seed

Typical structure:

- `README.md`;
- `AGENTS.md` when coding agents are used;
- `.repo-standard.json` when adopting this standard;
- `CHANGELOG.md` only when the project has releases or user-visible version history worth maintaining.

Add nothing else by default.

### Advance when

- work repeatedly survives beyond one session or agent;
- information begins landing in the wrong artifact because no scoped owner exists.

## Level 1 — Persistent work

Add a task-scoped work artifact when substantial work needs durable execution state.

A project may use a single `work/` or `plans/` location, issues, or another existing system. The filename and directory are less important than the ownership boundary.

### Trigger

At least one of these is true:

- the task spans sessions or agents;
- the task has material uncertainty or multiple dependent steps;
- validation state must survive context loss;
- continuation information would otherwise leak into README, changelog, or generic notes.

### Do not add

A permanent handoff system, plan archive, roadmap hierarchy, or program-management taxonomy merely because one task needed persistence.

## Level 2 — Durable knowledge

Add durable technical documentation or decision records when knowledge repeatedly matters beyond the task that discovered it.

### Trigger for durable documentation

The information is non-obvious, repeatedly needed, and expensive or risky to rediscover from code/configuration alone.

### Trigger for a decision record

- credible alternatives existed;
- the choice creates a long-lived constraint;
- a future maintainer or agent could reasonably undo it without knowing the rationale.

### Do not add

A directory for a category that contains only one small document unless the directory itself provides real scoping or tool behavior.

## Level 3 — Domains

Split instructions and documentation by subsystem when global context becomes noisy or different areas genuinely have different rules.

### Trigger

- subsystem-specific rules are irrelevant elsewhere;
- different areas have distinct validation commands or architectural boundaries;
- agents repeatedly apply one area's conventions to another;
- a single durable document has multiple independent owners or retrieval paths.

### Typical controls

- nested `AGENTS.md` or path-scoped rules;
- domain-specific documentation;
- explicit package/service boundaries.

### Do not add

Nested instructions simply to mirror the directory tree.

## Level 4 — Mechanical governance

Move recurring rules into deterministic checks when convention alone is producing repeated defects or unsafe behavior.

### Trigger

- the same rule is violated repeatedly;
- the rule is mechanically testable;
- the cost of violation exceeds the maintenance cost of enforcement;
- concurrency makes manual discipline unreliable.

### Typical controls

- tests and linters;
- architecture/boundary checks;
- schema validation;
- hooks and permission rules;
- CI checks;
- generated inventories or drift checks.

### Do not add

Automation for hypothetical failures that have not occurred and carry low consequence.

## Level 5 — Organization scale

Introduce catalogs, ownership metadata, dependency policy, platform-level governance, or automated knowledge maintenance when repository topology itself becomes a coordination problem.

### Trigger

- many independently evolving domains/services exist;
- ownership cannot be inferred reliably;
- cross-domain changes routinely require coordination;
- local checks cannot enforce organization-wide invariants;
- discoverability and dependency direction become systemic bottlenecks.

This level is not a destination. Most repositories should never need it.

## Regression is allowed

A repository may move down the model.

If a subsystem disappears, a workflow becomes trivial, or enforcement replaces a prose process, remove the structure that no longer earns its maintenance cost.
