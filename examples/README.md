# Annotated Repository Examples

Each example folder contains a `tree.md` with a Markdown directory tree, inline notes on important paths, and an explanation of when the structure is useful. These are reference layouts, not starter kits.

The root [AGENTS.md](../AGENTS.md) contains shorter versions of the trees so agents can orient quickly. Open the linked `tree.md` for the full notes.

## Start with the project shape

| Example | What it demonstrates |
| --- | --- |
| [Seed project](seed-project/tree.md) | A small, coherent project with no speculative structure. |
| [Application project](application-project/tree.md) | A product application with UI, server behavior, data, and tests. |
| [Library or SDK](library-project/tree.md) | A reusable package with a public API, consumer examples, compatibility, and release concerns. |
| [Monorepo](monorepo/tree.md) | Multiple applications, services, and shared packages in one workspace. |
| [Agent-first project](agent-first-project/tree.md) | Agent context, skills, specialist agents, evaluations, and durable plans. |
| [Research or data project](research-project/tree.md) | Data provenance, notebooks, reusable analysis, experiments, and reports. |

## Add patterns when the work earns them

| Example | What it demonstrates |
| --- | --- |
| [Growing project](growing-project/tree.md) | Durable architecture, operational knowledge, and decision records. |
| [Scoped instructions](scoped-instructions/tree.md) | Local agent instructions for genuinely distinct domains. |
| [Repeatable workflows](repeatable-workflows/tree.md) | On-demand skills and their references, scripts, and assets. |
| [Semantic project map](semantic-project-map/tree.md) | Ownership, dependencies, entry points, and flows that paths alone do not explain. |
| [Organization scale](organization-scale/tree.md) | Service catalogs and cross-repository ownership/dependency views. |

Project shape and project scale are different dimensions. A library can have scoped instructions; a monorepo can need a semantic map; a research project can use repeatable workflows. Combine only the patterns that solve real problems.

## How to read a tree

Every tree is illustrative. Inline comments explain the role of each path; notes below the tree explain its trigger, lifecycle, and optional pieces.

- **Keep** a path when the responsibility exists and needs that owner.
- **Omit** it when the responsibility does not exist or another system already owns it.
- **Split** a file into a directory when several independently useful artifacts need separate lifecycles.
- **Scope** instructions only where local behavior differs.
- **Adapt** names and layout to the language, framework, build system, and agent tools actually used.

The trees are intentionally selective. A real repository also contains the source files, language manifests, build configuration, deployment resources, generated artifacts, and other project-specific material its work requires. No example is a complete list of everything a project must contain.
