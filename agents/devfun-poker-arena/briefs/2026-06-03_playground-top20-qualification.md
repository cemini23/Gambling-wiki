---
title: Playground qualification — top 20 to tournament
type: brief
tags: [brief, poker, devfun, playground, tournament, qualification]
created: 2026-06-03
target: agents/devfun-poker-arena/examples/cemini_decide.py
---

## Target

dev.fun **Playground S1** → tournament knockout (Jun 2026). One claimed agent: `cemini_wiki_poker`.

## Summary

Qualification is **top 20 agents by chip score** per playground window (**not** top 25%). Two playground stages: **Jun 3–7** and **Jun 7–11** (future seasons announced). Knockout tournament stage advances **top 25** separately. Cemini **bestRank #4** early S1, then bleed to **rank ~215 @ 540 chips** — likely **below table buy-in (1000)** with **rebuy API disabled**, so stage-1 re-entry blocked until stage 2 or operator restores valid API key.

## Body

### Qualification ladder (dev.fun)

| Stage | Window | Advance |
|-------|--------|---------|
| Playground S1a | Jun 3–7 | **Top 20** → tournament |
| Playground S1b | Jun 7–11 | **Top 20** (second chance) |
| Tournament KO | TBA | Top **25** → next round |
| Researcher / finale | TBA | separate tracks |

Leaderboard metric: **`totalScore`** (season chips). ~258 agents in field; rank **#20 ≈ 1607 chips** (moving target).

### Cemini status (2026-06-03 evening UTC)

| Field | Value |
|-------|-------|
| Claimed handle | `cemini_wiki_poker` |
| Agent ID | `cmpy4lcyi001y11vnekn1zlo3` |
| Rank | **215** |
| Chips | **540** |
| Hands | 94 (17 won) |
| **bestRank** | **4** (was in qualification zone) |
| Rebuy | **403 disabled** on Playground S1 |
| Buy-in | **1000** chips (`initialChips`) |

**Blockers**

1. **540 < 1000 buy-in** → `409 Agent does not have enough chips` — cannot sit new tables.
2. **Prod credential split** — deploy overwrote prod key; lobby re-registered as `cemini_wiki_poker-2ef8b3` (duplicate, unclaimed). Must restore API key for **claimed** agent only.
3. Local `.arena-credentials` points at retired id `cmpvvczea…` (401).

### Hand-history scan (2026-06-03 ~18:30 UTC)

100-hand prod analyze after latest deploy. **Still bleeding; SB dominates worst hands.**

| Priority | Pattern | Examples from worst 15 |
|----------|---------|------------------------|
| P0 | SB bust lines | `22`, `79`, `96`, `88`, `JJ` paired, `A8`/`K6` SB |
| P1 | Weak ace postflop | `A6` BB on 999, `A7` CO paired, `A9` BTN preflop |
| P2 | BTN overcall scary boards | `QAh` on 55776, `AT` monotone |
| OK | Value hands | `TT` +396, `77` +284, `AK` +122 |

**Status:** rank **230**, **782 chips**, gap to #20 **+1193**. Buy-in **1000** → 409 when between tables. Patches (JJ SB, 83o, KQo MP, survival mode) need post-deploy sample before next HL round.

See `LESSONS.md` L6.

1. **Survival first** — one bust from 1000 ≈ season over (no rebuy). HL patches (SB trash, JJ paired river, KQ OOP) reduce bleed.
2. **Volume when +EV** — leaders run **50–100+ hands**; chip edge compounds (e.g. #1: 6810 / 102 hands).
3. **HL loop cadence** — `./examples/cemini_hl_loop.sh --from-prod` → patch → preflight → deploy **without** `CEMINI_FORCE_CREDS=1`.
4. **Monitor cutoff** — `./scripts/cemini_playground_status.sh` (rank vs #20 floor).
5. **Stage 2 (Jun 7–11)** — treat as fresh 1000-chip runway if S1a ends busted; same bot, zero duplicate agents.

### Do not

- Auto-register new handles on prod (`ARENA_NO_AUTO_REGISTER=1` in prod `.env` recommended).
- Deploy with `CEMINI_FORCE_CREDS=1` unless intentionally rotating keys.
- Optimize self-play bb/100 — optimize **live chip survival + accumulation**.

## Sources

- https://dev.fun/ (playground top 20 / KO top 25)
- @concepts/poker-hl-analyst-loop.md
- @entities/bots/cemini-devfun-poker-agent.md

## Implementation status

| Field | Value |
|-------|-------|
| Status | IN_PROGRESS |
| Proof | `scripts/cemini_playground_status.sh`; deploy creds guard |
| Follow-up | Jun 7–11 stage: **multi-agent probe** (L5) — 5–10 unclaimed, claim best |

## Next playground — multi-agent funnel (L5)

Observed meta: many entrants run **multiple unclaimed agents**, tune in secret, **claim only when rank/chips look good**.

| Phase | Action |
|-------|--------|
| Pre-window | Register 5–10 official agents; store `credentials/agent-{1..N}.json` |
| Days 1–2 | Parallel lobby/self-play; branch `cemini_decide` or train profiles per agent |
| Gate | `cemini_playground_status.sh` per agent; pick top 1–2 by rank + chip runway |
| Claim | X-verify **winners only**; point prod lobby at winner creds |
| Retire | Abandon or archive losers; never deploy stale beta keys |

We did the opposite: one claimed agent, early public lock-in, single-strategy bleed. Correct for brand visibility; wrong for qualification EV.
