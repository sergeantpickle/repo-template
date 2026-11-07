# Documentation Governance

## Purpose

Keep repository knowledge trustworthy, navigable, and usable by fresh humans and agents.

## Authority

When repository artifacts conflict, use this precedence model:

1. Executable code, tests, schemas, configuration, and observed runtime behavior describe what currently exists.
2. Accepted decision records and architecture documents describe durable intended structure and constraints.
3. Product, design, operations, quality, and reference documents describe their scoped contracts.
4. Active execution plans describe work in progress and intended changes; they do not prove shipped behavior.
5. Research and handoffs provide evidence and continuation context; they are not canonical truth.
6. Generated documents are authoritative only for facts derived from their generator and must be regenerated rather than hand-edited.

A contradiction should be resolved by updating the stale artifact, not by adding another explanation elsewhere.

## Lifetimes

### Durable

Architecture, product contracts, accepted decisions, operations, quality rules, and technical reference remain current until intentionally changed or superseded.

### Active

Execution plans are living task records. Keep them accurate while work is active.

### Historical

Completed plans, superseded decisions, research snapshots, and dated handoffs are retained for provenance but must not masquerade as current state.

### Generated

Generated artifacts must identify their source or generator.

## Update protocol

When behavior or architecture changes:

1. update the implementation;
2. update the canonical durable documentation affected by the change;
3. record a durable decision when the change introduces a meaningful long-lived choice or invariant;
4. update the active execution plan;
5. update `docs/README.md` if navigation changed;
6. run repository knowledge checks when available.

## Naming

Use lower-case kebab-case filenames under `docs/` unless a tool or ecosystem convention requires otherwise.

Recommended dated artifact form:

`YYYY-MM-DD-topic.md`

Decision records may use:

`NNNN-short-title.md`

## Metadata

Add metadata only where it provides mechanical value. Avoid front matter that no check or workflow consumes.

## Duplication

Prefer one canonical explanation with links from other surfaces. Repeated prose becomes drift.

## Deletion

Delete obsolete documentation when it has no historical value. Historical retention is not a reason to keep every intermediate note.
