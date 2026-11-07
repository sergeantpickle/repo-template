# Audit Model

This document is normative for the standard's audit tooling.

The auditor is a growth-control aid, not an autonomous repository rewriter.

## Rule identity

Normative and auditable rules use stable IDs from `rules.json`. Projects reference those IDs when recording explicit exceptions.

Rule IDs remain stable when wording is clarified. If the meaning changes incompatibly, the standard records the migration in its changelog and migration guidance.

## Levels

- **required** — normative requirement. A mechanically proven violation is a conformance failure unless that rule explicitly allows an exception.
- **recommended** — strong default. A deviation can be healthier than compliance when local evidence supports it.
- **advisory** — signal for human/agent review, not an automatic restructuring command.

A heuristic detector must not pretend to prove a manual rule.

## Detection classes

- **mechanical** — the condition can be established deterministically from available repository state.
- **heuristic** — the condition is a useful smell but can have legitimate false positives.
- **manual** — the rule requires contextual judgment and is documented but not automatically decided.

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

`--format json` provides machine-readable findings for higher-level tooling.

## False positives and false negatives

A false positive is evidence about the auditor, not evidence that the project should reorganize itself.

A false negative is evidence that the rule or detector may be incomplete.

Changes to heuristic detectors should be backed by a fixture or test demonstrating the failure mode they are intended to catch.
