# Audit Model

This document is normative for the standard's audit tooling and review process.

The auditor is a growth-control aid, not an autonomous repository rewriter.

## Rule identity

Normative and auditable rules use stable IDs from `rules.json`. Projects reference those IDs when recording explicit exceptions.

Rule IDs remain stable when wording is clarified. If the meaning changes incompatibly, the standard records the migration in its changelog and migration guidance.

`rules.json` is an index and machine contract, not a second normative prose source. Its `document` field names the canonical document that owns the rule's meaning; summaries in the catalog are routing aids. The standard self-check verifies that each active rule ID actually appears in its declared canonical document.

## RGS-AUDIT-001 — Audit claims state coverage and evidence limits

An audit must not imply that an uninspected or unobservable area passed.

Every contextual audit report states:

- the repository scope inspected;
- important areas intentionally or practically not inspected;
- whether history was sufficient for historical claims;
- whether CI/external-system evidence was actually observable;
- commands/checks that could not be run and why;
- any other limitation that materially lowers confidence.

"Not determined", "unverified", and "not inspected" are valid results. They are preferable to converting missing evidence into either a pass or a defect.

On a repository too large to inspect completely in one pass, audit by a declared boundary (for example capability/domain) and name the uncovered remainder.

This standard does not define a single aggregate compliance/readiness score. Mechanical errors, heuristic smells, manual judgments, exceptions, and coverage limits are different evidence classes and should remain distinguishable unless a project has independently earned and validated a scoring model.

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

1. State audit scope, coverage, and evidence limitations before drawing repository-wide conclusions.
2. Inventory persistent repository knowledge and instruction artifacts.
3. Assign each artifact a lifecycle from `docs/lifecycle.md`.
4. State the canonical responsibility of each artifact.
5. Identify overlapping owners, orphaned information, and files whose responsibility has silently expanded.
6. Inspect manual rules from `rules.json`, especially canonical ownership, earned structure, promotion, retirement, and enforcement.
7. Identify structures that no longer have an active trigger and are candidates for simplification.
8. Check scoped agent instructions for rules that belong only to one domain and global instructions for task state or historical narrative.
9. Identify any plan, handoff, status, or historical artifact that agents could mistakenly treat as current authorization for controlled actions; verify the actual authority mechanism is explicit.
10. Compare the project's last-aligned standard version with the latest released upstream target and review changed rules before proposing alignment.
11. Report findings with rule IDs, evidence, confidence, and the smallest corrective action that restores clear ownership.
12. Do not create new categories merely to resolve a finding when routing, deletion, or a smaller existing owner is sufficient.

A periodic audit is complete when the project can explain why each persistent organizational artifact still exists.

### Contextual review report shape

Before findings, report **Coverage and limits**: inspected scope, omitted scope, unavailable evidence, and any confidence limitation.

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

> Audit this repository against its Repository Growth Standard. Run the deterministic audit first, then perform the contextual review in `docs/audit.md`. Do not reorganize files while auditing. State coverage and evidence limits before findings. Report findings with rule IDs, evidence, confidence, current owner, smallest correction, growth effect, and trigger. Prefer routing or deletion over new structure when both solve the problem.

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
