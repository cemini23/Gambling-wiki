---
title: Daily digest news batch R1–R12 (2026-06-01 sweep)
type: source
tags: [source, web, daily-digest, kalshi, polymarket, ev-betting, world-cup, dfs]
keywords: [r1-r12, sweep, news, fees, vig, best-ball, adp]
related:
  - meta/daily-research-digest-cadence.md
  - sources/daily-digest-arxiv-batch-2026-06-01.md
  - sources/polygnosis-2-polymarket-osint-2026-06-01.md
  - sources/daily-digest-news-r1-r12-2026-06-02.md
  - sources/youtube-wsj-kalshi-polymarket-valuations-2026-06-01.md
  - entities/platforms/kalshi.md
  - entities/platforms/polymarket.md
  - entities/platforms/draftkings.md
  - entities/platforms/underdog-fantasy.md
  - concepts/sportsbook-pm-line-divergence.md
  - concepts/pm-commitment-grounded-language.md
  - concepts/sports-betting-fundamentals.md
  - concepts/line-shopping-and-clv.md
  - concepts/best-ball-strategy.md
  - entities/sports/world-cup-2026-betting.md
maturity: validated
read_status: read
created: 2026-06-01
updated: 2026-06-01
---

## Relations

- @sweeps/2026-06-01-daily.md — discovery rows R1–R12
- @sources/polygnosis-2-polymarket-osint-2026-06-01.md — PolyGnosis (same sweep day)

## Raw Concept

| Field | Value |
|-------|-------|
| **Ingest** | 2026-06-01 |
| **Method** | Brave Search snippets + curl meta (SI.com/R2 blocked direct fetch) |
| **Confidence** | [TENTATIVE] on numeric claims — verify at source before betting |

## Narrative

### Q1 — Kalshi / PM retail (R1–R3)

| ID | URL | Takeaways |
|----|-----|-----------|
| **R1** | [SI.com Kalshi vs Polymarket](https://www.si.com/prediction-markets/reviews/kalshi-vs-polymarket) | Kalshi: CFTC-regulated, USD, US retail onboarding. Polymarket: deeper global markets, crypto-native. **PM sports taker fee** (from Mar 30, 2026): probability-based, **peak ~0.75%** at 50¢, lower at extremes; makers pay on limit fills; sells no taker fee [TENTATIVE — SI/Brave]. |
| **R2** | [Tech-Insider vig gap](https://tech-insider.org/prediction-markets-vs-sportsbooks/) | Structural **~4.5% sportsbook hold** vs **~0.5–1.5%** implied vig on flagship Kalshi sports vs **-110/-110** books. Worked example: Chiefs ML Kalshi 58.5% vs DK -135 → ~1.1¢ better effective on Kalshi [TENTATIVE]. Notes **Section 1256** tax treatment for Kalshi gains vs ordinary gambling income for books. Sharp limits at books vs no PM equivalent. |
| **R3** | [WSJ YouTube](https://www.youtube.com/watch?v=S2g0TwfecJE) | **Transcript ingested** — `@sources/youtube-wsj-kalshi-polymarket-valuations-2026-06-01.md`: CFTC DCM vs offshore PM, sports >70% Kalshi volume, state license fight, Kalshi Trading LLC MM, sharp limits narrative, insider-trading tail risks. |

### Q2 — Sports betting +EV (R4–R6)

| ID | URL | Takeaways |
|----|-----|-----------|
| **R4** | [ProfitDuel EV strategies](https://www.profitduel.com/blog/optimal-ev-betting-strategies) | Ranked list: (1) promo/matched betting, (2) **CLV tracking**, (3) promos, (4) arb, (5) sharp line / Pinnacle benchmark. Marketing for ProfitDuel tools — extract **process**, not tool endorsement. |
| **R5** | [BettingPros +EV](https://www.bettingpros.com/articles/what-is-ev-betting-the-strategy-behind-long-term-profitability/amp/) | +EV = odds imply lower probability than true chance. Long-term profitability requires **finding mispriced lines**, not picking winners. |
| **R6** | [Wannabet French Open](https://wannabet.com/french-open-futures-are-moving-fast-tonight/) | Thin **futures line-move** note (tennis); illustrates **steam** on outrights — not core strategy doc. |

### Q3 — World Cup 2026 (R7–R9)

| ID | URL | Takeaways |
|----|-----|-----------|
| **R7** | [Covers WC odds](https://www.covers.com/world-cup/odds) | Outright futures + win prob framing; **Spain/France co-favorites** cited in meta [TENTATIVE date-stamped]. |
| **R8** | [Flashscore WC outright](https://www.flashscoreusa.com/news/soccer-world-championship-world-cup-2026-winner-odds-predictions-best-bets/ELeZQXLr/) | General outright predictions/odds article. |
| **R9** | [Yahoo Fanatics hub](https://sports.yahoo.com/articles/fanatics-teams-official-fifa-world-183400761.html) | Fanatics + **official FIFA prediction partner** hub: PM-style features, news, stats — retail **distribution** for WC wagering/PM crossover. |

### Q4 — DFS best ball (R10–R12)

| ID | URL | Takeaways |
|----|-----|-----------|
| **R10** | [Fantasy Footballers DK BBM](https://www.thefantasyfootballers.com/best-ball/draftkings-best-ball-roster-construction-archetypes-advance-rates/) | DK best ball **archetypes + advance rates** for Milly Maker-style GPP. |
| **R11** | [DK Network ADP 5/26](https://dknetwork.draftkings.com/2026/05/26/draftkings-20m-nfl-best-ball-strategy-adp-trends-for-5-26-26/) | **$20M** NFL best ball contest; ADP risers/fallers snapshot. |
| **R12** | [BestBallTeamBuilder Underdog](https://www.bestballteambuilder.com/underdog-best-ball-team-builder) | Third-party **live-draft companion**: ADP, stacks, playoff correlation for Underdog BB. |

## Snippets

> "A $50,000 annual volume on a sportsbook at 4.5% hold means roughly $2,250… The same volume on Kalshi at 1-2% fee blend means $500-$1,000." [Source: tech-insider.org via Brave, R2]

> "+EV betting means placing wagers where the odds exceed the true probability of an outcome." [Source: bettingpros.com meta, R5]

## Dead Ends

- R3 YouTube — ingested → `@sources/youtube-wsj-kalshi-polymarket-valuations-2026-06-01.md`
- R6 — single-event blog, low structural value
- R1/R2 — direct HTML fetch failed; rely on Brave/SI secondary snippets
