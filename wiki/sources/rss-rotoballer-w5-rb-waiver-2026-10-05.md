---
title: "RotoBaller Week 5 RB waiver wire — handcuff tiers and rostered thresholds (2026-10-05)"
type: source
tags: [source, rss, nfl, week-5, fantasy, waiver-wire, k181]
keywords: [ollie-gordon, emanuel-wilson, keaton-mitchell, kendre-miller, handcuffs, rostered-percent, faab]
related:
  - concepts/season-long-fantasy-waiver-wire.md
  - entities/sports/nfl-betting.md
  - concepts/player-usage-models.md
  - sources/daily-digest-batch-k181-2026-10-06.md
maturity: draft
read_status: deep-read
created: 2026-10-06
updated: 2026-10-06
location: cemini-egress-fi:/opt/cemini-bulk/research/gambling/rss-rotoballer-2026-10-05-running-back-fantasy-football-waiver-wire-pickups-for-week-5.md
phase_0_verdict: REFERENCE — free column; method and tier structure, not selections
wire_status: policy_wired
---

## Relations

- @concepts/season-long-fantasy-waiver-wire.md — the concept this seeds
- @concepts/player-usage-models.md — snap/target/carry share as the underlying measure
- @entities/sports/nfl-betting.md — W8 season lane
- @sources/daily-digest-batch-k181-2026-10-06.md — K181 hub

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | Running Back Fantasy Football Waiver Wire Pickups for Week 5 |
| **Author** | Phil Clark |
| **Feed** | RotoBaller (`rotoballer`) |
| **Published** | 2026-10-05 |
| **Access** | Free column; site body truncated on fetch, tiers recovered via Brave LLM Context |

## Narrative

### The tier structure

RotoBaller splits the waiver board into five bands. The banding is the transferable part — it maps a pickup decision to **how much of the backfield is already claimed**.

| Band | Players (team · % rostered) |
|------|------------------------------|
| **Top priorities** | Ollie Gordon II (MIA · 62%) · Emanuel Wilson (SEA · 45%) · Tank Bigsby (PHI · 28%) · Keaton Mitchell (LAC · 35%) · Kendre Miller (NO · 14%) |
| **Secondary** | Austin Ekeler (WAS · 3%) · Zach Charbonnet (SEA · 60%) · Kaelon Black (SF · 42%) · Samaje Perine (CIN · 3%) · Woody Marks (HOU · 55%) |
| **High-upside handcuffs** | Mike Washington Jr. (LV · 35%) · Brian Robinson Jr. (ATL · 30%) · Emmett Johnson (KC · 31%) · Seth McGowan (IND · 1%) · Najee Harris (NYG · 6%) · Tyler Goodson (DAL · 0%) |
| **Also consider** | Chris Rodriguez Jr. (JAX · 38%) · Tyjae Spears (TEN · 28%) · Sione Vaki (DET · 1%) |
| **Add anywhere still available (>60%)** | Kyle Monangai (CHI · 82%) · Braelon Allen (NYJ · 80%) |

### The reasoning shape

The column reads **snap share and route participation**, not just carries — the same inputs as `@concepts/player-usage-models.md`. Example usage lines published in the companion all-positions column:

| Player | Snaps | Carries | Routes | Targets |
|--------|-------|---------|--------|---------|
| Emanuel Wilson (SEA) | 59% | 21 | 8 | 4 (120 yds, 2 TD) |
| Tank Bigsby (PHI) | 48% | 14 | 8 | 1 (55 yds) |
| Will Shipley (PHI) | 47% | 6 | 14 | 1 (23 yds) |
| Keaton Mitchell (LAC) | 38% | 10 | 13 | 6 (63 yds) |
| George Holani (SEA) | 38% | 7 | 9 | 1 (20 yds) |
| Kimani Vidal (LAC) | 37% | 5 | 14 | 3 (36 yds, TD) |

**Wilson is the clearest case:** a 59% snap share with 21 carries and 4 targets is a **lead role**, not a committee share. That is what separates the top band from the handcuff band.

**The distinction the column draws:** a **handcuff** is a back whose value is contingent on an injury ahead of him (Emmett Johnson behind KC's starter, Tyler Goodson at 0% rostered). An **RB3/RB4 with upside** already has a route to touches — Woody Marks is described as trending toward a **50/50 committee** with Montgomery, giving him RB4 value with RB3 upside if Montgomery is hurt.

**FAAB guidance (companion column):** the dollar bins name Tyjae Spears (may become 1A if Tony Pollard is traded), Austin Ekeler (split early work while Rachaad White returns to practice), Chris Rodriguez Jr. (a TD-plunge dart), Jaylen Wright, and Tyler Allgeier.

### Injury context

The Week 5 waiver week is shaped by a broad injury wave — the companion rankings column names **Saquon Barkley, DJ Moore, Ladd McConkey, Rashee Rice, Tee Higgins, and Lamar Jackson**. Miami's De'Von Achane went on IR 2026-09-28 with a torn ACL (recorded in @sources/rss-lsb-week4-game-cards-2026-10-02.md), which is what opens Ollie Gordon II's path.

## Snippets

> "Marks should be viewed as an RB4 with RB3 upside if Montgomery gets hurt… this is trending toward a 50/50 committee." [Source: RotoBaller Week 5 all-positions column, 2026-10-05]

## Dead Ends

- **Season-long fantasy is not a wagering lane.** This wiki's bankroll lanes are sportsbook, DFS, and prediction markets. Waiver pickups inform DFS priors; they are not a bet.
- **Rostered percentages move fast.** The counts are a snapshot from 2026-10-05. Do not treat them as current.
- **Do not import the selections.** The transferable content is the **tier structure** and the **snap-share reading**, not the names.
- Site body was truncated on fetch; the tier tables came via Brave LLM Context. Treat the percentages as [TENTATIVE].
