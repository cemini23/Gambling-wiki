# Gambling & Betting Wiki

> Public knowledge hub for **sports betting, casino games, poker, DFS, best ball, and prediction-market wagering** (consumer/strategy angle). LLM-managed, human-read.

## What this is

This workspace is a **librarian** for betting and gambling research. It:

- **Manages** raw sources (books, PDFs, course notes, repo snapshots, transcripts) you drop into `research to be indexed/`
- **Curates** them into an interlinked wiki under `wiki/` — platforms, tools, games, sports, and strategy concepts
- **Applies** them via briefs in `briefs/` for slate prep, study plans, and bankroll frameworks

## Quick start

1. Read `CLAUDE.md` — schema the LLM follows each session
2. Read `ROADMAP.md` — active workstreams
3. Copy `.env.example` → `.env` (optional Exa/Brave keys for external research)
4. Drop a source into `research to be indexed/` and ask Claude/Cursor to ingest it
5. Lint: `python3 scripts/wiki_lint.py`

**CI (GitHub):** wiki lint only on push — no agent pytest in this public repo.

## Where code lives

| Content | Repo / path |
|---------|-------------|
| **This wiki** (public) | `wiki/`, `LESSONS.md`, `ROADMAP.md` |
| **dev.fun arena bot** (`cemini_decide`, deploy, briefs) | Private [llm-wiki-by-cemini](https://github.com/cemini23/llm-wiki-by-cemini) → `agents/devfun-poker-arena/` (open **OSINT WORKSPACE** locally) |
| **PM / CeminiSuite bots** | Same private osint repo — see `@osint-wiki` |

Public clone gets `agents/README.md` only (pointer stub). Do not commit competition strategy here.

## Folder layout

```
Gambling-wiki/
  CLAUDE.md
  README.md
  LESSONS.md
  ROADMAP.md
  agents/README.md          # stub → private bot repo (implementation gitignored)
  wiki/
    index.md              # catalog
    log.md                # operations log
    entities/
      platforms/          # sportsbooks, DFS sites, PM venues, poker rooms
      tools/              # odds services, optimizers, trackers
      games/              # poker, blackjack, craps, …
      sports/             # NFL, NBA, …
      people/
    concepts/             # bankroll, Kelly, DFS, house edge, …
    sources/
  scripts/                # wiki_lint.py, preingest_check.py
  prompts/
```

## Cemini wiki federation

**Eight** wikis + private **Cemini Financial Suite**. Cross-links: `@<alias>/path/to/page.md` (`CLAUDE.md` → Related Wikis).

| Alias | Repository | Focus |
|-------|------------|--------|
| **`gambling-wiki`** | **This repo** | Sports betting, casino, poker, DFS, best ball |
| `game-dev-wiki` | [Game-Dev-wiki](https://github.com/cemini23/Game-Dev-wiki) | Castle/RTS hobby dev, Godot evals, agent harness |
| `osint-wiki` | *private* ([llm-wiki-by-cemini](https://github.com/cemini23/llm-wiki-by-cemini)) | PM bots, dev.fun arena bot code, CeminiSuite, quant OSINT |
| `ccc-wiki` | [cemini-claude-code-CCC](https://github.com/cemini23/cemini-claude-code-CCC) | Agent workflow, MCP, skills |
| `cybersecurity-wiki` | [Cybersecurity-wiki](https://github.com/cemini23/Cybersecurity-wiki) | Pentest, SOC |
| `seo-wiki` | [SEO-GEO-B-M-Wiki](https://github.com/cemini23/SEO-GEO-B-M-Wiki) | Local SEO, creator ops |
| `3d-printing-wiki` | [3D-Printing-Wiki](https://github.com/cemini23/3D-Printing-Wiki) | FDM/print farms |
| `image-gen-wiki` | [uncensored-image-gen-wiki](https://github.com/cemini23/uncensored-image-gen-wiki) | ComfyUI, LoRA |

Cross-links: `@gambling-wiki/concepts/bankroll-management.md` ↔ `@osint-wiki/concepts/kelly-sizing-quarter.md`

```bash
git clone https://github.com/cemini23/Gambling-wiki.git
```

## Privacy

- `.env`, `raw-sources/`, `briefs/`, `hot.md`, and `agents/devfun-poker-arena/` are gitignored
- Never commit API keys, arena credentials (`.arena-credentials`), account PII, or live competition intel (ranks, leak clusters, patch toggles)

## Related

- Methodology newsletter: [Outlier Weekly Issue 3 — World Cup Bot](https://outlierweekly.substack.com/p/i-open-sourced-the-world-cup-lp-bot) · [home](https://outlierweekly.substack.com)
- YouTube: [@Cemini23](https://www.youtube.com/@Cemini23)
- Wiki federation hub: [cemini-claude-code-CCC](https://github.com/cemini23/cemini-claude-code-CCC)
- **World Cup LP bot (automation):** [world-cup-bot](https://github.com/cemini23/world-cup-bot) — shadow-first Polymarket LP + Kalshi gap alerts; launch writeup: [Issue 3](https://outlierweekly.substack.com/p/i-open-sourced-the-world-cup-lp-bot); pairs with `@gambling-wiki/entities/sports/world-cup-2026-betting.md`
- Tooling: [wikilint](https://github.com/cemini23/wikilint) · [vet](https://github.com/cemini23/vet)


## Support

Voluntary tips fund open research and tooling. **Donation-only addresses** — not trading or production wallets.

| Chain family | Address |
|--------------|---------|
| **EVM** (Ethereum, Polygon, Base, Arbitrum, …) | `0x444C5C2eC439E0382aa5a17F70313c536BcC5D58` |
| **Solana / SVM** | `J4zNn4hK9jTrKBFY8sbAGJHLoZvXvQf4B9pQSbSrocZE` |
| **Polymarket** (referral) | [polymarket.com/?r=Cemini23](https://polymarket.com/?r=Cemini23) |


## License

MIT — see `LICENSE`.
