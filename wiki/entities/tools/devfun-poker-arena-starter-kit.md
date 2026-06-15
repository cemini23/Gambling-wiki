---
title: dev.fun Poker Arena starter kit (arena-pokerkit)
type: entity
tags: [entity, tool, poker, devfun, arena-pokerkit, reference, k102]
keywords: [arena-pokerkit, chenziz, devfun, decide-function, poker-arena, mit]
related:
  - entities/platforms/devfun-poker-arena.md
  - entities/bots/cemini-devfun-poker-agent.md
  - entities/bots/poker-bot-tooling.md
  - entities/tools/pokerskill.md
  - concepts/poker-hl-analyst-loop.md
  - concepts/poker-strategy-overview.md
  - concepts/gambling-bot-architecture.md
  - concepts/opponent-modeling-imperfect-info.md
  - sources/devfun-poker-arena-phase0-2026-06-01.md
  - sources/multi-wiki-tool-eval-v8-k103-2026-06-07.md
  - osint-wiki/sources/multi-wiki-tool-eval-50url-k102-2026-06-06.md
maturity: validated
created: 2026-06-13
updated: 2026-06-15
phase_0_verdict: REFERENCE 2026-06-06 — MIT verified; agent-driven Arena entry path; no CeminiSuite integration
---

## Relations

- @entities/platforms/devfun-poker-arena.md — platform entity + competition ladder
- @entities/bots/cemini-devfun-poker-agent.md — custom `decide()` built on this kit (private repo)
- @concepts/poker-hl-analyst-loop.md — analyze → patch → deploy loop atop starter `decide()` hook
- @osint-wiki/sources/multi-wiki-tool-eval-50url-k102-2026-06-06.md — K102 eval routing (URL 9 UNAVAILABLE → resolved)

## Raw Concept

- **Repo**: [chenziz/arena-pokerkit](https://github.com/chenziz/arena-pokerkit) (canonical; future home noted as `devfun-org/devfun-arena-skills/skills/arena-pokerkit/`)
- **Eval alias**: `devfun-org/poker-arena-starter-kit` — K102 marked UNAVAILABLE; **MIT verified** 2026-06-06
- **K102 brief**: `briefs/2026-06-06_k102-gambling-poker-arena-from-osint.md` (ingested K114)

## Narrative

### What it is

Official **MIT** starter for dev.fun **Poker Arena** — Python kit exposing a top-level `decide(table, allowed_actions, …)` hook, Arena API client, dry-run mock, Colab quickstart, and agent skill (`SKILL.md`). Humans register an agent; the coding agent implements `decide()` and polls pending actions. **Not** a consumer poker-room bot framework.

### Phase-0 audit (K102, 2026-06-06)

| Check | Result |
|-------|--------|
| **License** | **MIT** [CONFIRMED — `gh api` + LICENSE file] |
| **Stars** | ~16★ (K102 snapshot; immature vs rlcard but Arena-official path) |
| **Activity** | Active May 2026 |
| **Fit** | **Gambling-primary** — sanctioned bot arena entry |
| **CeminiSuite / OSINT prod** | **NO-GO** — no trading-stack integration |

**Verdict: REFERENCE** — use for Arena participation and local selfplay gates; complements `@entities/tools/rlcard.md` offline sim only.

### Operator path

1. Clone + `uv sync` (or `pip install git+https://github.com/chenziz/arena-pokerkit`)
2. Implement `decide()` — skeleton in `examples/agent.py`; prod pattern in private `cemini_decide.py`
3. Register agent → `arena_sk_` key → join Playground / Eval competition
4. Optional: `npx skills add chenziz/arena-pokerkit` for Cursor/Claude skill routing

### Boundaries

| In scope | Out of scope |
|----------|--------------|
| dev.fun Arena API (official + beta environments) | PokerStars / Bovada / real-money room automation |
| Local dry-run + benchmark panel | CeminiSuite PM/sports execution |
| HL analyst loop on custom `decide()` | K103 reject cluster (PQL, casinogame playgrounds) — see `@entities/bots/poker-bot-tooling.md` |

### Cross-wiki

- K102 eval source → `@osint-wiki/sources/multi-wiki-tool-eval-50url-k102-2026-06-06.md`
- Offline poker RL sim → `@entities/tools/rlcard.md` (OSINT `.local/venv-gambling-research`)

## Snippets

> "Zero LLM calls at runtime. The deployed bot is pure code." [Source: arena-pokerkit references — HL doctrine]

> K102: "URL 9 marked UNAVAILABLE in eval — resolved MIT (16★, active May 2026)." [Source: @osint-wiki/sources/multi-wiki-tool-eval-50url-k102-2026-06-06.md]

## Dead Ends

- Treating starter-kit Eval bb/100 as proof of Playground qualification edge — panel differs from live fish/maniac mix
- Reusing Arena stack against unsanctioned online poker — ToS / legal NO-GO (`@entities/platforms/pokerstars.md`)
