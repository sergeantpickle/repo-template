# Information Ownership

Repository information stays useful when each kind of information has a clear owner and lifecycle. Choose where something belongs by asking what it describes, who needs it, and how long it remains useful—not by choosing whichever file is easiest to append to.

## Common information owners

| Owner | What it is for |
| --- | --- |
| `README.md` | Project purpose, setup, normal usage, and essential entry points for people. |
| `AGENTS.md` | Broad, non-derivable agent instructions: boundaries, exact commands, conventions, and pointers to deeper context. |
| Scoped `AGENTS.md` | Instructions that apply only within a subsystem, package, or domain. |
| Active work record | The objective, scope, progress, discoveries, validation state, blockers, and next action for one bounded task. This may live in an issue, PR, plan, or existing work system. |
| Durable technical documentation | Current behavior, contracts, operations, and system knowledge that is expensive or risky to reconstruct. |
| Decision record | The rationale for a durable choice when credible alternatives existed and the reasoning will matter later. |
| Research notes | Sources, experiments, and findings worth preserving because they will inform future decisions. |
| `CHANGELOG.md` | Notable shipped changes when users or release consumers benefit from a release history. |
| Git, issues, and pull requests | Chronology, diffs, review, discussion, and provenance. |
| Generated reference | Derived information with a known source and regeneration process. |

A project does not need every owner in this table. Use the systems it already has where they fit.

## Give information the right lifecycle

A useful way to route information is to identify how long it should remain active.

- **Temporary:** scratch reasoning, transient output, and details that are cheap to rediscover. Usually do not persist these.
- **Active:** information needed to finish one bounded piece of work. Keep it with that work and retire or close it when the work ends.
- **Current and durable:** non-obvious knowledge that describes how the project works now. Update it when the system changes.
- **Historical:** information retained to explain what happened or why an earlier choice existed. Keep it out of the default working context unless relevant.
- **Mechanically enforced:** behavior constrained by tests, schemas, configuration, permissions, or other executable controls. Keep a concise explanation when people still need to understand why the control exists.

Information can move between these states. When it does, update the previous owner so that stale copies do not remain as competing sources of truth.

## Keep the boundaries clear

README explains the project; it is not the place to maintain ongoing task progress.

AGENTS explains how agents should work in the project; it is not a repository encyclopedia or a running session transcript.

Active work records explain what is happening now for one bounded task. They do not become permanent policy merely because a task lasts several weeks.

Durable documentation describes the system that exists. Planned behavior belongs with the work that will implement it until it is validated and becomes current.

A changelog, when useful, records shipped changes for its audience. It does not need to reproduce every commit or development session.

A handoff is useful when there is a real transfer boundary that the active work system does not already cover. A generic root-level notes or log file is rarely a useful long-term owner because unrelated kinds of information accumulate there.

## Maps and indexes

A project map is useful when it explains semantic relationships that are difficult to infer from the directory tree: ownership, runtime entry points, dependency direction, subsystem boundaries, or where validation differs.

A map that only lists folders and files repeats information the repository already provides. Start with a short README section or links in existing documentation; give the map its own document only when it has a distinct purpose and update lifecycle. See the [semantic project-map example](../examples/semantic-project-map/tree.md) for a useful layout, and the [growing-project example](../examples/growing-project/tree.md) for a smaller documentation structure.

## Information is not authority

A plan can say that deployment is the next step without authorizing deployment. A status file can say that a release is ready without granting permission to publish it.

If agents can perform controlled actions, the project must make the authority boundary clear: who or what grants permission, what it covers, and how current that permission must be. Do not infer permission from an old handoff, plan, issue comment, or historical approval.
