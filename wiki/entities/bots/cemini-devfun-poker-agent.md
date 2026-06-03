---
title: Cemini dev.fun poker agent (cemini_decide)
type: entity
tags: [entity, bot, poker, devfun, arena-pokerkit]
keywords: [cemini, devfun, cemini_decide, arena-pokerkit, decide-function]
related:
  - entities/platforms/devfun-poker-arena.md
  - entities/tools/pokerskill.md
  - entities/bots/poker-bot-tooling.md
  - concepts/poker-strategy-overview.md
  - concepts/gambling-bot-architecture.md
  - concepts/poker-hl-analyst-loop.md
  - sources/devfun-poker-arena-phase0-2026-06-01.md
  - entities/games/poker.md
maturity: draft
created: 2026-06-01
updated: 2026-06-03
adoption_status: ACTIVE-DEV
claim_status: VERIFIED 2026-06-01 — @cemini23
---

## Relations

- @entities/platforms/devfun-poker-arena.md — venue + Phase-0
- @entities/tools/pokerskill.md — skill-binding pattern (full PokerSkill repo not wired yet)
- @concepts/poker-hl-analyst-loop.md — **HL analyst loop** (analyze → patch → preflight → deploy)
- `briefs/2026-06-03_playground-top20-qualification.md` — top-20 cutoff + survival strategy
- Code: `agents/devfun-poker-arena/examples/cemini_decide.py`

## Raw Concept

| Field | Value |
|-------|-------|
| **Name** | Cemini Wiki Poker |
| **Handle** | `cemini_wiki_poker` |
| **Agent ID** | `cmpy4lcyi001y11vnekn1zlo3` [CONFIRMED 2026-06-03] — was `cmpvvczea…` (retired) |
| **Playground S1 rank** | **#219 @ 540 chips** (Jun 3); **bestRank #4** same day [CONFIRMED] |
| **Qualification** | Top **20** agents per playground window (Jun 3–7, Jun 7–11) → tournament KO |
| **Owner** | **@cemini23** — X verified [CONFIRMED] |
| **Quote** | "structured skills over swagger" |
| **Tournament S28** | Prod lobby `cmpr1vesh2it1x69xmtpiaecp` from 2026-06-02 [CONFIRMED] — **entry fee 0.01 MON** (402 until paid on dev.fun) |
| **Prod service** | `cemini-devfun-poker-lobby.service` on **cemini-prod** → `/opt/devfun-poker-arena` [CONFIRMED 2026-06-02] |
| **Base kit** | arena-pokerkit + `cemini_decide.py` |

## Narrative

### Architecture

```
arena API (pending-actions → action)
  → agent.py loop
  → cemini_decide.decide(table, deadline_s, research_context)
       ← retrieve_solver_context: research_static_chart + skill_binding stub
```

### Layers (recommended scaffold)

1. **Auto Research** — `research_static_chart` preflop open/defend hints
2. **Skill binding stub** — scenario labels in YAML reasoning (`open_defend`, `wet_board_pot_control`, …) — PokerSkill-shaped, not full lbn187/PokerSkill repo yet
3. **Postflop** — treys Monte Carlo equity vs pot odds (from starter `agent.py`)
4. **Clock** — check/fold when `deadline_s < 2`

### Next iterations

- Wire **PokerSkill** expert library when license verified on GitHub
- Optional L2: `examples/llm_agent.py` with `ANTHROPIC_API_KEY`
- Heartbeat LaunchAgent before June 3 main season

### Entry fee (Tournament S28)

`POST /texas/join` returns **402** until paid: **0.01 MON** on Monad chain to `0xa0af9ED64C8fe5d00ce879BADD40e94b47dB2542`. Pay via dev.fun UI; prod lobby auto-retries every 60s (no systemd crash).

### Runbook

See `agents/devfun-poker-arena/README-CEMINI.md`.

**Chip bleed — run HL loop first:**

```bash
./examples/cemini_hl_loop.sh --from-prod    # analyze + brief → patch in Cursor
./examples/cemini_hl_loop.sh --preflight-only
./examples/cemini_hl_loop.sh --deploy        # does NOT overwrite prod creds by default
./scripts/cemini_playground_status.sh      # rank vs top-20 floor
```

**Qualification:** top **20** agents (not 25%) per playground stage → tournament. Monitor cutoff with `cemini_playground_status.sh`. **Do not bust** — Playground S1 rebuy API disabled; buy-in = 1000 chips.

### Wallet (MON) — beta vs official [CONFIRMED 2026-06-03]

| Environment | Agent ID | Wallet | MON (Jun 3) |
|-------------|----------|--------|-------------|
| **Official** | `cmpy4lcyi001y11vnekn1zlo3` | `0x7d2a755dfa58e70eFde21d5e88b23632AfeF0bEF` | 0 |
| Beta (retired) | `cmpvvczea0iyndve98srkcwwq` | `0x3fB1933ee94635e2cb8aFfbC0B62ac683b80c40D` | ~648 |

MON on beta **does not** appear on official. API blocks agent-to-agent transfer (`403`). Fund official via MoonPay / external send; `./scripts/cemini_wallet_check.sh`. See `LESSONS.md` L4.

| Script | Use |
|--------|-----|
| `scripts/cemini_wallet_check.sh` | Beta vs official MON balances + MoonPay link |
| `examples/cemini_hl_loop.sh` | **HL analyst loop** — analyze → brief → preflight → deploy |
| `examples/run_cemini.py` | Poker **Eval benchmark** (`benchmark/start`) |
| `examples/run_cemini_lobby.py` | **Playground / Tournament** lobby (`texas/join`) |

## Snippets

> "structured skills over swagger" — agent quote at registration [CONFIRMED 2026-06-01]

> Claim card: **AGENT CLAIMED** · owner @cemini23 · verified · entered 2026-06-01 [Source: arena.dev.fun claim UI]

## Dead Ends

- Deploying same bot against `@entities/platforms/pokerstars.md` or Bovada — arena-only scope
