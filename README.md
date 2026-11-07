# Repository Growth Standard

This repository is an upstream guide for AI-primary software repositories.

It is not a directory tree that every project should copy. It defines how a project should decide where information belongs, when new structure is justified, when rules should become mechanical, and how obsolete structure should disappear.

Current standard version: **0.1.0**

## The problem this solves

Coding agents are good at adding information and weak at protecting information boundaries over long periods. Without explicit ownership, a README becomes a handoff, a changelog becomes a work log, temporary notes become permanent policy, and duplicated instructions drift apart.

This standard treats that as an organizational-control problem rather than a documentation-volume problem.

The core rule is:

> Every class of durable information has one canonical owner. Other surfaces link to it rather than absorbing copies.

## How projects use this repository

A project adopts a specific version of this standard and records that adoption in a small local manifest such as `.repo-standard.json`.

The project does **not** copy this repository's full documentation hierarchy. It grows only the structures justified by its own work.

When repository organization, agent instructions, documentation ownership, or work-state handling needs review, compare the project against the adopted standard and the latest upstream version.

See:

- [STANDARD.md](STANDARD.md) — normative rules.
- [docs/adoption.md](docs/adoption.md) — how a project adopts and updates the standard.
- [docs/routing.md](docs/routing.md) — where information belongs.
- [docs/growth.md](docs/growth.md) — when repository structure should grow.
- [docs/examples.md](docs/examples.md) — concrete growth and restraint examples.
- [docs/evidence.md](docs/evidence.md) — current research behind the standard.
- [starter/](starter/) — a minimal downstream example, not a mandatory project layout.

## What belongs here

This upstream repository may be richer than a downstream project because it owns:

- normative repository-growth rules;
- routing and lifecycle rules;
- growth triggers;
- non-normative examples;
- standard versioning and migration guidance;
- project-audit tooling;
- the evidence base used to revise the standard.

A downstream project should contain only what its own work has earned.

## Design rule for this repository

The guide must follow its own standard. New permanent files, directories, checks, and categories require a demonstrated responsibility that an existing artifact cannot own cleanly.
