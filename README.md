# Repository Growth Standard

A versioned upstream guide for keeping AI-primary repositories understandable as they grow.

The standard does not prescribe a large project tree. It defines **jurisdiction, lifecycle, growth triggers, exceptions, and enforcement** so agents do not gradually turn README files into handoffs, changelogs into work logs, or one-off observations into permanent bureaucracy.

Current version: **0.1.0**  
Status: **Draft** — usable for trials, not yet published as an immutable release.

## Core idea

> Every class of durable information has one canonical owner. New permanent structure must earn existence through an observed coordination need.

A project adopts this repository by reference and version. It keeps its own project-specific instructions and knowledge; it does not copy this guide wholesale.

## Operating model

```text
repo-template (upstream guide/control plane)
  ├─ normative rules
  ├─ growth examples
  ├─ evidence
  └─ audit implementation
          │
          │ export starter / adopt by version
          ▼
project
  ├─ README + project-specific agent rules
  ├─ .repo-standard.json
  └─ only the structure its work has earned
          │
          │ structural change or periodic review
          ▼
pinned audit against adopted version
          │
          ├─ routing / lifecycle findings
          ├─ contextual AI review
          └─ explicit exceptions
          │
          │ newer upstream version detected
          ▼
review changelog + changed rules
          │
          └─ deliberately adopt, except, or stay pinned
```

The upstream guide evolves; projects do not silently inherit it.

## Start here

- [STANDARD.md](STANDARD.md) — normative principles and stable rule IDs.
- [docs/lifecycle.md](docs/lifecycle.md) — how information moves from ephemeral to active, durable, historical, or mechanical.
- [docs/routing.md](docs/routing.md) — which artifact owns which information.
- [docs/growth.md](docs/growth.md) — when new files, directories, scoped rules, and automation are justified.
- [docs/adoption.md](docs/adoption.md) — downstream adoption and periodic upstream checks.
- [docs/audit.md](docs/audit.md) — audit levels, heuristic limits, and explicit exceptions.
- [examples/](examples/) — growth trajectories and recovery examples.
- [docs/evidence.md](docs/evidence.md) — dated research behind current guidance.

## Create a new downstream project

Do **not** use GitHub's native "Use this template" copy as the normal bootstrap path for this repository. GitHub template repositories copy the upstream directory structure and files, which would copy the guide itself into the project.

From a checkout of this standard, export only the minimal starter:

```bash
python scripts/init_project.py /path/to/new-project
```

The exporter refuses to overwrite existing `README.md`, `AGENTS.md`, or `.repo-standard.json`.

For an existing project, do not export starter files over it. Run a pre-adoption review instead:

```bash
python scripts/audit_project.py /path/to/existing-project --pre-adoption
```

Then adopt deliberately by adding the manifest and only the project-specific instructions the repository actually needs.

If GitHub's native **Use this template** button is a hard requirement, the clean architecture is a separate minimal template repository generated from `starter/`, while this repository remains the versioned guide/control plane. Do not make the guide itself minimal merely to satisfy GitHub's copy semantics.

## Downstream baseline

The `starter/` directory intentionally contains very little:

```text
README.md
AGENTS.md
.repo-standard.json
```

It is an example baseline, not a mandatory tree. Projects add structure when the triggers in `docs/growth.md` are actually met.

## Audit a project

From a checkout of this standard:

```bash
python scripts/audit_project.py /path/to/project
python scripts/audit_project.py /path/to/project --strict
python scripts/audit_project.py /path/to/project --format json
```

Check whether the project is behind the current upstream `VERSION`:

```bash
python scripts/check_latest.py /path/to/project
```

The repository also exposes a composite GitHub Action (`action.yml`) so downstream projects can run the pinned audit logic periodically without copying it. See `docs/adoption.md` and `examples/github-actions/`.

## Maintain this standard

Run:

```bash
python scripts/check_standard.py
```

The standard must follow itself: no new permanent category, workflow, or rule is added merely because it might be useful someday.
