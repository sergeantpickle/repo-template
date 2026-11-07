# Audit Model

This document is normative for the standard's audit tooling and review process.

The auditor is a growth-control aid, not an autonomous repository rewriter.

## Rule identity

Normative and auditable rules use stable IDs from `rules.json`. Projects reference those IDs when recording explicit exceptions.

Rule IDs remain stable when wording is clarified. If the meaning changes incompatibly, the standard records the migration in its changelog and migration guidance.

`rules.json` is an index and machine contract, not a second normative prose source. Its `document` field names the canonical document that owns the rule's meaning; summaries in the catalog are routing aids. The standard self-check verifies that each active rule ID actually appears in its declared canonical document.

## Levels

- **required** — normative requirement. A mechanically proven violation is a conformance failure unless that rule explicitly allows an exception.
- **recommended** — strong default. A deviation can be healthier than compliance when local evidence supports it.
- **advisory** — signal for human/agent review, not an automatic restructuring command.

A heuristic detector must not pretend to prove a manual rule.

## Detection classes

- **mechanical** — the condition can be established deterministically from available repository state.
- **heuristic** — the condition is a useful smell but can have legitimate false positives.
- **manual** — the rule requires contextual judgment and is documented but not automatically decided.

## Periodic AI review

A useful repository audit has two layers.

### 1. Run deterministic/heuristic tooling

Run the pinned standard audit first:

```bash
python scripts/audit_project.py /path/to/project
```

For an existing repository that has not adopted the standard yet:

```bash
python scripts/audit_project.py /path/to/project --pre-adoption
```

Pre-adoption mode skips only the missing-manifest error. It does not imply conformance or create an adoption record.

Treat heuristic findings as prompts for inspection, not automatic proof that the repository should be reorganized.

### 2. Perform the contextual review

The reviewing agent should then:

1. Inventory persistent repository knowledge and instruction artifacts.
2. Assign each artifact a lifecycle from `docs/lifecycle.md`.
3. State the canonical responsibility of each artifact.
4. Identify overlapping owners, orphaned information, and files whose responsibility has silently expanded.
5. Inspect manual rules from `rules.json`, especially canonical ownership, earned structure, promotion, retirement, and enforcement.
6. Identify structures that no longer have an active trigger and are candidates for simplification.
7. Check scoped agent instructions for rules that belong only to one domain and global instructions for task state or historical narrative.
8. Compare the project's adopted standard version with current upstream and review changed rules before proposing adoption.
9. Report findings with rule IDs, evidence, confidence, and the smallest corrective action that restores clear ownership.
10. Do not create new categories merely to resolve a finding when routing, deletion, or a smaller existing owner is sufficient.

A periodic audit is complete when the project can explain why each persistent organizational artifact still exists.

### Contextual review report shape

For each material finding, report:

- **Rule** — stable rule ID.
- **Evidence** — concrete files/sections/observations.
- **Confidence** — high, medium, or low.
- **Current owner** — which artifact currently owns the information/responsibility, even if that ownership is accidental.
- **Problem** — overlap, orphaning, stale lifecycle, unnecessary persistence, missing enforcement, or another specific failure.
- **Smallest correction** — route, delete, merge, scope, promote, retire, or mechanize.
- **Growth effect** — none, grows structure, or shrinks structure.
- **Why now** — the observed trigger that makes the correction worth its maintenance cost.

Low-confidence findings should normally remain recommendations for inspection rather than structural changes.

A reusable audit instruction is:

> Audit this repository against its adopted Repository Growth Standard. Run the deterministic audit first, then perform the contextual review in `docs/audit.md`. Do not reorganize files while auditing. Report findings with rule IDs, evidence, confidence, current owner, smallest correction, growth effect, and trigger. Prefer routing or deletion over new structure when both solve the problem.

## Exceptions

Exceptions are recorded in `.repo-standard.json` under the rule ID:

```json
{
  "exceptions": {
    "RGS-ROUTE-HANDOFF-001": {
      "reason": "Release-train coordination uses a bounded root handoff until migration completes.",
      "scope": "HANDOFF.md",
      "review_after": "2027-01-31"
    }
  }
}
```

`reason` is required. `scope` and `review_after` are optional.

An exception does not hide the finding. Audit output reports it as excepted together with the reason. Unknown rule IDs and exceptions against non-exception rules are manifest errors.

A past `review_after` date creates an active warning so temporary exceptions do not become invisible permanent policy.

## Exit behavior

By default, `scripts/audit_project.py` fails only for malformed adoption state and other audit errors. Heuristic warnings are visible but non-blocking.

`--strict` makes active warnings fail while still allowing explicit valid exceptions.

`--require-version-match` makes a project/auditor version mismatch an error.

`--require-source <source>` makes a project/auditor source mismatch an error. The pinned downstream GitHub Action passes its own GitHub action-repository identity and uses both source and version checks; upgrade/comparison exploration can intentionally omit them.

`--format json` provides machine-readable findings for higher-level tooling. The top-level `schema_version` is currently `1`; consumers should reject unsupported schema versions rather than inferring compatibility.

## False positives and false negatives

A false positive is evidence about the auditor, not evidence that the project should reorganize itself.

A false negative is evidence that the rule or detector may be incomplete.

Changes to heuristic detectors should be backed by a fixture or test demonstrating the failure mode they are intended to catch.
