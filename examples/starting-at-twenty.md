# Example: Starting with Twenty Files

A new project begins with an application, tests, package metadata, container configuration, database migrations, generated API types, and deployment workflows. It already has twenty files before its first feature is complete.

That is a valid starting point. The repository's initial structure should reflect the responsibilities that already exist.

A useful initial arrangement might include:

- a README for purpose, setup, and normal use;
- an AGENTS.md for project-wide agent boundaries and exact validation commands;
- the source, tests, build configuration, migrations, and deployment files the project actually needs.

The project may also need a concise architecture or operations reference immediately if important boundaries are not apparent from the implementation. It does not need a project map merely to repeat the directory tree.

As the work develops, add a task record when work must survive sessions, durable documentation when non-obvious knowledge is repeatedly needed, and scoped instructions when domains diverge.

**Starting complexity can justify structure early. File count alone does not determine what the project needs.**
