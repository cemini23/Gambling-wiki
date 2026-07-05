---
title: Pick'em operator workflow
type: concept
tags: [concept, pickem, props, nfl, workflow, w-workflow, k147]
keywords: [pre-slate, batch-rank, manual-entry, injury-latency, live-defer]
related:
  - concepts/diy-nfl-pickem-props-tool-architecture.md
  - concepts/dfs-injury-and-news-workflow.md
  - concepts/pickem-data-sources.md
  - concepts/pickem-pipeline-integration-spec.md
  - concepts/pickem-slip-ev-and-correlation.md
  - concepts/bankroll-management.md
  - entities/platforms/prizepicks.md
  - entities/platforms/underdog-pickem.md
maturity: draft
created: 2026-07-05
updated: 2026-07-05
---

## Relations

- @concepts/dfs-injury-and-news-workflow.md — shared injury cadence; pick'em lines move faster on OUT tags
- @concepts/pickem-data-sources.md — manual posted-line capture schema
- @concepts/pickem-pipeline-integration-spec.md — `edges.csv` output consumed here

## Raw Concept

**Operator cadence** for using a DIY pick'em fair-value tool without platform APIs: pre-slate batch ranking as primary mode; live in-game deferred until CLI is graded.

## Narrative

### Primary mode: pre-slate batch (MVP)

```text
T-24h  → cemini project (or borrow CeminiDFS distributions)
T-90m  → injury/news pass (@concepts/dfs-injury-and-news-workflow.md)
T-60m  → operator screenshots / types posted lines into manual_lines.csv
T-45m  → prop-fair rank → edges.csv sorted by slip_ev
T-30m  → operator builds 2–3 slips manually on **Underdog** app; log entries in pick ledger
```

| Step | Owner | Output |
|------|-------|--------|
| Project | CLI | per-player stat distributions |
| Capture lines | Operator | `manual_lines.csv` with `captured_at` |
| Rank | CLI | `edges.csv` — fair_p, implied_p, edge, optional 2-leg stacks |
| Enter | Operator | App slip builder — **no auto-submit** |
| Ledger | Operator | Date, platform, legs, stake, result |

**Why batch first:** pick'em lounges have no licensed export API; manual capture is the bottleneck. Batch ranking once per main slate (Sun 1pm / SNF / MNF) matches operator W8 NFL rhythm.

### Live / in-game (defer Phase-2)

| Challenge | Why defer |
|-----------|-----------|
| Line refresh latency | Posted lines move on scoring events; manual capture cannot keep pace |
| Live stat boards | PrizePicks Live Squares / in-game boards — different payout rules |
| Injury during game | DNP/reboot rules platform-specific |
| Model inputs | In-game projections need drive-level updates not in MVP |

**Gate:** enable live workflow only after **≥1 season** walk-forward on pre-game batch edges (@concepts/pickem-backtesting-framework.md).

### Injury latency

Pick'em lines often **pull or reprice** within minutes of official OUT tags — faster than some DFS salary locks.

| Signal | Action |
|--------|--------|
| Official inactive (90m) | Re-run rank; drop affected legs from `edges.csv` |
| Questionable | Flag `[Q]` in manual log; reduce Kelly stake or skip |
| Late scratch after capture | Do not bet stale edge; re-capture line if still posted |

Reuse CeminiDFS injury loaders where possible; pick'em-specific rule: **void if DNP** varies by platform (@entities/platforms/prizepicks.md reboot rules, @entities/platforms/underdog-pickem.md void tiers).

### Manual line entry UX

Minimum viable capture (spreadsheet or CSV):

| Column | Required | Notes |
|--------|----------|-------|
| `platform` | yes | `prizepicks` \| `underdog` |
| `player_name` | yes | Normalize to nflverse id in CLI |
| `stat_type` | yes | @concepts/pickem-stat-type-mapping.md |
| `line` | yes | Posted number |
| `side` | yes | `more` \| `less` |
| `line_type` | no | `standard` \| `demon` \| `goblin` \| `scorcher` |
| `captured_at` | yes | ISO timestamp — backtest cutoff |
| `slip_multiplier` | no | If demon/goblin shifted — use app-displayed value |

**Tip:** photograph app screen with timestamp in filename for audit trail; type into CSV once.

### Platform rollout (locked 2026-07-05)

| Phase | Platform | Notes |
|-------|----------|-------|
| **MVP** | **Underdog Pick'em** | Default for all sessions — operator already on app for BBM7 |
| **Phase-2** | PrizePicks | Add when UD CLI graded; demon/goblin alt lines |
| **Benchmark** | Hard Rock / Odds API | Not lounge UX |

Capture `platform: underdog` in `manual_lines.csv` unless explicitly cross-shopping PP lines for comparison.

### Bankroll hygiene

- **Separate pool** from DFS GPP and BBM entries — @concepts/bankroll-management.md
- Size slips via fractional Kelly on **whole slip** — @concepts/pickem-slip-ev-and-correlation.md
- Cap daily lounge exposure; pick'em variance is high on 2-leg power plays

## Snippets

> "Pre-slate batch rank vs in-game live (live = harder; defer?)" [Source: @concepts/diy-nfl-pickem-props-tool-architecture.md Phase-0 checklist]
