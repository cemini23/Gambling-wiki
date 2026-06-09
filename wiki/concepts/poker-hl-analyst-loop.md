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
updated: 2026-06-09
---

## Relations

- @entities/bots/cemini-devfun-poker-agent.md — prod `cemini_decide.py` agent
- @entities/platforms/devfun-poker-arena.md — Arena venue + monitor
- @concepts/gambling-bot-architecture.md — bot fleet; HL loop is the **poker lane** iteration pattern
- @osint-wiki/concepts/cemini-knowledge-application-architecture.md — brief → verify → deploy (cross-wiki)
- Private repo: `llm-wiki-by-cemini/agents/devfun-poker-arena/` — HL loop scripts

## Raw Concept

Operator need: **stop bleeding chips** on dev.fun Playground by closing the loop from live hand history → targeted code patch → gated deploy — without burning time on RL-from-scratch or runtime LLM calls. Pattern mirrors @osint-wiki brief-driven prod iteration, scoped to `cemini_decide.py`.

## Narrative

### What HL is (and is not)

| | HL analyst loop | RL / egress sweep | Level 5 runtime LLM |
|---|-----------------|-------------------|---------------------|
| **When** | After live Arena session | Overnight batch on egress | Every action at runtime |
| **Trainer** | LLM patches `decide()` offline | Parameter grid search | Model inference |
| **Gate** | pytest + regression spots + self-play sanity checks | Rank profiles for HUD margins | N/A |
| **Cost** | Dev-tool + zero runtime LLM | CPU on egress | Paid per hand |
| **Use** | **Fix Playground leaks now** | Tune exploit margins | Not deployed for Cemini |

**Rule:** Self-play is a **deploy gate** (regression corpus + sanity checks) — **not** the objective function. Optimize against **Arena analyze** worst hands, not self-play bb/100. Specific numeric gates live in private preflight config during competition.

### Selfplay KPI gate (K107, 2026-06-09)

Run before deploy (private repo):

```bash
uv run python examples/cemini_selfplay_audit.py --hands 400 --seed 42 --gate
```

| Metric | Purpose |
|--------|---------|
| **EP VPIP** | Early-position leak detector (default gate ≤22%) |
| **VPIP − PFR gap** | Passive leak — open-spot bug shows gap **>10pp** with low PFR |
| **EP trash opens** | Chart trash raising UTG/MP |

**Open-spot detection:** prod `cemini_decide.py` routes preflop opens via `is_preflop_open_spot()` — handles Arena schema where first-in has `callChips=BB`. Audit 2026-06-09: boolean **fixed**; **PFR 2.1% vs VPIP 12.1%** still flags passive opens — tune `_preflop_open` / chart raise frequency against **live analyze**, not selfplay bb/100 alone.

### Loop (four steps)

```
1. ANALYZE   arena_monitor / analyze.py → failure report (position + worst hands)
2. PATCH     LLM reads brief (OSINT shape) → ONE leak fix in cemini_decide.py
3. PREFLIGHT pytest + regression + self-play gate + dry-run
4. DEPLOY    rsync cemini-prod + systemctl restart (optional flag)
```

### Commands (operator — private repo)

Run from `llm-wiki-by-cemini/agents/devfun-poker-arena/` on an operator machine with arena creds. The HL shell script sources OSINT `source_llm_routing_env.sh` when present (DeepSeek → OpenRouter failover for patch sessions).

Typical cadence: `--from-prod` analyze → patch in Cursor → `--preflight-only` → `--deploy`. Exact paths and flags: private `README-CEMINI.md`.

Artifacts:

| Path | Role |
|------|------|
| `reports/hl-loop/latest_analyze.txt` | Raw Arena failure report (private) |
| `reports/hl-loop/latest_brief.md` | OSINT-shaped patch packet for Cursor (private) |
| `prompts/cemini_hl_analyst_prompt.md` | Analyst rules (private) |
| `tests/fixtures/regression_spots.py` | Frozen leaks from prior analyze (private) |
| `scripts/cemini_preflight.sh` | Single pre-deploy gate (private) |

### Brief shape (OSINT-aligned)

Same sections as @osint-wiki `BRIEF_TEMPLATE.md`: **Target**, **Summary**, **Body**, **Sources**, **Implementation status** — but Target is `examples/cemini_decide.py`, not CeminiSuite. Built by `examples/cemini_hl_brief.py`.

### End-of-session cadence

1. Pull analyze brief from prod (private HL loop)
2. Patch **one** leak; add regression spot if repeat
3. Preflight then deploy
4. After ~50 hands, next analyze round

See private `README-CEMINI.md` for commands.

## Snippets

> "Zero LLM calls at runtime. The deployed bot is pure code." — arena-pokerkit HL doctrine (private references doc)

## Dead Ends

- **Training decide() on self-play bb/100** — misaligns with Playground fish/maniac mix; caused false confidence before S1 bleed
- **Patching `examples/agent.py`** — starter tests only; prod runs `cemini_decide.py`
- **RL-from-scratch on prod timeline** — defer to @entities/bots/poker-bot-tooling.md research lane
