---
title: IdeaGene-Bench (IG-Bench)
type: entity
tags: [entity, tool, foss, agents, research-eval, k155]
keywords: [ideagene, ig-bench, genomediff, pes, lineage, visionxlab]
related:
  - sources/arxiv-2607.08758-ideas-have-genomes-ig-bench-2026-07-14.md
  - concepts/custom-agent-methodology.md
  - concepts/poker-hl-analyst-loop.md
  - sources/brief-k155-ideagene-lineage-steals-2026-07-14.md
  - sources/daily-digest-batch-k155-2026-07-14.md
maturity: draft
created: 2026-07-14
updated: 2026-07-14
phase_0_verdict: CONDITIONAL-GO
license_verified: NOASSERTION — README License TBD; no LICENSE file 2026-07-14
---

## Relations

- @sources/arxiv-2607.08758-ideas-have-genomes-ig-bench-2026-07-14.md — paper
- @sources/daily-digest-batch-k155-2026-07-14.md — K155 batch
- @concepts/custom-agent-methodology.md — P5 lineage-competence eval
- @concepts/poker-hl-analyst-loop.md — GenomeDiff patch analogy
- @sources/brief-k155-ideagene-lineage-steals-2026-07-14.md — steals

## Raw Concept

| Field | Value |
|-------|-------|
| **GitHub** | https://github.com/VisionXLab/IdeasHaveGenomes |
| **Paper** | arXiv 2607.08758 |
| **Local** | `raw-sources/foss-evals/IdeasHaveGenomes/` (~26MB; gitignored) |
| **Deps** | openai, azure-identity, httpx |

## Phase-0 Audit (2026-07-14)

| Check | Result |
|-------|--------|
| Pricing | Free repo; eval burns OpenAI-compatible API credits |
| TOS | N/A for local exam; API provider TOS applies when running |
| License | **NOASSERTION** — README `## License` = **TBD**; no LICENSE file |
| Size | ~26MB shallow clone — under 500MB adopt budget |
| Failure mode | Incomplete lineage annotations; judge/API cost; compositional false confidence |
| vs wiki | New eval axis — complements DeepSearch-World (K154) + yardstick (K152) |

**Verdict: CONDITIONAL-GO** — steal Idea Genome / GenomeDiff / PES methodology now; do not redistribute or vendor into prod packages until SPDX clears. Re-run Phase-0 when LICENSE lands.

## Narrative

FOSS eval harness for **scientific lineage competence**. Smoke: `python -m gene_exam.evaluators.eval_benchmark --task-type T1-01_contribution_type --max-per-task 2`.

## Dead Ends

- Full daily IG-Arena without cost controls
- Treating as poker solver / wagering edge source
