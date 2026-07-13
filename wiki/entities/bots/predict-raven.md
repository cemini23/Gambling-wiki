---
title: predict-raven (Alchemist-X)
type: entity
tags: [entity, bot, prediction-markets, polymarket, steal-from, k151]
keywords: [predict-raven, raven-agent, market-pulse, polymarket-clob, belief-to-trade]
related:
  - concepts/gambling-bot-architecture.md
  - concepts/pm-proper-scoring-clob-profitability.md
  - concepts/prediction-markets-crossover.md
  - concepts/pm-structural-volatility.md
  - entities/platforms/polymarket.md
  - entities/bots/README.md
  - sources/arxiv-2607.03015-belief-to-trade-pm-agents-predict-raven-2026-07-10.md
  - sources/brief-k151-pm-belief-to-trade-volatility-steals-2026-07-10.md
  - sources/openreview-prophets-profit-pm-LYSTj2Cnuu-2026-06-17.md
  - sources/arxiv-2607.07820-deepsearch-world-self-distillation-2026-07-13.md
maturity: draft
created: 2026-07-10
updated: 2026-07-13
---

## Relations

- @sources/arxiv-2607.03015-belief-to-trade-pm-agents-predict-raven-2026-07-10.md — paper + Phase-0
- @entities/platforms/polymarket.md — primary venue (CLOB v2)
- @osint-wiki/entities/tools/polybot.md — complementary PM automation reference (cross-wiki)

## Raw Concept

- **Repo**: [github.com/Alchemist-X/predict-raven](https://github.com/Alchemist-X/predict-raven)
- **Paper**: arXiv [2607.03015](https://arxiv.org/abs/2607.03015) — **Raven-Agent** / belief-to-trade layer
- **Claim**: first open autonomous continuously-running Polymarket trading agent (MIT, ~65★ as of 2026-07-10)

## Narrative

### Architecture (strip-mine)

| Piece | Function |
|-------|----------|
| **Market Pulse** | Evidence gather + independent \(\mathbf{p}\) vs market \(\mathbf{q}\) |
| **Belief-to-trade** | Order policy under service-layer risk controls |
| **Market-blind mode** | WC forecasting without reading prices (calibration research) |

Stack: `@polymarket/clob-client-v2`, cloud continuous run, public decision log.

### Phase-0 audit (2026-07-10)

| Check | Result |
|-------|--------|
| License | **MIT** (`gh api` SPDX) |
| Maturity | ~65★; active 2026 (WC + trading spectator) |
| ToS / risk | **HIGH** — autonomous live trading; inventory + adverse selection |
| Overlap | Pairs K116 proper betting, K151 structural vol, K150 liquidity |

**Verdict: CONDITIONAL-GO (requirements / strip-mine)** — study **module split** (forecast vs trade) and **risk controls** for gambling-bot PM lane spec. **Prod deploy** → @osint-wiki with ToS + human gates. Do not treat public equity curve as verified edge.

## Snippets

> "The trading side is built around a single core component, Market Pulse … compares that evidence against the market's implied odds." [Source: predict-raven README via @sources/arxiv-2607.03015-belief-to-trade-pm-agents-predict-raven-2026-07-10.md]

## Dead Ends

- pip-install as prod Cemini PM bot without fork + ToS review
- Whale-copy of Raven wallet as proper betting
