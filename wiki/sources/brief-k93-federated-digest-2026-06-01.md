---
title: K93 federated daily digest — gambling-wiki install
type: source
tags: [source, brief, meta, federation, k93]
keywords: [k93, daily-digest, federated, automation]
related:
  - meta/daily-research-digest-cadence.md
  - meta/daily-research-digest-cadence.md
  - meta/cross-wiki-routing.md
  - concepts/gambling-wiki-scope.md
maturity: validated
read_status: deep-read
created: 2026-06-01
updated: 2026-06-01
cross-wiki-source: "@osint-wiki/concepts/federated-daily-research-digest.md"
---

## Relations

- @osint-wiki/concepts/federated-daily-research-digest.md — canonical federation concept
- @osint-wiki/sources/multi-wiki-tool-eval-v5-k93-2026-06-01.md — K93 tool eval (no gambling adopts)
- @meta/daily-research-digest-cadence.md — local cadence page

## Raw Concept

| Field | Value |
|-------|-------|
| **Brief** | `briefs/2026-06-01_k93-gambling-digest-from-osint.md` |
| **Target** | gambling-wiki |
| **Action** | Install federated daily digest scripts + LaunchAgent |
| **K93 tool eval** | 34 URLs on @osint-wiki — **zero gambling-surface Adopts** |

## Narrative

### Installed artifacts

- `scripts/daily_research_digest_run.py`, `daily_research_fetch.py` (copied from @osint-wiki)
- `scripts/daily_research_config.yaml` — domain topics (Kalshi retail, PM wagering, bankroll, WC cross-venue)
- `wiki/meta/daily-research-digest-cadence.md`
- `wiki/sweeps/` output directory + `_daily-template.md`
- LaunchAgent `com.cemini.daily-research-digest.gambling` @ 08:15

### K93 tool eval routing

OSINT K93 Adopts (harness, netviz, deptry, goaccess, agents-best-practices) route to **CCC / cybersec / SEO / OSINT** — not duplicated here. Gambling-wiki documents **digest automation** only for this batch.

## Snippets

> Install: `bash .../install_federated_daily_digest.sh ".../Gambling wiki" gambling` [Source: brief K93]

## Dead Ends

- K93 OmniVoice / OGI AGPL — hard reject on @osint-wiki; no gambling-wiki pages
