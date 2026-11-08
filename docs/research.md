# Research Notes

Last reviewed: **2026-11-07**

These notes capture useful patterns found in agent-heavy repositories, vendor guidance, and research. They inform the guide; they are not rules by themselves. Agent platforms change quickly, so revisit platform-specific claims before relying on them.

## Keep the always-loaded context small and useful

Recent agent-memory and coding-agent guidance favors a small persistent orientation layer with deeper information retrieved when relevant. Repository-wide instructions are most useful when they contain cross-project constraints, exact commands, and pointers—not a complete history or manual.

Useful references:

- [Anthropic: Components of Agent Memory](https://www.anthropic.com/research/components-of-agent-memory)
- [Claude Code: Memory and instruction files](https://code.claude.com/docs/en/memory)
- [OpenAI: Harness engineering](https://openai.com/index/harness-engineering/)

## Package repeated procedures, not imagined future needs

Skills and reusable workflows can hold stable procedures, scripts, and references without making every instruction part of the always-loaded context. They are most valuable when a process recurs and its steps are costly to restate correctly.

Useful references:

- [OpenAI: Skills in the API](https://developers.openai.com/cookbook/examples/skills_in_api)
- [OpenAI: Tools and skills](https://developers.openai.com/api/docs/guides/tools-skills)
- [Emanuel University: AI agent template](https://github.com/Emanuel-University/ai-agent-template)

## Keep one source of truth while allowing different work systems

Agent-forward repositories use several valid ways to manage active work: repository plans, issues, pull requests, change proposals, or external trackers. The common need is bounded ownership of continuation state, not one universal filename or workflow.

Useful references:

- [Codex repository template](https://github.com/xklob/codex-repo-template)
- [Agentic templates repository](https://github.com/agentic-templates/repo-template)
- [OpenAI Codex development workflow](https://github.com/openai/openai-cookbook/blob/main/examples/codex/iterating-development-workflows-with-codex.md)
- [OpenSpec concepts](https://github.com/Fission-AI/OpenSpec/blob/main/docs/concepts.md)

## Let structure follow real domain boundaries

Agent-heavy repositories demonstrate several useful approaches: concise root instructions, scoped domain guidance, generated tool-specific adapters, and deeper documentation loaded on demand. The right arrangement depends on how the project is actually divided.

Useful references:

- [anywhere-agents](https://github.com/yzhao062/anywhere-agents)
- [Diew/living-docs](https://github.com/Diew/living-docs)
- [Agent drift](https://github.com/untactit/agent-drift)

## Organization-scale knowledge is different from project-scale knowledge

When many independently evolving services or components exist, catalogs, ownership metadata, dependency maps, and shared interfaces can make the whole system discoverable. Those mechanisms earn their place when local context is no longer enough.

Useful references:

- [Backstage software catalog](https://backstage.io/docs/features/software-catalog/)
- [Repository standards/core](https://github.com/repository-standards/core)

## Read evidence in context

A public repository demonstrates one team's solution to its own constraints. A benchmark measures the tasks and environment it defines. Vendor documentation describes a platform's intended behavior. None of these alone establishes a universal rule.

Use sources to discover patterns, then ask whether the pattern solves a real problem in the project being changed. Prefer recent primary documentation for fast-moving platform behavior and record the date when a platform-specific claim was last checked.
