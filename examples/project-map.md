# Example: Does This Repository Need an INDEX or PROJECT Map?

A project map is not forbidden. It has to earn existence.

## Do not create one when

- it merely restates the directory tree;
- a fresh agent can identify entry points, tests, build commands, and boundaries cheaply from manifests and code;
- keeping the map current would duplicate information already owned by package metadata or generated tooling.

## Create one when

Repeated work shows that semantic relationships are expensive to reconstruct, for example:

- a monorepo has many packages whose ownership and dependency roles are not obvious from paths;
- several runtime entry points interact in ways the tree cannot express;
- generated, deployed, and source artifacts have important relationships that agents repeatedly misunderstand;
- validation commands differ by domain and discovery is repeatedly costly.

The map should add semantic navigation, not inventory every file.

## Growth path

Start with a concise section in an existing owner such as README or AGENTS if that solves the discoverability problem without mixing lifecycles.

If the map becomes independently useful and has its own update lifecycle, promote it to a dedicated document such as `PROJECT.md` or `docs/map.md`.

The filename is secondary to a clear responsibility and maintenance trigger.
