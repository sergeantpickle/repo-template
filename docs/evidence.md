# Evidence Base

Last reviewed: **2026-11-07**

This standard is intentionally revisable. Agent behavior and tooling change quickly, so vendor guidance and older work are evidence, not permanent doctrine.

## Small persistent context, deeper retrieval on demand

Anthropic's November 6, 2026 agent-memory research describes a hierarchy in which detailed event history and memories sit below a small injected layer. Current Claude Code documentation likewise favors concise persistent instructions, path-scoped rules, and skills for narrower procedures.

Implication: always-loaded repository instructions should be high-value and scoped; deeper knowledge should load when relevant.

Sources:

- https://www.anthropic.com/research/components-of-agent-memory
- https://code.claude.com/docs/en/memory

## Newer models need less forced scaffolding

OpenAI's September 11, 2026 GPT-6 Astra guidance warns that accumulated `AGENTS.md` and skill instructions can become bloated or contradictory. It specifically recommends against forcing a full repo map or stack of docs before every edit.

Implication: this standard should control growth without creating heavyweight mandatory onboarding for trivial tasks.

Source:

- https://developers.openai.com/blog/rethinking-skills-and-prompts-for-gpt-6-astra

## Agent-first scale still needs structured knowledge and garbage collection

OpenAI's 2026 harness-engineering case study reports that a monolithic instruction manual became stale and difficult to verify. Their larger agent-first repository moved toward short routing instructions, structured repository knowledge, task plans for complex work, mechanical checks, and recurring documentation gardening.

Implication: richer structure is justified by coordination pressure, but must be scoped and actively retired when stale.

Source:

- https://openai.com/index/harness-engineering/

## Repository context has mixed benchmark evidence

The 2026 AGENTBench study found repository-level context files did not generally improve task success and increased inference cost by more than 20% on average. A separate 2026 study found AGENTS.md associated with lower median runtime/output-token use in its smaller sample while maintaining comparable completion behavior.

Implication: persistent context should be treated as an optimization with cost, not a universal performance win.

Sources:

- https://arxiv.org/abs/2602.11988
- https://arxiv.org/abs/2601.20404

## Documentation drift compounds

An October 2026 study of 29,669 AI-generated pull requests reports that 63.2% changed code without documentation updates, and files changed without docs were later re-documented at roughly half the rate of files changed with docs over 90 days.

Implication: durable documentation needs clear ownership and co-change discipline; indiscriminate documentation creation is not the answer.

Source:

- https://arxiv.org/abs/2610.27381

## Central policy should not be copied into every generated artifact

GitHub Spec Kit's current upgrade model stopped propagating its constitution into dependent templates. Workflows resolve the live constitution at runtime because propagation created duplicate sources of truth and conflicted with centrally owned/versioned policy.

Implication: downstream projects should adopt this standard by reference/version rather than copying the full governance text.

Sources:

- https://github.github.com/spec-kit/upgrade.html
- https://github.com/github/spec-kit/blob/main/.specify/memory/constitution.md

## Progressive rigor counters ceremony

OpenSpec's current guidance favors the lightest workflow that keeps a change verifiable. Its model also separates active changes from archived history, and current maintainers are explicitly exploring ways to reduce archive ceremony where it does not earn its cost.

Implication: active/historical separation is valuable, but the standard should not force archival machinery into every project.

Sources:

- https://github.com/Fission-AI/OpenSpec/blob/main/docs/concepts.md
- https://github.com/Fission-AI/OpenSpec/issues/1968

## Native GitHub template copies are unsuitable for a rich upstream guide

Current GitHub template repositories create descendants with the same directory structure and files from the template branch. That behavior is useful for starter code but conflicts with this standard's architecture: the upstream repository intentionally contains governance, evidence, examples, tests, and audit implementation that should not become project-local knowledge.

Implication: this repository exports a minimal `starter/` into greenfield projects instead of using the full upstream tree as the downstream scaffold. Existing projects use pre-adoption review.

Sources:

- https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-repository-from-a-template
- https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-template-repository

## Copy-once templates have an update gap

The current `agentic-templates/repo-template` provides substantial agent-first automation but explicitly notes that repositories created from it do not receive later template changes.

Implication: initial scaffolding and long-lived governance are different problems. Long-lived governance needs an upstream version/update path.

Source:

- https://github.com/agentic-templates/repo-template

## Instruction drift is a measured independent problem

The independent `untactit/agent-drift` tool scans CLAUDE.md/AGENTS.md and other agent instruction files for copied versions that silently diverge.

Implication: multiple independent instruction surfaces are a drift risk unless differences are scoped or copies are generated/linked/checked.

Source:

- https://github.com/untactit/agent-drift

## Independent governance systems converge on canonical ownership, but differ on baseline size

The independent `Diew/living-docs` project uses a governance registry that maps every documentation file to what it owns, what it must not contain, and when an agent should load it. Its stated core rule is one owner per rule, with task-to-file routing.

That project also bootstraps a richer documentation skeleton (developer guide, reference, UI standards, refactor tracker, governance registry) than this standard assumes.

Implication: canonical ownership and contextual routing have independent practitioner support, while the amount of initial structure remains a design choice. This standard deliberately starts smaller and requires growth triggers before creating those categories.

Source:

- https://github.com/Diew/living-docs

## Independent instruction-bloat reports show a concrete context-budget failure

The September 2026 `anywhere-agents` v0.9.0 release notes report a shared AGENTS.md that had diverged to 66 KB and 75 KB across two copies. Their rewrite reduced the shared file to roughly 24 KB and moved rationale/version-history/how-to material into deeper docs; the authors report that the prior size exceeded Codex's default 32 KiB project-instruction budget and truncated later rules.

Implication: instruction growth is not only aesthetic debt. It can create real truncation and copy-drift failures, strengthening the case for small routed instructions and deeper on-demand material.

Source:

- https://github.com/yzhao062/anywhere-agents/releases/tag/v0.9.0

## Generated instruction adapters can solve multi-tool compatibility without creating independent policy

The current `anywhere-agents` repository keeps `AGENTS.md` as the shared source and generates `CLAUDE.md`/agent-specific files from it, with explicit generated-file headers and local override layers. In contrast, independent drift tools report unmanaged copies diverging across repositories and machines.

Implication: the risk is not multiple filenames by itself. The risk is multiple independently maintained policy owners. The auditor therefore recognizes a generated adapter that embeds the canonical AGENTS content, while continuing to warn when a claimed/generated adapter has diverged.

Sources:

- https://github.com/yzhao062/anywhere-agents
- https://github.com/untactit/agent-drift

## Stable rule identities and explicit suppressions scale better than prose-only policy

Ruff exposes stable rule codes and explicit global/per-file ignore mechanisms, while OpenSSF Scorecard exposes named checks with risk classifications. These are not agent-governance systems, but they demonstrate a mature pattern: findings need stable identities, machine-readable output, and explicit scoped deviations rather than silent suppression.

Implication: this standard uses stable rule IDs and visible structured exceptions instead of free-text "ignore this" behavior.

Sources:

- https://docs.astral.sh/ruff/settings/
- https://github.com/ossf/scorecard/blob/main/docs/checks.md

## Central reusable automation reduces copied workflow logic

Current GitHub Actions supports reusable workflows and composite actions from central repositories, referenced by branch/tag/SHA; GitHub recommends immutable SHAs for maximum stability. Scheduled workflows are available for periodic checks, but public-repository schedules can be disabled after 60 days of inactivity.

Implication: downstream projects can pin audit implementation upstream instead of copying it, while update checks remain advisory and deliberate.

Sources:

- https://docs.github.com/en/actions/how-tos/reuse-automations/reuse-workflows
- https://docs.github.com/en/actions/tutorials/create-actions/create-a-composite-action
- https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows

## Organization-scale ownership is a separate maturity problem

Backstage's catalog model centralizes metadata and explicit ownership so organizations can discover and manage large software estates. GitHub organization rulesets similarly apply centrally managed rules across selected repositories and expose rule-insight/bypass data.

Implication: catalogs, organization-wide ownership, and centrally enforced repository policies belong at organization scale, not in a seed repository by default.

Sources:

- https://github.com/backstage/backstage/blob/master/docs/features/software-catalog/index.md
- https://docs.github.com/en/organizations/managing-organization-settings/creating-rulesets-for-repositories-in-your-organization

## 2026-11-07 heuristic calibration against public agent-heavy repositories

The current audit heuristics were compared against several active public repository patterns rather than being designed only from synthetic fixtures.

- `agentic-templates/repo-template` uses one root AGENTS.md plus task-specific guides. Its current root README/AGENTS organization does not match the standard's README active-state or unmanaged root-copy smells.
- `anywhere-agents` uses AGENTS.md as a canonical shared source and generates CLAUDE.md with an explicit generated-file header. The initial auditor would have warned merely because the generated adapter differed by its header; the detector was changed to recognize a generated adapter that actually embeds the canonical AGENTS content while still warning when a claimed generated adapter has diverged.
- `Diew/living-docs` intentionally bootstraps a richer documentation/governance skeleton. That is not treated as an automatic audit failure: whether those categories are earned is a contextual RGS-GROW-001 review, illustrating why manual rules must not be reduced to filename heuristics.

Implication: heuristic findings should be calibrated against healthy counterexamples and narrowed when they produce noise. The audit suite includes regression cases for the generated-adapter calibration.

Sources:

- https://github.com/agentic-templates/repo-template
- https://github.com/yzhao062/anywhere-agents
- https://github.com/Diew/living-docs

## Review policy

Refresh this evidence when:

- a major coding-agent generation changes repository-context behavior;
- vendors materially change instruction/memory loading;
- new execution-graded research contradicts a normative assumption;
- real project audits reveal repeated false positives/false negatives;
- an observed repository failure suggests the standard is optimizing the wrong thing.

Older evidence can remain when the finding is still reproduced or independently supported. Vendor authority alone does not make a claim normative.
