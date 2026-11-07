# Alignment and Upstream Checks

This document is normative.

A downstream project aligns to this standard by reference. It does not copy this repository's complete guide tree.

For a new project, `python scripts/init_project.py /path/to/new-project` exports only `starter/README.md`, `starter/AGENTS.md`, and a current alignment manifest. This is preferred over GitHub's native template-copy operation, which copies the complete upstream file tree.

Before alignment, an existing repository can run `python scripts/audit_project.py /path/to/project --pre-alignment` to inspect routing/growth smells without first creating a manifest. Alignment remains a deliberate later action.

## Alignment manifest — RGS-ALIGN-001

A project records its upstream source and the semantic version it last deliberately aligned to in `.repo-standard.json`:

```json
{
  "schema_version": 1,
  "source": "https://github.com/sergeantpickle/repo-template",
  "version": "0.1.0",
  "last_checked": "2026-11-07",
  "exceptions": {}
}
```

`schema_version` identifies the manifest contract understood by tooling. `version` is the **last-aligned version**, not a declaration that the project may permanently ignore newer released standards. `last_checked` may be null until the first upstream comparison.

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

`reason` is required. `scope` and `review_after` are optional. Unknown IDs, empty reasons, and attempts to except non-exception rules are invalid alignment state.

## When to consult upstream

Do not fetch and reread the standard for every normal code edit.

Consult upstream when:

- aligning to the standard for the first time;
- changing repository-wide instruction/document structure;
- creating or splitting a permanent work/document category;
- resolving routing drift such as README, changelog, notes, or handoff contamination;
- adding a new enforcement layer;
- deliberately auditing repository organization;
- a newer released upstream standard is detected;
- a major coding-agent/tool change may invalidate an existing assumption.

## Periodic check

From a local checkout of the standard:

```bash
python scripts/check_latest.py /path/to/project
```

The checker derives the upstream `LATEST` URL from the manifest's `source` when `source` is a canonical GitHub repository URL. `LATEST` names the most recent stable released target and is independent of Draft work on `main`. For other source types, pass `--latest-url`. The checker reports alignment drift but never applies it.

For GitHub-hosted projects, this repository also exposes a composite action. A downstream workflow pins the action implementation corresponding to the project's last-aligned state and lets that pinned auditor separately check upstream `LATEST` for a newer released target.

See `examples/github-actions/repo-standard.yml`.

Scheduled GitHub workflows are a convenience, not the only audit trigger. Public-repository schedules may be disabled after prolonged inactivity, so projects with stronger guarantees should also run the audit on an appropriate human or repository-maintenance event.

## Deliberate alignment process

When the latest released upstream standard is newer than the project's last-aligned `version`:

1. Read `CHANGELOG.md` for every intervening version.
2. Read the normative documents for rules that changed.
3. Run the newer released audit logic against the project when practical.
4. Identify which findings are actual project problems, false positives, or justified deviations.
5. Apply relevant migrations and structural changes.
6. Record explicit exceptions where the project intentionally differs.
7. Update `last_checked`.
8. Change `version` only after the project has deliberately aligned to the newer released standard.

An upstream change must never silently rewrite the project. Remaining behind is visible drift to resolve, not an alternate permanently-current standard.

## Drafts and released standards

A version number in `VERSION` identifies the standard line being developed. While `STANDARD.md` is **Draft**, that version is provisional and may change before its first immutable release.

Projects may trial a draft by pinning a reviewed commit SHA. During draft trials, the pinned SHA—not the provisional version string—is the immutable implementation identity. Do not use a moving branch such as `main` as an aligned implementation.

Once a version is released/tagged, its normative meaning is immutable. Later semantic changes receive a new version according to the rules below.

## Pinning audit code

A project should pin externally executed audit code to an immutable commit SHA or a reviewed release tag. The project's manifest version and the audit-code ref should represent the same **last-aligned** standard release.

The provided composite action enforces both the last-aligned version and source before auditing. GitHub exposes both the executing action's repository identity and server URL to composite actions, so a fork, alternate standard, or GitHub Enterprise host cannot silently claim equivalence merely by sharing the same version string.

A deliberately newer or alternate auditor can still be run manually without `--require-version-match` / `--require-source` during an upgrade or comparison review.

Using upstream `main` directly for enforcement couples a project to unreviewed future standard changes and defeats deliberate alignment.

## Released target and versioning

`LATEST` contains the latest stable released target, or `none` before the first stable release. Draft changes on `main` do not become the downstream target until released.

Release publication is ordered so the immutable tag/release exists **before** `LATEST` is advanced. This prevents a periodic checker from observing a target that has not actually been published.

The standard uses semantic versioning for governance meaning:

- **MAJOR** — incompatible governance, alignment, or rule semantics;
- **MINOR** — a new normative rule/lifecycle or materially expanded requirement;
- **PATCH** — clarification, example, evidence refresh, detector improvement, or tooling change without normative semantic expansion.

Migration guidance belongs in the changelog while migrations are few. If migrations become independently numerous enough to need their own retrieval lifecycle, the standard should then earn a migrations directory.
