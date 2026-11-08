# Repository Checkpoint and Audit

This guide describes how an AI agent checks whether a repository's organization still fits the work being done. The checkpoint is part of normal maintenance; a full audit is a deeper review when the project reaches a meaningful milestone, shows signs of drift, or its owner requests one.

An audit is an exercise in understanding and improving the actual repository. It is not a compliance score and does not require the project to resemble this reference. Use the structural patterns in the root `AGENTS.md` and the annotated `examples/*/tree.md` files as comparisons, not as a checklist of required paths.

## When to run a checkpoint

Perform a lightweight checkpoint:

- before introducing a permanent documentation category, instruction layer, workflow, skill, or specialized agent;
- after adding a new domain, package, service, or significant ownership boundary;
- when work repeatedly loses context between sessions or agents;
- when instructions or documentation have become difficult to navigate;
- after a meaningful milestone, major refactor, or release.

Do not interrupt every ordinary code edit with a repository-wide review. Check the part of the repository affected by the change.

## Lightweight checkpoint

Ask:

1. Does each changed or newly created artifact have one clear responsibility?
2. Is the information in the right place for its lifecycle and audience?
3. Does an existing file or system already own this responsibility?
4. Will the intended agents or people find this information when they need it?
5. Is global instruction being used for something that should be scoped or loaded on demand?
6. Does the new structure solve a recurring or consequential need?
7. Is there a clear way to keep it current and retire it if the need disappears?

If the structure is sound, continue working. Do not invent work to make the checkpoint appear useful.

## Full repository audit

When asked to audit a project using this guide, inspect the repository as a working system.

### 1. Establish scope

Identify the repository, its purpose, major domains, active work systems, and the areas inspected. State important areas you could not inspect and any evidence limitations. Do not imply that uninspected areas are healthy.

### 2. Understand how the project works

Use the source, configuration, tests, build/deploy setup, recent history, issues, and project instructions as evidence where available. Understand how agents and people actually work before judging the documentation.

### 3. Review the information owners

Inspect README, global and scoped agent instructions, active work records, durable docs, decisions, research, release history, generated references, and any project maps that exist.

For each persistent artifact, identify its responsibility, audience, lifecycle, update path, and whether it is still useful.

### 4. Review growth and agent context

Check whether the current structure reflects actual coordination needs. Look for opportunities to clarify ownership, scope instructions, make deeper knowledge discoverable, or simplify structures that no longer serve the project.

Consider whether skills, specialized agents, plans, catalogs, and automation solve recurring needs in this repository. Their presence is not automatically good or bad.

### 5. Form findings from evidence

Separate:
- a concrete defect that prevents correct work;
- an organizational ambiguity that causes repeated cost;
- a worthwhile improvement;
- a preference that has no demonstrated benefit.

For each material finding, include:

- **Finding:** what is happening.
- **Evidence:** specific files, behavior, history, or examples.
- **Impact:** why it matters to this project.
- **Confidence:** high, medium, or low.
- **Smallest useful correction:** the least disruptive way to improve it.
- **Growth effect:** whether the correction adds, moves, merges, or removes structure.

Do not assign an overall maturity or compliance score.

## Act proportionately

The checkpoint should be useful without turning every audit into a rewrite.

- Make clear, low-risk, reversible corrections autonomously when they are within the work already authorized.
- Preserve useful information when moving or consolidating it, and update links and references.
- Report what changed and why.
- Present larger structural changes before carrying them out.
- Ask before deleting unique information, changing project policy, or making a broad reorganization.
- If the evidence is incomplete, say what remains unknown rather than guessing.

Prefer a small correction that restores clear ownership over a new framework. Sometimes the right result is no change.

## A good audit outcome

The project is easier to understand and continue working on. Agents can find the right context, persistent information has clear owners, active work is distinguishable from current system knowledge, and every permanent structure has a reason to remain.

The audit should leave the repository with less ambiguity—not necessarily more files.
