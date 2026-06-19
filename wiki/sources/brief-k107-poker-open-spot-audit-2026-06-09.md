---
title: K107 — Arena open-spot preflop audit (cross-wiki brief)
type: source
tags: [source, brief, poker, devfun, preflop, pfr, k107, audit]
keywords: [k107, open-spot, is_preflop_open_spot, cemini_selfplay_audit, pfr-gap]
related:
  - concepts/poker-hl-analyst-loop.md
  - entities/bots/cemini-devfun-poker-agent.md
  - entities/platforms/devfun-poker-arena.md
  - sources/brief-k118-poker-agent-research-gaps-2026-06-17.md
  - sources/devfun-poker-arena-phase0-2026-06-01.md
  - osint-wiki/sources/trading-posts-compilation-7-2026-06-09.md
maturity: validated
read_status: deep-read
created: 2026-06-09
updated: 2026-06-19
cross-wiki-source: "@osint-wiki/sources/trading-posts-compilation-7-2026-06-09.md"
---

## Relations

- @concepts/poker-hl-analyst-loop.md — open-spot bug signature + selfplay KPI table
- @sources/brief-k118-poker-agent-research-gaps-2026-06-17.md — supersedes passive-PFR diagnosis (2026-06-17 refresh)
- Private brief: `briefs/2026-06-09_k107-gambling-poker-open-spot-AUDIT.md`

## Raw Concept

| Field | Value |
|-------|-------|
| **Brief** | K107 Arena open-spot preflop audit |
| **Date** | 2026-06-09 |
| **Origin** | @3d64r_89 Post 16 via OSINT trading-posts-compilation-7 |
| **Selfplay audit** | 400 hands seed 42 — VPIP 12.1%, PFR 2.1%, gap ~10pp |

## Narrative

### Verdict [CONFIRMED 2026-06-09, refreshed 2026-06-17]

**Open-spot boolean detection: FIXED in code.** Passive **PFR leak persists** — different root cause than raw `call_chips==0` misrouting.

| Check | Status |
|-------|--------|
| `is_preflop_open_spot(table, allowed, call_chips)` in prod | **Implemented** — not raw `call_chips==0` |
| `opponent_target.py` UTG-first-in (`callChips=BB`) | Handles `max_bet <= bb and pot <= blinds_pot + 2` |
| L719 `call_chips==0` | Postflop free-action only |

### Selfplay KPI (evolution)

| Metric | 2026-06-09 | 2026-06-17 (K118) | K107 bug signature | S1 rock target |
|--------|------------|-------------------|-------------------|----------------|
| VPIP | 12.1% | 11.5% | ~23% | 10–16% |
| PFR | 2.1% | 2.2% | ~6% | ≈ VPIP (−5pp) |
| VPIP−PFR gap | ~10pp | ~9pp | ~17pp | ~5pp |

**Interpretation:** Low PFR → `_preflop_open` check/call fallthrough, SB complete path, rock `open_steal_equity` ~0.99. **P0 fixes in K118** (min PFR gate, SB trash fold, lower steal threshold).

### Phase-0 (operator repo)

| Item | Verdict |
|------|---------|
| Open-spot routing fix | **GO** — already deployed |
| PFR / gap gate in `--gate` | **CONDITIONAL-GO** — K118 F1 backlog |
| Live Arena `spot_kind()` logging | **GO** — compare selfplay vs prod schema |

## Snippets

> "Open-spot misrouting is not the dominant leak. Low PFR suggests chart path is checking or calling where raise expected." [Source: briefs/2026-06-09_k107-gambling-poker-open-spot-AUDIT.md]

## Dead Ends

- **Re-patch `call_chips==0` for preflop open** — already superseded by `is_preflop_open_spot()`
- **Optimize selfplay bb/100** — misaligns with Playground fish/maniac analyze mix
