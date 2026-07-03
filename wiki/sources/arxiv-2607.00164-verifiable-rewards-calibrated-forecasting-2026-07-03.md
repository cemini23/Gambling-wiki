---
title: Verifiable rewards for calibrated probabilistic forecasting — NFL live WP (arXiv 2607.00164)
type: source
tags: [source, arxiv, sports-betting, nfl, calibration, rlvr, brier, k137]
keywords: [aleatoric-forecasting, empirical-win-rate, gradient-mask, in-game-win-probability, betting-market, ece]
related:
  - entities/sports/nfl-betting.md
  - concepts/sports-betting-fundamentals.md
  - concepts/line-shopping-and-clv.md
  - concepts/pm-proper-scoring-clob-profitability.md
  - concepts/pm-live-belief-updating.md
  - sources/arxiv-kalshi-live-belief-updating-2606.07811-2026-06-09.md
  - sources/brief-k137-swe-interact-rlvr-nfl-steals-2026-07-03.md
  - sources/daily-digest-batch-k137-2026-07-03.md
  - sweeps/2026-07-03-daily.md
maturity: draft
read_status: skimmed
created: 2026-07-03
updated: 2026-07-03
location: cemini-egress-fi:/opt/cemini-bulk/research/gambling/arxiv-2607.00164-verifiable-rewards-for-calibrated-probabilistic.pdf
phase_0_verdict: REFERENCE 2026-07-03 — paper-only (Cascade Research); no FOSS training repo in paper; NFL in-game WP vs market calibration methodology
---

## Relations

- @entities/sports/nfl-betting.md — W8 live-betting literacy
- @sources/brief-k137-swe-interact-rlvr-nfl-steals-2026-07-03.md — K137 operator steals

## Raw Concept

| Field | Value |
|-------|-------|
| **arXiv** | [2607.00164](https://arxiv.org/abs/2607.00164) |
| **Title** | Verifiable Rewards for Calibrated Probabilistic Forecasting |
| **Authors** | Singh, Reddy, Chopra (Cascade Research) |
| **Phase-0** | Paper-only — no public training repo cited |
| **Verdict** | **REFERENCE** — aleatoric RLVR recipe + market-calibration ceiling for NFL in-game WP |

## Narrative

**RLVR** with proper scoring rules (e.g. Brier) should train calibrated forecasters — but in practice RL **degrades calibration**, especially for **aleatoric** targets where the output *is* a probability and the label is one stochastic draw (not a verifiably correct answer).

Testbed: **NFL in-game win probability** (team in possession) with **betting market** as reference benchmark.

| Mechanism | Problem | Fix |
|-----------|---------|-----|
| Per-play Brier on realized outcome | High-variance label noise | **State-conditioned empirical win rate** from past outcomes (label-free, verifiable) |
| Policy gradient on chain-of-thought | Reasoning corruption | **Direct prediction** or **gradient mask** on answer tokens only |

Results (held-out seasons): **Qwen2.5-7B-Instruct** trained with empirical-rate reward alone (no SFT) reaches market-level calibration — **ECE ~0.029 vs market ~0.027** — and beats zero-shot frontier model. Frontier + tabular estimator match RL model Brier → **market's residual edge is live in-game information** beyond shared public state.

### Gambling-wiki relevance

| Lane | Fit |
|------|-----|
| **NFL live betting / W8** | **HIGH** — calibration discipline; market as ceiling for public-state models |
| **CLV / model vs line** | **MEDIUM** — don't confuse Brier calibration with +EV without vig/liquidity |
| **PM retail** | **LOW** — proper-scoring analogy only (aleatoric vs epistemic split) |
| **CeminiDFS** | **LOW** — per-play WP ≠ fantasy projection; cross-link calibration hygiene only |
| **Prod wagering bots** | NO-GO — research methodology, not deployable edge claim |

## Snippets

> "Rewarding the realized per-play outcome fails, because the single outcome is a noisy target and the policy gradient corrupts the chain of thought." [Source: arxiv:2607.00164 Abstract]

> "Trained with this reward alone, without human labels or supervised fine-tuning, a 7B model reaches the calibration of the betting market by direct prediction." [Source: arxiv:2607.00164 Abstract]

> "The market's small remaining edge as live in-game information beyond their shared inputs." [Source: arxiv:2607.00164 Abstract]

## Dead Ends

- Deploying 7B WP model as Hard Rock live-betting bot without latency, vig, and CLV gates
- Per-play Brier RL as DFS ownership projection trainer
- "Matches market ECE" ⇒ automatic +EV live betting
