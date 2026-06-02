#!/usr/bin/env python3
"""Texas Hold'em lobby loop for dev.fun (Playground / Tournament seasons).

Uses POST /texas/join (not benchmark/start). Pair with cemini_decide.
"""
from __future__ import annotations

import argparse
import json
import os
import random
import sys
import time
from pathlib import Path
from typing import Optional

from dotenv import load_dotenv

_EXAMPLES = Path(__file__).resolve().parent
if str(_EXAMPLES) not in sys.path:
    sys.path.insert(0, str(_EXAMPLES))

import cemini_decide  # noqa: E402
from agent import _normalize_action_name, _safe_research_context  # noqa: E402
from arena_client import (  # noqa: E402
    ArenaClient,
    ArenaError,
    DEFAULT_BASE,
    load_or_register,
    load_state,
    save_state,
)

POLL_INTERVAL = 2.0
POLL_JITTER = 0.5
JOIN_RETRY_S = 60.0


def _join(client: ArenaClient, competition_id: str) -> dict:
    return client.post("/texas/join", {"competitionId": competition_id})


def _pending(client: ArenaClient, competition_id: str) -> dict:
    return client.get(f"/texas/pending-actions?competitionId={competition_id}")


def run_lobby(args: argparse.Namespace) -> int:
    load_dotenv()
    client = ArenaClient(
        os.environ.get("ARENA_API_BASE", DEFAULT_BASE),
        api_key=os.environ.get("ARENA_API_KEY") or None,
    )
    competition_id = (
        args.competition_id or os.environ.get("ARENA_LOBBY_COMPETITION_ID")
        or "cmpr1uomm2is6x69xx4nyqz9r"
    )
    decide_fn = cemini_decide.decide
    retrieve_fn = cemini_decide.retrieve_solver_context
    state = load_state()
    hands_acted = 0
    rng = random.Random()
    last_join_at = 0.0

    try:
        creds = load_or_register(client, args.handle, args.name, args.quote)
        print(f"[cemini-lobby] agent={creds.get('agentId')} competition={competition_id}")

        def ensure_joined(force: bool = False) -> None:
            nonlocal last_join_at
            now = time.time()
            if not force and (now - last_join_at) < JOIN_RETRY_S:
                return
            try:
                join_resp = _join(client, competition_id)
                last_join_at = now
                print(f"[cemini-lobby] join: {json.dumps(join_resp, sort_keys=True)[:500]}")
            except ArenaError as e:
                if e.status == 402:
                    print("[cemini-lobby] entry fee required — see docs.dev.fun quickstart",
                          file=sys.stderr)
                    raise SystemExit(3) from e
                if e.status == 403:
                    print("[cemini-lobby] X claim required — verify owner on dev.fun",
                          file=sys.stderr)
                    raise SystemExit(3) from e
                # Already seated / idempotent re-join noise — log and continue
                print(f"[cemini-lobby] join note: {e.status} {e.body}", file=sys.stderr)
                last_join_at = now

        if not args.skip_join:
            ensure_joined(force=True)

        while True:
            try:
                pending = _pending(client, competition_id)
            except ArenaError as e:
                print(f"[cemini-lobby] pending-actions error: {e}", file=sys.stderr)
                ensure_joined(force=True)
                time.sleep(POLL_INTERVAL)
                continue

            tables = pending.get("tables") if isinstance(pending, dict) else []
            if not isinstance(tables, list):
                tables = []
            tables = sorted(tables, key=lambda t: (t.get("actionDeadlineAt") or 0))

            if tables:
                table = tables[0]
                deadline_ms = table.get("actionDeadlineAt") or 0
                deadline_s = (
                    max(0.0, (deadline_ms / 1000.0) - time.time()) if deadline_ms else 10.0
                )
                ctx = _safe_research_context(table, retrieve_fn)
                try:
                    action = decide_fn(table, deadline_s=deadline_s, research_context=ctx)
                except TypeError:
                    action = decide_fn(table, deadline_s=deadline_s)
                action = _normalize_action_name(action)
                payload = {"tableId": table["tableId"], **action}
                try:
                    client.post("/texas/action", payload)
                    hands_acted += 1
                    state["hands_played"] = state.get("hands_played", 0) + 1
                    save_state(state)
                    print(f"[cemini-lobby] action={action.get('action')} hands_acted={hands_acted}")
                except ArenaError as e:
                    if e.status == 409:
                        continue
                    if e.status == 400:
                        try:
                            client.post("/texas/action", {
                                "tableId": table["tableId"],
                                "action": "fold",
                                "message": "fallback after illegal action",
                                "reasoning": '{vr: "std", ke: "legal", pp: "pot control"}',
                            })
                        except ArenaError:
                            pass
                        continue
                    print(f"[cemini-lobby] action error: {e}", file=sys.stderr)
                    continue

            if args.max_actions and hands_acted >= args.max_actions:
                print(f"[cemini-lobby] hit --max-actions={args.max_actions}, stopping")
                return 0

            if not tables:
                # Stay in queue / re-enter when busted
                ensure_joined(force=False)
                time.sleep(POLL_INTERVAL + rng.uniform(-POLL_JITTER, POLL_JITTER))
    finally:
        client.close()


def main(argv: Optional[list[str]] = None) -> int:
    p = argparse.ArgumentParser(description="Cemini dev.fun texas lobby loop")
    p.add_argument("--competition-id", default=None)
    p.add_argument("--max-actions", type=int, default=0,
                   help="Stop after N actions submitted (0 = run until interrupt)")
    p.add_argument("--skip-join", action="store_true",
                   help="Skip initial join (still re-joins periodically when idle)")
    p.add_argument("--handle", default="cemini_wiki_poker")
    p.add_argument("--name", default="Cemini Wiki Poker")
    p.add_argument("--quote", default="structured skills over swagger")
    return run_lobby(p.parse_args(argv))


if __name__ == "__main__":
    raise SystemExit(main())
