---
title: Kalshi
type: entity
tags: [entity, platform, prediction-markets, regulated, sports]
keywords: [kalshi, event-contracts, cftc, dcm, sports-markets]
related:
  - concepts/favorite-longshot-bias.md
  - concepts/gambling-bot-architecture.md
  - concepts/gambling-wiki-scope.md
  - concepts/prediction-markets-crossover.md
  - concepts/pm-commitment-grounded-language.md
  - concepts/sharp-vs-soft-books.md
  - concepts/sportsbook-pm-line-divergence.md
  - concepts/world-cup-books-vs-pm-divergence.md
  - concepts/world-cup-prediction-market-types.md
  - entities/platforms/polymarket.md
  - entities/sports/world-cup-2026-betting.md
  - entities/tools/momentum-odds.md
  - sources/osint-cross-wiki-wc2026-retail-synthesis-2026-05-31.md
  - sources/youtube-sports-pm-retail-batch-2026-05-29.md
  - sources/daily-digest-news-r1-r12-2026-06-01.md
  - sources/daily-digest-news-r1-r12-2026-06-02.md
  - sources/daily-digest-arxiv-batch-2026-06-02.md
  - sources/youtube-wsj-kalshi-polymarket-valuations-2026-06-01.md
  - sources/arxiv-kalshi-live-belief-updating-2606.07811-2026-06-09.md
  - concepts/pm-live-belief-updating.md
  - entities/sports/nba-betting.md
  - entities/sports/wnba-betting.md
  - concepts/world-cup-pm-retail-hygiene.md
  - sources/brief-k108-gambling-wc-retail-hygiene-2026-06-09.md
  - concepts/pm-proper-scoring-clob-profitability.md
  - sources/openreview-prophets-profit-pm-LYSTj2Cnuu-2026-06-17.md
  - sources/arxiv-2606.30040-kalshi-macro-belief-distributions-2026-07-01.md
  - sources/arxiv-2606.31675-settlement-manipulation-prediction-markets-2026-07-01.md
  - concepts/kalshi-spotify-oracle-manipulation-2026-07.md
  - concepts/kalshi-michigan-sports-injunction-2026-06.md
  - concepts/pm-whale-conviction-bias-2026-07.md
  - sources/substack-rss-event-horizon-2026-07-03-how-artificial-spotify-streams-broke-a-kalshi-ma.md
  - sources/substack-rss-event-horizon-2026-06-29-michigan-court-orders-kalshi-to-stop-sports-even.md
  - sources/arxiv-2607.08199-pm-structural-volatility-kalshi-2026-07-10.md
  - concepts/pm-structural-volatility.md
  - sources/research-wnba-cold-streak-live-unders-2026-08-13.md
  - sources/daily-digest-rss-industry-2026-08-14.md
  - sources/substack-rss-event-horizon-2026-08-13-novig-responsible-trading.md
  - sources/brief-k222-k231-pm-retail-awareness-2026-08.md
  - sources/brief-k239-kalshi-sports-mention-2026-08-15.md
  - sources/brief-k240-kalshi-nv-geofence-2026-08-17.md
  - sources/brief-k242-eh-pm-ban-onshore-2026-08-19.md
  - sources/brief-k243-eh-pm-republican-comms-2026-08-20.md
  - sources/arxiv-2602.19520-pm-domain-calibration-2026-08-31.md
  - sources/daily-digest-rss-nfl-week0-2026-08-31.md
maturity: draft
created: 2026-05-31
updated: 2026-08-31
---

## Relations

- @concepts/kalshi-spotify-oracle-manipulation-2026-07.md — culture-chart oracle risk
- @concepts/kalshi-michigan-sports-injunction-2026-06.md — Michigan TRO
- @concepts/pm-whale-conviction-bias-2026-07.md — size-weighting bias
- @concepts/prediction-markets-crossover.md — retail vs bot lens
- @entities/sports/wnba-betting.md — WNBA series inventory (no last-2:00 contract)
- @osint-wiki/entities/platforms/kalshi.md — Cemini trading stack, regulation, bots
- @sources/daily-digest-rss-industry-2026-08-14.md — CFTC emergency vs NY AG (Aug 2026)
- @sources/substack-rss-event-horizon-2026-08-13-novig-responsible-trading.md — incentive-program advisory (cross-wiki)
- @sources/brief-k222-k231-pm-retail-awareness-2026-08.md — 15-min volume, Utah SJ, FlightAware, NY tax sanity-check
- @osint-wiki/sources/substack-rss-event-horizon-2026-08-14-kalshi-sports-mention.md — K239 sports mention markets sidelined + WA geofence
- @sources/brief-k239-kalshi-sports-mention-2026-08-15.md — K239 wiki stub
- @sources/brief-k240-kalshi-nv-geofence-2026-08-17.md — K240 NV $120k/day + optional-update geofence
- @osint-wiki/sources/substack-rss-event-horizon-2026-08-17-pm-policy-klein.md — K240 source of record
- @sources/brief-k242-eh-pm-ban-onshore-2026-08-19.md — K242 WA geofence day; ban ≠ offshore
- @sources/brief-k243-eh-pm-republican-comms-2026-08-20.md — K243 GOP-underdog comms tail risk
- @osint-wiki/sources/substack-rss-event-horizon-2026-08-19-pm-ban-onshore.md — K242 source of record
- @sources/arxiv-2602.19520-pm-domain-calibration-2026-08-31.md — sports short-horizon calibration (K168)
- @sources/daily-digest-rss-nfl-week0-2026-08-31.md — football volume, injury markets, 9th Circuit

## Raw Concept

CFTC-regulated prediction market (DCM). **Consumer/strategy** entity here; execution infrastructure in @osint-wiki.

## Narrative

Kalshi lists **event contracts** (sports, economics, weather, politics). Retail considerations: fee schedule, contract specs, FLB on sports lines, geoblocking.

### World Cup 2026

**Group qualifiers** (advance), **group winner**, **match games**, and **outright** series — cross-walk to Polymarket in `@concepts/world-cup-prediction-market-types.md`. Kalshi resolves many sports via **ESPN/Fox/WSJ/Reuters** consensus — may differ from FIFA-only PM paths on edge cases [TENTATIVE]. Hub: `@entities/sports/world-cup-2026-betting.md`.

For bot architecture, LP, logit pricing, regulatory preemption: `@osint-wiki/entities/platforms/kalshi.md`.

### Regulation and sports volume (R3 WSJ, 2026-06-01) [TENTATIVE]

- **CFTC DCM** — US event contracts regulated as **swaps** (CFTC, same agency as commodity futures per WSJ explainer).
- **Sports dominance** — WSJ cites **>70%** of Kalshi volume in sports; legal fight with **states** after sports expansion.
- **State gaming conflict** — Nevada and others push PMs toward **state gambling licenses**; research firm: **~69%** of volume from **19 states** without legal online sports betting.
- **“Not the house”** marketing vs **Kalshi Trading LLC** internal market maker — retail should assume **liquidity comes from designated MMs**, not peer-only pool.
- **Sharp migration** — pro bettor segment (WSJ: Frank Santolo) cites **higher limits** vs books that limit winners — aligns with `@concepts/sharp-vs-soft-books.md` PM column.

Hub source: `@sources/youtube-wsj-kalshi-polymarket-valuations-2026-06-01.md`.

### Fees vs sportsbooks (R2, 2026-06-01) [TENTATIVE]

Tech-Insider comparison: flagship Kalshi sports contracts **~0.5–1.5%** implied vig vs **~4.5%** standard -110/-110 book hold. Example: Chiefs ML priced **1.1¢** better effective on Kalshi vs DraftKings in May 2026 test. High-volume bettors: fee gap compounds ($50k/yr ≈ $2.25k vig at books vs $500–1k fees on Kalshi per article math). **Tax:** Kalshi gains may qualify for **Section 1256** 60/40 treatment vs ordinary gambling income on books [NEEDS VERIFICATION 2026-06-01].

### US volume share & NBA Finals stress test (R2, 2026-06-02) [TENTATIVE]

DeFi Rate week ending **2026-05-24** (Fair Stake / digest R2):

| Metric | Kalshi | Polymarket |
|--------|--------|------------|
| Weekly notional | **$3.99B** (+3% WoW) | **$1.65B** (-15% WoW) |
| Combined US share | **70.8%** (record per article) | ~29.2% |
| Sports notional | **$1.599B** (40% of Kalshi) | **$675.5M** |

Structural drivers cited: **USD bank on-ramp** vs PM USDC friction, **order-book** liquidity from traditional derivatives desks, **parlay self-certification** (early 2026). **Politics** still PM-heavy; **sports** now Kalshi-led in US.

**June 2026 watch:** NBA Finals from **2026-06-03** — game-level Kalshi prices reportedly tracked **Pinnacle** within **1–2¢** implied on NBA game contracts [TENTATIVE]. Thesis breaks if PM US sports product closes gap, sportsbook handle flat, or adverse **CFTC / state** rulings.

Hub: `@sources/daily-digest-news-r1-r12-2026-06-02.md`.

### Live NBA belief updating (arXiv 2606.07811, 2026-06-09) [CONFIRMED]

Angelini & De Angelis merge **1-min Kalshi NBA game-contract quotes** with **play-by-play**:

| Finding | Detail |
|---------|--------|
| Pre-game | Calibrated; Brier improves 0.204 → 0.199 in final 24h |
| Directional live | Prices react quickly to scoring, 3pt, lead changes, runs |
| Efficient live | **β ≈ 0.64** — 10pp public-info move → ~6.4pp mid move on impact |
| Drift | Updating gap predicts **5–15 min** further mid move; **not** executable after spread |
| Salience × liquidity | Visible events in **thin** markets underreact most |

Retail: live mids **track the game** but **lag full fair-value move** — size down in illiquid states; don't market-chase the lag. Bot: liquidity gate + drift-aware limits. Hub: `@concepts/pm-live-belief-updating.md`, `@sources/arxiv-kalshi-live-belief-updating-2606.07811-2026-06-09.md`.

### WNBA sports series (public catalog, 2026-08-13) [CONFIRMED]

Operator catalog pass (no auth): **88** WNBA / Women’s Pro Basketball series. Liquid objects: `KXWNBAGAME`, `KXWNBATOTAL`, `KXWNBASPREAD`, half/quarter totals (`KXWNBA1–4QTOTAL`, `1H`/`2HTOTAL`), `KXWNBATEAMTOTAL`. **No** last-2-minute / each-team-under-5 time-window series (Sports-wide search empty). Live 4Q ladders can be **too wide to fill** even in blowouts; game totals carry most OI. Hub: `@entities/sports/wnba-betting.md`, `@sources/research-wnba-cold-streak-live-unders-2026-08-13.md`.

### Short-horizon crypto + FlightAware (K225 / K231, Aug 2026) [CONFIRMED]

Trailing-7d (Event Horizon / Ticker Tracker): **~$1.5B** Kalshi crypto notional, **~$1.1B** on **BTC 15-min**; gold/silver 15-min added. Treat as casino-velocity products, not long-dated political markets. **FlightAware v. Kalshi** (SDNY): flight-cancellation series named FlightAware as primary settlement source after a free AeroAPI signup; DOT BTS is an alternate — series can delist or change oracle. Hub: `@sources/brief-k222-k231-pm-retail-awareness-2026-08.md`.

### Sports mention markets gone (K239, 2026-08-14) [CONFIRMED]

Kalshi **sidelined sports mention markets** ahead of football (Discord: temporarily; Event Horizon: short-term at least). NPR: federal review of mention markets (announcer/word-choice contracts). NFL/MLB already asked venues not to list easily manipulated events. Mention volume since Kalshi launched sports: **$1.2B**. Polymarket international still lists some. **Do not plan a mention-market bot.** If the category returns, treat as high-manipulation / league-hostile — not an LP lane.

King County **final order** geofences most of Kalshi's mix in Washington (sports, elections, politics, entertainment, culture, tech/science, **mentions**) — Aug 19 IP+residency, Sep 2 multi-source. Hub: `@osint-wiki/sources/substack-rss-event-horizon-2026-08-14-kalshi-sports-mention.md`, brief `../briefs/2026-08-15_k239-gambling-kalshi-sports-mention-gone.md`.

### WA geofence day + ban ≠ offshore (K242, 2026-08-19) [TENTATIVE]

**2026-08-19** is the King County IP+residency geofence date. Event Horizon argues a US ban/limit would **not** relocate all volume offshore (sports-betting legalization created new activity; CFTC already hit US-serving offshore venues). Mentions remain a tiny share under federal review. **No pm-bot scp.** Dual-ID: OSINT K242 ≠ Trajectory Sentinel K242. Hub: `@osint-wiki/sources/substack-rss-event-horizon-2026-08-19-pm-ban-onshore.md`, `@sources/brief-k242-eh-pm-ban-onshore-2026-08-19.md`.

### Nevada $120k/day + optional-update geofence (K240, 2026-08-17) [CONFIRMED]

Nevada GCB late-Friday filing: Kalshi missed the Aug 12 deadline to stop sports/election/entertainment contracts in NV and should face **$120,000/day** fines; investigators bought banned-category contracts from NV phones. Kalshi says the geofence was up Aug 12 and investigators spoofed residence. InGame: the full geofence works after an **optional** app update (also Michigan). Treat the geofence as **optional-update / residency-spoof fragile**, not a hard venue-down — same **$120k/day geolocation-fine class** as the Michigan TRO. Hub: `@osint-wiki/sources/substack-rss-event-horizon-2026-08-17-pm-policy-klein.md`, brief `../briefs/2026-08-17_k240-eh-kalshi-nv-geofence.md`.

### CFTC emergency authority vs NY AG (Aug 2026) [CONFIRMED]

CFTC used **emergency powers twice in ~30 days** — LSB: first uses since **1980**, and only **six times** in agency history — instructing KalshiEX to **keep operating** under CEA Core Principles in **Michigan** then **New York**. NY AG suit frames sports event contracts as illegal gambling and seeks up to **$36B** restitution; AG says CFTC cannot manufacture exclusive-jurisdiction conflict. Retail: NY/MI sports-PM access can flip on court papers overnight — do not size Kalshi sports as if state geofence is stable. Hub: `@sources/daily-digest-rss-industry-2026-08-14.md`, `@concepts/kalshi-michigan-sports-injunction-2026-06.md`, `@osint-wiki/concepts/prediction-market-regulation-2026.md`.

### Macro CPI belief distributions (K135) [TENTATIVE 2026-07-01]

@sources/arxiv-2606.30040-kalshi-macro-belief-distributions-2026-07-01.md (Angelini) recovers **full implied distributions** from adjacent **CPI / core CPI threshold** contracts — tail probabilities often carry signal beyond Reuters point consensus. Pairs live NBA updating paper above.

### Crypto event-contract volume (K135 context) [TENTATIVE]

@sources/arxiv-2606.31675-settlement-manipulation-prediction-markets-2026-07-01.md cites Kalshi crypto binaries passing **$1B/month** (Mar 2026) as horizons shrink — same **cash-settlement manipulation** structural risk applies when contracts settle on manipulable spot prices.

### Spotify culture-market oracle incident (2026-07) [TENTATIVE]

Event Horizon / trader Caleb Davies: alleged **stream-botting** resolved a low-probability **Malcolm Todd** chart bracket before Spotify audit removed fake plays; Kalshi paid out on pre-audit data. Hub: `@concepts/kalshi-spotify-oracle-manipulation-2026-07.md`, `@sources/substack-rss-event-horizon-2026-07-03-how-artificial-spotify-streams-broke-a-kalshi-ma.md`.

### Michigan sports-contract TRO (2026-06-29) [TENTATIVE]

14-day injunction: no Michigan sports event contracts without sports-betting license; **$120k/day** geolocation fine. Hub: `@concepts/kalshi-michigan-sports-injunction-2026-06.md`.

### NFL 2026 kickoff — volume, injury markets, 9th Circuit (K168) [CONFIRMED via OSINT EH]

TickerTracker: weekday notional **>$1B** (was ~$25M Aug 2025). Football preseason 30× YoY but still a small share of incremental growth vs parlays/crypto. Kalshi listed Week-1 **will-play** markets; CFTC/NFL remain hostile to injury-adjacent contracts. Ninth Circuit 3-0: sports event contracts **likely not CEA swaps** — NV/CA access can flip; Hard Rock stays the W8 book. Sports PM **game** prices inside a week are near-calibrated; month-plus futures are compressed toward 50%. Hub: `@sources/daily-digest-rss-nfl-week0-2026-08-31.md`, `@sources/arxiv-2602.19520-pm-domain-calibration-2026-08-31.md`. **No pm scp.**

### Whale size-weighting bias (2026-07) [TENTATIVE]

Daleep et al. via Klement: large bettors show **lower edge** than small — PM prices may mis-weight conviction. Hub: `@concepts/pm-whale-conviction-bias-2026-07.md`.

## Snippets

> "Kalshi priced KC YES at $0.585… DraftKings -135… Kalshi paid the better effective price by 1.1 cents." [Source: @sources/daily-digest-news-r1-r12-2026-06-01.md, R2]

> "Kalshi took $3.99 billion of weekly notional volume… lifting… share… to 70.8% — its highest reading on record." [Source: @sources/daily-digest-news-r1-r12-2026-06-02.md, R2]

> "A one-minute change in benchmark win probability is associated with only about a 0.64-for-one contemporaneous change in market prices." [Source: arxiv-2606.07811 via @sources/arxiv-kalshi-live-belief-updating-2606.07811-2026-06-09.md]
