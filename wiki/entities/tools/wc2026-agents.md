---
title: WC2026-Agents (FIFA2026LLM)
type: entity
tags: [entity, tool, foss, world-cup, forecasting, llm-agents, sports-betting, k160]
keywords: [wc2026-agents, fifa2026llm, graphuofm, contamination-free-benchmark]
related:
  - sources/arxiv-2607.17765-wc2026-agents-llm-forecasting-2026-07-21.md
  - entities/sports/world-cup-2026-betting.md
  - concepts/gambling-bot-architecture.md
  - concepts/favorite-longshot-bias.md
  - concepts/poker-hl-analyst-loop.md
  - concepts/custom-agent-methodology.md
  - entities/platforms/draftkings.md
  - sources/brief-k160-wc2026-agents-market-baseline-steals-2026-07-21.md
  - sources/daily-digest-batch-k160-2026-07-21.md
maturity: draft
created: 2026-07-21
updated: 2026-07-21
phase_0_verdict: GO
license_verified: MIT (code) + CC BY 4.0 (data/) — LICENSE file 2026-07-21
---

## Relations

- @sources/arxiv-2607.17765-wc2026-agents-llm-forecasting-2026-07-21.md — paper
- @entities/sports/world-cup-2026-betting.md — WC wagering hub
- @concepts/gambling-bot-architecture.md — agent loop template
- @entities/platforms/draftkings.md — primary odds source in benchmark

## Raw Concept

| Field | Value |
|-------|-------|
| **GitHub** | https://github.com/graphuofm/FIFA2026LLM |
| **HF Dataset** | https://huggingface.co/datasets/dingjiacheng/wc2026-agents |
| **Paper** | arXiv 2607.17765 |
| **Local** | `raw-sources/foss-evals/FIFA2026LLM/` (~9.3MB; gitignored) |
| **Reproduce** | `pip install -r requirements.txt` · `python src/run_all.py` |

## Phase-0 Audit (2026-07-21)

| Check | Result |
|-------|--------|
| Pricing | Free code + HF data; no paid API required for offline analysis |
| TOS | Research dataset; virtual bets only; public odds URLs |
| License | **MIT** code · **CC BY 4.0** `data/` |
| Size | ~9.3MB shallow clone — under 500MB |
| Failure mode | Single-tournament; opening-line odds (mostly one book); consumer-UI retrieval not API-controlled |
| vs wiki | Complements WC retail pages — **market-as-baseline agent eval**, not a tip sheet |

**Verdict: GO** — adopt eval methodology + local FOSS; do not treat agent P&L as betting advice.

## Narrative

Releases 416 forecasts + 414 reflections across 104 WC2026 matches with vig-removed 1X2 odds, ground truth (incl. penalty shootouts), and analysis/figure pipeline. Primary steal: three-axis scoring (calibration / decision / self-knowledge) with bookmaker as fifth competitor.

## Dead Ends

- Live sportsbook bot from transcripts
- Nightly multi-model consumer-UI scrape without cost/ToS review
- Claiming LLM alpha over closing consensus (paper uses opening lines)
