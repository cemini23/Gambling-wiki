---
title: Poker HL analyst loop (Heuristic Learning)
type: concept
tags: [concept, poker, bots, hl-loop, cemini, devfun, workflow]
keywords: [heuristic-learning, hl-loop, cemini_decide, analyze, preflight, regression-spots, llm-analyst]
related:
  - entities/bots/cemini-devfun-poker-agent.md
  - entities/platforms/devfun-poker-arena.md
  - concepts/gambling-bot-architecture.md
  - concepts/opponent-modeling-imperfect-info.md
  - concepts/poker-strategy-overview.md
  - entities/bots/poker-bot-tooling.md
maturity: validated
created: 2026-06-03
updated: 2026-06-03
---

## Relations

- @entities/bots/cemini-devfun-poker-agent.md — prod `cemini_decide.py` agent
- @entities/platforms/devfun-poker-arena.md — Arena venue + monitor
- @concepts/gambling-bot-architecture.md — bot fleet; HL loop is the **poker lane** iteration pattern
- @osint-wiki/concepts/cemini-knowledge-application-architecture.md — brief → verify → deploy (cross-wiki)
- Code: `agents/devfun-poker-arena/examples/cemini_hl_loop.sh`

## Raw Concept

Operator need: **stop bleeding chips** on dev.fun Playground by closing the loop from live hand history → targeted code patch → gated deploy — without burning time on RL-from-scratch or runtime LLM calls. Pattern mirrors @osint-wiki brief-driven prod iteration, scoped to `cemini_decide.py`.

## Narrative

### What HL is (and is not)

| | HL analyst loop | RL / egress sweep | Level 5 runtime LLM |
|---|-----------------|-------------------|---------------------|
| **When** | After live Arena session | Overnight batch on egress | Every action at runtime |
| **Trainer** | LLM patches `decide()` offline | Parameter grid search | Model inference |
| **Gate** | pytest + regression spots + EP VPIP self-play | Rank profiles for HUD margins | N/A |
| **Cost** | Dev-tool + zero runtime LLM | CPU on egress | Paid per hand |
| **Use** | **Fix Playground leaks now** | Tune exploit margins | Not deployed for Cemini |

**Rule:** Self-play thousands of hands is a **deploy gate** (EP VPIP ≤ 22%, zero EP trash opens, regression corpus green) — **not** the objective function. Optimize against **Arena analyze** worst hands, not self-play bb/100.

### Loop (four steps)

```
1. ANALYZE   arena_monitor / analyze.py → failure report (position + worst hands)
2. PATCH     LLM reads brief (OSINT shape) → ONE leak fix in cemini_decide.py
3. PREFLIGHT pytest + regression + self-play gate + dry-run
4. DEPLOY    rsync cemini-prod + systemctl restart (optional flag)
```

### Commands (try now)

```bash
cd agents/devfun-poker-arena
chmod +x examples/cemini_hl_loop.sh scripts/cemini_preflight.sh

# Live prod hands → brief (stop here; patch in Cursor)
./examples/cemini_hl_loop.sh --from-prod

# Or local creds
./examples/cemini_hl_loop.sh

# After patch
./examples/cemini_hl_loop.sh --preflight-only
./examples/cemini_hl_loop.sh --deploy
```

Artifacts:

| Path | Role |
|------|------|
| `reports/hl-loop/latest_analyze.txt` | Raw Arena failure report |
| `reports/hl-loop/latest_brief.md` | OSINT-shaped patch packet for Cursor |
| `prompts/cemini_hl_analyst_prompt.md` | Analyst rules (cemini_decide only) |
| `tests/fixtures/regression_spots.py` | Frozen leaks from prior analyze |
| `scripts/cemini_preflight.sh` | Single pre-deploy gate |

### Brief shape (OSINT-aligned)

Same sections as @osint-wiki `BRIEF_TEMPLATE.md`: **Target**, **Summary**, **Body**, **Sources**, **Implementation status** — but Target is `examples/cemini_decide.py`, not CeminiSuite. Built by `examples/cemini_hl_brief.py`.

### End-of-session cadence

1. `./examples/cemini_hl_loop.sh --from-prod` — get brief
2. Patch **one** leak; add regression spot if repeat
3. `--preflight-only` then `--deploy`
4. After ~50 hands, `--from-prod --round N+1`

See also `docs/TESTING-CEMINI.md` for the postmortem that motivated the gate stack.

## Snippets

> "Zero LLM calls at runtime. The deployed bot is pure code." — arena-pokerkit HL doctrine [Source: agents/devfun-poker-arena/references/heuristic-learning.md]

> EP VPIP gate: ≤ 22%; EP trash opens must be 0 — `cemini_selfplay_audit.py --gate` [CONFIRMED 2026-06-03]

## Dead Ends

- **Training decide() on self-play bb/100** — misaligns with Playground fish/maniac mix; caused false confidence before S1 bleed
- **Patching `examples/agent.py`** — starter tests only; prod runs `cemini_decide.py`
- **RL-from-scratch on prod timeline** — defer to @entities/bots/poker-bot-tooling.md research lane
