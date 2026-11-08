# Agent Checkpoint

This repository is a living reference for AI agents that build and maintain other repositories. It is **not** a software product, installable framework, compliance system, or directory scaffold.

Its purpose is to help agents make good structural decisions as a project grows, then recognize when existing structure needs to evolve or simplify.

## When this reference is used by another project

Treat this repository as guidance, not as a checklist or a tree to copy. Read only the sections relevant to the current decision.

- Before adding or reorganizing permanent structure, consult [growth](docs/growth.md) and [information ownership](docs/information.md).
- Before changing global or scoped instructions, skills, or specialized agents, consult [agent context](docs/agent-context.md).
- At meaningful milestones, check whether the project's structure still matches its actual responsibilities.
- When the owner asks to "audit this project using repo-template", follow [the audit guide](docs/audit.md).
- If clear organizational drift appears during ordinary work, address it as part of the task when the correction is safe and within the task's authority. Do not wait for a separate audit request to notice an obvious problem.

## How to make changes safely

1. Understand the project's actual work, code, people/agents, and coordination needs before recommending structure.
2. Identify the responsibility and lifecycle that need an owner.
3. Reuse or improve an existing owner when that solves the problem.
4. Add the smallest useful structure only when a recurring or consequential need earns it.
5. Keep useful information when moving or consolidating it; update references and links.
6. Revisit the result after the change and remove temporary scaffolding that no longer serves a purpose.

Make clear, local, reversible corrections autonomously when they are within the work already authorized. Ask before deleting unique information, making broad reorganizations, changing project policy, or taking actions outside the task's authority.

An audit is an assessment of the real repository, not a demand that it resemble this guide. Do not assign a compliance score or treat examples as mandatory layouts.

## Maintaining this reference

- Keep the guidance practical, positive, and centered on good repository growth.
- Keep each document focused on one responsibility. The README is the navigation page; do not create another index unless it solves a real navigation problem.
- Examples demonstrate good decisions in context. They are not required stages or templates.
- Keep fast-changing model- and tool-specific advice grounded in current sources. Recheck it before presenting it as current.
- Prefer a clearer explanation over a new rule catalog, version scheme, manifest, or enforcement mechanism.
- Do not reintroduce software machinery—auditors, scripts, tests, actions, exporters, manifests, or release automation—unless the owner explicitly changes the purpose of this repository and a demonstrated need justifies it.
