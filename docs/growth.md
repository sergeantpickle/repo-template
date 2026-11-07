# Growth Model

This document is normative.

Repository maturity is triggered by coordination needs, not by team size, line count, file count, or age. The levels below are diagnostic states, not achievements.

A repository can enter at any level and can move downward when complexity disappears.

## Level 0 — Seed

Typical baseline:

- project README;
- scoped agent instructions when coding agents are used;
- `.repo-standard.json` when adopting this standard;
- actual source/config/test files.

A changelog, project map, architecture doc, work directory, decision framework, research directory, and nested instructions are all conditional.

### Growth trigger

Advance only when a real responsibility repeatedly has no clean owner or coordination begins failing.

## Level 1 — Persistent work

Add task-scoped persistent work when substantial work must survive context loss.

### Trigger

At least one is true:

- the work spans sessions or agents;
- meaningful uncertainty or dependent steps must be tracked;
- validation state must survive context loss;
- continuation information would otherwise leak into README, changelog, or generic notes.

### Restraint

One persistent task does not justify a permanent handoff framework, archive taxonomy, roadmap hierarchy, or program-management layer.

### Procedure / skill trigger

A repeatable procedure may earn a skill or equivalent on-demand workflow when:

- the **how** matters across multiple tasks;
- the procedure is stable enough to version;
- it contains branching/validation steps that are costly to restate correctly;
- scripts, templates, fixtures, or reference assets belong with the procedure;
- keeping it out of always-loaded instructions materially reduces irrelevant context.

A one-off task, rapidly changing procedure, or generic advice does not justify a skill. Keep it in the task or prompt until repetition and stability are demonstrated.

A specialized subagent definition follows the same principle: create one when a repeated role, review lens, isolation boundary, or parallel-work pattern has stable value—not merely because the platform supports subagents.

## Level 2 — Durable knowledge

Add durable technical documentation or decision records when knowledge repeatedly matters beyond the task that discovered it.

### Durable-doc trigger

The information is non-obvious, repeatedly needed, and expensive or risky to reconstruct from code/configuration alone.

### Decision trigger

- credible alternatives existed;
- the choice creates a long-lived constraint;
- future maintainers could reasonably undo it without the rationale.

### Restraint

One decision document does not automatically justify a `decisions/` directory. One operations document does not automatically justify an `operations/` hierarchy.

## Level 3 — Domains

Split instructions and knowledge by subsystem when global context becomes noisy or misleading.

### Trigger

- subsystem-specific rules are irrelevant elsewhere;
- areas have materially different validation commands or boundaries;
- agents repeatedly apply one area's conventions to another;
- one document has developed several independently evolving responsibilities.

### Typical controls

- nested `AGENTS.md` or path-scoped rule mechanisms;
- domain-specific docs;
- explicit package/service ownership and boundaries.

### Restraint

Do not mirror the directory tree with nested instructions. Scope follows divergent responsibility, not path count.

## Level 4 — Mechanical governance

Move recurring deterministic rules into checks when convention alone is producing repeated defects or unacceptable risk.

### Trigger — RGS-ENFORCE-001

- the same rule is violated repeatedly, or one violation is sufficiently consequential;
- the condition is mechanically testable with acceptable false positives;
- the cost of violation exceeds the maintenance cost of enforcement;
- concurrency makes convention unreliable.

### Typical controls

Tests, linters, schema validation, boundary checks, hooks, permission controls, CI, generated freshness checks, or organization rulesets.

### Restraint

Do not automate hypothetical low-consequence failures merely because automation is possible.

## Level 5 — Organization scale

Introduce catalogs, ownership metadata, dependency policy, platform-level governance, or automated knowledge maintenance when topology itself becomes a coordination problem.

### Trigger

- many independently evolving domains/services exist;
- ownership cannot be inferred reliably;
- cross-domain change routinely requires coordination;
- local repository checks cannot enforce organization-wide invariants;
- discoverability and dependency direction are systemic bottlenecks.

This level is not a destination. Most repositories should never need it.

## Persistent-structure creation gate — RGS-GROW-001

Before creating a permanent file, directory, workflow, instruction layer, catalog, registry, or governance mechanism, answer these questions in order:

1. **Is persistence necessary?** If the information is cheap and safe to rediscover, keep it ephemeral.
2. **Does an existing owner already have jurisdiction?** Route or link instead of creating a second owner.
3. **Is the responsibility recurring or consequential?** One ordinary occurrence usually belongs to the current task.
4. **Can the new artifact state one bounded responsibility?** If not, the proposed artifact is probably another generic bucket.
5. **What is its lifecycle and retirement condition?** A permanent artifact with no update/retirement model is organizational debt at creation time.
6. **What is the lightest structure that works?** Prefer a section before a file, a file before a directory, and a local rule before an organization-wide system when scope permits.
7. **Will it enter hot agent context?** The broader the automatic loading scope, the higher the evidence threshold for adding content.
8. **Can an existing mechanical source own the fact?** Do not maintain prose that merely duplicates manifests, schemas, generated inventories, or other reliable machine-readable truth.

If the proposed structure cannot pass this gate, do not create it yet.

The gate is about responsibility, not numeric thresholds. Two artifacts can justify separation when their lifecycles are truly independent; ten artifacts can remain together when they still have one coherent owner.

## Directory growth rule

A directory should normally emerge from several independently useful artifacts sharing a lifecycle or retrieval scope. Do not create empty future categories as instructions to the agent about what it should eventually write.

## Regression is allowed — RGS-RETIRE-001

If a subsystem disappears, a workflow becomes trivial, or mechanical enforcement replaces a prose process, remove the structure that no longer earns its cost.
