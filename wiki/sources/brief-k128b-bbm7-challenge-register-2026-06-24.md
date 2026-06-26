---
title: K128b — BBM7 challenge register
type: source
tags: [source, brief, best-ball, bbm7, k128, draft-copilot]
keywords: [challenge-register, adp-staleness, exposure-caps, ledger-drift, fast-draft]
related:
  - sources/brief-k128-bbm7-draft-copilot-hub-2026-06-24.md
  - sources/brief-k128b-bbm7-challenges-and-solutions-2026-06-24.md
  - sources/research-nfl-dfs-id-mapping-2026-06-20.md
  - entities/platforms/underdog-fantasy.md
  - concepts/bbm7-portfolio-construction.md
maturity: validated
read_status: deep-read
created: 2026-06-24
updated: 2026-06-26
cross-wiki-source: "briefs/2026-06-24_bbm7-challenge-register.md"
---

## Relations

- @sources/brief-k128-bbm7-draft-copilot-hub-2026-06-24.md — K128 product hub
- @sources/brief-k128b-bbm7-challenges-and-solutions-2026-06-24.md — paired solutions playbook

## Raw Concept

| Field | Value |
|-------|-------|
| **Brief** | BBM7 live draft challenge register |
| **Date** | 2026-06-24 |
| **Scope** | 150-max portfolio · no Underdog API |

## Narrative

### Top 10 must-solve before Phase 1

1. **ADP staleness** — weekly/daily ingest without live API
2. **Name normalization** — Underdog ↔ projection sources
3. **Exposure caps vs CLV** — recommender when best pick violates 35% cap
4. **Archetype vs board** — Zero RB blocked by room
5. **Ledger drift** — local JSON vs completed drafts
6. **30s fast-draft clock** — CLI must return top 3 in <5s
7. **Tab switching UX** — room + CLI cognitive load
8. **No Underdog API** — manual/DOM state only until Phase 3
9. **Backtest without perfect data** — validate before $25 entries
10. **Weekly refresh** — scripted <5 min operator burden

Full severity/likelihood tables in operator brief.

## Dead Ends

- Automated Underdog draft API (does not exist publicly)
- Real-time scrape of live draft rooms (ToS high risk)
