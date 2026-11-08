# Repository Growth

A repository should grow in response to the coordination its work actually requires. The goal is not to reach a particular maturity level or accumulate a complete set of documentation categories. The goal is to keep work understandable as complexity changes.

The examples below describe common transitions, not a required sequence. A project can begin at any point, skip stages, or simplify later.

## Begin with the project that exists

A useful starting point is usually:

- a README that explains purpose, setup, and normal use;
- an AGENTS.md when coding agents need project-specific instructions;
- the actual source, configuration, tests, and operational files the project needs.

A project that begins with twenty files does not automatically need twenty documentation files. A project with one maintainer can still need strong boundaries if the work is consequential. Start from actual responsibilities, not a preset folder tree.

## When work needs to survive context changes

When a task spans sessions, agents, or contributors, give that bounded body of work a durable place for its objective, scope, progress, discoveries, validation, blockers, and next action.

The owner can be an issue, pull request, task plan, change proposal, or a project-specific work record. Choose the system the project already uses well. A single task does not establish a need for a permanent handoff framework, roadmap hierarchy, or archive taxonomy.

## When knowledge becomes reusable

When a non-obvious fact, contract, operational procedure, or design rationale repeatedly matters beyond the task that discovered it, give it a durable home.

A decision record earns its place when there were credible alternatives and future maintainers could reasonably undo the choice without understanding its rationale. A technical reference earns its place when code and configuration alone are costly or risky to interpret.

Let the responsibility determine the document. A single useful document does not need a directory around it.

## When the project develops distinct domains

As separate areas acquire different conventions, validation commands, boundaries, and ownership, scope their instructions and documentation accordingly.

Keep root instructions for rules that genuinely apply across the project. Put local guidance near the domain that needs it. Add a project map when semantic relationships, entry points, ownership, or validation paths become difficult to discover from the repository itself.

The structure should follow real boundaries. It does not need to mirror every directory.

## When parallel work becomes normal

As more agents or contributors work independently, coordination benefits from clearer ownership, explicit interfaces, task boundaries, review expectations, and discoverable validation.

When a repeated requirement is deterministic and costly to miss, consider a test, schema, linter, generated check, permission boundary, or CI rule. Mechanical enforcement should replace repeated reminders where it can do so reliably.

The goal is to make coordination less dependent on everyone remembering the same prose—not to automate every convention.

## When many domains or repositories must work together

At larger scale, local documentation may no longer explain the whole system. Ownership catalogs, dependency maps, service inventories, shared interfaces, organization-wide policies, and automated drift reporting can become useful.

These mechanisms earn their place when the topology itself becomes difficult to understand or coordinate. They are not a seed-project baseline.

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
