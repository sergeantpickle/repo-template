# Information Lifecycle

This document is normative.

Repository information has a lifecycle. Routing decisions become much easier when an agent identifies the lifecycle before choosing a file.

## RGS-LIFE-001 — Keep lifecycles distinguishable

The standard recognizes five useful states.

### Ephemeral

Scratch reasoning, temporary exploration, transient command output, and information that is cheap to rediscover.

Default action: do not commit it.

### Active

Information required to complete a bounded body of work: objective, progress, discoveries, validation state, blockers, and next action.

Default owner: the active work artifact or existing issue/change system.

Active information has a retirement condition. It must not quietly become permanent repository policy because work lasted a long time.

### Durable current

Knowledge that describes the project as it exists now and is costly, risky, or repeatedly wasteful to rediscover.

Examples include non-obvious operational procedures, current contracts, system boundaries, and durable development constraints.

Durable current information must be updated when the truth it describes changes.

### Historical

Information preserved to explain what changed or why an old path existed, without claiming to describe current truth.

Examples include release history, completed work records, superseded decisions, Git history, issues, and pull requests.

Historical information should remain out of the default context path unless it is relevant to the task.

### Mechanical

Executable or machine-checked truth: tests, schemas, linters, permissions, hooks, CI, generated checks, and configuration that directly constrains behavior.

Mechanical controls can outrank prose for the narrow fact they actually enforce. They do not automatically explain why the rule exists.

## RGS-PROMOTE-001 — Promote through evidence

Typical transitions are:

```text
ephemeral observation
  -> active work discovery
  -> durable current knowledge
  -> mechanical enforcement
```

A transition requires evidence that the next level earns its maintenance cost.

Promotion into **durable current** knowledge should normally follow validation appropriate to the underlying change. Do not let an unverified implementation automatically teach future agents that its behavior is intended truth. When validation is incomplete, keep the claim in active work or mark its uncertainty explicitly.

Examples:

- One failed migration stays in the task record.
- The same non-obvious migration ordering requirement repeatedly matters, so it becomes durable guidance.
- The ordering can be detected reliably, so CI eventually enforces it.

Promotion must not leave unnecessary duplicate copies behind.

## RGS-RETIRE-001 — Retirement is part of maintenance

Useful reverse transitions include:

```text
active -> historical -> deleted
current -> superseded/historical -> deleted
prose rule -> mechanical control + smaller explanation
category -> merged into simpler owner
```

When information is promoted, demoted, superseded, or mechanically enforced, review the previous owner. Remove stale copies instead of keeping every layer forever.

## Authority during conflict

When two artifacts disagree, first identify what each one is allowed to claim.

For current behavior, executable code, configuration, tests, schemas, and observed runtime evidence describe what currently happens. Durable documentation may describe intended behavior and should be repaired when it is stale.

Active work describes intended or in-progress change, not shipped truth. Historical artifacts explain prior state and must not override current state merely because they are detailed.
