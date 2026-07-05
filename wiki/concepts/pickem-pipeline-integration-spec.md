---
title: Pick'em pipeline integration spec
type: concept
tags: [concept, pickem, props, nfl, pipeline, cli, w-integ, k147]
keywords: [prop-fair, edges-csv, cli, integration-spec, defer-extension]
related:
  - concepts/diy-nfl-pickem-props-tool-architecture.md
  - concepts/pickem-fair-probability.md
  - concepts/pickem-slip-ev-and-correlation.md
  - concepts/pickem-operator-workflow.md
  - concepts/pickem-data-sources.md
  - concepts/pickem-stat-type-mapping.md
  - entities/tools/ceminidfs.md
  - entities/platforms/underdog-fantasy.md
maturity: draft
created: 2026-07-05
updated: 2026-07-05
---

## Relations

- @entities/tools/ceminidfs.md — borrow projection distributions; **no pick'em code in that repo**
- @concepts/dfs-pipeline-integration-spec.md — sibling pattern for DFS CSV contract
- @entities/platforms/underdog-fantasy.md — BBM extension lessons; **defer** pick'em overlay

## Raw Concept

**CLI + CSV contract** for a future standalone pick'em repo (tentative *CeminiPick*). No browser extension until CLI walk-forward grades positive.

## Narrative

### Repo boundary

| Location | Contents |
|----------|----------|
| `gambling-wiki` | Research, specs, platform pages (this page) |
| `CeminiDFS` | Salary-cap DFS only — **no pick'em modules** |
| New repo (post gate) | `prop-fair`, `prop-rank`, grader, `manual_lines` ingest |

### CLI surface (MVP)

```bash
# Single prop fair value
prop-fair --player "Patrick Mahomes" --stat pass_yds --line 275.5 \
  --season 2025 --week 1

# Batch rank from manual posted lines (default: Underdog)
prop-rank --lines manual_lines.csv --platform underdog --slip-size 2 \
  --out edges.csv

# PrizePicks (Phase-2 — second payout profile)
prop-rank --lines manual_lines.csv --platform prizepicks --slip-size 2 \
  --out edges.csv

# Optional: emit distribution for inspection
prop-fair --player "Travis Kelce" --stat rec_yds --line 62.5 --show-dist
```

| Command | Input | Output |
|---------|-------|--------|
| `prop-fair` | player, stat, line, week context | `fair_p_over`, `fair_p_under`, median, sigma |
| `prop-rank` | `manual_lines.csv` + platform payout profile | `edges.csv` ranked by edge or slip_ev |
| `prop-grade` | ledger + actuals | backtest report (Phase-1) |

### `edges.csv` schema (canonical)

| Column | Type | Description |
|--------|------|-------------|
| `slate_id` | str | e.g. `2025-w01-sun` |
| `platform` | str | `prizepicks` \| `underdog` |
| `player_key` | str | nflverse-compatible id |
| `player_name` | str | display |
| `stat_type` | str | canonical — @concepts/pickem-stat-type-mapping.md |
| `line` | float | posted line |
| `side` | str | `more` \| `less` |
| `fair_p` | float | P(win side) |
| `implied_p` | float | from payout table / leg multiplier |
| `edge` | float | `fair_p - implied_p` |
| `line_type` | str | `standard` \| `demon` \| `goblin` \| … |
| `captured_at` | iso | from manual log |
| `slip_ev` | float | optional — populated when stacking in `prop-rank` |
| `stack_partner_id` | str | optional — 2-leg same-game pair |

### Projection input (Phase-1 borrow)

**Do not fork CeminiDFS on day one.** Options:

1. **Copy-paste** stat distribution export from `ceminidfs project` CSV columns
2. **Thin package** `cemini-nfl-core` extract (later) — shared env/usage/dist only
3. **Subprocess** call CeminiDFS CLI if installed — document version pin

Required per-player fields for `prop-fair`:

`pass_yds_median`, `pass_yds_sd` (or full samples), same for rush/rec/TD stats per @concepts/pickem-stat-type-mapping.md.

### Payout profiles (config)

Platform-specific JSON in repo `config/payout_profiles/`:

**Ship order:** `underdog.json` (MVP) → `prizepicks.json` (Phase-2).

```json
{
  "platform": "underdog",
  "mode": "standard",
  "legs": 2,
  "multiplier": 3.5,
  "breakeven_per_leg": 0.5345
}
```

UD-specific: support `flex`, `scorcher`, and **shifted payout** when alt-line multipliers ≠ 1.0 (@entities/platforms/underdog-pickem.md). PP demon/goblin profile deferred to Phase-2.

Source tables: @entities/platforms/underdog-pickem.md (primary), @entities/platforms/prizepicks.md, @concepts/pickem-payout-and-breakeven.md.

### Extension (Phase-3 — deferred)

| Approach | Status | Notes |
|----------|--------|-------|
| Read-only overlay showing fair_p next to app line | **Defer** | Verify ToS per @concepts/pickem-legal-and-tos-posture.md |
| Auto-fill slip | **NO-GO** | ToS violation risk |
| BBM MV3 fork | **Do not** | Different DOM — @entities/platforms/underdog-fantasy.md §6–7 lessons only |

**Gate:** extension spike only after CLI `prop-grade` shows calibrated edges over one season.

### End-to-end flow

```text
nflreadpy + CeminiDFS dist borrow
    → prop-fair (per line)
    → prop-rank (batch)
    → edges.csv
    → operator manual entry on **Underdog** app (PP Phase-2 later)
    → pick ledger
    → prop-grade (weekly)
```

## Snippets

> "CLI shape: `prop-fair --player \"Mahomes\" --stat pass_yds --line 275.5`" [Source: @concepts/diy-nfl-pickem-props-tool-architecture.md]

> "Extension: defer until CLI graded" [Source: K147 Phase-0 engineering checklist]
