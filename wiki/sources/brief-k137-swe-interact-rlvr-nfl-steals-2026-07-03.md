---
title: K137 — SWE-INTERACT multi-turn eval + RLVR NFL calibration steals
type: source
tags: [source, brief, agents, nfl, sports-betting, calibration, k137]
keywords: [swe-interact, user-simulator, rlvr, in-game-win-probability, empirical-win-rate, gradient-mask]
related:
  - sources/arxiv-2606.30573-swe-interact-user-driven-coding-agents-2026-07-03.md
  - sources/arxiv-2607.00164-verifiable-rewards-calibrated-forecasting-2026-07-03.md
  - sources/daily-digest-batch-k137-2026-07-03.md
  - sources/arxiv-2606.26027-tool-rl-collapse-supervisory-signals-2026-07-02.md
  - sources/arxiv-2606.25819-toolbench-x-tool-unreliability-2026-06-26.md
  - concepts/custom-agent-methodology.md
  - concepts/poker-hl-analyst-loop.md
  - entities/sports/nfl-betting.md
  - concepts/line-shopping-and-clv.md
maturity: validated
read_status: deep-read
created: 2026-07-03
updated: 2026-07-03
cross-wiki-source: "briefs/2026-07-03_k137-rlvr-nfl-live-calibration-steal.md"
---

## Relations

- @sources/arxiv-2606.30573-swe-interact-user-driven-coding-agents-2026-07-03.md — multi-turn user-sim benchmark
- @sources/arxiv-2607.00164-verifiable-rewards-calibrated-forecasting-2026-07-03.md — aleatoric RLVR + market ceiling
- Private brief: `briefs/2026-07-03_k137-rlvr-nfl-live-calibration-steal.md`
- OSINT arena brief: `agents/devfun-poker-arena/briefs/2026-07-03_k137-swe-interact-multiturn-steal.md`

## Raw Concept

| Field | Value |
|-------|-------|
| **Brief** | K137 SWE-INTERACT + RLVR NFL steals |
| **Date** | 2026-07-03 |
| **Batch** | K137 daily digest (3 PDFs; 2 ingested) |

## Narrative

### SWE-INTERACT steal (2606.30573)

| Idea | Action |
|------|--------|
| **Single-turn ≠ interactive** | ~50% → ~25% solve rate drop — don't qualify bundle agents on one-shot MCP tasks alone |
| **User simulator pattern** | Vague initial brief → progressive requirement reveal → workspace inspection → feedback loop |
| **Failure taxonomy** | Track over-agentic edits, forgotten constraints, rework — in HL patch regression notes |
| **Pairing** | K136 training stability + K131 runtime recovery + K132 verifier triad |
| Phase-0 | **Apache-2.0** `scaleapi/SWE-Interact` (~14★) — read task schema; no prod install |

### RLVR NFL calibration steal (2607.00164)

| Idea | Retail / W8 action |
|------|---------------------|
| **Aleatoric vs epistemic** | Live WP is probability output + stochastic label — different from "confidence in correct answer" |
| **Market ceiling** | Public-state models match market ECE (~0.027–0.029); residual edge = **live info** not in shared features |
| **Noisy per-play Brier** | Don't train/eval WP models on single realized play outcomes without variance reduction |
| **CoT + RL hazard** | Gradient on reasoning corrupts forecasts — separate reasoning from scored probability head |
| **Calibration ≠ +EV** | Market-matching Brier does not imply beatable live lines after vig/latency |

### Operator checklist addendum

- [ ] Arena: add **partial-spec** scenario to private bundle eval (not only fully-specified join→submit)
- [ ] NFL W8: treat in-game WP models as **calibration-checked** vs closing line, not auto-bet
- [ ] Cross-link @osint-wiki for any live WP bot — no prod config in public wiki

## Dead Ends

- SWE-bench pass rate as HU TrueSkill proxy
- 7B WP model as Hard Rock automation without CLV journal
- Interval-belief NN verification (30105 reject) as PM ladder math
