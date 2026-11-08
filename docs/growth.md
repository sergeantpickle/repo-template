# Repository Growth

A repository should grow in response to the coordination its work actually requires. The goal is not to reach a particular maturity level or accumulate a complete set of documentation categories. The goal is to keep work understandable as complexity changes.

The examples are patterns, not a required sequence. A project can begin at any point, combine patterns, skip stages, or simplify later. The [example index](../examples/README.md) links to annotated directory trees with notes explaining each path.

## Choose the project shape first

Project type and project scale are separate dimensions. A library, application, monorepo, and research project have different natural layouts; each can be small or large. Start with the closest shape, then add the growth patterns that match actual needs.

- [Application project](../examples/application-project/tree.md) — product code, server behavior, data, and tests.
- [Library or SDK](../examples/library-project/tree.md) — public package boundaries, consumer examples, compatibility, and releases.
- [Agent-first project](../examples/agent-first-project/tree.md) — agent context, skills, evaluations, and durable work.
- [Research or data project](../examples/research-project/tree.md) — provenance, notebooks, experiments, and reproducibility.
- [Monorepo](../examples/monorepo/tree.md) — multiple applications, services, and shared packages.

These are illustrative shapes, not technology mandates. Use the source tree, language conventions, and existing build system that fit the project.

## Begin with the project that exists

A useful starting point is usually a README, a concise root AGENTS.md when agents need project-specific guidance, and the source, configuration, and tests the project actually needs.

[See the seed-project tree](../examples/seed-project/tree.md).

A project that begins with twenty files does not automatically need twenty documentation files. A project with one maintainer can still need strong boundaries if the work is consequential. Start from actual responsibilities, not a preset folder tree.

## When work needs to survive context changes

When a task spans sessions, agents, or contributors, give that bounded body of work a durable place for its objective, scope, progress, discoveries, validation, blockers, and next action.

The owner can be an issue, pull request, task plan, change proposal, or a project-specific work record. Choose the system the project already uses well. A single task does not establish a need for a permanent handoff framework, roadmap hierarchy, or archive taxonomy.

For an agent-intensive workflow, see [the agent-first project tree](../examples/agent-first-project/tree.md).

## When knowledge becomes reusable

When a non-obvious fact, contract, operational procedure, or design rationale repeatedly matters beyond the task that discovered it, give it a durable home. A decision record earns its place when there were credible alternatives and future maintainers could reasonably undo the choice without understanding its rationale.

[See the growing-project tree](../examples/growing-project/tree.md) for a project whose durable knowledge has earned its own documents.

## When the project develops distinct domains

As separate areas acquire different conventions, validation commands, boundaries, and ownership, scope their instructions and documentation accordingly.

Keep root instructions for rules that genuinely apply across the project. Put local guidance near the domain that needs it. A nested AGENTS.md should explain what is different in its scope; it should not repeat the entire root instruction set.

[See scoped instructions](../examples/scoped-instructions/tree.md) and the [monorepo example](../examples/monorepo/tree.md).

## When parallel work becomes normal

As more agents or contributors work independently, coordination benefits from clearer ownership, explicit interfaces, task boundaries, review expectations, and discoverable validation.

When a repeated requirement is deterministic and costly to miss, consider a test, schema, linter, generated check, permission boundary, or CI rule. Mechanical enforcement should replace repeated reminders where it can do so reliably.

A skill or reusable procedure may help when a workflow recurs and benefits from being maintained separately. [See the repeatable-workflows tree](../examples/repeatable-workflows/tree.md).

## When the project needs a map

A project map earns its place when semantic relationships, ownership, entry points, dependency direction, or validation paths are difficult to reconstruct from the repository itself. A map that merely restates the directory tree adds another freshness obligation without adding knowledge.

[See the semantic project-map tree](../examples/semantic-project-map/tree.md).

## When many domains or repositories must work together

At larger scale, local documentation may no longer explain the whole system. Ownership catalogs, dependency maps, service inventories, shared interfaces, and organization-wide policies can become useful when the topology itself becomes a coordination problem.

[See the organization-scale tree](../examples/organization-scale/tree.md). These mechanisms are not a seed-project baseline.

## A practical growth decision

Before adding a permanent file, directory, instruction layer, skill, specialized agent, workflow, or registry, consider:

1. What recurring or consequential responsibility needs an owner?
2. Where does that information or responsibility live today?
3. Can the existing owner be clarified or improved?
4. Who or what will use the new structure, and when?
5. What makes the structure worth maintaining?
6. How will it stay current, and when can it be retired?
7. Is there a smaller or more local solution?

If the answers are vague, keep the idea in the current task rather than creating permanent structure prematurely.

## Growth includes simplification

Projects change direction. Domains disappear, procedures become obvious, teams consolidate, and mechanical checks replace repeated instructions. Remove or shrink structure when its original responsibility no longer exists.

A mature repository is not the one with the most governance. It is the one whose structure continues to fit its work.
