# Adoption and Upstream Checks

This document is normative.

A downstream project adopts this standard by reference. It does not copy this repository's complete guide tree.

## Adoption manifest — RGS-ADOPT-001

A project records its adopted source and semantic version in `.repo-standard.json`:

```json
{
  "source": "https://github.com/sergeantpickle/repo-template",
  "version": "0.1.0",
  "last_checked": "2026-11-07",
  "exceptions": {}
}
```

`last_checked` may be null until the first upstream comparison.

The manifest is deliberately small. Project-specific structure remains in the project, not in the standard manifest.

## Exceptions — RGS-EXCEPT-001

Exceptions are keyed by stable rule ID and remain visible in audit output:

```json
{
  "exceptions": {
    "RGS-ROUTE-HANDOFF-001": {
      "reason": "Release-train coordination temporarily uses a bounded root handoff.",
      "scope": "HANDOFF.md",
      "review_after": "2027-01-31"
    }
  }
}
```

`reason` is required. `scope` and `review_after` are optional. Unknown IDs, empty reasons, and attempts to except non-exception rules are invalid adoption state.

## When to consult upstream

Do not fetch and reread the standard for every normal code edit.

Consult upstream when:

- adopting the standard for the first time;
- changing repository-wide instruction/document structure;
- creating or splitting a permanent work/document category;
- resolving routing drift such as README, changelog, notes, or handoff contamination;
- adding a new enforcement layer;
- deliberately auditing repository organization;
- a newer upstream `VERSION` is detected;
- a major coding-agent/tool change may invalidate an existing assumption.

## Periodic check

From a local checkout of the standard:

```bash
python scripts/check_latest.py /path/to/project
```

The checker compares the project's adopted version with the current upstream `VERSION` on `main`. It reports an available update but does not adopt it.

For GitHub-hosted projects, this repository also exposes a composite action. A downstream workflow can pin the action to the immutable commit or release tag it has adopted and let that pinned auditor separately check upstream `VERSION` for newer guidance.

See `examples/github-actions/repo-standard.yml`.

Scheduled GitHub workflows are a convenience, not the only audit trigger. Public-repository schedules may be disabled after prolonged inactivity, so projects with stronger guarantees should also run the audit on an appropriate human or repository-maintenance event.

## Deliberate update process

When upstream `VERSION` differs:

1. Read `CHANGELOG.md` for every intervening version.
2. Read the normative documents for rules that changed.
3. Run the newer audit logic against the project when practical.
4. Identify which findings are actual project problems, false positives, or justified deviations.
5. Apply relevant migrations and structural changes.
6. Record explicit exceptions where the project intentionally differs.
7. Update `last_checked`.
8. Change the adopted `version` only when the project has deliberately adopted the new standard.

An upstream change must never silently rewrite the project.

## Pinning audit code

A project should pin externally executed audit code to an immutable commit SHA or a reviewed release tag. The project's manifest version and the audit-code ref should represent the same adopted standard release.

Using upstream `main` directly for enforcement couples a project to unreviewed future standard changes and defeats deliberate adoption.

## Versioning

The standard uses semantic versioning for governance meaning:

- **MAJOR** — incompatible governance, adoption, or rule semantics;
- **MINOR** — a new normative rule/lifecycle or materially expanded requirement;
- **PATCH** — clarification, example, evidence refresh, detector improvement, or tooling change without normative semantic expansion.

Migration guidance belongs in the changelog while migrations are few. If migrations become independently numerous enough to need their own retrieval lifecycle, the standard should then earn a migrations directory.
