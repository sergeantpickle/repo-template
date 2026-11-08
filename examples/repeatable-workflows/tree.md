# Repeatable Workflows

A project repeats a multi-step procedure often enough that the exact sequence, branches, validation, or supporting assets should be maintained separately from always-loaded instructions.

## Example tree

```text
project/
├── AGENTS.md
└── .agents/
    └── skills/
        └── release/
            ├── SKILL.md                 # Trigger, procedure, decisions, and stop conditions
            ├── references/
            │   └── release-checklist.md # Detailed checklist loaded when needed
            └── scripts/
                └── verify-release.sh    # Deterministic helper used by the procedure
```

## Notes

- **Root `AGENTS.md`** says when the procedure should be used and where the skill lives. It does not duplicate the entire procedure.
- **`SKILL.md`** explains the skill's purpose, activation conditions, inputs, sequence, validation, and failure/stop conditions.
- **`references/`** holds material needed only for some runs. Keep the main procedure readable and load detail when relevant.
- **`scripts/`** belongs when a repeatable step can be made deterministic and the helper is worth maintaining alongside the procedure.

The example uses `.agents/skills/` as one common location. Skill discovery and directory conventions are harness-specific; use a location the project's actual tools recognize.

## When to create a skill

A one-off task, unstable procedure, or generic reminder does not earn a skill. Create one when the process recurs, its steps matter, and keeping it on demand improves the always-loaded context.

Procedures that publish, deploy, delete, or affect external systems should make their authorization and approval boundaries explicit.

See [agent context guidance](../../docs/agent-context.md).
