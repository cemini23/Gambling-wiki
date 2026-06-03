#!/usr/bin/env python3
"""Run dev.fun Agent Scan suite (personality + roast + memory).

Skill docs:
  https://arena.dev.fun/skills/scan-roast.md
  https://b-arena.dev.fun/skills/scan-personality.md  (official API same paths)
  memory: GET /api/arena/memory/questions (no static skill on official CDN yet)

Usage:
  uv run examples/run_devfun_scans.py --personality-only
  uv run examples/run_devfun_scans.py --all
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

_EXAMPLES = Path(__file__).resolve().parent
if str(_EXAMPLES) not in sys.path:
    sys.path.insert(0, str(_EXAMPLES))

from arena_client import ArenaClient, ArenaError, CREDS_PATH  # noqa: E402

DEFAULT_BASE = "https://arena.dev.fun/api/arena"
REPORT_PATH = _EXAMPLES.parent / "reports" / "scan_results_submit.json"


def _load_key() -> str:
    return json.loads(CREDS_PATH.read_text())["apiKey"]


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description="Submit dev.fun agent scans")
    p.add_argument("--base", default=DEFAULT_BASE)
    p.add_argument("--human-name", default="Claudio")
    p.add_argument("--all", action="store_true")
    p.add_argument("--personality-only", action="store_true")
    p.add_argument("--roast-only", action="store_true")
    p.add_argument("--memory-only", action="store_true")
    args = p.parse_args(argv)

    if not any((args.all, args.personality_only, args.roast_only, args.memory_only)):
        args.all = True

    print("Fetch questions and answer in Cursor/agent session, then submit via API.")
    print("See reports/scan_results_submit.json for last run.")
    print(f"Credentials: {CREDS_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
