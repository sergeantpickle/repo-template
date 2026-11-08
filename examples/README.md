# Annotated Repository Examples

These examples show concrete directory layouts for different project types and coordination needs. Each folder contains a `tree.md` with a Markdown directory tree, inline path notes, and an explanation of when each part is useful.

They are reference patterns, not starter kits. A project may combine patterns, start with a subset, or use a different structure that fits its language and tools.

## Choose by project shape

| Example | Use it to understand |
| --- | --- |
| [Seed project](seed-project/tree.md) | The smallest useful shape for a coherent project. |
| [Application project](application-project/tree.md) | A product application with UI, server behavior, data, and tests. |
| [Library or SDK](library-project/tree.md) | A reusable package with a public API, consumer examples, and release concerns. |
| [Growing project](growing-project/tree.md) | Durable architecture, operational knowledge, and decisions. |
| [Scoped instructions](scoped-instructions/tree.md) | Local agent instructions for genuinely distinct domains. |
| [Monorepo](monorepo/tree.md) | Multiple applications, services, and shared packages in one workspace. |
| [Agent-first project](agent-first-project/tree.md) | Agent instructions, skills, specialist agents, evaluations, and durable plans. |
| [Research or data project](research-project/tree.md) | Data provenance, notebooks, reusable analysis, experiments, and reports. |
| [Repeatable workflows](repeatable-workflows/tree.md) | On-demand skills and their references or helper scripts. |
| [Semantic project map](semantic-project-map/tree.md) | Ownership, dependencies, entry points, and flows that paths alone do not explain. |
| [Organization scale](organization-scale/tree.md) | Service catalogs and cross-repository ownership/dependency views. |

## How to read a tree

Every tree is illustrative. Inline comments explain the role of each path; notes below the tree explain its trigger, lifecycle, and optional pieces.

- **Keep** a path when the responsibility exists and needs that owner.
- **Omit** it when the responsibility does not exist or another system already owns it.
- **Split** a file into a directory when several independently useful artifacts need separate lifecycles.
- **Scope** instructions only where local behavior differs.
- **Adapt** names and layout to the language, framework, build system, and agent tools actually used.

The trees are intentionally selective. A real repository also contains the source files, language manifests, build configuration, deployment resources, generated artifacts, and other project-specific material its work requires. No example is a complete list of everything a project must contain.
