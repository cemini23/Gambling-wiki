---
title: Line shopping and closing line value (CLV)
type: concept
tags: [concept, clv, line-shopping, sharp-betting]
keywords: [clv, closing-line-value, line-shopping, steam, reverse-line-movement]
related:
  - concepts/sports-betting-fundamentals.md
  - concepts/live-betting-match-integrity.md
  - concepts/sharp-vs-soft-books.md
  - concepts/vig-and-hold.md
  - entities/platforms/pinnacle.md
  - entities/tools/momentum-odds.md
  - concepts/world-cup-books-vs-pm-divergence.md
  - concepts/sportsbook-pm-line-divergence.md
  - entities/sports/world-cup-2026-betting.md
  - sources/youtube-sports-pm-retail-batch-2026-05-29.md
  - entities/sports/nfl-betting.md
  - entities/sports/nba-betting.md
  - entities/tools/sports-betting-georgedouzas.md
  - entities/bots/bovada-hand-history-converter.md
  - sources/daily-digest-news-r1-r12-2026-06-01.md
  - entities/tools/unabated.md
  - sources/youtube-operator-batch-sports-betting-research-2026-05-31.md
  - entities/tools/pickfinder.md
  - concepts/dfs-backtesting-framework.md
  - concepts/diy-nfl-dfs-model-architecture.md
  - sources/cross-wiki-k125-diy-dfs-sweep-2026-06-20.md
  - sources/arxiv-2607.00164-verifiable-rewards-calibrated-forecasting-2026-07-03.md
  - sources/brief-k137-swe-interact-rlvr-nfl-steals-2026-07-03.md
  - concepts/daily-edge-card.md
maturity: validated
created: 2026-05-31
updated: 2026-07-03
---

## Relations

- @concepts/sharp-vs-soft-books.md — Pinnacle close as benchmark
- @entities/platforms/pinnacle.md — sharp reference line
- @entities/tools/momentum-odds.md — multi-book signal feed (also used for PM routing in @osint-wiki)
- @concepts/daily-edge-card.md — P0 CLI: de-vig reference vs Hard Rock

## Raw Concept

Line shopping reduces vig; CLV measures whether your bet beat the closing sharp line.

## Narrative

### Line shopping

Same bet at -105 vs -110 is **material** over hundreds of bets. Maintain accounts at multiple legal books; use odds aggregators responsibly (verify lines before click).

### CLV definition

**Calibration vs CLV:** A model can match the market on **Brier/ECE** for in-game win probability using only public state (@sources/arxiv-2607.00164-verifiable-rewards-calibrated-forecasting-2026-07-03.md) while still failing to beat **closing lines** after vig and latency. Treat calibration checks and CLV as separate gates.

**Closing Line Value** = your bet's implied edge vs the **closing line** (often Pinnacle or consensus sharp close). Positive CLV over large sample → strong signal of skill even if short-term P&L is negative.

```
CLV ≈ (your_implied_prob − closing_implied_prob) × stake_equivalent
```

[TENTATIVE — multiple CLV calculation conventions exist; standardize in ingest]

### Steam and RLM

- **Steam move**: rapid line movement across books (often sharp action)
- **Reverse line movement (RLM)**: line moves opposite public bet % — potential sharp fade signal [NEEDS VERIFICATION 2026-05-31 — model-specific]
- **Opening vs current line** — compare to spot possible sharp action before betting [Source: u3VEGPWwKHc]
- **Line-movement filter** — narrow slate to games with ML/total/spread moves, then research [Source: nimjqe3P5lA, wtE5aXrUHzQ]

### CLV in practice

Extranet Shaquille example: bet +150 promo side but **CLV −300** vs close — positive short-term result can still be −EV process [Source: XZvXWVztJoY]. Log CLV, not just W/L.

### PM analog

Cross-venue price vs Kalshi/Polymarket — `@concepts/sportsbook-pm-line-divergence.md` (retail); `@osint-wiki/concepts/cross-venue-arbitrage-pattern.md` (automation).

## Snippets

> Positive CLV over large sample → strong skill signal even if short-term P&L is negative. [TENTATIVE — standard sharp betting literature]

> "Closing line value or CLV … good deal at plus 150 and the CLV was minus 300." [Source: XZvXWVztJoY via @sources/youtube-operator-batch-sports-betting-research-2026-05-31.md]
