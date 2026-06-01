---
title: Sportsbook vs prediction-market line divergence
type: concept
tags: [concept, line-shopping, kalshi, polymarket, sportsbooks]
keywords: [line-divergence, consensus, totals, moneyline, cross-venue-shopping]
related:
  - concepts/gambling-bot-architecture.md
  - concepts/line-shopping-and-clv.md
  - concepts/pm-copy-trading-retail-risks.md
  - concepts/prediction-markets-crossover.md
  - concepts/pm-commitment-grounded-language.md
  - concepts/sharp-vs-soft-books.md
  - concepts/sports-betting-fundamentals.md
  - concepts/world-cup-books-vs-pm-divergence.md
  - entities/platforms/draftkings.md
  - entities/platforms/fanduel.md
  - entities/platforms/kalshi.md
  - entities/platforms/polymarket.md
  - entities/sports/nba-betting.md
  - entities/tools/momentum-odds.md
  - sources/gemini-github-sports-betting-landscape-2026-05-30.md
  - sources/youtube-sports-pm-retail-batch-2026-05-29.md
maturity: validated
created: 2026-05-31
updated: 2026-05-31
---

## Relations

- @concepts/gambling-bot-architecture.md — divergence bot lane
- @concepts/line-shopping-and-clv.md — CLV on books; divergence is cross-venue CLV analog
- @entities/tools/momentum-odds.md — commercial multi-book + PM routing feed
- @concepts/world-cup-books-vs-pm-divergence.md — WC-specific nation-level gaps

## Raw Concept

When **FanDuel/DK/Pinnacle implied probability** differs materially from **Kalshi/Polymarket** on the same sporting outcome — and how retail bettors evaluate (not automate) the gap.

## Narrative

### Core idea (multi-source K80)

YouTube batch (Beast Sports, MomentumOdds/Odds channel): edge framed as **sportsbook consensus vs PM line** on totals and moneylines — not sub-second in-play scraping for most retail.

```
Sportsbook consensus (60+ books via MomentumOdds, or sharp close via Pinnacle)
        ↓ compare implied %
Kalshi / Polymarket contract mid
        ↓ if gap > fees + model uncertainty
Consider bet on cheaper venue (or pass)
```

### Workflow

1. Convert all prices to **implied probability**
2. Subtract **fees/hold** on each venue (`@concepts/vig-and-hold.md`, PM taker fees)
3. Confirm **same resolution** (regulation vs OT, push rules)
4. Size with fractional Kelly — `@concepts/kelly-criterion-betting.md`
5. Log result vs **closing** for skill tracking

### Fiat sharp/soft analog

Gemini landscape: Pinnacle moves first; soft books lag → short-window arb. PM×Kalshi behaves similarly — regulated vs crypto CLOB efficiency gradient `@concepts/sharp-vs-soft-books.md`.

### Failure modes

- **False equivalence** — PM "Team wins" vs book spread are not the same bet
- **Latency** — gap closes before manual execution
- **Marketing signals** — MomentumOdds/Odds Jam promos overstate hit rate; verify 3+ months
- **Geoblock / KYC** — cannot always execute on both legs

### World Cup extension

Nation-level book vs PM gaps (USA, Switzerland, etc.) — `@concepts/world-cup-books-vs-pm-divergence.md`.

## Snippets

> Edge as sportsbook consensus vs prediction-market line (totals, moneylines). [Source: @sources/youtube-sports-pm-retail-batch-2026-05-29.md — Beast Sports + MomentumOdds synthesis]
