---
title: Pick'em stat type mapping (CeminiDFS → platform)
type: concept
tags: [concept, pickem, props, nfl, stat-mapping, w-stat-map, k147]
keywords: [pass-yards, rush-yards, receptions, combo-props, kicker, dst, prizepicks, underdog, ceminiidfs]
related:
  - concepts/diy-nfl-pickem-props-tool-architecture.md
  - concepts/dfs-stat-projection-engine.md
  - concepts/dfs-distribution-layer.md
  - concepts/pickem-fair-probability.md
  - concepts/pickem-data-sources.md
  - concepts/pickem-pipeline-integration-spec.md
  - entities/tools/ceminidfs.md
  - entities/platforms/prizepicks.md
  - entities/platforms/underdog-pickem.md
  - entities/sports/nfl-betting.md
maturity: draft
created: 2026-07-05
updated: 2026-07-05
---

## Relations

- @concepts/diy-nfl-pickem-props-tool-architecture.md — W-STAT-MAP layer (SA-07)
- @entities/tools/ceminidfs.md — projection output boundary; no pick'em code in repo
- @concepts/dfs-distribution-layer.md — per-stat marginals feed `P(stat > line)`

## Raw Concept

**Canonical mapping** from CeminiDFS counting-stat projections and distributions to PrizePicks / Underdog Pick'em stat menu entries. Goal: one internal stat ID per gradable prop type, with explicit combo and K/DST gap handling.

## Narrative

### Design principle

Pick'em lounges grade **raw counting stats** (yards, receptions, TDs) — not FanDuel half-PPR fantasy points. CeminiDFS `project` outputs must be **re-labeled and sometimes re-aggregated** before fair-probability math runs. Internal keys use snake_case; platform labels differ by operator.

### Core single-stat map (GO — direct reuse)

| Internal ID | CeminiDFS source | Typical PP / UD label | Distribution note |
|-------------|------------------|----------------------|-------------------|
| `pass_yds` | QB passing yards | Pass Yards | Skew-normal / lognormal tail |
| `pass_tds` | QB pass TD count | Pass TDs | Poisson / NB discrete |
| `pass_att` | QB attempts | Pass Attempts | Poisson-ish; lower volume |
| `pass_cmp` | QB completions | Completions | Derived from att × cmp% |
| `rush_yds` | RB/QB rush yards | Rush Yards | Gamma / skew-normal |
| `rush_att` | RB carries | Rush Attempts | Poisson / NB |
| `rec_yds` | WR/TE/RB rec yards | Receiving Yards | Hurdle-lognormal |
| `receptions` | WR/TE/RB catches | Receptions | Poisson / NB discrete |
| `rec_tds` | Any rec TD | Receiving TDs | Hurdle / Bernoulli mix |
| `rush_tds` | Any rush TD | Rushing TDs | Hurdle / Bernoulli mix |
| `anytime_td` | Rush + rec TD (0/1+) | Anytime TD | Bernoulli / hurdle sum |

**Grading rule:** `P(stat > line)` uses the **same stat definition the platform publishes** (e.g. gross pass yards, not net). Verify per platform Phase-0 checklist — @entities/platforms/prizepicks.md, @entities/platforms/underdog-pickem.md.

### Combo props (CONDITIONAL — aggregate before distribution)

Combo lines sum two or more counting stats on **one player**. Model must draw **jointly** or sum correlated marginals — not median(A) + median(B).

| Internal ID | Components | Example platform label | Modeling approach |
|-------------|------------|------------------------|-------------------|
| `rush_rec_yds` | `rush_yds` + `rec_yds` | Rushing + Receiving Yards | Sum of correlated draws from same player sim |
| `pass_rush_yds` | `pass_yds` + `rush_yds` | Passing + Rushing Yards | QB dual-threat; same-game correlation high |
| `fantasy_score` | Site-specific weights | Fantasy Score | **Defer** until platform formula documented — not FD scoring |

**Reference UI:** BettingPros combo prop pages (e.g. rush+rec yards) — cited in architecture reading queue.

**Implementation:** extend distribution layer with `combo_id → [component_ids, weights]`; Monte Carlo sum per iteration, then `P(sum > line)`.

### TD and binary props

| Internal ID | Graded as | CeminiDFS bridge |
|-------------|-----------|------------------|
| `pass_tds` | Integer count O/U | Poisson/NB from red-zone + volume |
| `anytime_td` | 0 vs 1+ (sometimes 2+) | P(TD ≥ 1) from rush+rec TD rates |
| `first_td` | Binary scorer | **GAP** — needs first-TD model or defer |
| `multi_td` | 2+ TDs | Tail of combined TD count |

### Kicker and DST gaps (NO-GO day one unless scoped)

CeminiDFS pipelineExecute projection stack is **skill-position centric**. Pick'em menus often list K and DST — treat as explicit gaps until models exist.

| Platform stat | CeminiDFS coverage | Verdict | Phase-1 workaround |
|---------------|-------------------|---------|-------------------|
| K — FG made | None | **GAP** | Manual fade / skip; or borrow team ITT → attempt model |
| K — kicking points | None | **GAP** | Same |
| K — PATs | None | **GAP** | Low priority |
| DST — sacks | None | **GAP** | Opponent pass-rate prior only |
| DST — points allowed | None | **GAP** | Implied team total inverse |
| DST — fantasy / combo | None | **GAP** | Skip until scoring rules documented |

**Operator rule:** rank only props with `mapping_status: GO` in `edges.csv`; flag `GAP` rows as non-actionable.

### Platform divergence matrix [NEEDS VERIFICATION]

Document per operator as Phase-0 completes:

| Internal ID | PrizePicks NFL | Underdog Pick'em | Notes |
|-------------|----------------|------------------|-------|
| `pass_yds` | [ ] | [ ] | Alt lines / demon-goblin variants |
| `rush_rec_yds` | [ ] | [ ] | Combo availability differs |
| `fantasy_score` | [ ] | [ ] | Weights may differ from DFS |
| K / DST menu | [ ] | [ ] | Often sparse vs NBA |

### CLI / schema contract

Stat IDs in @concepts/pickem-pipeline-integration-spec.md must match this page:

```text
prop-fair --player "Mahomes" --stat pass_yds --line 275.5
```

Posted lines CSV uses same `stat_id` column for join to projection export.

### Reuse from CeminiDFS (do not duplicate)

| Layer | Action |
|-------|--------|
| Usage → volume | **Direct** — drives att/rec/yds means |
| Game environment (ITT, pace) | **Direct** — team pass rate → QB yards |
| Position distributions | **Adapt** — discard FD scoring; keep counting stat marginals |
| Ownership, pydfs, FD CSV | **Skip** |

Future: thin `cemini-nfl-core` package exporting stat distributions only — see architecture reuse map.

## Snippets

> "Pick'em uses raw yards, TDs, combos — site-specific." [Source: @concepts/diy-nfl-pickem-props-tool-architecture.md reuse table]

> "Map stat types offered vs CeminiDFS projection outputs (yards, rec, TDs, combos, K/DST)." [Source: K147 Phase-0 checklist]
