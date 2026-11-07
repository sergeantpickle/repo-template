# Example: From One Maintainer to Organization Scale

This example uses people/agent counts only to make the coordination pressure intuitive. The numbers are **not thresholds**. A repository grows when the pressure appears, not when a headcount counter changes.

## One maintainer or one primary agent

Typical pressure: almost none. The person/agent can reconstruct most context directly.

Useful structure may be only:

- README;
- local agent instructions;
- source/tests/configuration;
- standard adoption manifest.

Failure mode to avoid: building a future company's bureaucracy before the first recurring coordination problem exists.

## A few concurrent contributors or agents

New pressure:

- work survives individual context windows;
- two actors can touch the same area with different assumptions;
- current task state needs a bounded owner.

Possible growth:

- task-scoped persistent work;
- exact validation commands;
- branch/issue/PR discipline if concurrency needs it.

Do not automatically add architecture councils, global roadmaps, or permanent handoff files.

## Several independently evolving areas

New pressure:

- frontend/backend/data/infra rules diverge;
- global instructions become noisy;
- one team's conventions leak into another area;
- validation paths differ.

Possible growth:

- scoped/nested agent instructions;
- domain-level durable docs;
- explicit boundaries and ownership;
- dependency-direction checks if repeated mistakes justify them.

The trigger is divergent responsibility, not a package-count threshold.

## Dozens of parallel workstreams

New pressure:

- repeated cross-domain mistakes;
- reviewers cannot manually remember every invariant;
- duplicated instructions begin drifting;
- deployment/release/compatibility rules become expensive to enforce by memory.

Possible growth:

- mechanical boundary checks;
- generated inventories;
- reusable CI;
- centralized policy for genuinely shared invariants;
- explicit exception mechanisms;
- service/package ownership metadata.

Do not centralize rules that remain genuinely local.

## Hundreds of independently changing components

New pressure:

- repository/service topology is hard to discover;
- ownership becomes non-obvious;
- local documentation cannot answer organization-wide dependency questions;
- policy rollout and exception review become systems problems.

Possible growth:

- software/service catalog;
- organization-level rulesets;
- dependency/ownership graph;
- policy-as-code;
- automated drift reporting;
- standardized interfaces between domains.

At this point a catalog can earn existence because the topology itself is now expensive to reconstruct.

## Thousands of contributors/agents or organization-scale automation

New pressure:

- policy changes must propagate without copying prose everywhere;
- central standards need versions and migrations;
- exceptions need ownership and review dates;
- governance itself requires observability;
- changes to the control plane can affect many repositories.

Possible growth:

- versioned upstream standards;
- centrally managed reusable enforcement;
- adoption telemetry;
- exception inventories;
- migration tooling;
- policy change review and staged rollout;
- automated knowledge gardening.

The control plane is now a product with its own reliability requirements.

## The important inversion

The mature organization is not defined by having every item above.

It is defined by having **earned controls for the coordination failures it actually experiences** and by removing controls whose pressure disappears.

A one-person safety-critical system can need Level 4 mechanical governance immediately. A 5,000-person organization can still have a tiny utility repository that remains Level 0 or Level 1.
