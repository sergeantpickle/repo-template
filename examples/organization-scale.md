# Example: Growing from One to Thousands

This trajectory uses people and agents to illustrate changing coordination needs. The numbers are not maturity thresholds. A repository grows when its responsibilities and coordination pressure grow.

## One maintainer or primary agent

The project is coherent enough to understand directly. A README, concise project instructions, and the actual source/configuration may be all it needs.

The maintainer can make most decisions locally and reconstruct context without a large knowledge system.

## A few concurrent contributors or agents

Work now crosses sessions and independent contexts. Bounded task records preserve scope, progress, validation, and next actions. Review and ownership become explicit where parallel changes can collide.

The project keeps its work system lightweight and uses the issue, pull request, or planning approach that already fits its workflow.

## Several independently evolving domains

Different areas develop their own conventions, dependencies, commands, and boundaries. Scoped instructions and domain documentation let each area carry the context it needs without loading it into every task.

Cross-domain interfaces and ownership become easier to discover.

## Dozens of parallel workstreams

Coordination now depends on reliable interfaces, clear ownership, discoverable validation, and consistent review. Repeated deterministic requirements move into tests, schemas, linters, generated checks, or permissions.

When the number of components makes relationships difficult to reconstruct, a semantic project map or ownership catalog can become valuable.

## Hundreds of independently changing components

The repository's topology becomes a system of its own. People and agents need to discover component ownership, dependencies, contracts, operational responsibilities, and change impact.

Service catalogs, dependency maps, shared interfaces, and organization-level documentation can provide that view.

## Thousands of contributors or agents

The organization needs consistent ways to evolve shared practices across many repositories and domains. Central guidance, ownership metadata, policy, migration support, and automated knowledge maintenance may now earn their cost.

Local projects still retain their own context and structure. Central guidance provides direction; it does not replace local understanding.

## The principle across every scale

The same question applies at every size:

**What coordination problem does this structure solve, and does it make the work clearer than the structure it adds?**

A small safety-critical repository can need strong controls immediately. A repository inside a 5,000-person organization can remain simple if its responsibility is simple. Growth follows the work, not the headcount.
