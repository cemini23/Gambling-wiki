---
title: Odds Jam (Prediction Insiders)
type: entity
tags: [entity, tool, polymarket, copy-trading, odds-jam]
keywords: [odds-jam, prediction-insiders, copy-alerts, +ev]
related:
  - concepts/prediction-markets-crossover.md
  - concepts/bankroll-management.md
  - concepts/pm-copy-trading-retail-risks.md
  - entities/platforms/polymarket.md
  - entities/people/alex-monahan.md
  - sources/youtube-sports-pm-retail-batch-2026-05-29.md
  - sources/gemini-github-sports-betting-landscape-2026-05-30.md
  - sources/youtube-operator-batch-sports-betting-research-2026-05-31.md
  - concepts/sports-betting-fundamentals.md
  - entities/tools/pickfinder.md
  - sources/youtube-operator-batch-casino-2026-05-31.md
  - sources/cross-wiki-k125-diy-dfs-sweep-2026-06-20.md
maturity: draft
created: 2026-05-31
updated: 2026-05-31
---

## Relations

- @concepts/pm-copy-trading-retail-risks.md — retail discipline
- @entities/people/alex-monahan.md — founder context
- @osint-wiki/entities/tools/odds-jam-prediction-insiders.md — full experiment table

## Raw Concept

**Odds Jam** suite: traditional sportsbook +EV tools + **Prediction Insiders** (Polymarket high-ROI wallet alerts with suggested sizing).

## Narrative

### Prediction Insiders (PM)

- Surfaces trades from tracked profitable Polymarket wallets
- One-click copy sizing suggestions
- Marketing cites extreme ROI stats — treat as **upper bound marketing** [TENTATIVE]

### Financial Wolf 30-day experiment (May 2026) [TENTATIVE]

| Phase | Note |
|-------|------|
| Start | $1,000 bankroll |
| Week 1 | ~13% gain; heavy trade count |
| Mid | Drawdown to ~$740; **54% win rate** |
| Day 30 | ~$224 PM profit on ~$7.5k wagered; total ~$1,698 incl. **non-PM** bonus EV |
| Filter | Later trades >80 confidence only |

**Retail read:** small edge possible vs random after fees; **underperforms** headline product stats; high variance.

### Traditional Odds Jam (+EV scanner, promos, model tools)

Separate product line for **sportsbook** promos and +EV — Phase-0 on pricing, state availability, TOS.

**Model-building tutorial (6HN-d9mC0DI)** [TENTATIVE — creator content]:

1. Build on **market prices**, not naive public stats books already embed
2. Benchmark fair probability vs **Pinnacle/Circa** sharp lines
3. **Devig** juice from sharp two-way markets before comparing soft-book offers
4. **Kelly criterion** for bankroll sizing after edge estimate
5. **Crossed markets** = arb alert pattern (verify latency and ToS)

See `@sources/youtube-operator-batch-sports-betting-research-2026-05-31.md`.

**AI experiment (pgTc2OQN60U)** [TENTATIVE — OddsJam promo]:

- Creator tests **ChatGPT** for +EV sports betting guidance vs disciplined process
- Reinforces **positive EV**, **bankroll management**, **Kelly** mention, multi-book line shopping
- Verdict: mixed good/bad AI advice — **not** a replacement for OddsJam +EV scanner or sharp-line devig; useful as cautionary retail content

See `@sources/youtube-operator-batch-casino-2026-05-31.md`.

### Verdict

**Reference** — calibrate copy-trading expectations; subscribe only with `@concepts/pm-copy-trading-retail-risks.md` checklist.

## Snippets

> "We profited $224.10 … marking a 22% gain versus an 18.7% expected loss if we just randomly place bets." [Source: gSGI82Ej76M via @sources/youtube-sports-pm-retail-batch-2026-05-29.md]

> "375 trades placed so far, our win rate is only 54%." [Source: same]

> "You can devig the market … remove the juice from Pinnacle." [Source: 6HN-d9mC0DI via @sources/youtube-operator-batch-sports-betting-research-2026-05-31.md]

> "…positive expected value betting… bankroll management is non-negotiable… the Kelly…" [Source: pgTc2OQN60U via @sources/youtube-operator-batch-casino-2026-05-31.md]
