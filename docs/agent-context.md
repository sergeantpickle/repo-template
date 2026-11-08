# Agent Context and Instructions

Agent-facing repository structure has two connected jobs:

1. Give every agent a reliable entry point into the project.
2. Make deeper instructions, procedures, and knowledge available only when relevant.

For annotated layouts, see [scoped instructions](../examples/scoped-instructions/tree.md), [monorepos](../examples/monorepo/tree.md), [agent-first projects](../examples/agent-first-project/tree.md), and [repeatable workflows](../examples/repeatable-workflows/tree.md).

## The root instruction file

A useful root `AGENTS.md` usually contains:

- what the project is and what belongs in it;
- the most important repository-wide boundaries;
- exact commands that already work;
- a short directory/architecture map;
- where to find deeper guidance for common tasks;
- permission boundaries for risky or irreversible actions.

Treat it as an orientation and routing document, not an encyclopedia. Include enough of the tree to make the project legible, then link to deeper documents for architecture, operations, product behavior, or specialist procedures.

Keep rules concrete and current. A command that no longer works or an architectural rule that describes an aspiration rather than the code can mislead every new session.

## Different tools discover different files

Do not assume every coding agent reads the same filenames or uses the same inheritance rules.

- Codex recognizes `AGENTS.md` and supports directory-scoped instruction files.
- Claude Code uses `CLAUDE.md`, supports nested instruction files, and also provides `.claude/rules/` for path-scoped rules.
- Other tools may use their own instruction files, configuration, or project settings.

When multiple tools need the same guidance, keep one canonical source and use supported imports, symlinks, or small adapters where practical. Do not maintain several full independent copies of the same rules.

See [Anthropic's instruction-file guidance](https://code.claude.com/docs/en/memory) and the [Codex AGENTS.md guide](https://developers.openai.com/codex/guides/agents-md).

## Scope instructions by real differences

Nested instruction files are useful when a subtree has different:

- build or validation commands;
- architectural or dependency boundaries;
- security or data-handling requirements;
- code conventions or review expectations;
- owners and working practices.

Keep shared rules at the root. A local file should explain only what differs and point back to shared context where needed.

For cross-cutting concerns that affect multiple non-contiguous paths, use a tool's path-scoped rule mechanism when it is supported. Do not mirror every source directory with an instruction file.

## Skills and reusable procedures

A skill is useful when a procedure recurs and benefits from its own trigger, steps, decision points, validation, and supporting resources.

Common skill structure:

```text
.agents/
└── skills/
    └── data-migration/
        ├── SKILL.md
        ├── references/
        └── scripts/
```

The location is tool- and ecosystem-dependent. Claude Code uses `.claude/skills/`; other agent ecosystems recognize other paths. Choose the location the project actually uses and avoid duplicate independently maintained skill copies.

Keep the skill's main instructions focused. Put large reference material in `references/` and deterministic helpers in `scripts/` only when they genuinely support the procedure.

## Specialized agents

A specialist agent can help when a distinct role, review perspective, tool boundary, or parallel-work pattern recurs.

```text
.claude/
└── agents/
    ├── code-reviewer.md
    └── test-engineer.md
```

This is a Claude Code-specific example, not a universal directory convention. Do not create a collection of agents just because the platform supports them. Define their scope, tools, expected output, and handoff clearly.

## Plans, evaluations, and feedback

Long-running or multi-agent work may justify persistent plans. Agent-driven features may need evaluations that test behavior beyond ordinary unit tests. Put these where the project can find and maintain them:

- active and completed execution plans, when work spans sessions or multiple contributors;
- `evals/`, when model or agent behavior needs repeatable evaluation;
- scripts and CI checks, when a deterministic guarantee is important;
- concise architecture and decision records, when context is expensive to reconstruct.

These are independent capabilities. A project does not need all of them.

See [agent-first project](../examples/agent-first-project/tree.md) and [OpenAI's harness engineering case study](https://openai.com/index/harness-engineering/).
