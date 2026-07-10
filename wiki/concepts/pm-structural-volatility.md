---
title: PM structural volatility (binary contracts)
type: concept
tags: [concept, polymarket, kalshi, volatility, microstructure]
keywords: [binary-volatility, wright-fisher, deadline-resolution, glosten-milgrom, fifty-fifty]
related:
  - concepts/pm-live-belief-updating.md
  - concepts/pm-proper-scoring-clob-profitability.md
  - concepts/prediction-markets-crossover.md
  - concepts/kelly-criterion-betting.md
  - entities/platforms/kalshi.md
  - entities/platforms/polymarket.md
  - sources/arxiv-2607.08199-pm-structural-volatility-kalshi-2026-07-10.md
  - sources/arxiv-2607.01198-liquidity-tail-risk-large-trades-2026-07-09.md
  - sources/brief-k151-pm-belief-to-trade-volatility-steals-2026-07-10.md
maturity: draft
created: 2026-07-10
updated: 2026-07-10
---

## Relations

- @sources/arxiv-2607.08199-pm-structural-volatility-kalshi-2026-07-10.md — Xi et al. Kalshi panel (K151)
- @concepts/pm-live-belief-updating.md — in-play **directional** underreaction (complementary)

## Raw Concept

**Forward volatility** on **binary prediction markets**: bounded prices, known resolution time, binary payoffs — structurally different from equity return volatility.

## Narrative

### Two mechanisms (08199)

| Component | Economic role |
|-----------|---------------|
| **Wright–Fisher deadline-resolution** | Remaining uncertainty forced to resolve as expiry approaches |
| **Glosten–Milgrom order-flow** | Informed trading reflected in spreads and volume |

Plain ARCH/GARCH on PM prices is dominated by structural specs; pooled structural model transfers across Kalshi categories.

### Retail / bot heuristics [TENTATIVE]

1. **50¢ zone** — highest vol near coin-flip prices; tighten size discipline
2. **Resolution window** — vol rises into settlement; avoid oversized entries late without edge
3. **Category** — sports more jump/event-concentrated than economics/macro
4. **Pairs with** — liquidity gate (K150), proper betting (K116), belief-to-trade layer (K151)

### Not the same as

- Equity σ for Kelly on PM — use structural state + fractional Kelly
- Live β underreaction alone — that's directional drift, not vol level

## Snippets

> "Volatility is highest near fifty-fifty prices, rises near resolution." [Source: @sources/arxiv-2607.08199-pm-structural-volatility-kalshi-2026-07-10.md]

## Dead Ends

- Import equity GARCH σ directly into Kalshi sizing
- Vol forecast without edge + liquidity gates as auto-trade
