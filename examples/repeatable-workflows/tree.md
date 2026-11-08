# Repeatable Workflows

A project repeats a multi-step procedure often enough that the exact sequence, branches, validation, or supporting assets should be maintained separately from always-loaded instructions.

## Example tree

```text
project/
├── AGENTS.md
└── .agents/
    └── skills/
        └── release/
            ├── SKILL.md                  # Trigger, inputs, procedure, decisions, and stop conditions
            ├── references/
            │   ├── release-checklist.md  # Detailed checklist loaded only when relevant
            │   └── rollback.md           # Recovery detail for the cases that need it
            ├── scripts/
            │   └── verify-release.sh     # Deterministic helper used by the procedure
            └── assets/
                └── release-notes.md     # Template or fixture used by the workflow
```

## Notes

- **Root `AGENTS.md`** says when the procedure should be used and where the skill lives. It does not duplicate the entire procedure.
- **`SKILL.md`** explains the skill's purpose, activation conditions, required inputs, sequence, validation, and failure/stop conditions.
- **`references/`** holds material needed only for some runs. Keep the main procedure readable and load detail when relevant.
- **`scripts/`** belongs when a repeatable step can be made deterministic and the helper is worth maintaining alongside the procedure.
- **`assets/`** belongs when the procedure uses stable templates, fixtures, or other supporting files. Omit it when the skill is self-contained.
- **`.agents/skills/`** is one common shared skill location. Claude Code uses `.claude/skills/`; other harnesses may use different locations. Confirm the actual discovery mechanism and keep one canonical copy rather than maintaining independent duplicates.

## When to create a skill

A one-off task, unstable procedure, or generic reminder does not earn a skill. Create one when the process recurs, its steps matter, and keeping it on demand improves the always-loaded context.

Procedures that publish, deploy, delete, or affect external systems should make their authorization and approval boundaries explicit.

See [agent context guidance](../../docs/agent-context.md) and [the agent-first project](../agent-first-project/tree.md).
