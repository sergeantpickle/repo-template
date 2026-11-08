# Research Notes

Last reviewed: **2026-11-07**

These notes record patterns observed in public agent-oriented repositories and current platform guidance. They inform this reference; they are not universal rules. Repository examples demonstrate local choices, while platform documentation describes behavior that can change.

## A strong example library uses complexity-based folders and annotated structures

[Fending's context-engineering repository](https://github.com/fending/context-engineering) organizes examples into separate folders for a single instruction file, a context directory, cascading instructions, agents, and agent teams. Each folder has a README that explains when to use the pattern, shows its structure, and points to concrete example files. The root AGENTS.md describes the example catalog and tells contributors to update the relevant README when an example's structure changes.

Implication: this guide should have example folders organized around distinct repository patterns. Each example should include its own annotated tree and notes, while the root AGENTS.md provides a compact map of the patterns.

Source: https://github.com/fending/context-engineering

## Realistic filled examples teach more than empty folder lists

[Agent Context Kit](https://github.com/pinkpixel-dev/agent-context-kit) pairs a concise agent instruction template with filled-in context documents from a fictional project. Its README explains which information belongs in each file and separates current project state from dated decisions and debugging lessons.

Implication: annotated trees should be paired with concrete file examples or meaningful descriptions of what the files contain. A tree of empty placeholders does not teach an agent how the information is used.

Source: https://github.com/pinkpixel-dev/agent-context-kit

## Root AGENTS files work best as maps to deeper context

[Harness Template](https://github.com/experiments-with-ai/harness-template) describes its root AGENTS.md as a map, not an encyclopedia. It points to architecture, workflow, bootstrap, and review guides. Its docs directory has a separate AGENTS.md that indexes documentation subdomains, and specialized subdirectories own their own instruction files.

Implication: the root of this reference should contain structural patterns and direct links to the annotated examples. Deeper explanation belongs in docs and example folders.

Source: https://github.com/experiments-with-ai/harness-template

## A document index is useful when it tells agents what to read and when

[Emanuel University's AI agent template](https://github.com/Emanuel-University/ai-agent-template) keeps its root AGENTS.md short and uses a document index that maps each file to its subject and the moment an agent should read it. It also recommends thin pointers for tool-specific instruction files rather than independently maintained copies.

Implication: the root map should route by task and responsibility, not merely enumerate filenames. A separate index is useful when it provides meaningful selection guidance.

Source: https://github.com/Emanuel-University/ai-agent-template

## Nested AGENTS files are a real context boundary

Current [Codex instruction discovery](https://learn.chatgpt.com/docs/agent-configuration/agents-md) collects applicable instructions from the repository root down to the current working directory. [GitHub Copilot](https://github.blog/changelog/2025-08-28-copilot-coding-agent-now-supports-agents-md-custom-instructions/) also supports root and nested AGENTS.md files. Other agent harnesses have their own instruction filenames, scopes, and loading rules.

Implication: examples should show nested AGENTS.md files only where a domain has distinct conventions or boundaries, and should explain that discovery behavior is harness-dependent.

Sources:

- https://learn.chatgpt.com/docs/agent-configuration/agents-md
- https://github.blog/changelog/2025-08-28-copilot-coding-agent-now-supports-agents-md-custom-instructions/
- https://code.visualstudio.com/docs/agents/reference/custom-instructions-reference

## Skills and deeper references are a useful on-demand layer

[OpenAI's agent skills guidance](https://developers.openai.com/api/docs/guides/tools-skills) describes skills as reusable procedures that can bundle instructions, scripts, and references. The [Agent Context Kit](https://github.com/pinkpixel-dev/agent-context-kit) uses this separation to keep detailed context-maintenance procedures out of the always-loaded instruction file.

Implication: a skills directory belongs in an example for recurring procedures, not in every seed repository. The path and discovery rules must match the agent harness being used.

Sources:

- https://developers.openai.com/api/docs/guides/tools-skills
- https://github.com/pinkpixel-dev/agent-context-kit

## Large agent-first repositories use layered knowledge, not one universal tree

OpenAI's [harness engineering case study](https://openai.com/index/harness-engineering/) describes an agent-first codebase using concise entry instructions, structured repository knowledge, execution plans for complex work, mechanical checks, and ongoing documentation maintenance. The [agentic-templates repo-template](https://github.com/agentic-templates/repo-template) demonstrates a more prescriptive workflow with issue admission, branches, pull requests, hooks, and release automation.

Implication: richer structures can support substantial parallel work, but the operational machinery in those repositories should not be treated as a default layout for every project.

Sources:

- https://openai.com/index/harness-engineering/
- https://github.com/agentic-templates/repo-template

## Documentation ownership and deliberate promotion prevent context drift

[Diew's Living Docs](https://github.com/Diew/living-docs) uses a registry to map documents to the information they own and the tasks that should load them. It also recommends a human confirmation point before promoting implementation details into durable knowledge. This is a more prescriptive system than the one described here, but its ownership and promotion concerns are useful.

Implication: examples should annotate why each file exists, who owns its information, and what event should update it. Do not create a registry unless the project's size makes a simple index insufficient.

Source: https://github.com/Diew/living-docs

## Review policy

Refresh these notes when:

- agent harnesses materially change instruction discovery or skill loading;
- strong new repository examples demonstrate a different structural pattern;
- benchmark or field evidence contradicts a current recommendation;
- repeated project reviews reveal that an example encourages unnecessary structure.

Prefer primary platform documentation for claims about current tool behavior. Treat individual repository layouts as examples of choices, not proof that every project should make the same choices.
