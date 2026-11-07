# Execution Plans

Execution plans are task-scoped living documents for substantial work.

Create one when work is multi-step, crosses important components, contains meaningful uncertainty, or is likely to be handed between agents or sessions.

Small, obvious changes do not need a plan.

## Location

Active plans:

`docs/plans/active/YYYY-MM-DD-topic.md`

Completed plans:

`docs/plans/completed/YYYY-MM-DD-topic.md`

## Required content

Each plan should make sense to a fresh agent without chat context and should contain:

- objective;
- context;
- scope;
- non-goals;
- acceptance criteria;
- relevant files/systems;
- implementation approach;
- progress;
- discoveries;
- decisions made during execution;
- validation evidence;
- blockers or risks;
- next action.

Use `docs/templates/exec-plan.md` as the starting point.

## Lifecycle

1. Create the plan before substantial implementation.
2. Update progress and discoveries as work proceeds.
3. Promote durable conclusions into architecture, decision, product, operations, quality, or reference docs rather than leaving them trapped in the plan.
4. When acceptance criteria are met and validation is complete, mark the plan completed and move it to `docs/plans/completed/`.
5. Completed plans are historical engineering records and are not expected to remain instructions for current behavior.
