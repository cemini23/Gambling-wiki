---
title: "NFL Week 3 DFS research — Friday env card (2026-09-26)"
type: source
tags: [source, nfl, dfs, week-3, friday-env, k177]
keywords: [itt-table, designation-deltas, stack-keep, stack-fade]
related:
  - entities/sports/nfl-betting.md
  - sources/nfl-week3-scheme-breakdown-2026-09-23.md
  - sources/nfl-week3-saturday-deltas-2026-09-26.md
  - sources/daily-digest-batch-k177-2026-09-28.md
  - concepts/dfs-strategy-overview.md
maturity: draft
read_status: skimmed
created: 2026-09-28
updated: 2026-09-28
location: cemini-egress-fi:/opt/cemini-bulk/research/gambling/NFL Week 3 DFS Research.docx
phase_0_verdict: REFERENCE — Friday baseline; supersede weather rows with Sat deltas source
wire_status: policy_wired
---

## Relations

- @sources/nfl-week3-saturday-deltas-2026-09-26.md — **authoritative** for Sat weather/roof flips
- Salary export: `week 3.csv` archived with batch (operator; not in git)

## Raw Concept

| Field | Value |
|-------|-------|
| **File** | `NFL Week 3 DFS Research.docx` |
| **sha256** | `e1470e0f9ea19886…` |
| **Type** | Gemini — Friday ITT, designation deltas, stack card |

## Friday designation deltas (Sun main)

| Player | Fri tag | DFS action |
|--------|---------|------------|
| Nico Collins | OUT | Scratch |
| Rico Dowdle | OUT | Scratch |
| Teven Jenkins | OUT | Scratch |
| Brock Bowers | Q | Warn — exclude from primary LV stack |
| Zay Flowers | Q | Warn / late swap |
| Michael Pittman Jr. | Q | Warn |
| Keon Coleman | Q | Warn |
| Aaron Jones | Active (FP) | Stack keep |
| Tony Pollard | Active (FP) | Stack keep / TEN ground |
| Sam Darnold | Named starter | WAS fade still (Mariota home) |

## ITT samples [TENTATIVE — verify live books]

| Game | Spread / total | Note |
|------|----------------|------|
| TEN @ NYG | NYG −2.5 / **39.5** | Slate-low total |
| SEA @ WAS | SEA −7.5 / 40.0 | WAS ITT ~16.25 |
| BAL @ DAL | Wed baseline BAL −3.5 / **52.5** | Highest total on board |

Many rows in export marked **NO_EVIDENCE** for Fri citations — do not size off blank ITT cells.

## Stack card (matches Sat freeze)

Keep: BAL@DAL · BUF+LAC · LV@NO (without Bowers).  
Fade: WAS pass · TEN@NYG · PIT pass.

Weather-by-market (Fri): TEN@NYG wind/rain supports Pollard rush overs; bar deep passing overs — **upgrade wind severity per Sat deltas source**.
