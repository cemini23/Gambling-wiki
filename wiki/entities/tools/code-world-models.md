---
title: Code World Models (JaviMaligno)
type: entity
tags: [entity, tool, foss, poker, agents, world-models, k158]
keywords: [cwm, code-world-models, mcts, play-adequacy, javimaligno]
related:
  - sources/arxiv-2607.14169-play-adequacy-code-world-models-2026-07-17.md
  - concepts/poker-hl-analyst-loop.md
  - concepts/custom-agent-methodology.md
  - concepts/opponent-modeling-imperfect-info.md
  - entities/tools/rlcard.md
  - sources/brief-k158-play-adequacy-cwm-steals-2026-07-17.md
  - sources/daily-digest-batch-k158-2026-07-17.md
maturity: draft
created: 2026-07-17
updated: 2026-07-17
phase_0_verdict: CONDITIONAL-GO
license_verified: NOASSERTION — no LICENSE file; pyproject has no license field 2026-07-17
---

## Relations

- @sources/arxiv-2607.14169-play-adequacy-code-world-models-2026-07-17.md — paper
- @concepts/poker-hl-analyst-loop.md — play-adequacy gates
- @entities/tools/rlcard.md — Kuhn/Leduc sibling sim lane

## Raw Concept

| Field | Value |
|-------|-------|
| **GitHub** | https://github.com/JaviMaligno/code-world-models |
| **Paper** | arXiv 2607.14169 |
| **Local** | `raw-sources/foss-evals/code-world-models/` (~4.8MB; gitignored) |
| **Python** | ≥3.11; deps openai, python-dotenv; pytest |

## Phase-0 Audit (2026-07-17)

| Check | Result |
|-------|--------|
| Pricing | Free code; Azure/OpenAI API for synthesis runs (~$2 paper total) |
| TOS | Provider API TOS; research games only |
| License | **NOASSERTION** — no LICENSE / SPDX |
| Size | ~4.8MB shallow — under 500MB |
| Failure mode | API spend; Azure `.env` required; not Arena protocol |
| vs wiki | Complements RLCard — **play-adequacy eval**, not GTO |

**Verdict: CONDITIONAL-GO** — steal play-adequacy / danger-law methodology; do not redistribute until SPDX. Re-run Phase-0 when LICENSE lands.

## Narrative

MVP reproducing CWM + MCTS vs LLM-as-policy; includes Kuhn imperfect-info pipeline validation and experiment docs under `docs/`.

## Dead Ends

- Drop-in for `cemini_decide` / arena-pokerkit
- Nightly multi-model synthesis without cost cap
