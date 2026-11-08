# repo-template

A living reference for AI agents that build and maintain repositories.

This repository explains how repository structure, documentation, agent instructions, and working practices can grow with a project. It helps an AI keep a project understandable as its code, domains, contributors, and concurrent work increase.

**This is a guide to reference, not a project scaffold to copy or a software package to install.** Projects keep their own structure. Agents consult the guidance when making structural decisions and revisit it as the project grows.

## How projects use this guide

Add a short reference to the project's `AGENTS.md`. Agents should consult this repository when they:

- introduce or reorganize persistent documentation or repository structure;
- change global or scoped agent instructions;
- add a recurring workflow, skill, or specialized agent;
- introduce a new domain, package, service, or ownership boundary;
- reach a meaningful project milestone;
- notice that context, responsibilities, or information ownership are becoming unclear.

A lightweight checkpoint should happen as part of normal work. A full audit is useful when the project is visibly drifting or its owner asks for one.

## Reference note for project AGENTS.md

Copy this note into a project's existing `AGENTS.md`, adapting the wording only where the project needs a different boundary:

> ## Repository organization reference
>
> This project uses [repo-template](https://github.com/sergeantpickle/repo-template) as its living reference for repository organization and growth.
>
> Consult its `AGENTS.md` checkpoint and the relevant guidance before introducing persistent files, directories, documentation categories, agent instructions, skills, or workflows. Apply the principles to this project's actual needs; do not copy the reference repository's tree or create structures merely because an example contains them.
>
> Check organizational fit as part of structural changes and meaningful milestones. If clear, low-risk drift appears, correct it while preserving useful information and report what changed. Ask before destructive changes or broad restructuring.
>
> When asked to **"audit this project using repo-template,"** perform the contextual review described in [the audit guide](https://github.com/sergeantpickle/repo-template/blob/main/docs/audit.md).

## Start here

- [`AGENTS.md`](AGENTS.md) — the agent checkpoint and operating instructions for using this reference.
- [Growth](docs/growth.md) — how a repository can grow from one maintainer or agent to organization scale.
- [Information ownership](docs/information.md) — what belongs in README, AGENTS, active work, durable docs, decisions, history, and other common owners.
- [Agent context](docs/agent-context.md) — how to keep instructions useful, scoped, and loaded only when relevant.
- [Audit guide](docs/audit.md) — how an agent checks a project, reports drift, and makes proportionate corrections.
- [One agent to a mature project](examples/seed-to-mature.md)
- [Starting with twenty files](examples/starting-at-twenty.md)
- [Growing from one to thousands](examples/organization-scale.md)
- [A useful project map](examples/project-map.md)
- [Research notes](docs/research.md) — observations and sources that inform the guidance.

## The central idea

A repository should contain enough structure to make work clear and reliable, and no more structure than its real responsibilities can justify.

Growth follows coordination pressure—not file count, age, team size, or somebody else's preferred folder tree. A project can start with twenty files and need very little documentation; a small but safety-critical project may need stronger controls immediately. The right structure is the one that makes ownership, context, and work clear at the project's current scale.
