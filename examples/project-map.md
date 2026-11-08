# Example: A Project Map That Adds Meaning

A project map earns its place when it helps an agent understand relationships that are difficult to infer from paths and filenames.

Imagine a repository with several services, shared packages, generated clients, and deployment units. The directory tree shows where files live, but it does not explain:

- which service owns a particular capability;
- which packages are shared contracts versus implementation details;
- which runtime entry points depend on which services;
- where validation differs;
- which generated artifacts come from which source.

A concise map can explain those relationships and point to the authoritative files. It should answer common navigation questions quickly, not inventory every file.

Start with the smallest useful form: a short section in README or a relevant domain document. Give the map a separate file when it has enough content and an independent update responsibility to justify one.

Keep the map semantic. Let the repository tree, package manifests, and generated tooling provide information they already own.
