---
title: Live betting and match-integrity monitoring
type: concept
tags: [concept, sports-betting, live-betting, integrity, fraud]
keywords: [match-fixing, in-play, live-betting, sportradar, outlier-detection]
related:
  - concepts/sports-betting-fundamentals.md
  - concepts/line-shopping-and-clv.md
  - concepts/favorite-longshot-bias.md
  - concepts/sharp-vs-soft-books.md
  - sources/daily-digest-arxiv-batch-2026-06-01.md
maturity: draft
created: 2026-06-01
updated: 2026-06-01
---

## Relations

- @concepts/sports-betting-fundamentals.md — live betting as product lane
- @concepts/line-shopping-and-clv.md — in-play line moves vs integrity signals

## Raw Concept

Academic + industry framing for **detecting match-fixing** via **in-play betting market dynamics** (stakes and odds), not pre-game alone.

## Narrative

### Why live markets matter

European live betting is ~**50%** of sports betting revenue [TENTATIVE — EGBA cited in Winkelmann et al. 2026]. Manipulation incentives scale with liquidity; **second-tier football** (e.g. Italian Serie B) is historically exposed when player/referee compensation is low but markets remain liquid.

### Detection pattern (Winkelmann et al. 2026)

1. **Model normal dynamics** — state-space model of expected log-stakes conditional on score, xG, red cards, implied probs, market open/closed.
2. **Flag outliers** — large positive deviations in stake volume vs model expectation (especially late in match on unlikely outcomes).
3. **Use volumes + odds** — Ötting et al. (2018) pre-game Serie B: volumes improve detection when odds alone hide manipulation.

Industry analog: Sportradar **UFDS** compares in-play odds to model forecasts [Source: paper §2.3].

### Retail bettor lens

- **Not a +EV angle** — integrity monitoring is book/regulator tooling.
- **Live-bet discipline** — unusual line moves + volume spikes on obscure leagues are **red flags** for market quality, not invitations to chase.
- **FLB context** — paper reviews favorite-longshot bias in European football; pre-game “inefficiencies” often noise (Winkelmann et al. 2024).

### Responsible gambling

Match-fixing erodes trust in sport; avoid leagues/markets with repeated integrity scandals when building long-term +EV processes.

## Snippets

> "To comprehensively monitor irregular betting activity, there is thus a pressing need to develop fraud warning systems for the live betting market as well." [Source: arxiv-2605.30209 p.1]

> "Unusual betting patterns or poor on-field performance may simply result from players conserving energy in low-stakes matches." [Source: same — false-positive caution]
