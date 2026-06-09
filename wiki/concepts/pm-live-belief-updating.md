---
title: Prediction-market live belief updating
type: concept
tags: [concept, prediction-markets, kalshi, live-betting, market-efficiency, nba]
keywords: [live-betting, underreaction, belief-updating, salience, liquidity, kalshi, in-play]
related:
  - concepts/prediction-markets-crossover.md
  - concepts/sportsbook-pm-line-divergence.md
  - concepts/sports-betting-fundamentals.md
  - concepts/vig-and-hold.md
  - concepts/gambling-bot-architecture.md
  - concepts/sharp-vs-soft-books.md
  - entities/platforms/kalshi.md
  - entities/platforms/polymarket.md
  - entities/sports/nba-betting.md
  - sources/arxiv-kalshi-live-belief-updating-2606.07811-2026-06-09.md
maturity: validated
created: 2026-06-09
updated: 2026-06-09
---

## Relations

- @sources/arxiv-kalshi-live-belief-updating-2606.07811-2026-06-09.md — primary evidence (Kalshi NBA, arXiv 2606.07811)
- @concepts/sportsbook-pm-line-divergence.md — static cross-venue gaps (complementary, not duplicate)
- @concepts/prediction-markets-crossover.md — retail PM checklist
- @entities/platforms/kalshi.md — venue entity

## Raw Concept

How **live prediction-market prices** incorporate **public in-game information** — distinguishing **directional responsiveness** from **efficient (magnitude-correct) updating**, and what that means for retail timing and bot design.

## Narrative

### Two notions often conflated

| Notion | Question | Kalshi NBA evidence [CONFIRMED — 2606.07811] |
|--------|----------|-----------------------------------------------|
| **Directional updating** | Does price move the right way after news? | **Yes** — scoring, 3pt, lead changes, runs all move mid symmetrically |
| **Efficient updating** | Does price move **one-for-one** with public-info fair value? | **No** — 1-min ∆benchmark → **~0.64×** ∆Kalshi mid on impact |

Market-implied probabilities can be **timely and directionally right** yet **temporarily incomplete** in level.

### Mechanism: attention × liquidity

```
Public signal (play-by-play)
        ↓
Salience → faster recognition (3pt, lead change, run)
        ↓
Liquidity → how fully price adjusts on impact
        ↓
Thin market + salient event → largest underreaction gap
        ↓
Gap predicts 5–15 min midpoint drift (net of new public info)
        ↓
Spread/fees → executable returns still negative
```

**Retail:** after a visible run in a **low-volume** game, mid may **continue drifting** toward a model-fair prob — but crossing the spread to "catch up" is usually -EV.

### Pre-game vs live

- Pre-game Kalshi NBA prices **calibrate well** and **improve** in the final 24h (Brier 0.204 → 0.199).
- Live benchmark (public state only) matches live Kalshi Brier (**0.164**) — both beat pre-game close (**0.211**).
- Incomplete updating is a **within-game dynamic** problem, not "PM prices are useless."

### Practical checklist (live PM sports)

1. **Check liquidity** — spread, recent volume, open interest before sizing live entries.
2. **Salient event ≠ fully priced** — lead changes in thin markets underreact most.
3. **Clutch time** — updating coefficient drops to **~0.51** vs ~0.64 average (Appendix C) — more drift risk late in close games.
4. **Use limits / patience** — maker-style entry may capture drift; market-buying the lag often loses to vig.
5. **Log drift vs benchmark** — if building models, track **gap = fair∆ − mid∆** not just direction.

### Bot architecture hooks

| Requirement | Why |
|-------------|-----|
| Liquidity gate | Skip or reduce size when illiquidity index high |
| Drift-aware hold | Gap may mean **wait** rather than **chase** |
| Benchmark separate from mid | Don't embed live price in fair-value model when testing efficiency |
| TCA on ask/bid | Midpoint alpha ≠ executable alpha |
| Play-by-play feed | NBA PBP + 1-min quotes minimum for this research design |

Prod Kalshi execution patterns: `@osint-wiki/entities/platforms/kalshi.md`.

### Scope limits

- Evidence is **Kalshi NBA game contracts** only (2026 paper).
- Does **not** prove identical underreaction on **sportsbooks**, **Polymarket**, or **non-sports** events.
- **World Cup / soccer** live PM — related literature (Croxson & Reade 2014; Angelini et al. 2022) cited in paper; basketball gives **denser** signal sequence.

## Snippets

> "Prices move in the right direction, but not far enough." [Source: arxiv-2606.07811, Abstract]

> "Informativeness is not instantaneous efficiency." [Source: arxiv-2606.07811, §7 Conclusions]

## Dead Ends

- **Fade every live move** — direction is correct on average; edge is in **timing/liquidity**, not contrarian direction.
- **Assume 0.64 β on all PM sports** — category and venue-specific; re-estimate per product.
