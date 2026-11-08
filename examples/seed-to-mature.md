# Example: One Agent to a Well-Organized Project

This example shows one way a repository can gain structure as its work becomes more demanding. Each stage appears because the project has a new responsibility to support.

## Start — one agent, one coherent project

The repository has:

- a README that explains the project and how to use it;
- a concise AGENTS.md with project-wide boundaries and exact validation commands;
- the source, configuration, and tests needed by the project.

The agent can understand most of the system from the code and a small amount of context. No extra documentation framework is needed.

## Continuing work — context survives sessions

A substantial migration now spans several sessions. The agent needs to preserve the objective, decisions still under investigation, validation state, and next action.

The project gives that migration a bounded work record in the system it already uses: perhaps an issue, pull request, or task plan. The record closes when the work is complete.

## Reusable knowledge — the same rationale matters again

Several later changes depend on an append-only storage decision. The reasoning is not obvious from the code, and agents repeatedly need to reconstruct it.

The project records the decision once and links to it from relevant work. The decision has one clear owner and is updated if the constraint changes.

## Distinct domains — local context becomes useful

The project now contains an API and a data pipeline. Their commands, conventions, and validation differ enough that a single global instruction file is no longer the best place for every rule.

The project keeps cross-cutting instructions at the root and adds scoped guidance for the two domains.

## Repeated validation — a check becomes dependable

Agents repeatedly need to regenerate API clients after changing a schema. The project adds a deterministic freshness check so the guarantee no longer depends on remembering a sentence in AGENTS.md.

The instruction becomes shorter and points to the check.

## Simplification — the project changes again

The data pipeline is later retired. Its scoped instructions, domain reference, and special validation are removed. The repository returns to a simpler shape that fits its current work.

The project has grown and simplified without treating any stage as permanent.
