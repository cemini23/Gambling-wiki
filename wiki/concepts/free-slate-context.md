---
title: Free slate context (weather + pitchers)
type: concept
tags: [concept, weather, mlb, nfl, unders, open-meteo]
keywords: [open-meteo, mlb-stats-api, unders, wind, probable-pitcher, roof]
related:
  - concepts/dfs-weather-adjustments.md
  - concepts/nfl-dfs-data-sources.md
  - concepts/daily-edge-card.md
  - entities/sports/nfl-betting.md
  - concepts/parlay-and-correlated-bets.md
maturity: draft
created: 2026-08-15
updated: 2026-08-15
---

## Relations

- @concepts/dfs-weather-adjustments.md — DFS wind/dome thresholds this CLI reuses
- @concepts/nfl-dfs-data-sources.md — GO stack: Open-Meteo + Odds API; ESPN NO-GO
- @concepts/daily-edge-card.md — market-relative EV card; this page is environment context only
- @entities/sports/nfl-betting.md — NFL totals / weather as a situational input
- @concepts/parlay-and-correlated-bets.md — unders parlays are still correlated (weather hits the whole slate)

## Raw Concept

Zero-cost context layer for **unders** and MLB tickets: **Open-Meteo** (stadium hour) + **MLB Stats API** (probable pitchers, roof, coords) + static **NFL venue** lat/lon. Not a projection model. Does not replace The Odds API for prices.

## Narrative

### What is free (no key)

| Source | Role | Key? |
|--------|------|------|
| Open-Meteo | Hourly temp / wind / precip at lat/lon | No (personal / non-commercial cap) |
| MLB Stats API | Schedule, probable pitchers, venue roof + coords | No |
| Static NFL stadium table | Home-team → park + roof | Local file |
| The Odds API **free tier** | Live HR/DK/FD totals + moneylines | Free key, **quota** — not a paid plan |

Not wired (on purpose): ESPN undocumented JSON (wiki **NO-GO** as a pipeline), NWS (extra User-Agent dance; Open-Meteo is enough for a lean flag), paid odds vendors.

### Run

```bash
# Weather + pitchers only (no Odds API credit)
python scripts/slate_context.py mlb --hours 36

# Live unders parlay — prefers LEAN_UNDER games, still confirm in Hard Rock
python scripts/ticket_builder.py mlb --legs 4 --mode unders --min-odds +300
python scripts/ticket_builder.py nfl --legs 3 --mode unders
```

`--no-context` skips weather/pitchers if you only want prices.

### Under lean (heuristic)

Positive score → `LEAN_UNDER`. Enclosed roofs → `INDOOR` (weather off). Retractable still shows weather — **confirm roof** in-app.

| Signal | Score |
|--------|-------|
| Precip chance ≥40% | +2 |
| Precip ≥0.05 in | +1 |
| Wind ≥15 mph | +2 |
| Wind 10–14 mph | +1 |
| Temp ≤45°F | +2 |
| Temp 46–55°F | +1 |
| Coors / Mile High | −2 (altitude often fades weather unders) |

Score ≥2 → lean under. This is a **screen**, not fair probability. Books already bake a lot of weather into the total.

### What this is not

- A run-expectancy or EPA model
- Auto-bet / scrape of Hard Rock
- License to treat ESPN scoreboard JSON as a product feed

## Snippets

> Free tier: Less than 10'000 API calls per day … You may only use the free API services for non-commercial purposes. [Source: https://open-meteo.com/en/terms (retrieved 2026-06-20)]
