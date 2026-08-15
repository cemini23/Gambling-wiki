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
  - sources/brief-k118-poker-agent-research-gaps-2026-06-17.md
  - sources/brief-k107-poker-open-spot-audit-2026-06-09.md
  - concepts/custom-agent-methodology.md
  - sources/arxiv-2606.11869-agents-all-the-way-down-2026-06-19.md
  - concepts/heads-up-arena-strategy.md
  - sources/brief-k125-eval-gate-discipline-2026-06-22.md
  - sources/devfun-researcher-sandbox-bundle-discord-2026-06-20.md
  - sources/brief-k124-mafp-memory-poker-steals-2026-06-21.md
  - sources/arxiv-2606.19308-mafp-multi-agent-fictitious-play-2026-06-21.md
  - sources/brief-k126-garip-selfplay-pm-forecast-steals-2026-06-23.md
  - sources/arxiv-2606.22688-garip-last-iterate-selfplay-2026-06-23.md
  - sources/arxiv-2606.23995-emagnet-selfplay-regularization-2026-06-24.md
  - sources/brief-k127-emagnet-irumai-selfplay-steals-2026-06-24.md
  - sources/brief-k129-celeus-tmax-eval-steals-2026-06-25.md
  - sources/arxiv-2606.25819-toolbench-x-tool-unreliability-2026-06-26.md
  - sources/brief-k131-toolbench-ganzfried-steals-2026-06-26.md
  - sources/arxiv-2606.20785-fara-computer-use-agents-2026-06-27.md
  - sources/brief-k132-fara-agent-env-steals-2026-06-27.md
  - sources/arxiv-2606.26294-red-queen-godel-machine-2026-06-29.md
  - sources/brief-k133-rqgm-evaluator-steals-2026-06-29.md
  - sources/brief-k134-ganzfried-ped-deal-games-steals-2026-06-30.md
  - sources/arxiv-2606.29169-ganzfried-ped-nash-imperfect-info-2026-06-30.md
  - sources/arxiv-2606.29457-takeover-auction-diligence-games-2026-06-30.md
  - sources/brief-k136-tool-rl-collapse-steals-2026-07-02.md
  - sources/arxiv-2606.26027-tool-rl-collapse-supervisory-signals-2026-07-02.md
  - sources/arxiv-2606.30573-swe-interact-user-driven-coding-agents-2026-07-03.md
  - sources/brief-k149-policy-ssl-advent-poker-steals-2026-07-07.md
  - sources/brief-k152-expert-yardstick-forgetting-regret-steals-2026-07-11.md
  - sources/brief-k153-mppo-style-pm-evidence-steals-2026-07-12.md
  - sources/brief-k154-metagame-memory-search-steals-2026-07-13.md
  - sources/arxiv-2607.08692-pokemon-tcg-nash-lean-metagame-2026-07-13.md
  - sources/arxiv-2607.07666-ensemble-qsp-hierarchical-memory-2026-07-13.md
  - sources/devfun-sandbox-researcher-guide-2026-06-26.md
  - sources/arxiv-2607.08758-ideas-have-genomes-ig-bench-2026-07-14.md
  - sources/brief-k155-ideagene-lineage-steals-2026-07-14.md
  - entities/tools/ideagene-bench.md
  - sources/arxiv-2607.10251-risk-sensitive-llm-poker-2026-07-15.md
  - sources/brief-k156-risk-sensitive-llm-poker-steals-2026-07-15.md
  - entities/tools/agent-texas-poker.md
  - sources/arxiv-2607.14169-play-adequacy-code-world-models-2026-07-17.md
  - sources/brief-k158-play-adequacy-cwm-steals-2026-07-17.md
  - entities/tools/code-world-models.md
  - sources/arxiv-2607.08043-aleena-alignment-agent-2026-07-18.md
  - sources/brief-k159-aleena-decision-continuity-steals-2026-07-18.md
  - entities/tools/aleena.md
  - sources/arxiv-2607.17765-wc2026-agents-llm-forecasting-2026-07-21.md
  - sources/brief-k160-wc2026-agents-market-baseline-steals-2026-07-21.md
  - entities/tools/wc2026-agents.md
  - sources/arxiv-2607.23333-swap-regret-attention-2026-07-29.md
  - sources/brief-k163-swap-regret-attention-shelf-2026-07-29.md
  - sources/arxiv-2607.27035-ccs-mccfr-2026-07-30.md
  - sources/brief-k164-ccs-mccfr-chance-sampling-steals-2026-07-30.md
  - sources/arxiv-2607-28520-cs-rnr-safe-opponent-exploitation.md
  - sources/arxiv-2608.09389-regret-equilibrium-learning-games-guide-2026-08-12.md
  - sources/arxiv-2608.09256-distributed-team-orchestration-supervisor-2026-08-12.md
  - sources/daily-digest-batch-k166-2026-08-12.md
  - sources/brief-k166-regret-learning-games-shelf-2026-08-12.md
  - sources/brief-k271-redagentbench-arena-eval-2026-08-12.md
maturity: validated
created: 2026-06-03
updated: 2026-08-15
---

## Relations

- @entities/bots/cemini-devfun-poker-agent.md — prod `cemini_decide.py` agent @sources/arxiv-2607-28520-cs-rnr-safe-opponent-exploitation.md
- @entities/platforms/devfun-poker-arena.md — Arena venue + monitor
- @sources/brief-k118-poker-agent-research-gaps-2026-06-17.md — research → agent gap matrix + fix backlog
- @sources/brief-k107-poker-open-spot-audit-2026-06-09.md — K107 open-spot audit + selfplay KPI baseline
- @concepts/custom-agent-methodology.md — HL loop as P3→P4→P5 instance (K120)
- @concepts/gambling-bot-architecture.md — bot fleet; HL loop is the **poker lane** iteration pattern
- @sources/brief-k155-ideagene-lineage-steals-2026-07-14.md — K155 GenomeDiff patch-lineage steal
- @sources/arxiv-2607.08758-ideas-have-genomes-ig-bench-2026-07-14.md — IdeaGene-Bench
- @sources/brief-k156-risk-sensitive-llm-poker-steals-2026-07-15.md — K156 VPIP/PFR risk spectra
- @entities/tools/agent-texas-poker.md — AgentTexasPoker FOSS assay
- @sources/brief-k158-play-adequacy-cwm-steals-2026-07-17.md — K158 play-adequacy ship gates
- @entities/tools/code-world-models.md — CWM play-adequacy FOSS
- @sources/brief-k159-aleena-decision-continuity-steals-2026-07-18.md — K159 decision/risk continuity
- @entities/tools/aleena.md — Aleena FOSS (CONDITIONAL-GO)
- @sources/brief-k160-wc2026-agents-market-baseline-steals-2026-07-21.md — K160 three-axis eval / market baseline
- @entities/tools/wc2026-agents.md — WC2026-Agents FOSS (GO)
- @sources/arxiv-2607.23333-swap-regret-attention-2026-07-29.md — K163 swap-regret / smoothed FP theory shelf
- @sources/brief-k163-swap-regret-attention-shelf-2026-07-29.md — K163 shelf (confirm OSINT K198 docs)
- @sources/arxiv-2607.27035-ccs-mccfr-2026-07-30.md — K164 CCS-MCCFR offline sampler steal
- @sources/brief-k164-ccs-mccfr-chance-sampling-steals-2026-07-30.md — K164 steals (research branch only)
- @sources/arxiv-2608.09389-regret-equilibrium-learning-games-guide-2026-08-12.md — K166 FTRL/FP literacy shelf (no HL import)
- @sources/arxiv-2608.09256-distributed-team-orchestration-supervisor-2026-08-12.md — K166 team-FP supervisor shelf (no HL import)
- @sources/brief-k166-regret-learning-games-shelf-2026-08-12.md — K166 shelf (wont_wire)
- @sources/brief-k271-redagentbench-arena-eval-2026-08-12.md — faithful eval / harness-tuple (wont_wire)
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

### Eval measurement (K271) [REFERENCE]

When comparing agent variants, grade from **durable state** (ledger / chip receipts / API diffs), not the transcript. Report metrics as a `(harness, judging config, evaluation cue, judge backbone)` tuple — the same agent+scenario can swing tens of points from scaffolding alone. Restate the applicable constraint at each action boundary (“says the rule then violates it”). Paper: arXiv:2608.10669. Hub: `@sources/brief-k271-redagentbench-arena-eval-2026-08-12.md`. **wont_wire** — no `decide()` import.

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

### Selfplay KPI gate (K107 audit + K118 refresh)

Run before deploy (private repo):

```bash
uv run python examples/cemini_selfplay_audit.py --hands 400 --seed 42 --gate
```

| Metric | 2026-06-09 | **2026-06-17** | K107 bug signature | S1 rock target |
|--------|------------|----------------|-------------------|----------------|
| **VPIP** | 12.1% | **11.5%** | ~23% | 10–16% |
| **PFR** | 2.1% | **2.2%** | ~6% | ≈ VPIP (−5pp) |
| **VPIP − PFR gap** | ~10pp | **~9pp** | ~17pp | ~5pp |
| **SB VPIP** | — | **13.4%** | — | limp inflation |
| **EP VPIP** | 5.7% | **5.6%** | — | gate ≤22% |
| **EP trash opens** | 0 | **0** | — | gate 0 |

Open-spot boolean is **fixed**; **passive PFR leak persists** — `_preflop_open` fallthrough to `check`, SB complete path, and rock `open_steal_equity` ~0.99 suppress steals. **No PFR gate in `--gate` today** — K118 adds F1 (min PFR + max gap). Tune against **live Arena analyze** (log `spot_kind()` on first hero preflop decision), not selfplay bb/100 alone. Briefs: K107 audit; **K118** `@sources/brief-k118-poker-agent-research-gaps-2026-06-17.md`.

### Research vs agent gaps (K118) [CONFIRMED 2026-06-17]

| Research theme | Literature | Agent today | Fix lane |
|----------------|------------|-------------|----------|
| Multi-hand exploit | AlphaExploitem (arXiv:2605.09150) | `session_memory.py` aggression counts only | F6: showdown queue per villain |
| Solver tool use | ToolPoker (arXiv:2602.00528) | No runtime LLM (correct) | F12–F13: offline river lookup + PokerSkill |
| Consistent OM | COM (arXiv:2508.17671) | HUD margins + chart | Defer full COM |
| Eval vs live mix | Eval S1 DeepCFR panel | Playground fish/maniac analyze | F9–F11: separate eval cadence |
| Open frequency | TAG 6-max doctrine | PFR 2.2% | **P0 F1–F5** |

Do **not** optimize for selfplay bb/100; do **not** add runtime LLM decide() for ToolPoker parity.

### Loop (four steps)

Maps to @concepts/custom-agent-methodology.md **P3→P4→P5** (offline LLM patch + shipped CLI artifact + behavioral gate):

```
1. ANALYZE   arena_monitor / analyze.py → failure report (position + worst hands)   [P3]
2. PATCH     LLM reads brief (OSINT shape) → ONE leak fix in cemini_decide.py        [P3]
3. PREFLIGHT pytest + regression + self-play gate + dry-run                          [P5]
4. DEPLOY    rsync cemini-prod + systemctl restart (optional flag)                   [P4 ship]
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

### Patch lineage (K155 IdeaGene) [TENTATIVE]

@sources/arxiv-2607.08758-ideas-have-genomes-ig-bench-2026-07-14.md: treat successive HL patches as **GenomeDiff** — record parent mechanism Inherited / Mutated / Lost / Novel. Reject steals that share poker/task ecology without a driver-mechanism link. Pairs P5 joint-consistency gates.

### Risk spectra under pressure (K156 AgentTexasPoker) [TENTATIVE]

@sources/arxiv-2607.10251-risk-sensitive-llm-poker-2026-07-15.md: LLM / AI foes have stable **VPIP/PFR** profiles and unequal plasticity when blinds or stacks burn. Re-check open/3-bet gates by pressure band; separate entry contraction from raise de-escalation. JSON parse/retry telemetry should not count as folds.

### Play-adequacy gates (K158 Code World Models) [TENTATIVE]

@sources/arxiv-2607.14169-play-adequacy-code-world-models-2026-07-17.md: transition-accuracy / log-match gates can pass while play loses — rare pivotal omissions evade sampling with probability `(1−rarity)^N`. Prefer play / search-distribution regression; complete the heuristic spec instead of flooding similar hands.

### Decision continuity across patch sessions (K159) [TENTATIVE]

@sources/arxiv-2607.08043-aleena-alignment-agent-2026-07-18.md: offline HL analyze→patch→preflight should leave structured **decisions / risks / open questions**, not only a patch file — reduces lost context between sessions. Vocabulary-drift checks on Arena/heuristic terms when definitions conflict. Do not auto-merge draft PRs; runtime `decide()` stays pure code.

### End-of-session cadence

1. Pull analyze brief from prod (private HL loop)
2. Patch **one** leak; add regression spot if repeat
3. Preflight then deploy
4. After ~50 hands, next analyze round

See private `README-CEMINI.md` for commands.

### Researcher sandbox harness (K131) [CONFIRMED 2026-06-26]

HL loop fixes **`decide()` policy**; researcher **bundle submit** adds **`arena-tool` MCP** hazard layer (@sources/arxiv-2606.25819-toolbench-x-tool-unreliability-2026-06-26.md). Function-call correctness ≠ match completion — harness needs retry/fallback on timeout, schema drift, and `reasoning_text` rejection.

**FaraGen verifier triad** (K132 — @sources/arxiv-2606.20785-fara-computer-use-agents-2026-06-27.md): private bundle regression should score **correctness**, **efficiency**, and **critical-point adherence** alongside K131 hazard injection. See @sources/brief-k132-fara-agent-env-steals-2026-06-27.md.

**RQGM eval epochs** (K133 — @sources/arxiv-2606.26294-red-queen-godel-machine-2026-06-29.md): static regression gates drift as policy improves — version private eval utility per **epoch** (frozen within epoch, changelog at boundary). Optional co-evolved agent-as-judge on `reasoning_text` before full sim; adversarial epoch if PvE panel over-accepts AI bundles. See @sources/brief-k133-rqgm-evaluator-steals-2026-06-29.md.

**Exploitability literacy** (K134 — @sources/arxiv-2606.29169-ganzfried-ped-nash-imperfect-info-2026-06-30.md, @sources/arxiv-2606.29457-takeover-auction-diligence-games-2026-06-30.md): multiplayer Nash ε(σ) and FP-PED hybrid are **theory anchors** — selfplay `--gate` and TrueSkill are **not** exploitability certificates. See @sources/brief-k134-ganzfried-ped-deal-games-steals-2026-06-30.md.

**Tool-RL structural collapse** (K136 — @sources/arxiv-2606.26027-tool-rl-collapse-supervisory-signals-2026-07-02.md): if fine-tuning sandbox MCP bundle agents, use **interleaved SFT + RL** on golden `arena-tool` trajectories; monitor polluted/collapsed tool formats. See @sources/brief-k136-tool-rl-collapse-steals-2026-07-02.md.

**SWE-INTERACT partial-spec eval** (K137 — @sources/arxiv-2606.30573-swe-interact-user-driven-coding-agents-2026-07-03.md): offline analyze briefs are **user-driven** (vague → evolving requirements). Add private scenarios that test requirement memory and mid-loop constraint reveals — single-turn MCP pass is insufficient. See @sources/brief-k137-swe-interact-rlvr-nfl-steals-2026-07-03.md.

**Constraint substrate + cognitive security** (K148 — @sources/arxiv-2607.02389-steerability-constraints-coding-agents-2026-07-06.md, @sources/arxiv-2606.30587-llm-vuln-detection-cognitive-heuristics-2026-07-06.md): enforce linters/docs CLI on bundle repo; treat LLM vuln triage on analyze output as **advisory** — preflight + regression remain deploy gates. See @sources/brief-k148-agent-framework-pm-betting-steals-2026-07-06.md.

**Policy SSL + ADVENT spot taxonomy** (K149 — @sources/arxiv-2607.01498-policy-representation-ssl-poker-2026-07-07.md, @sources/arxiv-2607.01585-advent-ilp-poker-predicate-invention-2026-07-07.md): Leduc policy embeddings for opponent archive; LLM→verify loop for named regression-spot predicates. See @sources/brief-k149-policy-ssl-advent-poker-steals-2026-07-07.md.

**Expert yardstick + forgetting regret** (K152 — @sources/arxiv-2607.06854-lightweight-game-agent-expert-yardstick-2026-07-11.md, @sources/arxiv-2607.07078-forgetting-factor-regret-zero-sum-2026-07-11.md): regression gates vs fixed exploit/expert pool (not self-play Elo alone); recency-weighted regret when league drifts. See @sources/brief-k152-expert-yardstick-forgetting-regret-steals-2026-07-11.md.

**MPPO style-preserving league upgrade** (K153 — @sources/arxiv-2506.16995-mppo-style-preserving-game-agents-2026-07-12.md): demonstration-mixed RL when strengthening stylized opponents; track style drift on promotion. See @sources/brief-k153-mppo-style-pm-evidence-steals-2026-07-12.md.

**Metagame Nash + bounded memory** (K154 — @sources/arxiv-2607.08692-pokemon-tcg-nash-lean-metagame-2026-07-13.md, @sources/arxiv-2607.07666-ensemble-qsp-hierarchical-memory-2026-07-13.md): field share ≠ Nash EV; hierarchical capped epoch memory with eviction. See @sources/brief-k154-metagame-memory-search-steals-2026-07-13.md.

**Market-baseline three-axis eval** (K160 — @sources/arxiv-2607.17765-wc2026-agents-llm-forecasting-2026-07-21.md): accuracy-only gates can be a null when agents converge. Pair variants with a hard non-LLM baseline; separately track calibration, policy P&L vs baseline, and reflection/admit-wrong honesty. See @sources/brief-k160-wc2026-agents-market-baseline-steals-2026-07-21.md / @entities/tools/wc2026-agents.md.

**FTRL / FP literacy shelf (K166 — @sources/arxiv-2608.09389-regret-equilibrium-learning-games-guide-2026-08-12.md, @sources/arxiv-2608.09256-distributed-team-orchestration-supervisor-2026-08-12.md):** two REFERENCE papers, `wont_wire`. 09389 (Mertikopoulos) gives the unified regularized-learning story behind FP/MAFP — Brown–Robinson convergence, zero-sum ergodic Gap bound, folk theorem (strict NE attract, mixed NE avoided by EXP3-style play). Read as literacy next to K163/K157/K152, not as a patch source. 09256 (DTOA/BR-DTOA) is team-FP over supervisor beliefs with Byzantine resilience — shelf-only adjacency to MAFP, **no** decide()/HL import. No FOSS for either (09256 claimed repo HTTP 404).

## Snippets

> "Zero LLM calls at runtime. The deployed bot is pure code." — arena-pokerkit HL doctrine (private references doc)

## Dead Ends

- **Training decide() on self-play bb/100** — misaligns with Playground fish/maniac mix; caused false confidence before S1 bleed
- **Patching `examples/agent.py`** — starter tests only; prod runs `cemini_decide.py`
- **RL-from-scratch on prod timeline** — defer to @entities/bots/poker-bot-tooling.md research lane
