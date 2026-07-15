---
title: Behavioural signatures of risk-sensitive LLM poker (arXiv 2607.10251)
type: source
tags: [source, arxiv, poker, llm-agents, risk, k156]
keywords: [agenttexaspoker, vpip, pfr, risk-plasticity, homogeneous-selfplay, mixed-table]
related:
  - concepts/poker-hl-analyst-loop.md
  - concepts/opponent-modeling-imperfect-info.md
  - concepts/heads-up-arena-strategy.md
  - concepts/custom-agent-methodology.md
  - entities/tools/agent-texas-poker.md
  - sources/brief-k156-risk-sensitive-llm-poker-steals-2026-07-15.md
  - sources/daily-digest-batch-k156-2026-07-15.md
  - sweeps/2026-07-15-daily.md
maturity: draft
read_status: skimmed
created: 2026-07-15
updated: 2026-07-15
location: cemini-egress-fi:/opt/cemini-bulk/research/gambling/arxiv-2607.10251-behavioural-signatures-of-risk-sensitive-decisio.pdf
phase_0_verdict: CONDITIONAL-GO 2026-07-15 — XuankunRong/AgentTexasPoker ~688KB; no SPDX LICENSE; methodology + VPIP/PFR assay Adopt
---

## Relations

- @entities/tools/agent-texas-poker.md — Phase-0 FOSS bench
- @concepts/poker-hl-analyst-loop.md — VPIP/PFR gates + blind-pressure adaptation
- @concepts/opponent-modeling-imperfect-info.md — model-specific risk spectra

## Raw Concept

| Field | Value |
|-------|-------|
| **arXiv** | [2607.10251](https://arxiv.org/abs/2607.10251) |
| **Authors** | Rong, Huang, Du, Tao, Ye |
| **Code** | https://github.com/XuankunRong/AgentTexasPoker |
| **Data** | Hugging Face `XuankunRong/AgentTexasPoker` (logs; not auto-adopted) |
| **Verdict** | **CONDITIONAL-GO** — risk-sensitive NLHE behavioural assay for LLM agents |

## Narrative

Controlled multi-model NLHE framework quantifies LLM risk with **Participation (VPIP)** and **Proactiveness (PFR)**. Homogeneous 6-max self-play reveals stable model-specific spectra (conservative Gemini/Qwen/DeepSeek ≈18–23% VPIP vs aggressive GPT-5.4 ≈45% VPIP / ≈21% PFR). Heterogeneous mixed tables mostly preserve ranks but extremes diverge; outcome equity becomes unequal once styles interact (GPT-5.4 overall WR ≈30.8% mixed vs Gemini ≈8.1%).

**Risk plasticity** under rising blinds (BB 10→200, stack 1000 fixed): broad contraction (Claude/Xiaomi/DeepSeek), selective de-escalation (GPT keeps participation, cuts raise aggression), near-invariant (Gemini). Short-stack personal exposure also yields heterogeneous adaptation.

| Lane | Fit |
|------|-----|
| **Poker arena / HL** | **HIGH** — opponent risk spectra; stack/blind pressure adaptation; JSON decide() parser/retry audit |
| **Custom-agent P5** | **MEDIUM** — behavioural risk probes beyond task accuracy |
| **Bankroll / Kelly** | LOW — not sizing theory |
| **David / TipDrop** | LOW — no persona install |
| **CeminiDFS** | LOW |

Paper disclaimer: poker is a controlled uncertainty assay, not a claim about gambling skill.

## Snippets

> "Frontier LLMs exhibit stable, model-specific risk profiles, forming a spectrum from conservative to aggressive decision styles." [Source: arxiv:2607.10251 Abstract]

> "Under global risk pressure and personal resource constraint, models adapt in structured but heterogeneous ways, ranging from broad behavioural contraction to selective de-escalation and near-invariant behaviour." [Source: arxiv:2607.10251 Abstract]

## Dead Ends

- Importing GPT-5.4 aggression as a Cemini_decide() target
- Treating HF full logs as required laptop adoption (size unknown; code-only Adopt)
- Reading one-hand case studies as skill rankings
