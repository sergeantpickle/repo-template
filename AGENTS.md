# Agent Instructions

This repository is the upstream Repository Growth Standard. It is not a normal project scaffold.

## Read based on the task

- Normative rule change: read `STANDARD.md`, `rules.json`, and the delegated normative document being changed.
- Routing/lifecycle change: read `docs/lifecycle.md` and `docs/routing.md`.
- Growth trigger change: read `docs/growth.md` and relevant examples.
- Audit/tooling change: read `docs/audit.md`, `rules.json`, and tests.
- Fast-moving agent/tool guidance: verify current sources and update `docs/evidence.md` when the conclusion changes.

Do not require every task to read every document.

## Change discipline

- A normative rule has one canonical owner and a stable ID in `rules.json`.
- Examples are non-normative. They demonstrate judgment; they do not create rules.
- Do not add a permanent file or directory because a mature project might someday need it. Apply `docs/growth.md` to this repository too.
- Prefer one document before a directory when the responsibility is still singular.
- Do not duplicate normative prose. Link to the canonical rule.
- Heuristic audit checks must be labeled as heuristics and backed by tests for the failure mode they target.
- Exceptions must remain visible in audit output; do not implement silent suppression.
- Hard deterministic requirements should move toward tooling when repeated failures justify it.

## Normative rule proposal gate

Before adding or materially expanding a normative rule, establish:

1. the observed failure, recurring ambiguity, coordination cost, or safety/correctness risk it addresses;
2. why an existing rule/owner cannot solve the problem more simply;
3. the rule's scope and canonical document;
4. whether it is required, recommended, or advisory and whether detection is mechanical, heuristic, or manual;
5. likely false-positive or over-compliance behavior, especially how an agent might cargo-cult the rule;
6. impact on existing adopters and any migration required;
7. whether the rule can eventually shrink, become mechanical, or be retired.

If these cannot be stated concretely, keep the idea in evidence/examples until it earns normative status.

## Versioning

`VERSION` is the current standard line.

While `STANDARD.md` is marked **Draft**, that version is provisional and may evolve before its first immutable release. Draft trial adopters must pin a reviewed commit SHA; the semantic version alone is not an immutable implementation identity.

After a version is released/tagged, normative semantic changes advance `VERSION` and `CHANGELOG.md`:

- MAJOR: incompatible governance, adoption, or rule semantics.
- MINOR: new normative rule, lifecycle, or materially expanded requirement.
- PATCH: clarification, example, evidence refresh, or tooling change with no normative semantic expansion.

A released version is not edited in place. Rule wording may be clarified in a later release without changing the rule ID when meaning is preserved. Incompatible rule meaning requires migration guidance.

`LATEST` names the latest stable released target and remains unchanged while the next standard line is Draft **and while a release candidate is being validated**. A release transaction:

1. marks the exact candidate Active and finalizes `VERSION`/changelog;
2. passes validation and remote CI on that exact candidate;
3. tags/releases that exact commit;
4. only after the immutable release exists, advances `LATEST` on the development branch to the released version.

This ordering prevents downstream projects from observing a release target that has not been published yet. Later Draft development advances `VERSION` while `LATEST` remains on the prior stable release.

## Validation

Run:

```bash
python scripts/check_standard.py
```

This runs the focused unit tests and audits the minimal downstream starter in strict mode.
