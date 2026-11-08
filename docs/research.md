# Research Notes

Last reviewed: **2026-11-07**

This guide is informed by real agent-oriented repositories, official agent-tool documentation, and practical workflow examples. The sources below demonstrate patterns that exist in particular environments; they are not universal prescriptions.

## Patterns that recur in real repositories

### AGENTS.md as a map, backed by deeper repository knowledge

OpenAI's harness-engineering case study describes a small root `AGENTS.md` that points into a structured `docs/` knowledge base. Its example includes design documents, active and completed execution plans, product specifications, generated references, and domain guidance. The stated reason is progressive disclosure: agents begin with a concise map and retrieve the relevant knowledge for the task.

Source: [OpenAI — Harness engineering](https://openai.com/index/harness-engineering/)

### Concrete trees in agent instructions

Real project instructions often contain a directory map with inline comments. Apache Airflow's root `AGENTS.md` describes its monorepo's major packages, key subdirectories, and architecture boundaries. AWS's Bedrock AgentCore SDK TypeScript repository includes a much more detailed tree with path-by-path descriptions and asks maintainers to update it when structure changes.

Sources:

- [Apache Airflow — AGENTS.md](https://github.com/apache/airflow/blob/main/AGENTS.md)
- [AWS Bedrock AgentCore SDK — AGENTS.md](https://github.com/aws/bedrock-agentcore-sdk-typescript/blob/main/AGENTS.md)

### Different project types and work styles use different layouts

OpenAI's Codex workflow example shows a small application using `AGENTS.md`, `GOALS.md`, `PLANS.md`, `PROMPTS.md`, and a `harness/` directory for phase plans, context, build logs, and review records. The example explicitly says these are optional conventions and warns against assuming every project needs the same harness.

Source: [OpenAI Cookbook — Iterating development workflows with Codex](https://developers.openai.com/cookbook/examples/codex/iterating-development-workflows-with-codex)

### Tool-specific instruction surfaces have different loading behavior

Anthropic documents root and nested `CLAUDE.md` files, path-scoped rules, skills, and subagents as distinct mechanisms. Root instructions are always present for the session; nested instructions and path-scoped rules can be limited to relevant work; skill bodies load when invoked; subagents work in isolated contexts.

OpenAI's Codex guidance describes root-to-leaf discovery of `AGENTS.md` files. These are related approaches, but the exact filenames, scope, and loading rules are tool-specific.

Sources:

- [Anthropic — Steering Claude Code](https://claude.com/resources/articles/steering-claude-code-skills-hooks-rules-subagents-and-more)
- [Claude Code — Memory and instruction files](https://code.claude.com/docs/en/memory)
- [OpenAI — Codex prompting guide](https://developers.openai.com/cookbook/examples/gpt-5/codex_prompting_guide)

### Root structure maps and "where to look" pointers

The `Emanuel-University/ai-agent-template` keeps its root `AGENTS.md` practical: a short `Structure` section describes the folders, and a `Where to look` section points to the architecture, testing, workflow, decisions, and state documents. Its architecture guide explicitly describes the system shape rather than every file.

This is a useful companion to the larger annotated trees: keep the root agent file navigable, then send the agent to the detailed owner when the task needs it.

Sources:

- [Emanuel University — AI agent template](https://github.com/Emanuel-University/ai-agent-template)
- [Architecture guide](https://github.com/Emanuel-University/ai-agent-template/blob/main/docs/architecture.md)

### Documentation categories work when each answers a different question

The `bketelsen/agentic-template` repository separates architecture decisions (why), design (how), specifications (what), and plans (when). The `Sukitly/agentic-docs-templates` repository demonstrates a richer knowledge base with state, deployment, testing, product specifications, design documents, execution plans, and references.

These are useful examples of explicit ownership. Their full structures are intentionally more prescriptive than most projects need.

Sources:

- [bketelsen/agentic-template](https://github.com/bketelsen/agentic-template)
- [Sukitly/agentic-docs-templates](https://github.com/Sukitly/agentic-docs-templates)

### Agent-heavy repositories use more than instructions

The `q-agent-harness` project organizes its guidance around a map, guardrails, feedback loops, and memory. The `mcqua007/agents-skeleton` project uses a short AGENTS table of contents, an architecture map, deeper docs, execution plans, product specifications, references, and skills.

These demonstrate that agent context, executable verification, and durable project knowledge are separate but connected parts of a working environment.

Sources:

- [q-agent-harness](https://github.com/kju4q/q-agent-harness)
- [agents-skeleton](https://github.com/mcqua007/agents-skeleton)

## A current counterweight: do not over-prescribe context

OpenAI's September 2026 guidance for GPT-6 Astra says accumulated `AGENTS.md` and skill instructions should be revisited as models improve. It specifically warns against requiring a full repository map or stack of documentation before every small edit; the agent should read the documents relevant to the task.

Source: [OpenAI — Rethinking skills and prompts for GPT-6 Astra](https://developers.openai.com/blog/rethinking-skills-and-prompts-for-gpt-6-astra)

This is why the guide puts compact structural references in `AGENTS.md` and detailed notes in examples, but does not tell every agent to read every example on every task.

## What this guide takes from the research

1. **Show the tree, then explain it.** A directory tree with inline notes makes a structure legible quickly. The example file should then explain triggers, ownership, optional paths, and tradeoffs.
2. **Put a compact map in AGENTS.md.** Agents need enough structure to choose the right path without loading every example. Link each tree to its detailed annotated example.
3. **Organize examples by real project shape.** Applications, libraries, monorepos, research projects, and agent-heavy projects have different natural structures. Growth patterns such as scoped instructions or semantic maps can be layered onto them.
4. **Separate shared guidance from tool-specific configuration.** A project may have a canonical AGENTS.md plus Claude-specific rules, skills, or agents. Show tool-specific directories only in the examples where they add value.
5. **Keep documentation categories optional.** Plans, ADRs, product specs, operations guides, evaluations, catalogs, and generated references each need a real owner and recurring use.
6. **Do not mistake a large example for a recommended baseline.** Some successful agent-first projects use substantial harnesses. Their structure is evidence of what can work at that scale, not a reason to install it in every repository.
7. **Make retrieval contextual.** A map should help an agent choose what to read, not become a ritual that forces every task through every document.

## How to use these sources

A repository demonstrates a solution to its own constraints. A vendor guide describes a particular tool's behavior. A case study reports one team's experience. Use them to identify useful patterns, then check whether those patterns fit the project being changed.

Prefer current primary documentation for tool-specific loading behavior. Revisit this research when major agent tools change their instruction discovery, skills, subagent, or context-loading models.
