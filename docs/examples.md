# Growth Examples

These examples are non-normative. They demonstrate how to apply the standard without turning every observed problem into permanent structure.

## 1. README contamination

### Observed

`README.md` contains setup instructions, current implementation progress, unfinished TODOs, three prior release summaries, blockers, and the next agent's instructions.

### Diagnosis

The README has acquired several incompatible lifecycles because no routing rule prevented convenient dumping.

### Action

- Keep project purpose, setup, and normal usage in README.
- Move shipped release-facing changes to the changelog if the project uses one.
- Move current progress, blockers, validation state, and next action to the scoped active-work artifact.
- Promote only genuinely durable discoveries to durable documentation.
- Delete temporary debugging narrative that no longer has value.

### Growth

None. The fix is routing, not a new documentation category.

## 2. HANDOFF.md becomes enormous

### Observed

A permanent `HANDOFF.md` grows for months and contains multiple completed features, old blockers, architecture notes, release notes, and current work.

### Diagnosis

The handoff file has no bounded owner or retirement point.

### Action

Move current continuation state into the active task's work artifact. Promote durable conclusions to their proper owners. Let Git/issues/PRs retain raw history.

Delete or archive the old handoff after useful information has been promoted.

### Growth

Create task-scoped persistent work only if work actually crosses sessions/agents. Do not replace one global handoff with a larger handoff framework.

## 3. CHANGELOG.md becomes a development diary

### Observed

The changelog contains attempted fixes, abandoned approaches, blockers, internal refactors, TODOs, and session summaries.

### Diagnosis

Release history is being used as active work storage.

### Action

Keep only notable shipped changes appropriate to the project's users or release consumers. Move active state to the current work artifact. Leave raw implementation chronology to Git/issues/PRs.

### Growth

None.

## 4. One architecture discussion occurs

### Observed

A task requires choosing between two internal module layouts.

### Wrong response

Create `docs/architecture/`, an architecture index, ADR tooling, and an architecture-review workflow.

### Better response

Record the task-level choice in the active work artifact. If the choice later becomes a durable boundary that future work repeatedly needs, promote it then.

### Growth

None yet.

## 5. The same durable decision keeps being rediscovered

### Observed

Three separate agents propose replacing SQLite with Postgres. Each time, maintainers explain the same offline-first and deployment constraints.

### Diagnosis

The rationale is non-obvious, durable, repeatedly needed, and expensive to reconstruct.

### Action

Create one decision record explaining the constraint, alternatives, and consequences. Link to it from relevant project documentation rather than copying the rationale.

### Growth

One decision document. Do not create a `decisions/` directory until enough independent decisions justify it.

## 6. An agent repeatedly forgets a required generation step

### Observed

Schema changes repeatedly ship without regenerating a client.

### Progression

1. First occurrence: record it in the task and fix the immediate defect.
2. Repetition: add a concise durable instruction if agents cannot infer the requirement.
3. Mechanical opportunity: add a stale-generation check to validation/CI.
4. After enforcement is reliable: shrink prose to the reason and remediation path.

### Growth

The rule graduates from observation to instruction to enforcement. It does not remain duplicated at every level.

## 7. A monorepo's backend and frontend have conflicting rules

### Observed

Global agent instructions contain separate backend and frontend command stacks, test rules, and conventions. Agents apply the wrong rules across areas.

### Diagnosis

Global context has become noisy and scope-specific.

### Action

Keep only cross-repository rules at the root. Move subsystem-specific rules to nested `AGENTS.md` files or path-scoped mechanisms supported by the coding tool.

### Growth

This is a Level 3 domain trigger because the rules have genuinely different scopes.

## 8. A documentation file becomes large

### Observed

`docs/operations.md` reaches 500 lines.

### Wrong response

Split it solely because the line count feels large.

### Better response

Inspect responsibility and retrieval patterns. If the file still has one coherent owner and readers usually need the whole thing, keep it. If deployment, incident response, backups, and migrations now evolve independently, split along those responsibilities.

### Growth

Size alone is not the trigger. Independent ownership/lifecycle is.

## 9. A project starts with twenty files

### Observed

A new project already contains source, tests, CI, manifests, deployment configuration, and several tool-generated files.

### Action

Do not mirror the upstream guide's structure. Establish only the owners the project already needs:

- README for project/use information;
- AGENTS for non-derivable agent rules and commands;
- adoption manifest if using this standard;
- changelog only if release history matters;
- additional durable/work artifacts only when the existing twenty files create an actual ownership gap.

### Growth

Starting file count does not determine maturity level.

## 10. The upstream standard changes

### Observed

The project adopts standard 0.1.0 and upstream releases 0.2.0 with a new routing rule.

### Action

Compare versions, read the changelog and changed normative guidance, audit the project, record any justified exception, and deliberately adopt 0.2.0 when ready.

### Growth

The project does not copy upstream files or automatically restructure itself.
