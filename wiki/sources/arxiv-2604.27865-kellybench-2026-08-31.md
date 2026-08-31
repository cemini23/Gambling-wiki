---
title: KellyBench — LLM agents lose money in sports betting (arXiv 2604.27865)
type: source
tags: [source, arxiv, kelly, sports-betting, llm-agents, k168]
keywords: [kellybench, epl, bankroll, frontier-models, sophistication-rubric]
related:
  - concepts/kelly-criterion-betting.md
  - concepts/bankroll-management.md
  - concepts/gambling-bot-architecture.md
  - entities/sports/nfl-betting.md
  - sources/arxiv-2607.17765-wc2026-agents-llm-forecasting-2026-07-21.md
  - sources/brief-k160-wc2026-agents-market-baseline-steals-2026-07-21.md
  - sources/daily-digest-batch-k168-2026-08-31.md
  - sources/brief-k168-nfl-season-paper-rss-2026-08-31.md
  - meta/daily-research-digest-cadence.md
  - sweeps/2026-08-31-daily.md
maturity: draft
read_status: skimmed
created: 2026-08-31
updated: 2026-08-31
location: cemini-egress-fi:/opt/cemini-bulk/research/gambling/arxiv-2604.27865.pdf
phase_0_verdict: REFERENCE 2026-08-31 — EPL agent bench; pairs K160; no NFL tip bot
wire_status: wont_wire
---

## Relations

- @concepts/kelly-criterion-betting.md — growth-rate staking is the named objective; agents still lose
- @concepts/gambling-bot-architecture.md — LLM-as-bettor is not an NFL season plan
- @entities/sports/nfl-betting.md — same "do not fade the market with a chatbot" rule as K160
- @sources/arxiv-2607.17765-wc2026-agents-llm-forecasting-2026-07-21.md — K160 WC 1X2 sibling (soccer too)
- @sources/brief-k168-nfl-season-paper-rss-2026-08-31.md — operator steals

## Raw Concept

| Field | Value |
|-------|-------|
| **arXiv** | [2604.27865](https://arxiv.org/abs/2604.27865) |
| **Title** | KellyBench: A Benchmark for Long-Horizon Sequential Decision Making |
| **Authors** | Grady, Parker, Zarov, Course, Taylor, Taylor (General Reasoning) |
| **Env** | 2023–24 **English Premier League**; 1X2 + O/U 2.5; ~5.3% vig in the odds |
| **FOSS** | API at `https://openreward.ai/GeneralReasoning/KellyBench`; GitHub search 2026-08-31 **0** SPDX clones |
| **Verdict** | **REFERENCE** — agent eval. Soccer, not NFL. |

## Narrative

Frontier LLMs get historical stats, lineups, and public odds, then must size bets across a season to grow bankroll. **All evaluated models lose money on average across five seeds.** Best mean ROI **−8%** (GPT-5.4). Only 3/25 seeds finish positive; none stay positive when averaged. Several hit ruin. Human-expert sophistication rubric: Claude Opus 4.6 scores **26.5%**. Extra literature + Claude Code harness did not flip the P&L.

This is the same lesson as K160 WC agents: accuracy or a fancy loop is not a market-beating staking policy. NFL sides/totals are at least as sharp as EPL 1X2. **Do not** stand up an LLM pick agent for Week 1.

### Gambling-wiki relevance

| Lane | Fit |
|------|-----|
| **W8 NFL bets** | **HIGH as a negative** — no chatbot tickets |
| **Kelly / bankroll** | **MEDIUM** — growth-rate objective without edge still ruins |
| **Gambling bots** | Eval pattern only; `wont_wire` |
| **FanDuel DFS** | **NONE** — not GPP |

## Snippets

> "We find that all frontier models evaluated lose money on average over the course of the season for five seeds. The best performing model achieves an average return of -8%." [Source: arxiv:2604.27865 Abstract]

> "A predictive model that is more accurate than the public on average need not be profitable, and can lead to ruin if the edge on some bets is wrongly estimated." [Source: arxiv:2604.27865 §1]

## Dead Ends

- Running KellyBench as an NFL Week 1 picker
- Treating −8% EPL ROI as a Hard Rock CLV number
- Cloning the OpenReward API into `/route` or CeminiDFS
