---
title: Paid DFS tool projection methodologies
type: concept
tags: [concept, dfs, nfl, projections, paid-tools, methodology]
keywords: [stokastic, fantasylabs, sabersim, etr, the-blitz, ownership, monte-carlo]
related:
  - concepts/dfs-strategy-overview.md
  - concepts/diy-nfl-dfs-model-architecture.md
  - entities/tools/stokastic-dfs.md
  - entities/tools/fantasylabs-dfs.md
  - entities/tools/pydfs-lineup-optimizer.md
  - sources/research-diy-dfs-model-master-plan-2026-06-20.md
maturity: draft
created: 2026-06-20
updated: 2026-06-20
---

## Relations

- @entities/tools/stokastic-dfs.md — operator W8 primary paid tool
- @entities/tools/fantasylabs-dfs.md — runner-up / ETR bundle
- @concepts/diy-nfl-dfs-model-architecture.md — DIY pipeline benchmark target
- @concepts/dfs-strategy-overview.md — GPP / ownership framework

## Raw Concept

How major paid NFL DFS services **publicly disclose** building projection CSVs — inputs, stat layers, sims, ownership, export format. Black-box gaps noted. Expanded by K125 subagent research (W-PAID-RE).

## Narrative

### Shared pipeline (industry pattern)

1. **Inputs** — Vegas spreads/totals, usage (snap/target/carry), matchups, weather, injuries
2. **Stat layer** — Project attempts, yards, TDs, receptions (bottom-up) *or* regress to fantasy points
3. **Scoring layer** — Site-specific: FanDuel half-PPR vs DraftKings full-PPR + yardage bonuses
4. **Distribution** — Ceiling/floor, boom/bust %, percentiles
5. **Field layer** — Ownership projections (often ML on historical contest entries)
6. **Export** — Flatten slate table → CSV/spreadsheet; **no public API**

### By vendor (public disclosures)

| Tool | Projection approach | Sims / ownership | CSV export |
|------|---------------------|------------------|------------|
| **Stokastic** | Alex Baker stat-first: passing/rushing/receiving stats → fantasy points; real-time injury refresh | Boom/bust, top stacks, contest sims (Core/Max); ownership ML | Excel/CSV/spreadsheet for members [CONFIRMED] |
| **FantasyLabs** | Sean Koerner predictive models; Models 3.0 conditional tweaks; Raybon alternate model | Correlation-aware optimizer; SimLabs | Blue download on Models page [CONFIRMED] |
| **SaberSim** | **Sim-first:** thousands of play-by-play game sims → projection = sim output distribution | Contest-specific ownership; optimizer consumes full range | In-app export; median + percentiles |
| **ETR + Solver** | Analyst team projections; value vs salary expectation (not raw $/pt) | 20k contest sims; field lineups + game sims with correlation | Auto-sync to Solver/Labs with ETR sub |
| **THE BLITZ** | Derek Carty metrics: air yards, YAC, snaps, RZ targets, O-line, dynamic pass/run | ML ownership; ceiling/floor/percentile | Lineup HQ import |

### Architectural split

| Paradigm | Examples | CSV contains |
|----------|----------|--------------|
| Expert stat → points | Stokastic, ETR, Koerner | Mean/median FPTS + leverage columns |
| Metrics / ML regression | THE BLITZ | Mean + percentiles |
| Sim-first | SaberSim, Stokastic sims, ETR Solver | Mean = average of simulated game scripts |

**Paid edge** is less the secret median and more **ownership**, **distributions**, and **contest ROI sims**. pydfs pipeline consumes mean projection only unless extended.

### Methodology depth (K125 reverse-engineering)

| Tool | Projection method (disclosed) | Sim approach | Black box |
|------|----------------------------|--------------|-----------|
| **SaberSim** | Play-by-play sim thousands× → distribution | Contest-specific fields | Transition probabilities |
| **Stokastic** | Stat tabs → fantasy points; copula-style slate sims | 1k–10k lineup ROI sims | Correlation matrices, base medians |
| **FantasyLabs** | Koerner models + MS of FP + Opp +/- | SimLabs hybrid SimWgt 0–99 | SimLabs internal generator |
| **ETR** | Analyst + quant base + human overrides | Solver 20k contest sims | Manual bump rules |
| **THE BLITZ** | Air yards, snaps, O-line, dynamic pass/run | ML ownership + percentiles | Full regression weights |

### DIY benchmark role

Retain **one** paid export as accuracy benchmark — **Stokastic Core** (W8 operator) or **FantasyLabs $49.95** (cheapest clean CSV). Benchmark-only; manual export per ToS. Not a runtime dependency.

## Snippets

> "We simulate every game thousands of times, play-by-play… These aren't your typical projections." [Source: https://support.sabersim.com/en/articles/12078831-how-projections-work (retrieved 2026-06-20)]

> "File downloads for all data in Excel, CSV, and other formats." [Source: https://www.stokastic.com/nfl/nfl-dfs-projected-stats (retrieved 2026-06-20)]

> "We have added the ability to export our projections directly into a .CSV file." [Source: https://www.fantasylabs.com/articles/export-projections-feature-live-fantasylabs-models/]

## Dead Ends

- **Public APIs** — none from Stokastic, Labs, SaberSim, ETR for projection feeds
- **Full model recipes** — proprietary; only feature lists (BLITZ) or high-level sim descriptions (SaberSim) published
