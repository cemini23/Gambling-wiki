---
title: "Gemini DR — GitHub sports betting & open-source tool landscape"
type: source
tags: [source, gemini-deep-research, github, sports-betting, dfs, phase-0]
keywords: [open-source, pydfs, sharp-soft-arb, copy-trading, landscape]
related:
  - concepts/dfs-strategy-overview.md
  - concepts/sharp-vs-soft-books.md
  - concepts/prediction-markets-crossover.md
  - concepts/pm-copy-trading-retail-risks.md
  - concepts/sportsbook-pm-line-divergence.md
  - entities/tools/momentum-odds.md
  - entities/tools/pydfs-lineup-optimizer.md
  - entities/tools/odds-jam.md
  - entities/sports/nfl-betting.md
  - entities/sports/nba-betting.md
  - entities/sports/world-cup-2026-betting.md
maturity: validated
created: 2026-05-31
updated: 2026-05-31
read_status: deep-read
---

## Relations

- @osint-wiki/sources/gemini-github-sports-betting-repos-landscape-2026-05-30.md — full report incl. PM bot Phase-0 queue
- @entities/tools/pydfs-lineup-optimizer.md — primary DFS tool candidate
- @concepts/sharp-vs-soft-books.md — Pinnacle vs soft book arb pattern

## Raw Concept

| Field | Value |
|-------|-------|
| Title | The Convergence of Autonomous AI Agents, ML, and Decentralized Prediction Markets (GitHub landscape) |
| Author | Gemini Deep Research |
| Location | `cemini-librarian:/opt/cemini-bulk/research/GitHub Sports Betting Repositories Evaluation.docx` |
| Retrieved | 2026-05-30 |
| Read status | deep-read (gambling-wiki lens: fiat/DFS/retail; PM bot rows on @osint-wiki) |

## Narrative

Broad survey of open-source **sports betting, DFS, arbitrage, and Polymarket** repos. Gambling-wiki extracts **retail-relevant** layers; bot adoption verdicts stay on `@osint-wiki`.

### Layer map (retail focus)

| Layer | Examples | Gambling-wiki use |
|-------|----------|-------------------|
| Data / stats | `roclark/sportsipy`, `bttmly/nba` | Reference for building projections |
| **Classical ML / DFS** | `kyleskom/NBA-Machine-Learning-Sports-Betting`, **`pydfs-lineup-optimizer`** | DFS + model research — `@entities/tools/pydfs-lineup-optimizer.md` |
| **Fiat sharp/soft arb** | `Live-Sports-Arbitrage-Bet-Finder`, `pretrehr/Sports-betting` | Alert-only pattern — `@concepts/sharp-vs-soft-books.md` |
| Copy-trading PM bots | Multiple GitHub forks | **NO-GO retail** — `@concepts/pm-copy-trading-retail-risks.md` |
| DRL / quant | `machine-learning-for-trading` | Out of scope unless quant ingest |

### Sharp vs soft (fiat)

Report: **Pinnacle** as sharp reference, **Bwin/PMU** as soft execution — latency arb when soft book lags sharp move. Open-source finders are **alert-only**; autonomous arb hits ToS, limits, and stale-line risk [TENTATIVE].

### Copy-trading caution [CONFIRMED report + YouTube experiments]

Whale-copy bots cascade on large wallet trades — hundreds of followers consume liquidity in seconds, amplifying slippage. Retail should assume **adverse selection** when copying public alerts (Odds Jam, PolySniper promos).

### Security hygiene (any self-hosted bot)

Accidental `.env` commits with wallet private keys remain the most common catastrophic loss in open-source PM repos — never run unaudited fork with real keys.

### Phase-0 queue (gambling-wiki)

| Tool/repo | Verdict | Notes |
|-----------|---------|-------|
| `pydfs-lineup-optimizer` | **CONDITIONAL-GO** | Verify license + NFL/NBA slate fit before install |
| Fiat arb finders | **Reference only** | Manual confirmation required |
| Copy-trading bots | **NO-GO** | Strategy + flow toxicity |
| Closed SaaS (MomentumOdds, Odds Jam) | **Reference** | Commercial TOS + track record |

## Snippets

> Copy-trading bots cascade when a whale trades — hundreds of bots consume order book liquidity in seconds, amplifying slippage. [Source: GitHub Sports Betting Repositories Evaluation.docx]

> Pinnacle as sharp reference, Bwin/PMU as soft execution targets for latency arbitrage pattern. [Source: same]
