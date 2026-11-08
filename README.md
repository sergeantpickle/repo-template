# repo-template

A living reference for AI agents that build and maintain repositories.

This repository explains how repository structure, documentation, agent instructions, and working practices can grow with a project. It helps an AI keep a project understandable as its code, domains, contributors, and concurrent work increase.

**This is a guide to reference, not a project scaffold to copy or a software package to install.** Projects keep their own structure. Agents consult the guidance when making structural decisions and revisit it as the project grows.

## How projects use this guide

Add a short reference to the project's `AGENTS.md`. Agents should consult this repository when they introduce or reorganize persistent structure, change agent instructions, add recurring workflows, establish new domains, or reach meaningful project milestones.

A lightweight checkpoint belongs in normal structural work. A full audit is useful when the project is visibly drifting or its owner asks for one.

## Reference note for project AGENTS.md

Copy this note into a project's existing `AGENTS.md`, adapting the wording only where the project needs a different boundary:

> ## Repository organization reference
>
> This project uses [repo-template](https://github.com/sergeantpickle/repo-template) as its living reference for repository organization and growth.
>
> Before introducing permanent files, directories, documentation categories, agent instructions, skills, or workflows, consult the relevant guidance and annotated structures in its [AGENTS.md](https://github.com/sergeantpickle/repo-template/blob/main/AGENTS.md). Use the trees as examples to adapt, not as a structure to copy wholesale.
>
> Check organizational fit during structural changes and meaningful milestones. Correct clear, low-risk drift when it is within the task's authority; preserve useful information and report what changed. Ask before destructive changes or broad restructuring.
>
> When asked to **"audit this project using repo-template,"** follow its [audit guide](https://github.com/sergeantpickle/repo-template/blob/main/docs/audit.md).

## Start here

- [`AGENTS.md`](AGENTS.md) — the structural reference, with Markdown directory trees and links to annotated examples.
- [Growth](docs/growth.md) — when repository structure should evolve.
- [Information ownership](docs/information.md) — what belongs in README, AGENTS, active work, durable docs, decisions, and history.
- [Agent context](docs/agent-context.md) — how to organize root instructions, scoped instructions, skills, and specialized agents.
- [Audit guide](docs/audit.md) — lightweight checkpoints and full contextual reviews.
- [Examples](examples/README.md) — annotated directory trees for seven common repository patterns.
- [Research notes](docs/research.md) — patterns observed in real agent-oriented repositories and sources behind the guidance.

## The central idea

A repository should contain enough structure to make work clear and reliable, and no more structure than its real responsibilities can justify.

Growth follows coordination pressure—not file count, age, team size, or somebody else's preferred folder tree. A project can start with twenty files and need little documentation; a small but safety-critical project may need strong boundaries immediately. The right structure makes ownership, context, and work clear at the project's current scale.
