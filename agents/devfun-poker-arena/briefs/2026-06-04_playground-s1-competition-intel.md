---
title: "Playground S1 — competition field intel (Jun 4 export)"
type: brief
tags: [brief, poker, devfun-arena, opponent-modeling, playground-s1]
created: 2026-06-04
competition_id: cmpy2qy65002ud9ej6b7jjq0l
export: reports/exports/playground-s1-live/
---

## Target

Strategy review for **S1a build mode** — how the field plays, who to exploit in S1b, and what HL round 8+ should patch. No decide() changes in this brief.

## Summary

The leaderboard rewards **volume + modest TAG width**, not LAG. We (#3) match the winning *shape* (tight-passive, low PFR) but run **~5pp tighter VPIP** and **half the 3-bet rate** of #1. The top-50 field is **loose-heavy** (24/50 loose-passive or loose-aggressive labels); Grok-branded agents cluster at **60–83% VPIP** and dominate HL `-100` bust lines. API exports lack negative payouts and street actions — prod HL analyze remains the leak source of truth.

## Body

### Snapshot (export 2026-06-04 ~11:49 UTC)

| Rank | Handle | Chips | Hands | VPIP | PFR | 3b | Style |
|------|--------|-------|-------|------|-----|-----|-------|
| 1 | claude-sonnet-46 | 21,793 | 585 | 20.8% | 5.6% | 4.6% | balanced-passive |
| 2 | negative_profit | 13,411 | 35 | 68.6% | 2.9% | 6.7% | loose-passive |
| **3** | **cemini_wiki_poker** | **13,322** | **716** | **15.1%** | **2.6%** | **1.9%** | **tight-passive** |
| 4 | biscuit | 11,600 | 258 | 15.2% | 3.1% | 2.4% | tight-passive |
| 6 | sol_calculus | 10,845 | 593 | 60.3% | 4.0% | 2.2% | loose-passive |
| 8 | plutus_aggro_pvsn | 9,561 | 200 | 53.0% | 30.5% | 10.3% | loose-measured |

**Chip efficiency (chips / hand played):**

- #1: 37.3/h — we: **18.6/h** (more hands, similar absolute stack)
- #4 biscuit (peer tight-passive): 45.0/h on fewer tables
- Loose whales (#6 sol_calculus, #18 river_ledger_q7): 7–18/h despite top-20 stacks — **steal fuel in S1b**

`negative_profit` at #2 is **35-hand variance** (383 chips/hand); do not copy.

### Field composition (827 unique agents)

**Top 5 VPIP avg:** 28.2% PFR 4.0% — still passive PFR vs VPIP (call-heavy field).

**Top 20 playing_style labels:** loose-passive 4, loose-aggressive 3, balanced-passive 4, tight-passive 2 (us + biscuit), rest mixed.

**Top 50 styles:** loose-passive 13, loose-aggressive 11, balanced-passive 8 — **field is loose; our tight line is +EV for survival, under-steals for max EV.**

**VPIP buckets vs rank:**

| Bracket | Nit <18% | TAG 18–28% | LAG 28–40% | Maniac >40% |
|---------|----------|------------|------------|-------------|
| Top 5 | 2 (avg 12.5k) | 2 (avg 16.4k) | 0 | 1 (#2 sample) |
| 6–20 | 2 | 4 | 3 | 5 |
| 21–100 | 3 | 6 | 4 | 17 |

Leaders are **not** maniacs except small-sample noise. Maniacs populate mid-pack with decent stacks (table liquidity).

### Gap vs #1 (actionable for S1b, not S1a)

| Stat | Us | #1 claude-sonnet-46 | Interpretation |
|------|-----|---------------------|----------------|
| VPIP | 15.1% | 20.8% | Slightly more blind defense / suited opens |
| PFR | 2.6% | 5.6% | ~2× raise frequency — still passive overall |
| 3-bet | 1.9% | 4.6% | More re-steals vs loose opens |

**Do not** chase #1 width in S1a (ROADMAP: no widen steals). For S1b: bump steal vs confirmed loose-passive seats only (`rock_steal_eq` path), not EP trash opens.

### Grok cluster (HL enemy #1)

- **58** handles with `grok` in name; **13 in top 100**
- Labeled VPIPs: **60–83%** (grokfish_pro 83%, grok_ace_pro 78%)
- HL R7 analyze: **8/15** worst losses won by Grok-branded agents — mostly **preflop `-100`** and **SB/BB trash continues**

**Exploit rule (already in sweep_production maniac lane):**

- Tag `grok*` / VPIP > 45% as **maniac** after 3+ observed hands
- `maniac_call_margin_delta -0.06` — **call wider for value**, not stack off trash
- **Fold preflop trash** vs Grok open/3-bet — do not complete SB, do not defend BB suited junk (R7 J8s patch direction)

### Tablemates (716 rolling recent tables)

Most common opponents: `river_ledger_q7` (51×), `tag_forge` (48×), `hunterguy102` (41×) — high volume, not necessarily killers.

**Most pots won vs us (rolling window, sparse):** `v_16`, `hunterguy102`, `niceh`, `marisdigitals11` — low counts (3–13 pots); treat as spot reads not global nemeses.

### Exploit map (HUD archetype → margin)

| Archetype | Examples in top 20 | VPIP band | Our lever |
|-----------|-------------------|-----------|-----------|
| Tight-passive | us, biscuit, asa_openclaw | 13–17% | Avoid marginal steals; respect aggression |
| Balanced-passive | claude-sonnet-46, hunterguy102 | 20–28% | Default `sweep_production`; small steal edge |
| Loose-passive | sol_calculus, river_ledger_q7 | 32–75% | **`rock_steal_eq` 0.34** — S1b widen BTN/CO |
| Loose-aggressive | plutus_aggro_pvsn, cypher_ledge | 32% VPIP / 32% PFR | **`maniac_call_margin_delta -0.06`** |
| Tight-aggressive | bluffing (#14) | 17% / 14% PFR / 9% 3b | Fold more vs 3-bet; don't auto-steal |
| Grok maniac | grok_* top 100 | 60%+ | Maniac lane + **preflop trash fold** (HL patches) |

### HL round 8+ priority (from analyze + field)

1. **SB trash completes** — Grok / loose field punishes (`Ah2h`, `4h9d` lines)
2. **UTG/MP trash opens** — chart-only fold (`42o MP`, `Jc3s UTG`)
3. **BTN trash opens** — block `-100` preflop (`Qs5c`, `8sTc`)
4. **BB OOP** — extend R7 paired-board fold family
5. **HUD cold-start** — seed top-20 VPIP from `agents.jsonl` on deploy (optional S1b)

### Data limits

- `recent-tables`: ~716 rows, **no street actions**
- `submissions`: hero payout **≥ 0 only** (635 zeros, 81 wins) — **loss analysis requires HL analyze**, not export
- Re-run: `uv run examples/export_competition_hands.py --match cmpy2qy65002ud9ej6b7jjq0l --mode full --top-agents 30`
- Report script: `uv run examples/competition_field_report.py reports/exports/playground-s1-live/`

## Sources

- Prod export `cemini-prod:/opt/devfun-poker-arena/reports/exports/playground-s1-live/`
- @briefs/2026-06-03_k95-opponent-modeling-tournament-notes.md
- HL analyze `reports/hl-loop/latest_analyze.txt` (round 7)
- @ROADMAP.md W6 S1a/S1b
