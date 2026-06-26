---
title: K128b — BBM7 challenges and solutions playbook
type: source
tags: [source, brief, best-ball, bbm7, k128, draft-copilot]
keywords: [solutions, playbook, draft-copilot, exposure, adp, cli]
related:
  - sources/brief-k128-bbm7-draft-copilot-hub-2026-06-24.md
  - sources/brief-k128b-bbm7-challenge-register-2026-06-24.md
  - entities/platforms/underdog-fantasy.md
  - entities/tools/ceminidfs.md
maturity: validated
read_status: deep-read
created: 2026-06-24
updated: 2026-06-26
cross-wiki-source: "briefs/2026-06-24_bbm7-challenges-and-solutions.md"
---

## Relations

- @sources/brief-k128b-bbm7-challenge-register-2026-06-24.md — ranked challenge list
- @sources/brief-k128-bbm7-draft-copilot-hub-2026-06-24.md — architecture hub

## Raw Concept

| Field | Value |
|-------|-------|
| **Brief** | BBM7 challenges + solutions playbook |
| **Date** | 2026-06-24 |
| **Build** | `../CeminiDFS/briefs/2026-06-24_bbm7-draft-copilot-implementation-brief.md` |

## Narrative

Paired solutions for each challenge in the register. Highlights:

| Challenge | Solution direction |
|-----------|-------------------|
| ADP staleness | Weekly BestBallTeamBuilder CSV + manual refresh script |
| Name normalize | `gsis_id` registry + alias JSON (see `@sources/research-nfl-dfs-id-mapping-2026-06-20.md`) |
| Exposure vs CLV | Tiered recommender: cap-hard vs cap-soft modes per archetype |
| Fast clock | Pre-computed candidate pool; rules engine <5s SLA |
| Ledger drift | Post-draft CSV export (desktop web) → ingest pipeline |
| No API MVP | CLI manual pick entry; Phase 3 DOM overlay optional |

Full playbook sections: data layer, rules engine, portfolio ledger, UX phases, validation plan.

## Dead Ends

- Building contest EV simulator (buy THE SOLVER / ETR)
- Auto-click draft picks (Underdog ToS violation)
