---
title: "NFL Week 2 Sunday main slate — env + personnel analysis (2026-09-18)"
type: source
tags: [source, nfl, dfs, week-2, weather, k172]
keywords: [environment-card, implied-team-total, stack, roof, nico-collins, kyler-murray]
related:
  - entities/sports/nfl-betting.md
  - concepts/free-slate-context.md
  - concepts/dfs-weather-adjustments.md
  - concepts/nfl-weekly-slate-hub-workflow.md
  - sources/daily-digest-batch-k172-2026-09-18.md
  - sources/brief-k172-w02-env-rss-2026-09-18.md
  - meta/daily-research-digest-cadence.md
maturity: draft
read_status: skimmed
created: 2026-09-18
updated: 2026-09-18
location: cemini-egress-fi:/opt/cemini-bulk/research/gambling/NFL Week 2 Slate Analysis.docx
phase_0_verdict: REFERENCE 2026-09-18 — Week 2 env/personnel snapshot; verify live before bet/contest
wire_status: policy_wired
cross-wiki-source: "briefs/2026-w02-slate-hub-sun.md"
---

## Relations

- @entities/sports/nfl-betting.md — Week 2 Sunday main slate
- @concepts/free-slate-context.md — env card / roof / wind inputs
- @concepts/dfs-weather-adjustments.md — SoFi semi_open confirmed
- Gitignored hub: `briefs/2026-w02-slate-hub-sun.md`
- CeminiDFS steal: `../CeminiDFS/briefs/2026-09-19_w02-fri-env-steals-from-analysis.md`

## Raw Concept

| Field | Value |
|-------|-------|
| **File** | `NFL Week 2 Slate Analysis.docx` |
| **sha256** | `7ae5c80bf7553953…` (preingest 2026-09-19) |
| **Type** | Operator / research dossier — env card + ITT + stack hygiene |
| **Phase-0** | **REFERENCE** — Friday close; verify roofs/inactives Sunday |
| **Wire** | `policy_wired` — nfl-betting + free-slate-context |

## Narrative

**13-game** Sunday main slate env card. Retractable roofs stay **tentative** until ~90 min pre-kick declaration. **SoFi (LV@LAC)** = **semi_open**, `weather_exposed=false` [CONFIRMED per docx].

### Environment flags [TENTATIVE — verify Saturday prefetch]

| Risk | Venue / game |
|------|----------------|
| **Heat** | PHI@TEN — 96°F, heat index ~108°F |
| **Rain/wind** | GB@NYJ — 70–80% precip, gusts to 15 mph |
| **Highest total** | WAS@DAL — **50.5**, DAL −4 |

### Stack hygiene (Friday close)

| Game | Posture | Driver |
|------|---------|--------|
| **WAS@DAL** | **Keep** | 50.5 total; narrow spread |
| **CIN@HOU** | **Fade** | Nico Collins OUT; total 46.0; HOU ITT 24.25 |
| **MIN@CHI** | **Jefferson solo** | Murray OUT → Wentz; fade full MIN stack |
| **ATL pass** | **Fade** | Penix OUT; Rush starts; ATL ITT 20.50 |
| **MIA@SF** | **Fade stacks** | SF −13.5; MIA ITT 15.75 |
| **PIT@NE** | **Fade** | Total 41.5; Pittman Q; rain Foxborough |

### Personnel [TENTATIVE — Sunday inactives]

- **OUT:** Nico Collins (hamstring); Kyler Murray (concussion) → Wentz
- **Doubtful:** Zay Flowers, Brock Bowers
- **Active:** Alvin Kamara (full Friday)
- **Watch:** Pittman (foot), McConkey (ribs), roof calls ATL/HOU/ARI/DAL

**Do not** auto-lineup or auto-bet. Pair with gitignored `briefs/2026-w02-slate-hub-sun.md`.

## Snippets

> "SoFi Stadium features an open-air perimeter beneath a fixed canopy roof, classifying the venue as semi-open and sheltered from direct precipitation and surface wind exposure." [Source: NFL Week 2 Slate Analysis.docx]

> "Washington at Dallas … highest total on the board at 50.5 points, paired with a narrow 4.0-point spread." [Source: same]

## Dead Ends

- Treating Friday ITT as live without re-checking Sunday boards
- Full-game stacks in MIA@SF or PIT@NE on tournament builds
