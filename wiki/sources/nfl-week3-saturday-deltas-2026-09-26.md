---
title: "NFL Week 3 Saturday lock-day deltas (2026-09-26)"
type: source
tags: [source, nfl, dfs, week-3, saturday-lock, k177]
keywords: [ten-nyg-wind, lucas-oil-roof-open, t-90, theme-freeze, scratch-frozen]
related:
  - entities/sports/nfl-betting.md
  - concepts/free-slate-context.md
  - concepts/dfs-weather-adjustments.md
  - concepts/nfl-weekly-slate-hub-workflow.md
  - sources/nfl-week3-dfs-research-2026-09-26.md
  - sources/daily-digest-batch-k177-2026-09-28.md
  - meta/nfl-gemini-weekday-prompt-addendum.md
maturity: draft
read_status: skimmed
created: 2026-09-28
updated: 2026-09-28
location: cemini-egress-fi:/opt/cemini-bulk/research/gambling/NFL Main Slate Saturday Deltas.docx
phase_0_verdict: REFERENCE 2026-09-26 — Saturday-only deltas; verify T-90 inactives Sunday
wire_status: policy_wired
cross-wiki-source: "briefs/2026-w03-slate-hub-sun.md"
---

## Relations

- @sources/nfl-week3-dfs-research-2026-09-26.md — Friday env + stack card; this doc is **Sat deltas only**
- Gitignored hub: `briefs/2026-w03-slate-hub-sun.md`
- CeminiDFS / Parlays: `2026-09-28_w03-sat-lock-hub.md`

## Raw Concept

| Field | Value |
|-------|-------|
| **File** | `NFL Main Slate Saturday Deltas.docx` |
| **sha256** | `826a9d0cdac453cb…` |
| **Type** | Gemini Deep Research — Saturday lock checklist (13-game FanDuel main) |
| **Phase-0** | **REFERENCE** — operator slate; no new tool |
| **Wire** | `policy_wired` — nfl-betting, free-slate-context |

## Saturday forecast deltas

| Game | Sat vs Fri | Action |
|------|------------|--------|
| **TEN @ NYG** | Wind advisory — sustained **21–25 mph**, gusts **~47 mph**, **~90%** rain [CONFIRMED NWS] | Rush lean · pass caution · bar deep passing / first-TD props |
| **HOU @ IND** | Lucas Oil roof + window **OPEN** [CONFIRMED] | Open-air default; mild Indy weather |
| **BAL @ DAL** | Retractable roof **uncalled** | `weather_exposed=true` until venue posts |
| BUF / CLE / PIT outdoor | ~10–13 mph, low precip | No Sat flip vs Fri |
| DET, NO | Fixed dome | No weather exposure |

## Saturday injury / walkthrough (no scratch overturn)

| Player | Sat note | Action |
|--------|----------|--------|
| **Brock Bowers** | Rehab plan; traveled; **Q** — GTD screen | Unticketed in core builds until active |
| **Zay Flowers** | LP Fri; **Q**; snap cap if active | T-90 ~14:55 ET |
| **Michael Pittman Jr.** | LP week; **Q** foot | T-90 ~11:30 ET |
| **Keon Coleman** | **Q** ankle; 50/50 [TENTATIVE] | T-90; BUF TE/slot pivot if OUT |
| **Tyjae Spears** | **Q**; no Sat progression | Pollard volume if OUT |
| **Tyson Campbell** | **Q** | NE boundary bump if OUT — secondary |
| **Sam Darnold** | Cleared; no Sat setback | SEA starter @ WAS |

## Scratch repository (frozen to Fri + Sat doc)

Pierce (IR) · Brooks (IR) · Dart (OUT) · Daniels (OUT) · Onwenu (IR) · **Collins (OUT)** · **Dowdle (OUT)** · **Jenkins (OUT)** — no CSV write in wiki; operator before `ceminidfs run`.

## Theme freeze (six lanes)

| Lane | Verdict |
|------|---------|
| **BAL @ DAL** | Stack keep — late window; Flowers Q with swap plan |
| **BUF pass + LAC bring-back** | Stack keep — McConkey full Fri; Coleman Q |
| **LV @ NO** | Stack keep — **no Bowers** in primary stack |
| **SEA @ WAS** | Fade WAS pass (Mariota · low ITT) |
| **TEN @ NYG** | Fade game stacks — wind + Winston/Dart |
| **CIN @ PIT** | Fade PIT pass — Dowdle OUT · Pittman Q |

Exclude from main export: **ATL@GB**, **LAR@DEN**, **PHI@CHI** (not 13-game main).

## Operator rules [from docx]

- FanDuel CSV: **13 main contests only**
- **CeminiDFS before Parlays** — same inactive set
- Parlay cap: **≤2 legs per market**; no same-game first-TD correlation spam
- **No Week 2 retune**

## Snippets

> "MetLife … sustained northeast airflow of 21–25 mph with gusts reaching 47 mph … strict bar on deep-passing and first-touchdown markets." [Source: NFL Main Slate Saturday Deltas.docx, 2026-09-26]
