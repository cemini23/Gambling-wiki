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
  - osint-wiki/sources/trading-posts-compilation-7-2026-06-09.md
maturity: validated
created: 2026-06-03
updated: 2026-06-13
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

### Open-spot bug (K107, @3d64r_89 Post 16) [CONFIRMED]

Classic preflop misdetection when porting from generic poker engines to Arena schema:

| Anti-pattern | Symptom | Fix |
|--------------|---------|-----|
| `call_chips == 0` marks "open" | Non-blind first-to-act has `callChips = BB > 0` → treated as **facing a bet** → limp-heavy | Open when **`current_bet <= big_blind`** |
| Bug signature | VPIP ~**23%**, PFR ~**6%**, gap ~**17pp** | TAG target: VPIP 10–16%, PFR within ~5pp of VPIP |

```python
bb = int(table.get("bigBlindChips") or 20)
current_bet = int(table.get("currentBetChips") or table.get("currentBet") or 0)
is_open_spot = current_bet <= bb
```

**Audit 2026-06-09:** prod uses `is_preflop_open_spot()` in private `opponent_target.py` (handles `callChips=BB` for UTG first-in; `max_bet <= bb and pot <= blinds_pot + 2`). Raw `call_chips==0` on L719 is **postflop free-action only** — not preflop open routing. Source: `@osint-wiki/sources/trading-posts-compilation-7-2026-06-09.md` Post 16.

### Selfplay KPI gate (K107 audit, 2026-06-09)

Run before deploy (private repo):

```bash
uv run python examples/cemini_selfplay_audit.py --hands 400 --seed 42 --gate
```

| Metric | Result (400h) | K107 bug signature | S1 rock target |
|--------|---------------|-------------------|----------------|
| **VPIP** | **12.1%** | ~23% | 10–16% |
| **PFR** | **2.1%** | ~6% | ≈ VPIP (−5pp) |
| **VPIP − PFR gap** | **~10pp** | ~17pp | ~5pp |
| **EP VPIP** | 5.7% | — | gate ≤22% |
| **EP trash opens** | 0 | — | gate 0 |

Open-spot boolean is **fixed**; **passive PFR leak persists** — `_preflop_open` / chart path likely **checking or calling** where raise expected. Tune against **live Arena analyze** (log `spot_kind()` on first hero preflop decision), not selfplay bb/100 alone. Brief: `briefs/2026-06-09_k107-gambling-poker-open-spot-AUDIT.md`.

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
