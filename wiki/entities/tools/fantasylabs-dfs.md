---
title: FantasyLabs (DFS tools)
type: entity
tags: [entity, tool, dfs, nfl, fanduel, paid, action-network]
keywords: [fantasylabs, simlabs, csv-export, koerner, etr-bundle]
related:
  - concepts/dfs-strategy-overview.md
  - concepts/dfs-paid-tool-methodologies.md
  - concepts/diy-nfl-dfs-model-architecture.md
  - concepts/diy-nfl-pickem-props-tool-architecture.md
  - sources/fantasylabs-picklabs-launch-2026-07-05.md
  - concepts/dfs-backtesting-framework.md
  - concepts/dfs-ownership-projection.md
  - entities/platforms/fanduel.md
  - entities/platforms/draftkings.md
  - entities/tools/stokastic-dfs.md
  - entities/tools/pydfs-lineup-optimizer.md
  - sources/web-dfs-hero-nfl-gpp-strategy-2026-06-20.md
maturity: validated
created: 2026-06-20
updated: 2026-07-05
---

## Relations

- @entities/tools/stokastic-dfs.md — alternative paid GPP stack (pick one)
- @entities/platforms/fanduel.md — CSV lineup upload supported
- @entities/tools/pydfs-lineup-optimizer.md — FOSS gen from exported projections

## Raw Concept

**FantasyLabs** (Action Network) — paid DFS research + optimizer + **SimLabs** lineup generator. Strong **CSV projection export** for downstream tooling.

| Field | Value |
|-------|-------|
| **URL** | https://www.fantasylabs.com/ |
| **NFL via ETR bundle** | ~**$49.95/mo** NFL optimizer add-on (ETR subscribers only) [CONFIRMED — ETR promo page] |
| **All-sports** | ~$69.95/mo (ETR page; verify on fantasylabs.com) [NEEDS VERIFICATION 2026-06-20] |
| **Export** | **CSV projection export** from models [CONFIRMED — Labs article] |
| **Lineup export** | FanDuel CSV upload from Labs builder [CONFIRMED] |
| **API / MCP** | **None public** |

## Narrative

### Phase-0 verdict

**CONDITIONAL-GO** — **runner-up** to Stokastic for operator W8; **best choice if already paying ETR** for content/Underdog research.

| Check | Result |
|-------|--------|
| FanDuel NFL | Yes — lineup builder + export tutorial |
| Projection export | CSV from Pro Models (Koerner NFL cited on Labs) |
| SimLabs | Contest sim lineup gen; export back to optimizer **limited** per Labs product note |
| 150-lineup MME | Supported in Lineup Builder (ETR promo) |
| API / MCP | **NO-GO** |
| Support | FantasyLabs / Action Network — not ETR |

### ETR bundle note

Establish The Run sells Labs optimizer access at discounted NFL rate with **ETR + Labs projections preloaded** and Levitan ownership. Separate company from ETR's **Solver** best-ball draft assistant — do not conflate.

### PickLabs (props / pick'em) — 2026-07-05

Separate product surface from salary-cap DFS — **player props** and **DFS pick'em** edges (PrizePicks, Underdog, Sleeper + sportsbooks via Playbook). **Not** integrated into CeminiDFS.

| Field | Value |
|-------|-------|
| **Gating** | **All-Access** membership (launch article CTA) — not a documented standalone SKU |
| **Edge metrics** | Win probability, edge %, value grade vs market consensus |
| **Workflow** | Pick Board → slip builder → manual place at book/app; Playbook odds compare |
| **Export** | **UI-only** — no PickLabs CSV/API (DFS Player Model CSV export is a different feature) |
| **K147 verdict** | Paid **benchmark** only — see @sources/fantasylabs-picklabs-launch-2026-07-05.md (validated deep-read) and @concepts/diy-nfl-pickem-props-tool-architecture.md |

### Integration path

Same as Stokastic: export CSV → inbox → `scripts/fanduel_slate_optimize.py` or nfl-fanduel-slate-prep skill.

Expected Labs export columns vary — skill documents normalize to pydfs `Name`, `Position`, `Salary`, `FPPG`.

## Snippets

> "We have added the ability to export our projections directly into a .CSV file." [Source: https://www.fantasylabs.com/articles/export-projections-feature-live-fantasylabs-models/]

> "ETR subscribers… $49.95/mo for NFL access… Optimize up to 150 lineups… Export lineups easily to DFS sites." [Source: https://establishtherun.com/etr-promotion-fantasylabs-dfs-optimizer/]

## Dead Ends

- SimLabs → optimizer round-trip — "not accessible" for manual edit/export in some SimLabs flows [Source: Labs SimLabs product update]
- Public API — none documented
