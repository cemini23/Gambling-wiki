---
title: "NFL Week 2 Saturday lock-day deltas (2026-09-19)"
type: source
tags: [source, nfl, dfs, week-2, saturday-lock, k173]
keywords: [pittman-out, porter-out, nws-weather, t-90, theme-freeze]
related:
  - entities/sports/nfl-betting.md
  - concepts/free-slate-context.md
  - concepts/dfs-weather-adjustments.md
  - concepts/nfl-weekly-slate-hub-workflow.md
  - sources/nfl-week2-slate-env-analysis-2026-09-18.md
  - sources/daily-digest-batch-k173-2026-09-20.md
  - sources/brief-k173-w02-sat-lock-2026-09-20.md
  - meta/daily-research-digest-cadence.md
maturity: draft
read_status: skimmed
created: 2026-09-20
updated: 2026-09-20
location: cemini-egress-fi:/opt/cemini-bulk/research/gambling/NFL Week 2 Saturday Deltas.docx
phase_0_verdict: REFERENCE 2026-09-19 — Saturday-only deltas; verify T-90 inactives Sunday
wire_status: policy_wired
cross-wiki-source: "briefs/2026-w02-slate-hub-sun.md"
---

## Relations

- @sources/nfl-week2-slate-env-analysis-2026-09-18.md — Friday baseline; this doc is **deltas only**
- Gitignored hub: `briefs/2026-w02-slate-hub-sun.md`
- CeminiDFS: `../CeminiDFS/briefs/2026-09-19_w02-sat-lock-hub.md` + `config/2026-w02-sun-scratch.csv`

## Raw Concept

| Field | Value |
|-------|-------|
| **File** | `NFL Week 2 Saturday Deltas.docx` |
| **sha256** | `346aea1a5d65a43f…` |
| **Type** | Gemini Deep Research — Saturday lock checklist |
| **Phase-0** | **REFERENCE** — no new arXiv; operator slate only |
| **Wire** | `policy_wired` — nfl-betting, free-slate-context, hub |

## Saturday forecast deltas (NWS `[CONFIRMED]`)

| Game | Sat vs Fri | Action |
|------|------------|--------|
| GB @ NYJ | Rain/showers likely ~70% | Pass downgrade |
| MIN @ CHI | 12–14 mph, showers ~60% | Pass downgrade / slight run lean |
| PHI @ TEN | Heat advisory; index **105–107°F** | Heat note |
| PIT @ NE | ~**100%** precip, heavy rain | Pass downgrade — **fade PIT@NE** |
| Retractable (ATL, HOU, ARI, DAL) | Roof **uncalled** | `weather_exposed=true` until T-90 |
| LV @ LAC | SoFi **semi_open** | Not a wind fade |
| NO@BAL, CLE@TB, JAX@DEN, MIA@SF | No confirmed flip | No change |

## Saturday injury deltas

| Player | Sat status | Action |
|--------|------------|--------|
| Michael Pittman Jr. (PIT) | **OUT** (foot) | Scratch · fade PIT@NE |
| Joey Porter Jr. (PIT) | **OUT** (back) | Scratch |
| Tua (ATL) | Oblique · **Rush starts** | Fade ATL pass |
| Ladd McConkey (LAC) | **Q** (ribs) | T-90 ~14:35 ET |
| Brock Bowers (LV) | **D** | Treat out · Mayer |
| Zay Flowers (BAL) | **D** | Treat out · Andrews/Bateman |
| Murray / Darnold | OUT | Wentz / Lock starts (unchanged) |
| Kamara | Active off report | Split with Etienne — not workhorse |

## Theme freeze (no new stacks)

Keep: **WAS@DAL** · **Jefferson solo**  
Fade: **CIN@HOU** · **ATL pass** · **MIA@SF game stacks** · **PIT@NE**

## Snippets

> "Roster scratch list remains locked to Friday baseline … and Saturday additions (Michael Pittman Jr. OUT, Joey Porter Jr. OUT)." [Source: NFL Week 2 Saturday Deltas.docx, 2026-09-19]
