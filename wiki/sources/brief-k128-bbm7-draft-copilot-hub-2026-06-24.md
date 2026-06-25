---
title: K128 — BBM7 Draft Copilot hub (live draft tool)
type: source
tags: [source, brief, best-ball, bbm7, underdog, k128, ceminidfs]
keywords: [bbm7, live-draft, draft-copilot, underdog, exposure, adp, extension]
related:
  - entities/platforms/underdog-fantasy.md
  - concepts/bbm7-portfolio-construction.md
  - concepts/bbm7-adp-delta-tracker.md
  - concepts/bbm7-playoff-week-construction.md
  - entities/tournaments/best-ball-mania-vii.md
  - entities/tools/ceminidfs.md
  - concepts/diy-nfl-dfs-model-architecture.md
  - sources/4for4-bbm7-guide-series-2026-06-18.md
maturity: validated
read_status: deep-read
created: 2026-06-24
updated: 2026-06-25
cross-wiki-source: "briefs/2026-06-24_bbm7-live-draft-tool-master-plan.md"
---

## Relations

- @entities/platforms/underdog-fantasy.md — draft room mechanics, ToS, CSV export (K128 deep research)
- @concepts/bbm7-portfolio-construction.md — 150-entry archetype matrix
- @entities/tools/ceminidfs.md — implementation home (W9)

## Raw Concept

| Field | Value |
|-------|-------|
| **Brief cluster** | K128 / K128b / K128c — BBM7 live draft execution |
| **Date** | 2026-06-24 |
| **Build target** | `../CeminiDFS` — `briefs/2026-06-24_bbm7-draft-copilot-implementation-brief.md` |

## Narrative

### Deliverables (operator briefs — gitignored `briefs/`)

| Brief | Path | Role |
|-------|------|------|
| **K128 master plan** | `briefs/2026-06-24_bbm7-live-draft-tool-master-plan.md` | Product architecture, build-vs-buy |
| **K128b challenge register** | `briefs/2026-06-24_bbm7-challenge-register.md` | Open problems ranked |
| **K128b solutions** | `briefs/2026-06-24_bbm7-challenges-and-solutions.md` | Playbook per challenge |
| **K128c implementation** | `../CeminiDFS/briefs/2026-06-24_bbm7-draft-copilot-implementation-brief.md` | Phased build spec |

### Product summary

**CeminiBBM Draft Copilot** — hybrid stack: wiki rules + portfolio ledger (**build**), ADP feed integrate (**buy**), optional projection CSV (**buy**), CLI MVP then optional Chrome overlay (Draft Co-Pilot fork pattern).

### Underdog platform hooks (ingested to entity page)

- Fast draft **30s** clock; slow draft **8h** compressing to **60s** near kickoff
- Exposure CSV **desktop web only**, **1/day** email export
- In-app ADP **48h rolling**, updated daily; external tools lag **12–36h**
- ToS: scraping prohibited; read-only overlay **low–medium risk**; auto-click **critical violation**

### Phase roadmap (ROADMAP W7)

1. Spikes — name normalize + CSV schema (CeminiDFS)
2. Phase 0 — `src/ceminidfs/bbm/` scaffold
3. Phase 1 — CLI draft assistant + portfolio ledger
4. Phase 2 — ADP normalizer + half-PPR projection merge
5. Phase 3 (optional) — browser overlay

## Dead Ends

- Scraping Underdog draft API (no public API; ToS violation)
- Building contest EV sims (buy THE SOLVER / ETR instead)
