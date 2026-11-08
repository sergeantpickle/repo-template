# Annotated Repository Examples

These examples show concrete repository layouts for common situations. Each example folder contains a `tree.md` file with an annotated Markdown directory tree and notes explaining the purpose of each path, when it earns its place, and what should remain optional.

They are reference patterns, not starter kits. Adapt them to the actual work instead of copying every path.

| Example | What it demonstrates |
| --- | --- |
| [Seed project](seed-project/tree.md) | A useful small repository without speculative structure. |
| [Growing project](growing-project/tree.md) | Durable technical knowledge and decision records with clear owners. |
| [Scoped instructions](scoped-instructions/tree.md) | Nested AGENTS files for domains with genuinely different rules. |
| [Monorepo](monorepo/tree.md) | Root guidance plus local context for independently evolving apps, services, and packages. |
| [Repeatable workflows](repeatable-workflows/tree.md) | Skills and supporting references for procedures that recur. |
| [Semantic project map](semantic-project-map/tree.md) | A map that explains relationships the directory tree cannot show. |
| [Organization scale](organization-scale/tree.md) | Catalogs, ownership, and dependency views when many components must coordinate. |

## How to read a tree

Each tree uses inline comments to identify a path's responsibility. Notes below the tree explain the trigger for adding it and what not to infer from its presence.

- **Keep** a path when the described responsibility exists in the project.
- **Omit** it when the responsibility does not exist or another system already owns it.
- **Split** a file into a directory only when several independently useful artifacts need their own lifecycle.
- **Scope** instructions only where local behavior differs from the root.

The trees are intentionally not exhaustive. A real repository also contains language manifests, build configuration, source files, generated output, deployment resources, and other project-specific material.
