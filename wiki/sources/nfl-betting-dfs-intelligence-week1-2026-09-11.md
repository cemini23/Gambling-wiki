---
title: "NFL Week 1 Sunday slate betting & DFS intelligence dossier (2026-09-11)"
type: source
tags: [source, nfl, dfs, sports-betting, week-1, k170]
keywords: [implied-team-total, proe, reverse-line-movement, gpp, vacated-volume, trench]
related:
  - entities/sports/nfl-betting.md
  - entities/platforms/fanduel.md
  - entities/platforms/draftkings.md
  - entities/platforms/hard-rock-bet.md
  - concepts/nfl-weekly-slate-hub-workflow.md
  - concepts/dfs-injury-and-news-workflow.md
  - sources/brief-k169-nfl-week1-ready-2026-08-31.md
  - sources/daily-digest-batch-k170-2026-09-11.md
  - sources/brief-k170-week1-papers-rss-2026-09-11.md
  - meta/daily-research-digest-cadence.md
maturity: draft
read_status: skimmed
created: 2026-09-11
updated: 2026-09-11
location: cemini-egress-fi:/opt/cemini-bulk/research/gambling/NFL Betting and DFS Intelligence (1).docx
phase_0_verdict: REFERENCE 2026-09-11 — Week 1 slate snapshot; verify live before bet/contest
wire_status: policy_wired
cross-wiki-source: "@osint-wiki/sources/nfl-betting-dfs-intelligence-2026-09-08.md"
---

## Relations

- @entities/sports/nfl-betting.md — Week 1 market baselines and sharp signals
- @entities/platforms/fanduel.md — GPP pricing inefficiencies
- @sources/brief-k169-nfl-week1-ready-2026-08-31.md — prior roster hub
- @osint-wiki/sources/nfl-betting-dfs-intelligence-2026-09-08.md — prior hash (K257); this docx is a **new sha256**
- Gitignored brief: `briefs/2026-09-11_nfl-week1-slate-hub.md`

## Raw Concept

| Field | Value |
|-------|-------|
| **File** | `NFL Betting and DFS Intelligence (1).docx` |
| **sha256** | `7bd023bb3d2a33a8…` (preingest 2026-09-11) |
| **Type** | Operator / research dossier — not a tool eval |
| **Dual-ID** | Gambling K170 ≠ OSINT K257 (2026-09-08 prior docx hash) |
| **Phase-0** | **REFERENCE** — snapshot numbers; verify live books/salaries |
| **Wire** | `policy_wired` — slate hub brief only; no auto-bet |

## Narrative

Thirteen-game **Sunday slate** dossier covering market baselines, reverse line movement (RLM), pace/PROE shootout environments, vacated volume, trench mismatches, and GPP pricing inefficiencies.

### Sharp / market signals [TENTATIVE — verify live]

| Signal | Detail |
|--------|--------|
| **BUF @ HOU RLM** | Opened BUF -1.5; 76% tickets on BUF; line moved to **HOU -1.5** (3-pt flip) |
| **CHI @ CAR total** | 43% tickets Over vs **92% handle** Over; total 45.5 → **47.5** |
| **GB @ MIN Under** | 44% tickets vs **87% handle** on Under 46.5 |
| **ARI @ LAC dog** | +11.5 → +10.0; 36% tickets vs 62% handle on ARI |

### Shootout environments [TENTATIVE]

| Game | Total | Pace / PROE |
|------|-------|-------------|
| **TB @ CIN** | 50.5 | 26.2 sec/snap; PROE +6.5% |
| **NO @ DET** | 50.5 | Dome; DET ITT 28.75 |
| **CHI @ CAR** | 47.5 | 26.5 sec/snap; sharp Over handle |

### GPP pricing inefficiencies [TENTATIVE — salaries frozen since late July]

| Player | Role | DK / FD |
|--------|------|---------|
| Travis Etienne Jr. | NO lead back (Kamara MCL) | $5,900 / $6,400 |
| MarShawn Lloyd | GB lead (Jacobs exempt) | $4,800 / $5,400 |
| Devaughn Vele | NO perimeter (88% route rate) | $3,500 / $4,800 |
| Matthew Golden | GB boundary X | 92% route rate |

**Post-kickoff injury updates (RSS K170):** A.J. Brown high-ankle (~4 weeks); Sam Darnold hip absence; Tua oblique day-to-day; Cooper Rush may start ATL@PIT; Jake Tonges MCL (prop refund question).

**Do not** auto-lineup, auto-bet, or treat dossier numbers as live without verification.

## Snippets

> "The most pronounced Reverse Line Movement on the slate occurs in Buffalo at Houston … a net 3.0-point market move against the public." [Source: NFL Betting and DFS Intelligence (1).docx Module A]

> "Operator salaries for Week 1 were released in late July and remained frozen despite subsequent training camp developments." [Source: same, Module D]

## Dead Ends

- Treating frozen July salaries as current without platform refresh
- Auto-betting RLM signals without confirming current line at Hard Rock / other books
