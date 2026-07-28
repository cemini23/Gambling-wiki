---
title: Daily digest reject cluster K162 (2026-07-28)
type: source
tags: [source, arxiv, daily-digest, reject, k162]
keywords: [digest, reject, 2607.22161, harnessllm, rust, ownership-types]
related:
  - meta/daily-research-digest-cadence.md
  - sweeps/2026-07-28-daily.md
  - sources/daily-digest-batch-k162-2026-07-28.md
maturity: validated
read_status: skimmed
created: 2026-07-28
updated: 2026-07-28
---

## Relations

- @sources/daily-digest-batch-k162-2026-07-28.md — sibling batch

## Raw Concept

| arXiv | Title | Verdict |
|-------|-------|---------|
| 2607.22161 | HarnessLLM: Rust Verification Harness Generation with Large Language Models | **Reject** — Rust memory-safety / BMC harness codegen |

**Archive:** PDF archived with batch to egress-fi.  
**Location:** `cemini-egress-fi:/opt/cemini-bulk/research/gambling/arxiv-2607.22161-harnessllm-rust-verification-harness-generation.pdf`

## Narrative

Wang / Liu / Huang (Ant Group) present HarnessLLM: LLM workflow that extracts API calling scenarios from Rust test suites, synthesizes nondeterministic verification harnesses for bounded model checking, and iteratively repairs fabricated types/APIs. Eval on 9 real-world Rust codebases (294 scenarios, 6 memory-safety bugs found). Pure systems / formal-methods SE. Digest false positive via `cemini-dfs-ownership-paper` — query OR’d bare `ownership` (Rust ownership/borrow checker) with DraftKings/FanDuel; **not** DFS ownership projection, GPP, or copula lineup sims.

## Dead Ends

- Rust ownership types as DFS “ownership %” field
- Verification harness generation as FanDuel MME / pydfs steal
- Autoharness / BMC tooling as poker-arena decide() verifier without a wagering paper
