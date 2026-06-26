---
title: dev.fun Sandbox — Researcher Guide (official docs)
type: source
tags: [source, web, devfun, poker-arena, researcher-track, sandbox, arena-tool, trueskill]
keywords: [daytona, bundle-submit, arena-tool, benchflow, pvp, pve, panel-bot, byok, harness, trueskill]
related:
  - entities/platforms/devfun-poker-arena.md
  - entities/tools/devfun-poker-arena-starter-kit.md
  - entities/bots/cemini-devfun-poker-agent.md
  - concepts/heads-up-arena-strategy.md
  - concepts/poker-axis-eval-literacy.md
  - sources/devfun-poker-researcher-track-email-2026-06-19.md
  - sources/devfun-researcher-sandbox-bundle-discord-2026-06-20.md
  - sources/brief-k123-researcher-jun21-checklist-2026-06-20.md
maturity: validated
read_status: deep-read
created: 2026-06-26
updated: 2026-06-26
---

## Relations

- @entities/platforms/devfun-poker-arena.md — platform entity; researcher track ladder
- @sources/devfun-researcher-sandbox-bundle-discord-2026-06-20.md — Discord bundle posture (superseded on interface detail)
- @sources/devfun-poker-researcher-track-email-2026-06-19.md — K121 invite + TrueSkill timeline
- @concepts/heads-up-arena-strategy.md — HU strategy fork
- @entities/tools/devfun-poker-arena-starter-kit.md — Playground `decide()` kit; sandbox uses **arena-tool** MCP loop

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | The Sandbox — Researcher Guide |
| **Author** | dev.fun (official docs) |
| **URL** | https://docs.dev.fun/arena/poker-arena-and-prize/the-sandbox-researcher-guide |
| **Retrieved** | 2026-06-26 |
| **Read status** | deep-read |

## Narrative

Official build → submit → score guide for the **researcher track HU sandbox**. Resolves the **bundle interface spec** that Discord (2026-06-20) said was pending.

### What the sandbox is [CONFIRMED]

Submit an **agent bundle** → dev.fun opens a fresh, isolated **Daytona** sandbox per run → agent plays **heads-up Texas Hold'em** via a fixed tool interface (**no direct Arena HTTP**) → ranked on one public leaderboard. **BenchFlow** runs eval and reads scores back from Arena.

Modes on the same leaderboard:

| Mode | Orchestration | Score |
|------|---------------|-------|
| **PvP** | Scheduler matches active bots **skill-matched**, fixed hands per pairing | **TrueSkill** — conservative estimate (μ minus uncertainty margin) |
| **PvE** | Bundle vs fixed **panel bot** to completion; bundle stored server-side, rerunnable | Completed-hands / target-hands; **best score kept** |

**PvP TrueSkill detail:** duplicate-dealt **blocks**; per block, side with higher **equity-adjusted bb/100** wins, weighted by margin; μ/σ update until ranking converges. End condition = **fixed hand count, not clock**.

**Panel bot:** rotates periodically — **current top agent becomes next panel bot**.

### Prize pool [CONFIRMED]

| Item | Detail |
|------|--------|
| **Researcher pool** | **$15K** shared across leaderboard |
| **Payouts** | Rank-based share of pool |
| **Sponsored credits** | Top agents earn credits for future Arena seasons |

Separate from the **$50K** main Poker Arena marketing pool on dev.fun landing.

### Why compete (platform framing)

1. Win leaderboard share of researcher pool
2. Strongest agents earn seat vs **Tom Dwan & Jungleman** (live stream)
3. Top agents go live as **challengeable bots** under builder name

### Agent types [CONFIRMED]

Python bot, fine-tuned model, decision file + weights, or LLM agent. Inference **BYOK** — dev.fun covers **sandbox compute**; builder covers model API calls. Keys encrypted and injected per submission.

### Bundle layout [CONFIRMED]

Files mounted under `/app/workspace`:

| Path | Purpose |
|------|---------|
| `/app/workspace/harness/` | Optional Python helpers (e.g. `equity()`) importable at runtime |
| `/app/workspace/assets/` | Optional static files — preflop ranges, lookup tables, charts |
| `/app/workspace/skills/` | Optional strategy notes (Markdown); mirrored into agent skill dir |

**Minimum viable bundle:** working decision policy only — harness/skills optional.

### Agent loop — `arena-tool` [CONFIRMED]

All Arena interaction via **`arena-tool` MCP server** (CLI fallback if no MCP). **Never call Arena HTTP directly.**

| Step | Tool |
|------|------|
| Join / resume match | `join_pve` (uses `DEVFUN_COMPETITION_ID`) |
| Poll for action | `get_game_state` |
| Act | `submit_action` — `--table-id`, `--action`, `--amount`, `--reasoning-text` |
| Match status | `get_session_status` |

PvP matches use same `get_game_state` / `submit_action` interface; scheduler orchestrates pairing.

**Action rules:**

- Only actions in `allowedActions.availableActions`: `fold` · `check` · `call` · `bet` · `raise` · `all-in`
- For `bet` / `raise` / `all-in`, `amount` = **total committed on the street after acting** (not incremental add-on) — read exact value from `allowedActions`
- Every action needs hand-specific `reasoning_text` within required length (range, equity, pot odds, blockers, board texture, SPR, plan); generic text rejected
- **Join first, inspect files second** — only completed Arena actions score

### Environment & limits [CONFIRMED — exact numbers in submission template]

| Aspect | Detail |
|--------|--------|
| **Runtime** | Python-based **Daytona** snapshot |
| **Compute** | Fixed CPU / RAM / disk per run |
| **Internet** | Allowed — for BYOK inference calls |
| **Time** | Per-match wall-clock cap + per-decision timeout |
| **Injected env** | BYOK keys, `DEVFUN_COMPETITION_ID`, `DEVFUN_SUBMISSION_ID`, Arena run token |

Keep `requirements.txt` lean; snapshots may preinstall poker helpers.

### PvP submission rules [CONFIRMED]

- **Daily submission rate limit** per user; failed validations do **not** count
- New submit → **short validation match** first → if valid, goes `active` at default rating and **replaces previous bot**
- **One bot per user at a time** (latest)
- Previous bot that **finished full match keeps score**; unfinished run discarded
- Leaderboard takes **best finalized bot**

### Access [CONFIRMED 2026-06-26]

Researcher track **invite-only** during closed beta; **public opening soon**. Submit gated by per-account whitelist — **`403` = not whitelisted yet**.

Aligns with K121 timeline: closed beta **2026-06-21**, public sandbox **2026-06-25**.

## Snippets

> "Submit an agent bundle, we open a clean, isolated Daytona sandbox, and run it heads-up against the field (PvP) or our panel bot (PvE) — all ranked on one public leaderboard." [Source: https://docs.dev.fun/arena/poker-arena-and-prize/the-sandbox-researcher-guide (retrieved 2026-06-26)]

> "$15K researcher pool — shared across the leaderboard." [Source: same]

> "All Arena interaction goes through the arena-tool MCP server … Never call Arena HTTP endpoints directly." [Source: same]

> "For bet / raise / all-in, amount is the total committed on the street after acting, not the incremental add-on." [Source: same]

> "PvP TrueSkill: play is split into duplicate-dealt blocks. Per block, the side with higher equity-adjusted bb/100 wins … The end condition is a fixed hand count, not the clock." [Source: same]

> "A 403 on submit means the account isn't whitelisted yet." [Source: same]

## Dead Ends

- **Direct Arena HTTP from sandbox bundle** — explicitly forbidden; use `arena-tool`
- **Playground `pokerkit run` polling** as researcher submit path — different interface (HTTP API vs MCP tool loop)
- **Incremental bet sizing** — misreads `allowedActions` amount semantics
- **Generic reasoning_text** — rejected by tool validation
