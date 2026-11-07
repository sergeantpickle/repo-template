# Example: Starting at Twenty Files

A new service already contains application code, tests, a package manifest, Docker configuration, two GitHub workflows, database migrations, generated API types, and deployment configuration.

That does not make it a Level 3 or Level 4 repository.

The initial control question is not "how many files exist?" It is "which coordination responsibilities already exist and which are ambiguous?"

A reasonable initial state may still be only:

```text
README.md
AGENTS.md
.repo-standard.json
<actual source/test/build/deploy files>
```

README explains purpose/setup/usage. AGENTS records exact validation commands and non-obvious boundaries. The standard adoption manifest points upstream.

Architecture documentation is added only if important relationships or boundaries are expensive to infer from the existing code/configuration. A project map is added only if semantic navigation is repeatedly costly. A changelog is added only when release history has an audience.

Starting complexity can justify earlier growth, but file count itself is not the trigger.
