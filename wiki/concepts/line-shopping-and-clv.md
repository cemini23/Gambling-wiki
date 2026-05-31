---
title: Line shopping and closing line value (CLV)
type: concept
tags: [concept, clv, line-shopping, sharp-betting]
keywords: [clv, closing-line-value, line-shopping, steam, reverse-line-movement]
related:
  - concepts/sports-betting-fundamentals.md
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
maturity: draft
created: 2026-05-31
updated: 2026-05-31
---

## Relations

- @concepts/sharp-vs-soft-books.md — Pinnacle close as benchmark
- @entities/platforms/pinnacle.md — sharp reference line
- @entities/tools/momentum-odds.md — multi-book signal feed (also used for PM routing in @osint-wiki)

## Raw Concept

Line shopping reduces vig; CLV measures whether your bet beat the closing sharp line.

## Narrative

### Line shopping

Same bet at -105 vs -110 is **material** over hundreds of bets. Maintain accounts at multiple legal books; use odds aggregators responsibly (verify lines before click).

### CLV definition

**Closing Line Value** = your bet's implied edge vs the **closing line** (often Pinnacle or consensus sharp close). Positive CLV over large sample → strong signal of skill even if short-term P&L is negative.

```
CLV ≈ (your_implied_prob − closing_implied_prob) × stake_equivalent
```

[TENTATIVE — multiple CLV calculation conventions exist; standardize in ingest]

### Steam and RLM

- **Steam move**: rapid line movement across books (often sharp action)
- **Reverse line movement (RLM)**: line moves opposite public bet % — potential sharp fade signal [NEEDS VERIFICATION 2026-05-31 — model-specific]

### PM analog

Cross-venue price vs Kalshi/Polymarket — `@concepts/sportsbook-pm-line-divergence.md` (retail); `@osint-wiki/concepts/cross-venue-arbitrage-pattern.md` (automation).

## Snippets

> Positive CLV over large sample → strong skill signal even if short-term P&L is negative. [TENTATIVE — standard sharp betting literature]
