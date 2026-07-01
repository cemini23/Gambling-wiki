---
title: Settlement manipulation in prediction markets (arXiv 2606.31675)
type: source
tags: [source, arxiv, prediction-markets, polymarket, kalshi, manipulation, k135]
keywords: [settlement-manipulation, cash-settlement, short-horizon, bitcoin, five-minute, retail, oracle]
related:
  - entities/platforms/polymarket.md
  - entities/platforms/kalshi.md
  - concepts/prediction-markets-crossover.md
  - concepts/world-cup-pm-retail-hygiene.md
  - concepts/sportsbook-pm-line-divergence.md
  - concepts/pm-live-belief-updating.md
  - concepts/gambling-bot-architecture.md
  - sources/arxiv-polymarket-v1-database-2606.04217-2026-06-05.md
  - sources/brief-k135-pm-settlement-macro-beliefs-steals-2026-07-01.md
  - sources/daily-digest-batch-k135-2026-07-01.md
  - sweeps/2026-07-01-daily.md
maturity: draft
read_status: skimmed
created: 2026-07-01
updated: 2026-07-01
location: cemini-egress-fi:/opt/cemini-bulk/research/gambling/arxiv-2606.31675-settlement-manipulation-in-prediction-markets.pdf
phase_0_verdict: REFERENCE 2026-07-01 — empirical + theory; no FOSS repo; retail hygiene for short-horizon asset-price PM contracts
---

## Relations

- @entities/platforms/polymarket.md — Polymarket 5-min BTC contract evidence
- @entities/platforms/kalshi.md — crypto event-contract volume context
- @sources/brief-k135-pm-settlement-macro-beliefs-steals-2026-07-01.md — K135 operator steals

## Raw Concept

| Field | Value |
|-------|-------|
| **arXiv** | [2606.31675](https://arxiv.org/abs/2606.31675) |
| **Title** | Settlement Manipulation in Prediction Markets |
| **Authors** | Dai, Jia, Yu (Stanford / SMU) |
| **Phase-0** | N/A — academic paper; on-chain Polymarket + Binance data |
| **Verdict** | **REFERENCE** — structural retail hazard on **asset-price** PM contracts |

## Narrative

When PM contracts settle on an **underlying asset price** manipulable via spot trading, wealth transfers from **prediction-market liquidity traders** (mostly retail) to manipulators and **degrades underlying price discovery** — contrary to classic election-market manipulation literature.

### Empirical footprint (Polymarket 5-min BTC, post Feb 2026 launch)

| Finding | Magnitude [TENTATIVE — paper] |
|---------|-------------------------------|
| Settlement-time Binance flow spike | ~**50%** above pre-launch in final 10s |
| Near-even cycles — flow jump vs rest | ~**3.9×** |
| Post-settlement price reversal (10s) | ~**25%** near-even; ~**10%** otherwise |
| Manipulator profit (pushed cycles) | **$8.2M** over ~2 months; **821** wallets |
| Retail share of losses | **~93%** (ex-MM) |
| **15-min** contract | Manipulation signature **largely absent** |

**Design remedy:** lengthen contract horizon — aggregates more spot information before close, reducing pivotal pushes.

### Gambling-wiki relevance

| Lane | Fit |
|------|-----|
| **Polymarket retail** | **HIGH** — avoid or size down **5-min crypto** contracts; prefer longer horizons |
| **Kalshi crypto/index binaries** | **HIGH** — same structural vulnerability as horizons shrink |
| **Sports / election PM** | Lower — non-cash-settlement-on-tradable-spot path (still read rules) |
| **PM bots (@osint-wiki)** | Cross-link — manipulation is adverse selection on short oracle windows |

Phase-0 **REFERENCE** — no code adoption; informs retail checklist and bot settlement-window guards.

## Snippets

> "Such contracts transfer wealth from prediction-market liquidity traders to manipulators and harm price discovery in the underlying." [Source: arxiv:2606.31675 Abstract]

> "Manipulation is largely absent in the fifteen-minute contracts: lengthening the contract horizon removes it." [Source: arxiv:2606.31675 Abstract]

> **821** manipulators (~1/300 of traders) captured **$8.2M** in pushed cycles; **93%** of non-MM losses fell on retail. [Source: arxiv:2606.31675 §1]

## Dead Ends

- "PM manipulation always reverts quickly" (election-market logic) applied to 5-min BTC
- Retail martingale on near-even 5-min BTC closes
- Bot arb without settlement-window oracle lag model
