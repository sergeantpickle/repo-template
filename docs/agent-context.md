# Agent Context and Instructions

Agent instructions are part of the repository's working interface. They should help an agent make good decisions without forcing every task to load the entire repository's history and design knowledge.

For annotated layouts, see [scoped instructions](../examples/scoped-instructions/tree.md), [monorepos](../examples/monorepo/tree.md), and [repeatable workflows](../examples/repeatable-workflows/tree.md).

## Keep the always-loaded layer useful

The root `AGENTS.md` should contain information that is important across most work, not already obvious from code or configuration, and costly or risky to rediscover.

Good candidates include project boundaries, non-obvious conventions, exact validation commands, important safety constraints, a concise repository map, and pointers to deeper documentation.

## Scope instructions where the work differs

Add nested or path-scoped instructions when a domain has genuinely different conventions, tools, validation, ownership, or safety boundaries.

Keep cross-project rules at the root and domain-specific rules close to the domain. A nested instruction file should explain what is different in its scope; it should not repeat the entire root instruction set.

Instruction discovery differs by agent harness. Codex and GitHub Copilot support nested AGENTS.md files; other tools may use different filenames, path rules, or activation behavior. Verify the target harness before relying on a particular inheritance model.

## Load deeper knowledge when it is relevant

Long procedures, architecture details, historical context, and specialist references should be discoverable without being loaded into every task.

A project map, documentation index, or directory README is useful when it reduces real discovery cost. It should add semantic navigation rather than restate the file tree.

## Let skills and specialized agents earn their place

A skill or reusable procedure is useful when a process recurs, has meaningful steps or branches, and benefits from being maintained separately from general instructions. It may include scripts, templates, examples, or reference material.

A one-off task, unstable procedure, or generic instruction usually belongs in the task itself—not in a permanent skill.

A specialized agent is useful when a distinct role, review perspective, isolation boundary, or parallel-work pattern repeatedly produces value. The platform's ability to create agents is not, by itself, a reason to create them.

## Revisit context as the project changes

When a rule becomes mechanically enforced, simplify the prose that used to remind agents to follow it. When a domain disappears, remove its scoped instructions. When a procedure changes, update the one canonical owner.

The aim is not the smallest possible instruction file. It is the smallest always-loaded context that reliably orients the agent, with deeper knowledge available when needed.
