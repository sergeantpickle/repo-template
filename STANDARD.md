# Repository Growth Standard

Version: **0.1.0**  
Status: **Draft**

## Purpose

This standard controls how AI-primary repositories accumulate instructions, documentation, work state, history, and enforcement as they grow.

Its purpose is not to maximize documentation. Its purpose is to prevent ambiguous ownership and uncontrolled structural growth.

## 1. One canonical owner

Each class of durable information must have one canonical owner.

If the same fact is useful elsewhere, link to the owner. Do not maintain parallel copies unless a tool requires one and the duplication is generated or mechanically checked.

When two artifacts appear to own the same information, resolve the ownership conflict instead of adding synchronization instructions.

## 2. Separate current truth, active work, and history

Repositories must distinguish:

- **current truth** — how the project works now;
- **active work** — what is being changed, discovered, blocked, or validated now;
- **history** — what changed or why an old path existed.

A document must not silently become responsible for more than one of these lifecycles.

README content, release history, active-task state, and historical implementation narrative are different responsibilities even when they concern the same feature.

## 3. Earn permanent structure

Do not create persistent files or directories merely because a mature repository might eventually need them.

Create structure when an observed responsibility has no clean owner, is likely to recur, and has enough durable value to justify maintenance cost.

Use the lightest artifact that solves the demonstrated problem. A single document should precede a directory unless multiple independently useful documents already justify the directory.

## 4. Persist what is expensive to rediscover

Do not store information merely because an agent can write it down.

Durable repository knowledge should primarily capture information that is:

- non-obvious from code and configuration;
- repeatedly needed;
- expensive or risky to rediscover;
- required to explain a durable constraint;
- necessary for reproducible operation or validation.

Repository maps that merely restate an easily inspected tree should not be maintained by default.

## 5. Promote through evidence

New information should normally begin in the narrowest relevant scope.

A useful progression is:

1. task-local observation;
2. repeated or consequential lesson;
3. durable project rule or reference;
4. deterministic enforcement when the rule is mechanically checkable and violations justify it.

Promotion is not automatic. A one-time incident can remain historical without becoming permanent policy.

## 6. Retire and demote

Growth control includes deletion.

When a rule becomes obsolete, an artifact loses its responsibility, or mechanical enforcement makes explanatory process text unnecessary, simplify or remove the old structure.

Historical value alone does not justify keeping every intermediate artifact in the hot path for future agents.

## 7. Keep always-loaded instructions small

Persistent agent instructions should contain only high-value, non-derivable rules and routing cues that apply broadly.

Task procedures, subsystem-specific rules, and long references should load only when relevant through the mechanisms supported by the active coding tool.

Do not force every task to read a full repository map or stack of documentation before trivial work.

## 8. Move hard requirements toward enforcement

Instruction files guide agent behavior; they are not reliable enforcement boundaries.

Repeated, deterministic, safety-critical, or correctness-critical requirements should move toward tests, linters, schemas, hooks, permissions, CI, generated checks, or other mechanical controls when practical.

## 9. The upstream standard is not copied wholesale

Projects adopt this standard by version. They do not mirror this repository's full structure.

A project may keep a small local adoption manifest and project-specific agent instructions. The normative growth rules remain upstream.

Projects must not silently adopt an upstream change. Standard updates are reviewed and adopted deliberately.

## 10. Exceptions are explicit

A project may deviate from this standard when its needs justify the deviation.

Material deviations should be recorded with a scoped reason. An exception is preferable to distorting the standard or duplicating structure solely to appear compliant.

## Delegated normative guidance

The following documents are part of the standard:

- `docs/routing.md` — artifact jurisdiction and ownership.
- `docs/growth.md` — triggers for adding organizational structure.
- `docs/adoption.md` — downstream adoption, audit, versioning, and exceptions.

`docs/examples.md` and `docs/evidence.md` are explanatory and evidentiary, not independently normative.
