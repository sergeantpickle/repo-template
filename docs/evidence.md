# Evidence Base

Last reviewed: **2026-11-07**

This standard is intentionally revisable. Coding-agent behavior and tooling change quickly, so vendor guidance and older work are treated as evidence, not permanent doctrine.

## Current findings

### Small persistent context, deeper retrieval on demand

Anthropic's November 6, 2026 memory research describes a hierarchy in which raw transcripts and detailed memories sit below a small injected layer. Current Claude Code documentation similarly loads only the first 200 lines or 25 KB of auto-memory into every session and recommends concise persistent instructions, path-scoped rules, and skills for narrower procedures.

Implication: always-loaded repository instructions should be small and high-value; deeper knowledge should be retrieved when relevant.

Sources:

- https://www.anthropic.com/research/components-of-agent-memory
- https://code.claude.com/docs/en/memory

### Newer models need less forced scaffolding

OpenAI's September 11, 2026 guidance for GPT-6 Astra warns that accumulated `AGENTS.md` and skill instructions can become bloated or contradictory. It specifically recommends against requiring a full repo map or stack of docs before every edit and favors contextual routing instead.

Implication: this standard should govern growth without forcing every task through heavyweight onboarding.

Source:

- https://developers.openai.com/blog/rethinking-skills-and-prompts-for-gpt-6-astra

### Large agent-first repositories still need structured knowledge and garbage collection

OpenAI's February 2026 harness-engineering case study reports that a monolithic instruction manual became stale and difficult to verify. Their larger agent-first repository moved toward a short instruction map, structured repository knowledge, execution plans for complex work, mechanical checks, and recurring documentation gardening.

Implication: richer structure is justified at scale, but it should be earned by coordination needs and backed by checks.

Source:

- https://openai.com/index/harness-engineering/

### Repository instruction files have mixed benchmark evidence

The February 2026 AGENTBench study found repository context files did not generally improve task success and increased inference cost by more than 20% on average. The authors conclude that human-written context files should retain only minimal requirements that are not otherwise available in the repository.

A separate January 2026 study found AGENTS.md associated with lower median runtime and output-token usage across its smaller sample while maintaining comparable completion behavior.

Implication: the standard should not assume that more persistent instructions improve performance. Keep only non-derivable, high-value instructions and evaluate additions against observed failures.

Sources:

- https://arxiv.org/abs/2602.11988
- https://arxiv.org/abs/2601.20404

### Documentation drift compounds in AI-generated changes

An October 2026 study of 29,669 AI-generated pull requests reports that 63.2% changed code without documentation updates. Files changed without documentation were later re-documented at roughly half the rate of files changed with documentation over 90 days, suggesting documentation debt compounds rather than naturally repairing itself.

Implication: current durable documentation needs explicit ownership and co-change expectations, but the answer is not indiscriminate documentation creation.

Source:

- https://arxiv.org/abs/2610.27381

### Central policy should not be copied into every generated artifact

GitHub Spec Kit's current upgrade model stopped propagating constitution content into dependent templates. Its workflows now resolve the live constitution at runtime, because propagation created duplicate sources of truth and conflicted with centrally owned, versioned policy.

Implication: downstream projects should adopt this standard by reference/version rather than copy its full governance text.

Sources:

- https://github.github.com/spec-kit/upgrade.html
- https://github.com/github/spec-kit/blob/main/.specify/memory/constitution.md

### Progressive rigor is a useful counterweight to ceremony

OpenSpec's current guidance explicitly recommends the lightest level that keeps a change verifiable and reserves fuller ceremony for riskier or cross-cutting work.

Implication: repository growth should be trigger-based rather than maturity theater.

Sources:

- https://github.com/Fission-AI/OpenSpec
- https://github.com/Fission-AI/OpenSpec/blob/main/docs/concepts.md

### Real-world AGENTS.md guidance favors exact commands and boundaries

GitHub's analysis of more than 2,500 public agent-instruction files emphasizes exact commands, testing instructions, project-specific boundaries, and iterative refinement based on observed mistakes.

Implication: project agent instructions should be operational and specific, not a general-purpose project encyclopedia.

Source:

- https://github.blog/ai-and-ml/github-copilot/how-to-write-a-great-agents-md-lessons-from-over-2500-repositories/

## Review policy

Refresh this evidence when:

- a major coding-agent generation changes repository-context behavior;
- major vendors materially change instruction/memory loading;
- new execution-graded research contradicts a normative assumption;
- an observed project failure suggests the standard is optimizing the wrong thing.

Older evidence may remain when its finding is still reproduced or independently supported. Vendor authority alone does not make a claim normative.
