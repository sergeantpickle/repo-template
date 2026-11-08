# Agent-First Project

A repository where coding agents perform a substantial share of implementation, review, research, or operations. The structure makes context discoverable, separates shared rules from tool-specific configuration, and provides repeatable ways to evaluate agent behavior.

This is a mature example. It combines patterns that should be introduced only when the work justifies them.

## Example tree

```text
agent-first-product/
├── AGENTS.md                         # Canonical project-wide entry point and routing map
├── CLAUDE.md                         # Claude entry point importing shared guidance, if needed
├── README.md                         # Human-facing product and developer entry point
├── ARCHITECTURE.md                   # Cross-domain system map, if needed
├── src/                              # Product implementation
├── tests/                            # Deterministic tests of product behavior
├── evals/
│   ├── README.md                     # What agent behavior is evaluated and how
│   ├── cases/                        # Representative prompts, fixtures, and scenarios
│   └── graders/                      # Human or deterministic evaluation criteria
├── .agents/
│   └── skills/
│       └── data-migration/
│           ├── SKILL.md              # Trigger, procedure, validation, and stop conditions
│           └── references/           # On-demand procedure detail
├── .claude/
│   ├── rules/
│   │   └── api-paths.md              # Claude-specific path-scoped constraints
│   ├── agents/
│   │   └── reviewer.md               # Claude-specific specialist definition
│   └── skills -> ../.agents/skills/  # Optional alias when supported and verified
└── docs/
    ├── design-docs/
    │   ├── index.md                  # Design document navigation
    │   └── system-boundaries.md      # Current architecture and rationale links
    ├── product-specs/
    │   └── core-workflows.md         # Durable user-facing behavior and acceptance context
    ├── exec-plans/
    │   ├── active/                   # Complex work still in progress
    │   └── completed/                # Completed plans retained when useful
    └── references/                   # External or vendor references needed for work
```

## Notes

- **`AGENTS.md`** is the shared entry point. It describes the project, core boundaries, commands, and where to find task-specific context. Keep it concise enough to be useful at session start.
- **`CLAUDE.md`** appears only when Claude Code needs its own entry point. Use a supported import or symlink to the canonical shared guidance rather than maintaining a second full instruction set. Other tools may require different adapters.
- **`ARCHITECTURE.md`** is useful when several domains or dependency layers need a single bird's-eye map. It should describe boundaries and dependency direction, not repeat every package README.
- **`evals/`** tests agent or model behavior against representative scenarios. It complements ordinary software tests; it does not replace them. A project without agent-specific behavior to evaluate does not need it.
- **`.agents/skills/`** illustrates a shared skill source used by some agent ecosystems. The project must verify the discovery path for its tools. Claude Code's native skills live under `.claude/skills/`; the tree shows an optional alias, not a second copy.
- **`.claude/rules/`** and **`.claude/agents/`** are Claude Code-specific surfaces. Other harnesses have their own rule and specialist-agent mechanisms. Add them only when using those capabilities.
- **`docs/design-docs/`** holds substantial design documents. An index is useful once several exist.
- **`docs/product-specs/`** describes durable product behavior or contracts when implementation details alone are not enough to orient work.
- **`docs/exec-plans/active/`** is useful when complex work must survive sessions or agents. Completed plans should be retained only when their history remains useful. A small task can stay in an issue or pull request.
- **`docs/references/`** stores material agents need to consult repeatedly. Avoid mirroring entire vendor documentation sets without a clear need.

## What not to copy

Do not create every folder at project initialization. Start with AGENTS.md and the real application structure. Add evaluations when agent behavior matters, skills when procedures repeat, plans when work spans contexts, and deeper documentation when the information is expensive to rediscover.

## Related patterns

- [Scoped instructions](../scoped-instructions/tree.md) for local context boundaries.
- [Repeatable workflows](../repeatable-workflows/tree.md) for skill structure.
- [Semantic project map](../semantic-project-map/tree.md) for architecture navigation.
- [OpenAI harness engineering](https://openai.com/index/harness-engineering/) and [Anthropic's Claude Code guidance](https://claude.com/resources/articles/steering-claude-code-skills-hooks-rules-subagents-and-more) for the practices behind this example.
