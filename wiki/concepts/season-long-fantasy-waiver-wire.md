---
title: Season-long fantasy waiver wire
type: concept
tags: [concept, fantasy, waiver-wire, nfl, usage]
keywords: [waiver-wire, faab, handcuff, snap-share, route-participation, rostered-percent, tiering]
related:
  - concepts/player-usage-models.md
  - concepts/dfs-strategy-overview.md
  - concepts/best-ball-strategy.md
  - entities/sports/nfl-betting.md
  - sources/rss-rotoballer-w5-rb-waiver-2026-10-05.md
  - sources/daily-digest-batch-k181-2026-10-06.md
maturity: draft
created: 2026-10-06
updated: 2026-10-06
---

## Relations

- @concepts/player-usage-models.md — snap/target/carry share, the underlying measure
- @concepts/dfs-strategy-overview.md — DFS priors that share these inputs
- @concepts/best-ball-strategy.md — roster construction by a different mechanism (no waivers)
- @sources/rss-rotoballer-w5-rb-waiver-2026-10-05.md — seed source

## Raw Concept

Adding and dropping players on a season-long fantasy roster. The decision is **how much of a backfield (or target tree) is still unclaimed**, measured in snap share and route participation.

**Scope note:** season-long fantasy is **not a wagering lane** in this wiki. It informs DFS priors. It is not a bet.

## Narrative

### The tier logic

A waiver board is a **claim-percentage** problem. The column structure below is the transferable part — it maps a pickup to how much of the role is already taken.

| Band | What it means |
|------|---------------|
| **Priority add** | Already holds a lead role. Add in all leagues |
| **Secondary** | A real role, smaller or contested |
| **Handcuff** | Value is **contingent on an injury ahead of him**. Zero standalone value |
| **Also consider** | Deep-league or dart throws |
| **Add if available** | Rostered above ~60% but still worth a claim |

**The priority/handcuff line is the important distinction.** A back with a **59% snap share, 21 carries, and 4 targets** holds a lead role — that is a priority add. A back with a 20% share behind a healthy starter is a handcuff: the pickup only pays if the starter misses time.

### Read usage, not just carries

The inputs that separate the bands:

- **Snap share** — the primary filter. 50%+ is a role; under 30% is a contingency.
- **Route participation** — a back who runs routes has a receiving floor and a second path to points.
- **Target share** — a back with 4+ targets per game in a committee is startable.
- **Carry share within the team** — the classic committee measure (`@concepts/player-usage-models.md`).

A back at **38% snaps / 10 carries / 13 routes / 6 targets** is more valuable in PPR than one at 48% snaps / 14 carries / 8 routes / 1 target. Role shape matters, not volume alone.

### The committee read

"Trending toward a **50/50 committee**" is a specific claim: it caps both backs' ceilings while giving each a floor. An RB4 with RB3 upside in a 50/50 split is a legitimate stash — not a starter.

### FAAB

Budget leagues convert the tier into a bid. The shape of the advice: **priority adds get a real bid; handcuffs get a dollar**. Deep-league stashes are near-zero bids. The dollar bins are for speculation on a role change (a trade, a returning backfield mate, a coach's stated plan).

### Injury wave

Waiver value spikes in weeks with broad injury news. The seed batch was shaped by a wave naming **Saquon Barkley, DJ Moore, Ladd McConkey, Rashee Rice, Tee Higgins, and Lamar Jackson**, plus Miami's De'Von Achane to IR (torn ACL, 2026-09-28) — which is what opens the next back's path.

**Do not chase a name because he is available.** Chase the usage line that the vacancy creates.

## Snippets

> "Marks should be viewed as an RB4 with RB3 upside if Montgomery gets hurt… this is trending toward a 50/50 committee." [Source: @sources/rss-rotoballer-w5-rb-waiver-2026-10-05.md]

## Dead Ends

- **Rostered percentages are a snapshot.** They move within hours of a news cycle. Never treat a published count as current.
- **A handcuff is not a pickup.** Roster spots spent on contingency backs have an opportunity cost; only stash them in leagues with deep benches.
- **Not a betting lane.** See @concepts/gambling-wiki-scope.md — this concept exists to inform DFS usage priors, not to generate wagers.
