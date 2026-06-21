---
title: Cross-wiki K125 DIY DFS sweep (all wikis)
type: source
tags: [source, cross-wiki, k125, diy-dfs, sweep]
keywords: [osint-wiki, weather-api, orchestration, federation, momentum-odds]
related:
  - concepts/diy-nfl-dfs-model-architecture.md
  - concepts/dfs-weather-adjustments.md
  - concepts/nfl-dfs-data-sources.md
  - concepts/dfs-model-orchestration.md
  - concepts/dfs-backtesting-framework.md
  - concepts/line-shopping-and-clv.md
  - concepts/kelly-criterion-betting.md
  - entities/tools/momentum-odds.md
  - entities/tools/odds-jam.md
maturity: draft
created: 2026-06-20
updated: 2026-06-20
---

## Relations

- @concepts/diy-nfl-dfs-model-architecture.md — K125 hub updated from this sweep
- @concepts/dfs-weather-adjustments.md — OSINT weather API matrix applied here

## Raw Concept

Parallel subagent sweep of **all sibling wikis** (2026-06-20) for content useful to the DIY NFL DFS projection model. Primary jackpot: **@osint-wiki weather API inventory** (6+ audited sources K125 had only partially covered).

## Narrative

### Wiki-by-wiki verdict

| Wiki | Useful? | Summary |
|------|---------|---------|
| **@osint-wiki** | **High** | Weather APIs (validated), ensemble NWP methodology, API credential registry, parquet/egress patterns, MomentumOdds, gambling federation routing |
| **@gambling-wiki** (local) | **High** | Underlinked K124 pages: CLV, Kelly, bankroll, parlay correlation, nfl-betting injury cadence, momentum-odds/odds-jam stubs |
| **@ccc-wiki** | **Medium** | Plan-then-execute DAG orchestration, scatter-gather subagents, lazy-tool/MCP fetch patterns — no DFS domain |
| **@game-dev-wiki** | **Low** | Daily digest Exa cadence only; no NFL/sports |
| **@seo-wiki** | **Low** | World Cup bot marketing cross-refs; weather-icons CSS (UI only) |
| **@cybersecurity-wiki** | **Low** | "Hacking APIs" book — scrape posture reference only |
| **@image-gen-wiki** | **None** | — |
| **@3d-printing-wiki** | **None** | — |

---

### @osint-wiki — Weather (W-WEATHER) — **upgrade K125**

| Page | Role for NFL DFS | Verdict | Key fact |
|------|------------------|---------|----------|
| `@osint-wiki/entities/data-sources/open-meteo.md` | Primary forecast + multi-model ensemble (ECMWF/GFS/ICON) | **GO** personal | No API key; **bias_correction=true claim RETRACTED** — build bias from historical forecast + station truth |
| `@osint-wiki/entities/data-sources/nws-weather-gov.md` | US ground truth + hourly forecast; cross-check Open-Meteo | **GO** | Free, User-Agent required, no key |
| `@osint-wiki/entities/tools/visualcrossing-weather.md` | Deep historical backtest (50yr) | **CONDITIONAL-GO** backtest only | 1k records/day free; **grid-interpolated NOT station-direct** — silent divergence at stadium |
| `@osint-wiki/entities/tools/wethr-net.md` | Station-direct METAR bounds | **GO** if budget | $24.99/mo Pro; `logic=nws` vs `logic=wu`; airport roster covers major NFL cities |
| `@osint-wiki/entities/tools/weatherapi-com.md` | Benchmark only | Reference | Shallow history (2010+) |
| `@osint-wiki/entities/tools/openweather-api.md` | Defer | Defer | Key in prod `.env` but OSINT defers until explicit thesis |
| `@osint-wiki/concepts/ensemble-weather-forecasting.md` | Multi-model blend methodology | Validated | EMOS/DEB calibration patterns; Open-Meteo ingestion CONFIRMED in prod |
| `@osint-wiki/concepts/nwp-bias-correction-ml-weather-trading.md` | Bias correction for forecast error | Reference | ML bias correction for NWP |
| `@osint-wiki/concepts/api-credential-registry.md` | Rate limits + key inventory | Core ops | Documents Open-Meteo/NWS free; OpenWeather ✅ held; Visual Crossing ❌ not held |

**Recommended NFL DFS weather stack (revised):**

1. **Forecast:** Open-Meteo hourly at stadium lat/lon (free, personal)
2. **Validation:** NWS gridpoint forecast for US games
3. **Backtest depth:** Visual Crossing unified timeline (backtest only; watch interpolation)
4. **Optional precision:** Wethr.net if paying for station-direct bounds near lock
5. **Methodology:** Borrow ensemble + bias-correction concepts from OSINT NWP pages — apply wind/precip thresholds from gambling-wiki Claremont citations

---

### @osint-wiki — Vegas / odds (W-VEGAS)

| Page | Role | Notes |
|------|------|-------|
| `@osint-wiki/entities/tools/momentum-odds.md` | Multi-book correlation signals | Commercial; 60+ books; webhook — **not a replacement for The Odds API** but useful for sharp-move detection |
| `@osint-wiki/concepts/gambling-wiki-federation.md` | Cross-wiki routing | momentum-odds ↔ gambling-wiki stub already mapped |
| `@osint-wiki/entities/platforms/kalshi.md` | PM resolution via ESPN etc. | NFL game markets secondary to traditional books for DFS ITT |

Gambling-wiki already has `@entities/tools/momentum-odds.md` and `@entities/tools/odds-jam.md` stubs cross-linking OSINT. **The Odds API** not documented in OSINT — K125 nflreadr + Odds API path stays gambling-wiki primary.

---

### @osint-wiki — Orchestration / data (W-ORCH, W-DATA)

| Page | Role |
|------|------|
| `@osint-wiki/entities/infrastructure/cemini-egress-fi.md` | Raw archive pattern: `cemini-egress-fi:/opt/cemini-bulk/research/gambling/` (same as gambling-wiki CLAUDE.md) |
| `@osint-wiki/entities/tools/arcticdb.md` | Time-series storage alternative to parquet [TENTATIVE for laptop DFS] |
| `@osint-wiki/concepts/pnl-attribution-versioning.md` | Run manifest / version discipline for backtests |
| `@osint-wiki/concepts/markov-regime-switching-models.md` | Regime ideas for early-season vs late-season projection weights [REFERENCE] |
| `@osint-wiki/concepts/time-series-arima-garch-framework.md` | Variance modeling for distribution layer [REFERENCE] |

---

### @ccc-wiki — Pipeline orchestration

| Page | K125 workstream | Use |
|------|-----------------|-----|
| `@ccc-wiki/concepts/plan-then-execute-topological-orchestration.md` | W-ORCH | DAG: fetch → project → sim → normalize → optimize |
| `@ccc-wiki/entities/patterns/scatter-gather.md` | W-ORCH | Parallel subagent/API fan-out (match K125 38-agent dispatch) |
| `@ccc-wiki/entities/tools/lazy-tool.md` | W-DATA external research | Exa/Brave/fetch when nflverse can't answer |

---

### @gambling-wiki — Underlinked local pages (wire to K125)

| Page | Workstream | Action |
|------|------------|--------|
| `@concepts/bankroll-management.md` | W-ORCH | DFS GPP 10–20% per slate |
| `@concepts/kelly-criterion-betting.md` | W-ORCH / W-DIST | Entry sizing / fractional Kelly for contest selection |
| `@concepts/line-shopping-and-clv.md` | W-BACKTEST | Sharp lines as projection benchmark |
| `@entities/sports/nfl-betting.md` | W-INJ / W-IMPLIED | Wed/Fri injury cadence; key numbers |
| `@concepts/parlay-and-correlated-bets.md` | W-CORR | Already linked via dfs-correlation-stacking |
| `@concepts/prediction-markets-crossover.md` | W-IMPLIED | PM underreaction patterns [REFERENCE for alt totals] |
| `@entities/tools/momentum-odds.md` | W-VEGAS | Cross-link OSINT deep page |
| `@sources/web-dfs-hero-nfl-gpp-strategy-2026-06-20.md` | W-CORR / W-OWN | MME pool template, FD 4-player team cap |

---

### Gaps filled vs K125 original research

| Gap | Filled by |
|-----|-----------|
| Only Open-Meteo mentioned | **6 OSINT weather sources** with Phase-0 verdicts |
| bias_correction parameter | **RETRACTED** per OSINT open-meteo page |
| Interpolation vs station-direct | Visual Crossing vs Wethr.net vs NWS roles clarified |
| Orchestration patterns | CCC DynAMO + scatter-gather; OSINT pnl versioning |
| CLV as projection benchmark | gambling-wiki line-shopping page |
| Kelly for contest bankroll | gambling-wiki kelly + bankroll pages |

### Still no cross-wiki coverage

- nflverse / nflreadpy (gambling-wiki only)
- Stokastic / FantasyLabs / DFS ownership (gambling-wiki only)
- FanDuel/DK salary schemas (gambling-wiki only)
- THE BLITZ / stat projection engines (gambling-wiki only)

## Snippets

> "Open-Meteo internally serves ECMWF + GFS + ICON + MetNo + JMA — use as primary; NWS as US tiebreaker." [Source: @osint-wiki/entities/data-sources/open-meteo.md]

> "Visual Crossing historical is grid-interpolated — do NOT use on live stadium path." [Source: @osint-wiki/entities/tools/visualcrossing-weather.md]

> "Wethr.net: station-direct METAR; logic=nws vs logic=wu must match resolution context." [Source: @osint-wiki/entities/tools/wethr-net.md]
