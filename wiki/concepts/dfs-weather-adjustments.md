---
title: DFS weather adjustments
type: concept
tags: [concept, dfs, nfl, weather, w-weather, cross-wiki]
keywords: [wind, open-meteo, nws, visualcrossing, wethr, dome, passing-efficiency, kicker]
related:
  - concepts/team-volume-pace-model.md
  - concepts/nfl-dfs-data-sources.md
  - concepts/diy-nfl-dfs-model-architecture.md
  - sources/cross-wiki-k125-diy-dfs-sweep-2026-06-20.md
maturity: draft
created: 2026-06-20
updated: 2026-06-20
---

## Relations

- @sources/cross-wiki-k125-diy-dfs-sweep-2026-06-20.md — OSINT weather API inventory (K125 cross-wiki)
- @osint-wiki/entities/data-sources/open-meteo.md — primary multi-model forecast
- @osint-wiki/entities/data-sources/nws-weather-gov.md — US validation / ground truth
- @osint-wiki/entities/tools/visualcrossing-weather.md — deep historical backtest (interpolation caveat)
- @osint-wiki/entities/tools/wethr-net.md — station-direct METAR bounds (paid)
- @concepts/team-volume-pace-model.md — pass-rate wind adjustments

## Raw Concept

Game-time weather → passing/kicking efficiency haircuts. **CONDITIONAL-GO** with proper stadium roof logic. Weather **data layer upgraded** from cross-wiki OSINT sweep (2026-06-20).

## Narrative

### Recommended API stack (NFL DFS)

| Priority | Source | Role | Verdict | Cross-wiki |
|----------|--------|------|---------|------------|
| 1 | **Open-Meteo** | Hourly wind/precip/temp at stadium lat/lon; multi-model ensemble | **GO** (personal/non-commercial) | @osint-wiki/entities/data-sources/open-meteo.md |
| 2 | **NWS / weather.gov** | US forecast validation; authoritative observations | **GO** (no key; User-Agent) | @osint-wiki/entities/data-sources/nws-weather-gov.md |
| 3 | **Visual Crossing** | 50yr historical for backtesting wind→passing regressions | **CONDITIONAL-GO** backtest only | @osint-wiki/entities/tools/visualcrossing-weather.md |
| 4 | **Wethr.net** | Station-direct METAR high/low bounds near lock | **GO** if budget ($24.99/mo Pro) | @osint-wiki/entities/tools/wethr-net.md |
| — | OpenWeather | Key held in prod `.env` | **Defer** for DFS | @osint-wiki/entities/tools/openweather-api.md |
| — | WeatherAPI.com | Benchmark | Reference only | @osint-wiki/entities/tools/weatherapi-com.md |

**Critical OSINT correction:** Open-Meteo `bias_correction=true` parameter claim is **RETRACTED** on @osint-wiki — build bias correction from Historical Forecast API + NWS station truth, not a magic query flag.

**Interpolation warning:** Visual Crossing history is **grid-interpolated**, not stadium METAR-direct. Fine for aggregate backtests; do not treat as exact stadium observation for a single game.

### Stadium table

- Base: greerreNFL/stadiums (lat/lon, roof type)
- Manual overrides: SoFi = semi-open; retractable = unresolved until NFL 90-min roof call

### Roof logic (not binary dome flag)

| Type | Weather adj |
|------|-------------|
| Fixed enclosed | Off |
| Retractable | Off only after NFL 90-min roof decision |
| Semi-open (SoFi) | **On** |
| Open | On |

### Cited DFS thresholds (unchanged)

| Condition | Effect |
|-----------|--------|
| +10 mph wind | ~-6.8% pass yards, -2.4% completion (Claremont thesis) |
| Wind ≥10 mph | FG success down (Clark et al.) |
| 15/25/35 mph tiers | Practical downgrade bands |

### Pass-rate bands (→ @concepts/team-volume-pace-model.md)

- <10 mph: none · 10–14: -1.5 pp · 15–19: -3.0 pp · 20+: -5 to -7 pp

### Ensemble methodology (borrow from OSINT)

@osint-wiki/concepts/ensemble-weather-forecasting.md documents blending ECMWF/GFS/ICON/MetNo/JMA — applicable when Open-Meteo returns multi-model spread; use spread as **uncertainty flag** for GPP ceiling/downgrade decisions, not just point wind speed.

## Snippets

> "Use NWS as resolution-truth cross-check when ensemble members disagree on US stadiums." [Source: @osint-wiki/entities/data-sources/nws-weather-gov.md]

> "Getting wethr logic=nws vs logic=wu wrong = silent bias." [Source: @osint-wiki/entities/tools/wethr-net.md]
