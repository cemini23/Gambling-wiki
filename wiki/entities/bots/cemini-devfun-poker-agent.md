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
  - sources/devfun-poker-arena-phase0-2026-06-01.md
  - entities/games/poker.md
maturity: draft
created: 2026-06-01
updated: 2026-06-02
adoption_status: ACTIVE-DEV
claim_status: VERIFIED 2026-06-01 — @cemini23
---

## Relations

- @entities/platforms/devfun-poker-arena.md — venue + Phase-0
- @entities/tools/pokerskill.md — skill-binding pattern (full PokerSkill repo not wired yet)
- Code: `agents/devfun-poker-arena/examples/cemini_decide.py`

## Raw Concept

| Field | Value |
|-------|-------|
| **Name** | Cemini Wiki Poker |
| **Handle** | `cemini_wiki_poker` |
| **Agent ID** | `cmpvvczea0iyndve98srkcwwq` [CONFIRMED 2026-06-01] |
| **Arena agent #** | **2865** (claim card S1) [CONFIRMED 2026-06-01] |
| **Owner** | **@cemini23** — X verified [CONFIRMED 2026-06-01] |
| **Quote** | "structured skills over swagger" |
| **Playground S1** | Joined + **rank #10** on first leaderboard snapshot [TENTATIVE] |
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

| Script | Use |
|--------|-----|
| `examples/run_cemini.py` | Poker **Eval benchmark** (`benchmark/start`) |
| `examples/run_cemini_lobby.py` | **Playground / Tournament** lobby (`texas/join`) |

## Snippets

> "structured skills over swagger" — agent quote at registration [CONFIRMED 2026-06-01]

> Claim card: **AGENT CLAIMED** · owner @cemini23 · verified · entered 2026-06-01 [Source: arena.dev.fun claim UI]

## Dead Ends

- Deploying same bot against `@entities/platforms/pokerstars.md` or Bovada — arena-only scope
