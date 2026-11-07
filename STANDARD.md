# Repository Growth Standard

Version: **0.1.0**  
Status: **Active**

## Purpose

This standard controls how AI-primary repositories accumulate instructions, documentation, work state, history, and enforcement as they grow.

It is intentionally a growth control rather than a universal folder tree.

## RGS-CORE-001 — One canonical owner

Each class of durable information must have one canonical owner.

If the same fact is useful elsewhere, link to the owner. Do not maintain parallel copies unless a tool requires duplication and the copies are generated, linked, or mechanically checked for drift.

When two artifacts appear to own the same information, resolve the ownership conflict instead of adding synchronization prose.

## RGS-LIFE-001 — Separate information lifecycles

Current truth, active work, historical record, evidence, and mechanical enforcement must remain distinguishable.

See `docs/lifecycle.md` for lifecycle definitions, promotion, retirement, and authority during conflicts.

## RGS-GROW-001 — Earn permanent structure

Do not create persistent files, directories, workflows, or instruction layers merely because mature repositories sometimes have them.

Create structure when an observed recurring responsibility has no clean owner and the new structure is worth maintaining.

Use the lightest artifact that solves the demonstrated problem. A single document should normally precede a directory.

## RGS-KNOW-001 — Persist what is expensive to rediscover

Durable repository knowledge should primarily capture information that is non-obvious from code/configuration and repeatedly useful, costly, or risky to reconstruct.

Do not maintain a project map that merely restates an easily inspected tree. Do not persist ordinary scratch reasoning simply because an agent can write it down.

## RGS-PROMOTE-001 — Promote through evidence

Information should begin at the narrowest useful scope and move into durable or mechanical forms only when repeated use, consequence, or reproducibility justifies promotion.

Promotion should remove unnecessary duplicate copies from the old owner.

## RGS-RETIRE-001 — Retire obsolete structure

Growth control includes deletion, demotion, supersession, and consolidation.

When a rule, category, handoff, subsystem, or document no longer earns its maintenance cost, remove it from the active knowledge path.

Historical value alone does not justify keeping every intermediate artifact hot forever.

## RGS-INSTR-001 — Keep persistent agent instructions scoped

Always-loaded agent instructions should contain high-value, non-derivable rules, exact commands, boundaries, and routing cues that apply broadly to their scope.

Active task state, long procedures, historical narrative, and broad repository encyclopedias should load only when relevant.

## RGS-INSTR-002 — Avoid unmanaged instruction copies

When several tools require different instruction files, differences must be intentional and scoped. Identical or substantially overlapping copies should be generated, linked, imported, or checked for drift when the toolchain permits it.

## RGS-ENFORCE-001 — Graduate repeatable hard rules to enforcement

Instruction prose is not a reliable enforcement boundary.

Repeated mechanically checkable correctness or safety requirements should move toward tests, schemas, linters, hooks, permissions, CI, generated checks, or other deterministic controls when the benefit exceeds their maintenance cost.

## RGS-ADOPT-001 — Adopt upstream by version

Projects adopt this standard by source and semantic version. They do not copy the upstream guide wholesale and they do not silently adopt upstream changes.

A project checks upstream periodically or at relevant structural changes, reviews the changed rules, and deliberately updates its adopted version.

See `docs/adoption.md`.

## RGS-EXCEPT-001 — Exceptions are explicit and reviewable

A project may deviate from exception-eligible rules when local evidence justifies it.

Exceptions reference stable rule IDs and record a reason. Temporary exceptions should record a review date. Audit output must keep exceptions visible rather than silently hiding them.

See `docs/audit.md`.

## Normative delegated documents

The following documents are part of this standard:

- `docs/lifecycle.md` — information states, promotion, retirement, and conflict authority;
- `docs/routing.md` — artifact jurisdiction;
- `docs/growth.md` — structural growth triggers;
- `docs/adoption.md` — downstream adoption and update behavior;
- `docs/audit.md` — audit levels, detection classes, and exception semantics.

`rules.json` is the machine-readable rule catalog. `docs/examples.md`, `examples/`, and `docs/evidence.md` are explanatory/evidentiary and do not independently create normative requirements.
