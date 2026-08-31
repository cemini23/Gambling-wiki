---
title: Prediction markets crossover (Kalshi, Polymarket)
type: concept
tags: [concept, prediction-markets, kalshi, polymarket, crossover]
keywords: [prediction-markets, event-contracts, kalshi, polymarket, fees, crossover]
related:
  - concepts/gambling-wiki-scope.md
  - concepts/favorite-longshot-bias.md
  - concepts/kelly-criterion-betting.md
  - concepts/sharp-vs-soft-books.md
  - concepts/best-ball-strategy.md
  - entities/platforms/kalshi.md
  - entities/platforms/polymarket.md
  - entities/tools/momentum-odds.md
  - entities/tools/odds-jam.md
  - concepts/sportsbook-pm-line-divergence.md
  - concepts/pm-copy-trading-retail-risks.md
  - concepts/pm-commitment-grounded-language.md
  - concepts/pm-perspective-mismatch-trading.md
  - sources/youtube-wsj-kalshi-polymarket-valuations-2026-06-01.md
  - sources/polygnosis-2-polymarket-osint-2026-06-01.md
  - entities/sports/world-cup-2026-betting.md
  - concepts/world-cup-prediction-market-types.md
  - sources/youtube-sports-pm-retail-batch-2026-05-29.md
  - sources/gemini-github-sports-betting-landscape-2026-05-30.md
  - sources/osint-cross-wiki-wc2026-retail-synthesis-2026-05-31.md
  - concepts/polymarket-weather-wagering-retail.md
  - entities/people/rufus-peabody.md
  - sources/youtube-operator-batch-sports-betting-research-2026-05-31.md
  - concepts/gambling-bot-architecture.md
  - concepts/polymarket-v1-research-database.md
  - sources/arxiv-polymarket-v1-database-2606.04217-2026-06-05.md
  - concepts/pm-live-belief-updating.md
  - sources/arxiv-kalshi-live-belief-updating-2606.07811-2026-06-09.md
  - concepts/world-cup-pm-retail-hygiene.md
  - sources/brief-k108-gambling-wc-retail-hygiene-2026-06-09.md
  - sources/arxiv-2606-13038-nous-prediction-market-cognitive-injection-2026-06-13.md
  - sources/openreview-prophets-profit-pm-LYSTj2Cnuu-2026-06-17.md
  - sources/openreview-llm-coherence-projection-Tqos7VqQhH-2026-06-17.md
  - concepts/pm-proper-scoring-clob-profitability.md
  - concepts/pm-structural-volatility.md
  - concepts/pm-llm-coherence-projection.md
  - concepts/pm-agent-cognitive-monoculture.md
  - sources/arxiv-2606.31675-settlement-manipulation-prediction-markets-2026-07-01.md
  - sources/arxiv-2606.30040-kalshi-macro-belief-distributions-2026-07-01.md
  - sources/brief-k135-pm-settlement-macro-beliefs-steals-2026-07-01.md
  - concepts/kalshi-spotify-oracle-manipulation-2026-07.md
  - concepts/kalshi-michigan-sports-injunction-2026-06.md
  - concepts/pm-whale-conviction-bias-2026-07.md
  - sources/substack-rss-event-horizon-2026-07-03-how-artificial-spotify-streams-broke-a-kalshi-ma.md
  - sources/substack-rss-klement-2026-07-02-a-fundamental-flaw-of-prediction-markets.md
  - sources/substack-rss-event-horizon-2026-07-07-north-carolinas-prediction-market-budget-process.md
  - sources/daily-digest-rss-industry-2026-08-14.md
  - sources/substack-rss-event-horizon-2026-08-13-novig-responsible-trading.md
  - sources/brief-k222-k231-pm-retail-awareness-2026-08.md
  - sources/brief-k239-kalshi-sports-mention-2026-08-15.md
  - sources/brief-k240-kalshi-nv-geofence-2026-08-17.md
  - sources/brief-k242-eh-pm-ban-onshore-2026-08-19.md
  - sources/brief-k243-eh-pm-republican-comms-2026-08-20.md
  - @seo-wiki/concepts/outlier-weekly-issue3-world-cup-bot-notes.md
  - @seo-wiki/concepts/generative-engine-optimization.md
  - sources/arxiv-2602.19520-pm-domain-calibration-2026-08-31.md
  - sources/daily-digest-rss-nfl-week0-2026-08-31.md
maturity: validated
created: 2026-05-31
updated: 2026-08-31
---

## Relations

- @sources/youtube-wsj-kalshi-polymarket-valuations-2026-06-01.md — R3 regulatory explainer

- @concepts/gambling-wiki-scope.md — scope split
- @entities/platforms/kalshi.md — regulated event contracts
- @entities/platforms/polymarket.md — crypto CLOB PM
- @osint-wiki/entities/platforms/kalshi.md — Cemini execution context
- @osint-wiki/entities/platforms/polymarket.md — bot/LP context
- @osint-wiki/concepts/cross-venue-arbitrage-pattern.md — automated arb
- @osint-wiki/concepts/sports-prediction-consensus-agent.md — sports PM entry signals
- @seo-wiki/concepts/outlier-weekly-issue3-world-cup-bot-notes.md — public PM/OSS education funnel (Outlier Weekly)
- @seo-wiki/concepts/generative-engine-optimization.md — citability for public PM explainers
- @sources/daily-digest-rss-industry-2026-08-14.md — DKeX COMBOS + CFTC/NY emergency
- @sources/substack-rss-event-horizon-2026-08-13-novig-responsible-trading.md — Novig responsible-trading + incentive advisory
- @sources/brief-k222-k231-pm-retail-awareness-2026-08.md — 15-min velocity, FanDuel→Crypto.com, Utah/NY tax/FlightAware
- @sources/brief-k239-kalshi-sports-mention-2026-08-15.md — mentions-gone + WA geofence
- @sources/brief-k240-kalshi-nv-geofence-2026-08-17.md — NV $120k/day + optional-update geofence
- @sources/brief-k242-eh-pm-ban-onshore-2026-08-19.md — WA geofence day; ban ≠ offshore
- @sources/brief-k243-eh-pm-republican-comms-2026-08-20.md — GOP-underdog comms tail risk
- @sources/arxiv-2602.19520-pm-domain-calibration-2026-08-31.md — Kalshi sports short-horizon calibration vs compressed futures
- @sources/daily-digest-rss-nfl-week0-2026-08-31.md — injury markets, 9th Circuit, Polymarket participation pull

## Raw Concept

How Kalshi and Polymarket fit the **wagering** knowledge base vs the **trading stack** in osint-wiki.

## Narrative

### Same activity, two lenses

| Lens | gambling-wiki | osint-wiki |
|------|---------------|------------|
| Question | "Is this contract +EV for my bankroll?" | "How does the bot quote/farm/arbitrage it?" |
| Fees | Retail fee math, withdrawal costs | Fee APIs in orchestrator |
| Sports | Consensus agents, MomentumOdds signals | Executor bots, WC LP |
| Regulation | Consumer rules, state gaming vs DCM; WSJ R3 state-fight timeline | CFTC, compliance briefs, `@osint-wiki/entities/tools/polygnosis.md` |

### Retail checklist before betting PM sports

1. Read **settlement rules** (void conditions, data sources)
2. Model **fees** + spread — effective hold in `@concepts/vig-and-hold.md`
3. Compare price vs **sportsbook line** (CLV analog)
4. Size with **fractional Kelly** — `@concepts/kelly-criterion-betting.md` + `@osint-wiki/concepts/kelly-sizing-quarter.md`
5. Know **jurisdiction** — geoblocks, KYC; state **gambling-license** fights may restrict sports contracts (`@sources/youtube-wsj-kalshi-polymarket-valuations-2026-06-01.md`)
6. **Horizon + cash-settlement** (K135 / K225) — **5-min** asset binaries stay NO-GO (settlement-push). Kalshi **15-min BTC** is now the crypto volume engine (~$1.1B of ~$1.5B crypto / 7d, Aug 2026) — clears the worst K135 signature but is still high-churn casino-velocity, not a political-market substitute (`@sources/arxiv-2606.31675-settlement-manipulation-prediction-markets-2026-07-01.md`, `@sources/brief-k222-k231-pm-retail-awareness-2026-08.md`)
7. **Third-party chart oracles** — culture markets (Spotify charts) where the data provider **audits after** PM settlement (`@concepts/kalshi-spotify-oracle-manipulation-2026-07.md`)
8. **State legalization quality** (K149) — light-touch budget inserts (e.g. NC 2026) may mean **low tax + minimal consumer protection** — read venue rules; don't confuse legislative approval with market quality (`@sources/substack-rss-event-horizon-2026-07-07-north-carolinas-prediction-market-budget-process.md`)
8. **Whale-weighted prices** — large OI holders may be **negative** signal on forecast quality (`@concepts/pm-whale-conviction-bias-2026-07.md`)
9. **Macro ladders** — on Kalshi CPI thresholds, read **tail distribution** not point mean alone (`@sources/arxiv-2606.30040-kalshi-macro-belief-distributions-2026-07-01.md`)

### Tools spanning both wikis

- **MomentumOdds** — sportsbook signal feed; tutorials target Kalshi execution (`@entities/tools/momentum-odds.md`, `@osint-wiki/entities/tools/momentum-odds.md`)
- **Odds Jam / Prediction Insiders** — Polymarket copy alerts (`@entities/tools/odds-jam.md`)

### Sports prediction markets (Novig and peers)

Wharton interview with `@entities/people/rufus-peabody.md` frames **sports-focused prediction markets** (Novig cited) as an alternative when **DK/FD limit sharp winners**. Tradeoffs vs books:

| Factor | Traditional book | Sports PM venue |
|--------|------------------|-----------------|
| Limits | Low for winners at soft US books | Liquidity caps `[TENTATIVE]` |
| Pricing | Embedded vig (-110) | Bid-ask + fees |
| Reference | Pinnacle close | Often still benchmark vs Pinnacle |

Retail: same checklist as Kalshi/PM — fees, settlement, bankroll. **Bot execution** — requirements on `@concepts/gambling-bot-architecture.md`; prod code on `@osint-wiki`.

**Aug 2026:** Novig published a responsible-trading framework (21+, incentive limits) while CFTC DMO flagged **Reg 40.5/40.6 incentive programs** — treat PM bonuses as compliance-risk. DraftKings **DKeX** listed football binaries + COMBOS (product of component YES). Kalshi vs NY AG: CFTC emergency “keep operating” vs $36B restitution claim. Same month: Kalshi **15-min BTC** dominates crypto volume; FanDuel Predicts sports → **Crypto.com**; Utah SJ (no CEA preemption); FlightAware sues over flight-cancellation oracles; NY **$10B/5y** PM-tax headline fails a population-share sanity check. Hubs: `@sources/substack-rss-event-horizon-2026-08-13-novig-responsible-trading.md`, `@sources/daily-digest-rss-industry-2026-08-14.md`, `@sources/brief-k222-k231-pm-retail-awareness-2026-08.md`, `@osint-wiki/concepts/prediction-market-regulation-2026.md`.

Also Aug: **Nevada GCB** moved to fine Kalshi **$120k/day** for missing its Aug 12 NV deadline; the full geofence works only after an **optional** app update (NV + MI) — treat as residency-spoof fragile, not hard venue-down. Hubs: `@sources/brief-k240-kalshi-nv-geofence-2026-08-17.md`, `@sources/brief-k239-kalshi-sports-mention-2026-08-15.md`. **2026-08-19** is the WA IP+residency geofence day; a US ban/limit is not assumed to move all volume offshore (`@sources/brief-k242-eh-pm-ban-onshore-2026-08-19.md`).

**K243 (2026-08-20):** a comms tail risk — if Republicans go into the midterms as underdogs, party-aligned comms could turn on prediction markets (and Polymarket's GOP skew) as an attack surface. Awareness only, no pm scp (`@sources/brief-k243-eh-pm-republican-comms-2026-08-20.md`).

**K168 (2026-08-31):** Ninth Circuit says Kalshi sports contracts are likely not CEA swaps (NV/CA access risk). Polymarket pulled NFL will-play filings. Kalshi **game-week** sports prices are near-calibrated; **month-plus** futures are not. Hubs: `@sources/daily-digest-rss-nfl-week0-2026-08-31.md`, `@sources/arxiv-2602.19520-pm-domain-calibration-2026-08-31.md`.

### When to stay in traditional books

Better liquidity on mainstream spreads; PM shines on **niche events**, **political/macroeconomic** contracts, and **cross-venue** mispricings (advanced).

### World Cup 2026

Expanded tournament + host nations (USA/Mexico/Canada) create **books vs PM/Kalshi divergence** on advance and futures — `@entities/sports/world-cup-2026-betting.md`, `@concepts/world-cup-books-vs-pm-divergence.md`. Contract-type cheat sheet: `@concepts/world-cup-prediction-market-types.md`. **Retail hygiene checklist (K108):** `@concepts/world-cup-pm-retail-hygiene.md`.

### Signal products

- **MomentumOdds** — `@entities/tools/momentum-odds.md` + `@concepts/sportsbook-pm-line-divergence.md`
- **Odds Jam / Prediction Insiders** — `@entities/tools/odds-jam.md` + `@concepts/pm-copy-trading-retail-risks.md`

### Offline research (K100)

**Polymarket-v1 dataset** (1.2B trades, Nov 2022 – Apr 2026) supports backtests of FLB, fee-reform impact, and category spread baselines without live API keys. See `@concepts/polymarket-v1-research-database.md`. Key retail lesson: **inferred buy/sell from public tape ≈ coin-flip** — copy products need on-chain aggressor side, not tick-rule proxies `[CONFIRMED — arXiv 2606.04217]`.

### Live in-play updating (Kalshi NBA)

Academic live study (arXiv **2606.07811**): Kalshi NBA mids are **directionally responsive** to play-by-play but **underreact on impact** (~**0.64×** public-info benchmark move). Gap predicts short-horizon drift; **spread absorbs executable edge**. See `@concepts/pm-live-belief-updating.md` — complements static **books vs PM** divergence above.

## Snippets

> Rufus Peabody on prediction markets vs books: sharp limits at major US sportsbooks push flow to Pinnacle or PM venues with different liquidity/fee profiles. [Source: M1T0OlG3XEU via @sources/youtube-operator-batch-sports-betting-research-2026-05-31.md]

*(cross-wiki — deep bot snippets live in @osint-wiki)*
