---
title: "NFL Week 4 Saturday lock — weather moderation + Nico Collins cleared (2026-10-03)"
type: source
tags: [source, nfl, week-4, weather, injury, dfs, k181]
keywords: [tampa-wind-lifted, baltimore-rain, nico-collins-cleared, nrg-roof, jayden-daniels-out, itt-refresh]
related:
  - entities/sports/nfl-betting.md
  - sources/nfl-week4-slate-env-2026-10-02.md
  - sources/nfl-week4-practice-reports-2026-10-01.md
  - sources/nfl-week4-tnf-result-postmortem-2026-10-02.md
  - meta/research-input-pipeline.md
  - sources/daily-digest-batch-k181-2026-10-06.md
maturity: draft
read_status: deep-read
created: 2026-10-06
updated: 2026-10-06
location: cemini-egress-fi:/opt/cemini-bulk/research/gambling/NFL Saturday Lock-Day Deltas Research.docx
phase_0_verdict: REFERENCE — final Gemini Deep Research artifact before the 2026-10-04 retirement
wire_status: policy_wired
---

## Relations

- @entities/sports/nfl-betting.md — W8 season lane
- @sources/nfl-week4-slate-env-2026-10-02.md — Friday card this page corrects
- @meta/research-input-pipeline.md — the pipeline this artifact was retired in favour of
- Gitignored hub: `briefs/2026-w04-slate-hub-sun.md`

## Raw Concept

| Field | Value |
|-------|-------|
| **File** | `NFL Saturday Lock-Day Deltas Research.docx` |
| **sha256** | `baef1a1ce567a10c…` |
| **Type** | Gemini Deep Research — Saturday prefetch deltas |
| **Status** | **Last Gemini artifact.** Gemini was retired from the weekly research 2026-10-04 |
| **Captured** | 2026-10-03 14:00–15:09 EDT |

## Narrative

### Weather — two cautions lifted

| Game | Friday | Saturday | Effect |
|------|--------|----------|--------|
| **GB @ TB** | 25 mph sustained | **6–8 mph ESE**, 60% precip (after 2 p.m.), 90°F | **Pass caution lifted.** Sustained wind falls below the 10 mph review threshold |
| **ARI @ NYG** | 11 mph | **9 mph NE**, 40% precip, 64°F | **Pass caution lifted.** Rain noted for secondary review |
| **TEN @ BAL** | 8 mph, 81% precip | 7 mph E, **40–60%** precip (tapering before 3 p.m.), 66°F | Rain recedes. Low-friction rush profile sustained |
| IND @ WAS (London) | 6 mph, gusts 15 | 5 mph SW, gusts <10, 10% precip, 70°F | Clear passing and kicking conditions |
| **DAL @ HOU** | NO_EVIDENCE | **Retractable; no league roof call** | Stays exposed `[TENTATIVE]` |
| NE @ BUF · NYJ @ CHI · JAX @ CIN · LAR @ PHI · LAC @ SEA · DEN @ SF | baseline | no confirmed Saturday flip | 5–9 mph holds |
| MIA @ MIN · KC @ LV | dome | dome | wind excluded |

**The Tampa Bay and MetLife pass cautions are lifted.** The Friday card had both games on a review note; those notes no longer apply. The team-level pass **fades** do not change — they were personnel-driven, not wind-driven.

### The Collins correction

**Nico Collins is CLEARED.** The Friday environment card carried him as OUT, sourced from a third-party aggregator (DraftEdge, not a club page). Saturday: he **practised fully on Friday** and was **omitted from the Texans' official game-status report**. He is upgraded to active pool eligibility `[CONFIRMED]`.

This is the exact failure mode `@meta/research-input-pipeline.md` cites as a reason the Gemini prose layer was retired: "The Friday hub had Nico Collins OUT on a DraftEdge-only cite; the Saturday club check cleared him."

### Other Saturday personnel

| Player | Team | Status | Ripple |
|--------|------|--------|--------|
| Jayden Daniels | WAS | **OUT** (elbow dislocation) | Mariota took first-team walkthrough reps in Watford, but the **QB cell stays open** `[TENTATIVE]` — no premature closure |
| Caleb Williams | CHI | **OUT** (club ledger) | Starter unassigned between Bagent and Keenum; revealed **90 minutes before kickoff**. Cell stays open |
| Baker Mayfield | TB | **OUT** (thumb dislocation) | **Tampa Bay QB cell stays entirely unfilled.** No backup assigned |
| Jaxson Dart | NYG | IR | Winston remains first-team |
| Sam Cosmi | WAS | **OUT** (concussion protocol, did not travel) | — |
| NE right guard | NE | **Open** | Ben Brown worked extensively with the starters; Walter Rouse remains an option. Not hardcoded |
| Justin Jefferson | MIN | **OUT** (ankle) | — |
| **Brock Bowers** | LV | **Unlisted** on the final report | Eligible; bring-back tied to gameday active filing |
| Bucky Irving | TB | Questionable | Stays in pool |
| D'Andre Swift (CHI), Chris Godwin (TB) | — | Full practice | **Does not lift** the baseline team passing fades |

**Suppressed strings** (corrupted third-party pairings, do not carry): Pittman Jr.→Pittsburgh, A.J. Brown→New England, Goedert→Chicago news, Zay Flowers→support caches, Ted Hurst snap logs.

### Saturday ITT refresh

| Game | Spread | Total | Move vs Friday |
|------|--------|-------|----------------|
| IND @ WAS | IND −3.5 | **47.5** | total −1.0 |
| ARI @ NYG | ARI −2.5 | **43.5** | total −1.0 |
| TEN @ BAL | BAL −11.5 | 42.5 | unchanged |
| NE @ BUF | **BUF −7.0** | 48.5 | spread widened 0.5 |
| NYJ @ CHI | CHI −3.5 | 42.5 | unchanged |
| JAX @ CIN | CIN −2.5 | **51.5** | unchanged (slate high) |
| DAL @ HOU | **HOU −2.5** | 47.5 | spread +0.5 |
| LAR @ PHI | **LAR −3.0** | 43.5 | spread +0.5 |
| GB @ TB | GB −3.5 | 38.5 | unchanged |
| MIA @ MIN | **MIN −10.5** | 38.5 | tightened from −11.5 |
| KC @ LV | KC −4.5 | 47.5 | unchanged |
| LAC @ SEA | SEA −7.0 | **42.5** | unchanged |
| DEN @ SF | **SF −2.5** | 47.5 | tightened from −3.0 |

### Stack context — six themes held

**Keeps:** JAX @ CIN (slate-high 51.5, low wind) · BUF passing (NE secondary depleted) · KC @ LV (conditional; Bowers unlisted makes him pool-eligible, bring-back needs gameday verification).

**Fades:** MIN passing (Jefferson out, 38.5 total) · CHI passing (Williams out, starter unannounced) · TB passing (Mayfield out, 38.5 total).

### T-90 watch list

Jayden Daniels (08:00 ET) · Bucky Irving, Tyjae Spears, Zay Flowers, CHI starter (11:30) · Justin Jefferson (14:35) · Brock Bowers, Ladd McConkey, Mike Evans (14:55).

## Snippets

> "Collins, who was flagged as an external scratch via third-party aggregators, logged a full practice on Friday and was completely omitted from the Texans' official game-status report, confirming his availability against Dallas." [Source: NFL Saturday Lock-Day Deltas Research.docx, 2026-10-03]

> "Touchdown distributions must not assume exclusive goal-line conversion roles based solely on backfield partner absences." [Source: same — the TNF rule carried forward]

## Dead Ends

- **This artifact type is retired.** Gemini Deep Research weekday prompts were stopped 2026-10-04. Do not commission another. See @meta/research-input-pipeline.md.
- **Weather is a forecast, not a reading.** The card was pulled 14:00–15:09 EDT Saturday; re-check at lock.
- **NRG roof remains uncalled** — the `[TENTATIVE]` tag is correct; do not assume closure.
- **The Collins flip is the page's most important line.** A third-party OUT was wrong; the club report cleared him. Prefer club filings over aggregators for status.
