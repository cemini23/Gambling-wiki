#!/usr/bin/env python3
"""Turn Arena analyze worst-hands into regression spot stubs.

After each Playground session (or mid-season when chips bleed):

    ssh cemini-prod 'cd /opt/devfun-poker-arena && ./venv/bin/python examples/arena_monitor.py analyze --match <id> --top 15' > /tmp/analyze.txt

Paste hand summaries into this tool's template, or (when creds present) fetch live:

    uv run python examples/export_regression_spots.py --match cmpy2qy65002ud9ej6b7jjq0l --top 10

Output: Python snippet to append to `tests/fixtures/regression_spots.py`.
"""
from __future__ import annotations

import argparse
import json
import os
import sys
from pathlib import Path

_EXAMPLES = Path(__file__).resolve().parent
if str(_EXAMPLES) not in sys.path:
    sys.path.insert(0, str(_EXAMPLES))


def _stub_from_analyze_row(row: dict) -> str:
    """Best-effort stub — operator fills hole cards / table shape from replay."""
    tid = row.get("tableId") or row.get("handId") or "unknown"
    delta = row.get("chipDelta") or row.get("delta") or 0
    pos = row.get("position") or row.get("heroPosition") or "MP"
    hc = row.get("handClass") or row.get("hole") or "??"
    return f"""        RegressionSpot(
            id="analyze_{tid[:12]}",
            source="analyze export chipDelta={delta}",
            table=mp_unopened(["X", "X"]),  # TODO: {hc} @ {pos} from replay
            forbidden=frozenset({{"bet", "raise", "all-in"}}),
            notes="Imported from analyze — verify table shape from replay URL",
        ),"""


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--match", help="Competition ID for live fetch")
    p.add_argument("--top", type=int, default=10)
    p.add_argument("--stdin", action="store_true", help="Read analyze JSON lines from stdin")
    args = p.parse_args(argv)

    rows: list[dict] = []
    if args.stdin:
        for line in sys.stdin:
            line = line.strip()
            if line:
                rows.append(json.loads(line))
    elif args.match:
        from arena_client import ArenaClient, CREDS_PATH, DEFAULT_BASE

        if CREDS_PATH.exists():
            creds = json.loads(CREDS_PATH.read_text())
            api_key = creds.get("apiKey")
            agent_id = creds.get("agentId") or creds.get("id")
        else:
            api_key = os.environ.get("ARENA_API_KEY")
            agent_id = os.environ.get("ARENA_AGENT_ID")
        if not api_key or not agent_id:
            print("Need .arena-credentials or ARENA_* env for live fetch", file=sys.stderr)
            return 2
        client = ArenaClient(os.environ.get("ARENA_API_BASE", DEFAULT_BASE), api_key=api_key)
        from analyze import build_failure_report  # noqa: WPS433

        text = build_failure_report(client, agent_id, args.match, args.top)
        print("# Paste analyze output and hand details manually for now:")
        print(text[:4000])
        print("\n# Stubs (edit hole cards before committing):")
        for i in range(min(args.top, 5)):
            rows.append({"tableId": f"hand_{i}", "chipDelta": -999, "position": "MP"})
    else:
        print("Provide --match or --stdin", file=sys.stderr)
        return 2

    print("# Append to regression_spots() in tests/fixtures/regression_spots.py:")
    for row in rows[: args.top]:
        print(_stub_from_analyze_row(row))
    return 0


if __name__ == "__main__":
    sys.exit(main())
