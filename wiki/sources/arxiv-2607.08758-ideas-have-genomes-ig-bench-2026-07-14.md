---
title: Ideas Have Genomes — IdeaGene-Bench lineage reasoning (arXiv 2607.08758)
type: source
tags: [source, arxiv, agents, research-eval, lineage, k155]
keywords: [ideagene, ig-bench, genome-diff, lineage-reasoning, pes, scientific-lineage]
related:
  - concepts/custom-agent-methodology.md
  - concepts/poker-hl-analyst-loop.md
  - concepts/gambling-bot-architecture.md
  - entities/tools/ideagene-bench.md
  - sources/brief-k155-ideagene-lineage-steals-2026-07-14.md
  - sources/daily-digest-batch-k155-2026-07-14.md
  - sweeps/2026-07-14-daily.md
maturity: draft
read_status: skimmed
created: 2026-07-14
updated: 2026-07-14
location: cemini-egress-fi:/opt/cemini-bulk/research/gambling/arxiv-2607.08758-2607-08758v1-ideas-have-genomes-benchmarking-sci.pdf
phase_0_verdict: CONDITIONAL-GO 2026-07-14 — VisionXLab/IdeasHaveGenomes ~26MB; no SPDX LICENSE file (README License section present); methodology Adopt, code WATCH until license clears
---

## Relations

- @entities/tools/ideagene-bench.md — Phase-0 entity
- @concepts/custom-agent-methodology.md — lineage competence as P5 eval dimension
- @concepts/poker-hl-analyst-loop.md — GenomeDiff analogy for patch inheritance

## Raw Concept

| Field | Value |
|-------|-------|
| **arXiv** | [2607.08758](https://arxiv.org/abs/2607.08758) |
| **Authors** | Zhou, Yang, Li, et al. (SJTU / CMU / MS / others) |
| **Repo** | https://github.com/VisionXLab/IdeasHaveGenomes |
| **Project** | https://visionxlab.github.io/IdeasHaveGenomes/ |
| **Verdict** | **CONDITIONAL-GO** — Idea Genome / GenomeDiff / PES methodology; FOSS eval harness local (~26MB) |

## Narrative

Scientific ideas inherit mechanisms, repair limitations, and recombine — paper-level retrieval/citation graphs blur this. **IdeaGene** represents each paper as typed, evidence-grounded **Idea Genome** objects (`niche`, `mechanism`, `observation`, `limitation`, `delta`, `claim`). **GenomeDiff** aligns predecessor→successor with Inherited / Mutated / Lost / Novel / External under six operational dynamics.

**IG-Bench:** 1,961 golden lineage traces · 1,085 Idea Genomes · 920 GenomeDiffs · 10 domains.

| Track | Role |
|-------|------|
| **IG-Exam** | 42 task types, 1,029 instances — abstraction, inheritance, evolutionary reasoning, verification |
| **IG-Arena** | Open-ended generation scored by **PES** (Heredity · Variation · Selection) under Question-only / Library / Lineage contexts |

**Empirical:** best of 14 LLM scientists ≈ **27.3% exact** on lineage exam; compositional bottleneck (local signals OK, joint consistency fails). Structured lineage context **reshuffles rankings** rather than helping everyone uniformly.

| Lane | Fit |
|------|-----|
| **CCC / research harness** | **HIGH** — eval whether proposals inherit the right mechanism, not topical proximity |
| **Poker HL loop** | **MEDIUM** — treat successive `decide()` patches as GenomeDiff (mechanism inherited vs mutated vs lost) |
| **PM evidence agents** | **MEDIUM** — reject topical co-location as lineage; require mechanism inheritance in briefs |
| **CeminiDFS / sportsbook** | LOW |
| **David / TipDrop** | LOW — no Comfy/Fish install path (eval-only if TipDrop adds auto-research) |

## Snippets

> "Scientific ideas rarely start from a blank page. They inherit mechanisms, repair known limitations, and recombine pieces of earlier work, much like biological genomes." [Source: arxiv:2607.08758 Abstract]

> "The strongest system reaches only 27.3% exact accuracy on lineage reasoning, and structured lineage context reshuffles system rankings rather than helping every participant uniformly." [Source: arxiv:2607.08758 Abstract]

## Dead Ends

- Treating citation edges as GenomeDiff
- Running full IG-Arena against paid APIs as a daily ritual without cost cap
- Shipping repo code into prod before SPDX license lands
