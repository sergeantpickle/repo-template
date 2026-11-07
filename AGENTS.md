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

`VERSION` is the current upstream standard version. Any normative semantic change must update `VERSION` and `CHANGELOG.md` in the same change:

- MAJOR: incompatible governance, adoption, or rule semantics.
- MINOR: new normative rule, lifecycle, or materially expanded requirement.
- PATCH: clarification, example, evidence refresh, or tooling change with no normative semantic change.

Rule wording may change without changing the rule ID when meaning is preserved. Incompatible rule meaning requires migration guidance.

## Validation

Run:

```bash
python scripts/check_standard.py
```

This runs the focused unit tests and audits the minimal downstream starter in strict mode.
