# Example: Seed to Mature Repository

This is a trajectory, not a target architecture.

## Stage A — seed

The repository begins with:

```text
README.md
AGENTS.md
.repo-standard.json
src/
tests/
```

The README explains the product and setup. AGENTS contains exact validation commands and two non-obvious boundaries. There is no changelog yet because there are no releases. There is no architecture file because the code is easy to inspect.

## Stage B — work survives context loss

A database migration spans several sessions. Progress and validation details start leaking into README.

Trigger: active work now needs a bounded durable owner.

The project creates one task artifact:

```text
work/
  migrate-storage.md
```

Nothing else is added.

## Stage C — one rationale keeps being rediscovered

Three later changes question why local storage is intentionally append-only. Reconstructing the rationale requires reading old issues and experiments.

Trigger: durable non-obvious rationale is repeatedly needed.

The project creates one decision document:

```text
docs/
  append-only-storage-decision.md
```

There is still no `docs/decisions/` directory because one file does not justify a taxonomy.

## Stage D — domains diverge

The repository becomes a web app plus a data pipeline. Their commands, dependencies, and validation rules are materially different, and agents repeatedly apply one domain's conventions to the other.

Trigger: global instructions have become noisy and misleading.

The project introduces scoped instructions near each domain while keeping only cross-project rules at the root.

## Stage E — repeated rule becomes mechanical

Agents repeatedly edit a schema without regenerating derived clients.

Trigger: the rule is repeated, mechanically detectable, and costly when missed.

CI gains a stale-generation check. The prose instruction shrinks because enforcement now owns the mechanical guarantee.

## Stage F — simplification

The data pipeline is later removed. Its scoped instructions, domain docs, and special checks are removed with it.

Maturity does not require preserving obsolete organizational structure.
