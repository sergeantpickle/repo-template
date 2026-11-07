# Adoption and Updates

A downstream project adopts this standard by reference. It does not copy the guide's complete documentation tree.

## Minimal adoption record

A project may keep `.repo-standard.json` at its root:

```json
{
  "source": "https://github.com/sergeantpickle/repo-template",
  "version": "0.1.0",
  "last_checked": "2026-11-07",
  "exceptions": {}
}
```

`exceptions` maps a stable audit/rule identifier to a concise reason for the deviation.

The repository may also keep a small `AGENTS.md` telling agents where project-specific rules live and when to consult the upstream standard. See `starter/` for an example.

## When to consult upstream

Do not fetch and reread the full standard for every ordinary code edit.

Consult upstream when:

- adopting the standard for the first time;
- changing repository-wide agent instructions;
- adding or splitting a permanent documentation/work category;
- resolving information-routing drift;
- introducing a new enforcement layer;
- performing a periodic repository-organization audit;
- a newer standard version is known to exist.

## Checking for updates

1. Read upstream `VERSION`.
2. If it differs from the project's adopted version, read `CHANGELOG.md` for the intervening versions.
3. Review the changed normative documents, not the entire repository by default.
4. Run the current audit tooling against the project when practical.
5. Decide which changes apply to the project.
6. Record intentional exceptions rather than forcing irrelevant structure.
7. Update `.repo-standard.json` only after the new version has been deliberately adopted.

A standard update must never silently rewrite a project.

## Standard versioning

The standard uses semantic versioning for governance meaning:

- **MAJOR** — incompatible changes to governance, routing, or adoption semantics;
- **MINOR** — new normative rules, lifecycles, or materially expanded requirements;
- **PATCH** — clarifications, examples, evidence refreshes, or tooling changes with no normative semantic change.

## Audit cadence

No universal calendar cadence is required. Audit when the expected value is real.

Useful triggers include:

- after repeated routing mistakes;
- after a major reorganization;
- after a substantial increase in agent concurrency;
- after adopting a materially different coding-agent generation or toolchain;
- when a standard update changes rules relevant to the project;
- on a periodic maintenance schedule for repositories that change continuously.

## Exceptions

An exception is healthy when it is explicit and scoped.

Bad exception behavior:

- copying an obsolete structure because the guide once showed it;
- changing the guide locally without recording the divergence;
- creating parallel documents to satisfy both local practice and the standard.

Good exception behavior:

- identify the rule or audit identifier;
- state why the project differs;
- keep the deviation as narrow as possible;
- remove the exception when the underlying reason disappears.
