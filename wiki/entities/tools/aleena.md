---
title: Aleena (UW SSEC)
type: entity
tags: [entity, tool, foss, agents, rse, k159]
keywords: [aleena, uw-ssec, lifecycle-alignment, litellm, github-app]
related:
  - sources/arxiv-2607.08043-aleena-alignment-agent-2026-07-18.md
  - concepts/custom-agent-methodology.md
  - concepts/poker-hl-analyst-loop.md
  - sources/brief-k159-aleena-decision-continuity-steals-2026-07-18.md
  - sources/daily-digest-batch-k159-2026-07-18.md
maturity: draft
created: 2026-07-18
updated: 2026-07-18
phase_0_verdict: CONDITIONAL-GO
license_verified: NOASSERTION — no LICENSE file; pyproject has no license field 2026-07-18
---

## Relations

- @sources/arxiv-2607.08043-aleena-alignment-agent-2026-07-18.md — paper
- @concepts/custom-agent-methodology.md — decision continuity / risk surfacing
- @concepts/poker-hl-analyst-loop.md — light HL trail steal

## Raw Concept

| Field | Value |
|-------|-------|
| **GitHub** | https://github.com/uw-ssec/Aleena |
| **Paper** | arXiv 2607.08043 |
| **Local** | `raw-sources/foss-evals/Aleena/` (~1.5MB; gitignored) |
| **Stack** | Pixi + FastAPI + React/Vite; LiteLLM; GitHub App/OAuth |

## Phase-0 Audit (2026-07-18)

| Check | Result |
|-------|--------|
| Pricing | Free code; LiteLLM + GitHub App credentials required to run |
| TOS | GitHub + LLM provider TOS; research/collab tooling |
| License | **NOASSERTION** — no LICENSE / SPDX |
| Size | ~1.5MB shallow — under 500MB |
| Failure mode | Credential sprawl; auto-issue/PR noise; invented facts if prompts weaken |
| vs wiki | Complements custom-agent P5 — **collaboration alignment**, not wagering runtime |

**Verdict: CONDITIONAL-GO** — steal structured decision/risk/vocabulary-drift patterns; do not redistribute until SPDX. Re-run Phase-0 when LICENSE lands.

## Narrative

Lifecycle alignment agent: transcript/chat → analyzers → GitHub issues/discussions/draft PRs + monitoring eval HTML. Pixi tasks: `aleena-web`, `test`, `monitor`, `evaluate`.

## Dead Ends

- Drop-in for `cemini_decide` / arena protocol
- Unattended auto-merge of draft PRs
- Nightly org-wide monitor without cost/noise caps
