---
title: WC2026-Agents — FIFA World Cup 2026 LLM forecasting vs bookmaker (arXiv 2607.17765)
type: source
tags: [source, arxiv, world-cup, forecasting, llm-agents, sports-betting, calibration, k160]
keywords: [wc2026-agents, fifa2026llm, contamination-free, brier, roi, search-act-reflect, draftkings-odds]
related:
  - entities/tools/wc2026-agents.md
  - entities/sports/world-cup-2026-betting.md
  - concepts/favorite-longshot-bias.md
  - concepts/vig-and-hold.md
  - concepts/sports-betting-fundamentals.md
  - concepts/gambling-bot-architecture.md
  - concepts/custom-agent-methodology.md
  - concepts/poker-hl-analyst-loop.md
  - entities/platforms/draftkings.md
  - sources/brief-k160-wc2026-agents-market-baseline-steals-2026-07-21.md
  - sources/daily-digest-batch-k160-2026-07-21.md
  - sweeps/2026-07-21-daily.md
  - sources/arxiv-2604.27865-kellybench-2026-08-31.md
maturity: validated
read_status: deep-read
created: 2026-07-21
updated: 2026-08-31
location: cemini-egress-fi:/opt/cemini-bulk/research/gambling/arxiv-2607.17765-fifa-world-cup-2026-as-a-contamination-free-benc.pdf
phase_0_verdict: GO 2026-07-21 — graphuofm/FIFA2026LLM MIT code + CC BY 4.0 data; ~3.5MB shallow
---

## Relations

- @entities/tools/wc2026-agents.md — Phase-0 FOSS + dataset
- @entities/sports/world-cup-2026-betting.md — retail WC hub
- @concepts/favorite-longshot-bias.md — favorites over-performed; fade-market loses
- @concepts/gambling-bot-architecture.md — search–act–reflect + market settlement template
- @concepts/poker-hl-analyst-loop.md — calibration vs decision vs self-knowledge axes (light)
- @sources/arxiv-2604.27865-kellybench-2026-08-31.md — EPL LLM betting agents also lose (K168)

## Raw Concept

| Field | Value |
|-------|-------|
| **arXiv** | [2607.17765](https://arxiv.org/abs/2607.17765) |
| **Authors** | Ding, Guo (Memphis); Xu (QuantaInsight) |
| **Repo** | https://github.com/graphuofm/FIFA2026LLM |
| **Dataset** | https://huggingface.co/datasets/dingjiacheng/wc2026-agents |
| **Window** | 104 WC2026 matches · 11 Jun – 19 Jul 2026 |
| **Verdict** | **GO** — market-baseline agentic forecasting benchmark |

## Narrative

Contamination-free agentic forecasting: four consumer frontier assistants (Claude Opus 4.8, ChatGPT GPT-5.5 Thinking, Gemini 3.1 Pro, Grok Expert) ran an identical **search–act–reflect** loop on every WC2026 1X2 match, staking up to $100 virtual against **real pre-match odds** (mostly DraftKings opening previews, vig-removed; mean overround ~1.05). Market is a fifth competitor on calibration only.

**Headline findings** [CONFIRMED — paper §§6–7 + README]

| Axis | Result |
|------|--------|
| **Prediction** | Identical top pick in **92%** of matches; accuracy ~65–68%; **none beats market Brier** (~0.469) |
| **Decision / ROI** | Grok **+$650** (~+10.3% ROI); Gemini +$322; ChatGPT +$118; Claude **−$275** (~−18%) |
| **Fade market** | Contrarian bets hit 21–40%; unprofitable for all four; Claude fades ~58% and is sole net loser |
| **Flat favorite baseline** | Flat $100 on market favorite every match **+$1,041** — beats all agents in absolute $ |
| **Info diet** | Market cited in 100% (Claude) → 12% (Gemini) of reasonings; picks still converge |
| **Self-knowledge** | On own wrong picks, admit “incorrect” **86%** (Gemini) → **36%** (ChatGPT) |
| **Shared misses** | 8 matches fooled everyone (all backed favorite); missed underdog defensive organisation (62%), knockout/penalty variance (32%) |

**Gambling fit**

| Lane | Fit |
|------|-----|
| **WC retail / books** | **HIGH** — market hard to beat; don't fade chalk blindly; price draw→shootout path |
| **Bot / agent eval** | **HIGH** — score calibration **and** staking **and** reflection honesty |
| **Poker HL** | **MEDIUM** — three-axis eval; reflection as deploy fingerprint (not runtime LLM) |
| **CeminiDFS / David** | LOW — soccer tournament; no slate / image path |

**Steals**

1. Always include a **market/price baseline** in forecasting agent evals
2. Separate **calibration · decision quality · self-knowledge** (accuracy alone is a null)
3. Never treat “fade the market” as default LLM alpha
4. Stake sizing is its own axis (Kelly-like confidence coupling vs max-bet habits)
5. Mine blind-spot priors: low-block underdogs; knockout 90' draw settlement vs advance

## Snippets

> "On what will happen, the agents are nearly interchangeable… none beats the market's Brier score… On what to do about it, they diverge sharply: betting ROI spans −18% to +10%" [Source: arxiv:2607.17765 Abstract]

> "fading the market loses money for every agent" [Source: arxiv:2607.17765 Abstract]

> "All betting in this study is virtual; the dataset is a measurement instrument, not gambling advice… no agent beats the market." [Source: arxiv:2607.17765 §9 Ethics]

## Dead Ends

- Treating any agent's +ROI as an actionable WC strategy (favorites over-performed this cup; single-tournament variance)
- Ensemble of same-web agents to cancel shared favorite bias
- Runtime LLM decide() for sportsbook / poker from this protocol
