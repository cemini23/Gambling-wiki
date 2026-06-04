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
from typing import Any, Optional

from dotenv import load_dotenv

_EXAMPLES = Path(__file__).resolve().parent
if str(_EXAMPLES) not in sys.path:
    sys.path.insert(0, str(_EXAMPLES))

import cemini_decide  # noqa: E402
from agent import _normalize_action_name, _safe_research_context  # noqa: E402
from session_memory import (  # noqa: E402
    exploit_from_memory,
    update_session_memory,
    villain_memory_for_table,
)
from qualification_guard import fetch_qualification_status  # noqa: E402
from blind_pressure import avg_blind_tax_per_hand, hands_to_erosion  # noqa: E402
from pace_control import join_retry_seconds  # noqa: E402
from arena_client import (  # noqa: E402
    ArenaClient,
    ArenaError,
    DEFAULT_BASE,
    load_or_register,
    load_state,
    save_state,
)
from output_sanitize import maybe_sanitize_action  # noqa: E402

POLL_INTERVAL = 2.0
POLL_JITTER = 0.5
LOBBY_LOG_INTERVAL_S = 120.0
QUAL_STATUS_INTERVAL_S = 600.0
PAYMENT_CONFIRM_WAIT_S = 5.0
PAYMENT_CONFIRM_ATTEMPTS = 24


def _arena_error_text(body: Any) -> str:
    """Normalize Arena error bodies (dict JSON or Cloudflare HTML) to text."""
    if isinstance(body, dict):
        for key in ("error", "message", "detail"):
            val = body.get(key)
            if val:
                return str(val)
        return str(body)
    return str(body or "")


def _join(client: ArenaClient, competition_id: str, tx_hash: Optional[str] = None) -> dict:
    body: dict = {"competitionId": competition_id}
    if tx_hash:
        body["txHash"] = tx_hash
    return client.post("/texas/join", body)


def _pay_entry_fee(client: ArenaClient, payment: dict) -> str:
    """Pay competition entry from agent wallet; return txHash."""
    dest = payment.get("to")
    amt = payment.get("amount")
    if not dest or not amt:
        raise ValueError(f"invalid payment requirements: {payment}")
    resp = client.post("/agent/wallet/transfer/native", {
        "chain": payment.get("chain") or "monad",
        "to": dest,
        "amount": str(amt),
    })
    tx_hash = resp.get("txHash")
    if not tx_hash:
        raise ValueError(f"transfer returned no txHash: {resp}")
    return tx_hash


def _join_with_entry_fee(
    client: ArenaClient,
    competition_id: str,
    payment: dict,
    state: Optional[dict] = None,
    save_state_fn=None,
) -> dict:
    """Transfer entry fee, then join with txHash (poll until mined)."""
    tx_hash = _pay_entry_fee(client, payment)
    print(f"[cemini-lobby] entry fee tx={tx_hash}")
    if state is not None:
        state["entry_fee_tx_hash"] = tx_hash
        if save_state_fn:
            save_state_fn(state)
    last_err: Optional[ArenaError] = None
    for attempt in range(1, PAYMENT_CONFIRM_ATTEMPTS + 1):
        time.sleep(PAYMENT_CONFIRM_WAIT_S)
        try:
            return _join(client, competition_id, tx_hash=tx_hash)
        except ArenaError as e:
            last_err = e
            msg = _arena_error_text(e.body)
            if e.status == 400 and "not yet mined" in msg.lower():
                print(f"[cemini-lobby] waiting for tx confirm ({attempt}/{PAYMENT_CONFIRM_ATTEMPTS})")
                continue
            raise
    if last_err:
        raise last_err
    raise RuntimeError("join with payment failed")


def _pending(client: ArenaClient, competition_id: str) -> dict:
    return client.get(f"/texas/pending-actions?competitionId={competition_id}")


def _lobby_status(client: ArenaClient, competition_id: str) -> dict:
    try:
        return client.get(f"/texas/lobby?competitionId={competition_id}")
    except ArenaError:
        return {}


def _log_lobby_queue(client: ArenaClient, competition_id: str) -> None:
    body = _lobby_status(client, competition_id)
    lob = body.get("lobby") if isinstance(body, dict) else None
    if not isinstance(lob, dict):
        return
    pos = lob.get("position")
    total = lob.get("total")
    if pos is not None:
        print(f"[cemini-lobby] queue position {pos}/{total} — waiting for table")


def _rebuy_with_payment(
    client: ArenaClient,
    competition_id: str,
    payment: dict,
) -> dict:
    tx_hash = _pay_entry_fee(client, payment)
    print(f"[cemini-lobby] rebuy tx={tx_hash}")
    last_err: Optional[ArenaError] = None
    for attempt in range(1, PAYMENT_CONFIRM_ATTEMPTS + 1):
        time.sleep(PAYMENT_CONFIRM_WAIT_S)
        try:
            return client.post("/texas/rebuy", {
                "competitionId": competition_id,
                "txHash": tx_hash,
            })
        except ArenaError as e:
            last_err = e
            msg = _arena_error_text(e.body)
            if e.status == 400 and "not yet mined" in msg.lower():
                print(f"[cemini-lobby] rebuy waiting for tx ({attempt}/{PAYMENT_CONFIRM_ATTEMPTS})")
                continue
            raise
    if last_err:
        raise last_err
    raise RuntimeError("rebuy with payment failed")


def _try_rebuy(client: ArenaClient, competition_id: str) -> bool:
    """Rebuy chips when table buy-in exceeds stack. Returns True if rebuy attempted."""
    try:
        resp = client.post("/texas/rebuy", {"competitionId": competition_id})
        print(f"[cemini-lobby] rebuy: {json.dumps(resp, sort_keys=True)[:300]}")
        return True
    except ArenaError as e:
        if e.status != 402:
            print(f"[cemini-lobby] rebuy failed: {e.status} {e.body}", file=sys.stderr)
            return False
        pay = e.body.get("paymentRequirements") or {} if isinstance(e.body, dict) else {}
        try:
            resp = _rebuy_with_payment(client, competition_id, pay)
            print(f"[cemini-lobby] rebuy after pay: {json.dumps(resp, sort_keys=True)[:300]}")
            return True
        except ArenaError as pay_err:
            print(f"[cemini-lobby] rebuy pay failed: {pay_err.status} {pay_err.body}",
                  file=sys.stderr)
            return False
        except Exception as exc:
            print(f"[cemini-lobby] rebuy pay error: {exc}", file=sys.stderr)
            return False


def run_lobby(args: argparse.Namespace) -> int:
    load_dotenv()
    client = ArenaClient(
        os.environ.get("ARENA_API_BASE", DEFAULT_BASE),
        api_key=os.environ.get("ARENA_API_KEY") or None,
    )
    competition_id = (
        args.competition_id or os.environ.get("ARENA_LOBBY_COMPETITION_ID")
        or "cmpr1vesh2it1x69xmtpiaecp"
    )
    decide_fn = cemini_decide.decide
    retrieve_fn = cemini_decide.retrieve_solver_context
    state = load_state()
    hands_acted = 0
    rng = random.Random()
    last_join_at = 0.0
    last_lobby_log_at = 0.0
    last_qual_check_at = 0.0
    qual_protect = False
    lead_protect = False
    in_queue_only = False
    last_pace_log_at = 0.0

    try:
        creds = load_or_register(client, args.handle, args.name, args.quote)
        print(f"[cemini-lobby] agent={creds.get('agentId')} competition={competition_id}")

        def ensure_joined(force: bool = False) -> None:
            nonlocal last_join_at, last_lobby_log_at, in_queue_only, last_pace_log_at
            now = time.time()
            retry_s = join_retry_seconds(
                lead_protect=lead_protect,
                qual_protect=qual_protect,
                in_queue_only=in_queue_only,
            )
            if (lead_protect or qual_protect) and (
                now - last_pace_log_at
            ) >= LOBBY_LOG_INTERVAL_S:
                tier = "lead" if lead_protect else "qualification"
                print(
                    f"[cemini-lobby] pace throttle ({tier}): "
                    f"join retry {retry_s:.0f}s — fewer tables, preserve buffer"
                )
                last_pace_log_at = now
            if not force and (now - last_join_at) < retry_s:
                if in_queue_only and (now - last_lobby_log_at) >= LOBBY_LOG_INTERVAL_S:
                    _log_lobby_queue(client, competition_id)
                    last_lobby_log_at = now
                return
            try:
                join_resp = _join(client, competition_id)
                last_join_at = now
                in_queue_only = False
                state.pop("entry_fee_tx_hash", None)
                save_state(state)
                print(f"[cemini-lobby] join: {json.dumps(join_resp, sort_keys=True)[:500]}")
            except ArenaError as e:
                err_text = _arena_error_text(e.body).lower()
                if e.status >= 500:
                    print(f"[cemini-lobby] join server error {e.status}, retry later",
                          file=sys.stderr)
                    last_join_at = now
                    return
                if e.status == 402:
                    pay = e.body.get("paymentRequirements") or {} if isinstance(e.body, dict) else {}
                    pending_tx = state.get("entry_fee_tx_hash")
                    if pending_tx:
                        print(f"[cemini-lobby] retrying join with pending tx {pending_tx}",
                              file=sys.stderr)
                        try:
                            join_resp = _join(client, competition_id, tx_hash=pending_tx)
                            last_join_at = now
                            state.pop("entry_fee_tx_hash", None)
                            save_state(state)
                            print(f"[cemini-lobby] join after pending tx: "
                                  f"{json.dumps(join_resp, sort_keys=True)[:500]}")
                            return
                        except ArenaError as pend_err:
                            msg = _arena_error_text(pend_err.body)
                            if pend_err.status == 400 and "not yet mined" in msg.lower():
                                print("[cemini-lobby] tx still indexing on Arena…", file=sys.stderr)
                                last_join_at = now
                                return
                            if pend_err.status != 402:
                                print(f"[cemini-lobby] pending tx join failed: "
                                      f"{pend_err.status} {pend_err.body}", file=sys.stderr)
                                last_join_at = now
                                return
                    amt = pay.get("amount", "?")
                    cur = pay.get("currency", "MON")
                    w = client.get("/agent/wallet?chain=monad")
                    bal = (w.get("nativeBalance") or {}).get("formatted", "?")
                    print(
                        f"[cemini-lobby] entry fee {amt} {cur} — agent balance {bal} MON",
                        file=sys.stderr,
                    )
                    try:
                        join_resp = _join_with_entry_fee(
                            client, competition_id, pay, state=state, save_state_fn=save_state)
                        last_join_at = now
                        state.pop("entry_fee_tx_hash", None)
                        save_state(state)
                        print(f"[cemini-lobby] join after pay: "
                              f"{json.dumps(join_resp, sort_keys=True)[:500]}")
                    except ArenaError as pay_err:
                        msg = _arena_error_text(pay_err.body)
                        if pay_err.status == 400 and "not yet mined" in msg.lower():
                            # _join_with_entry_fee raises before storing — handled below
                            pass
                        print(f"[cemini-lobby] entry pay/join failed: {pay_err.status} "
                              f"{pay_err.body}", file=sys.stderr)
                        last_join_at = now
                    except Exception as pay_exc:
                        print(f"[cemini-lobby] entry pay/join error: {pay_exc}",
                              file=sys.stderr)
                        last_join_at = now
                    return
                if e.status == 403:
                    print("[cemini-lobby] X claim required — verify owner on dev.fun",
                          file=sys.stderr)
                    raise SystemExit(3) from e
                if e.status == 409 and "not enough chips" in err_text:
                    if _try_rebuy(client, competition_id):
                        last_join_at = 0.0
                        in_queue_only = False
                    else:
                        last_join_at = now
                    return
                if e.status == 409 and "already in the matchmaking lobby" in err_text:
                    in_queue_only = True
                    last_join_at = now
                    if (now - last_lobby_log_at) >= LOBBY_LOG_INTERVAL_S:
                        _log_lobby_queue(client, competition_id)
                        last_lobby_log_at = now
                    return
                in_queue_only = False
                print(f"[cemini-lobby] join note: {e.status} {e.body}", file=sys.stderr)
                last_join_at = now

        if not args.skip_join:
            ensure_joined(force=True)

        def refresh_qualification(force: bool = False) -> None:
            nonlocal last_qual_check_at, qual_protect, lead_protect
            now = time.time()
            if not force and (now - last_qual_check_at) < QUAL_STATUS_INTERVAL_S:
                return
            last_qual_check_at = now
            try:
                st = fetch_qualification_status(client, competition_id)
                qual_protect = bool(st.get("qualification_protect"))
                lead_protect = bool(st.get("lead_protect"))
                if lead_protect:
                    print(
                        f"[cemini-lobby] LEAD protect ON "
                        f"rank={st.get('rank')} chips={st.get('chips')} "
                        f"buffer=+{st.get('buffer_chips')} vs #{st.get('cutoff_chips')} "
                        f"(blind tax ~{avg_blind_tax_per_hand():.1f}/hand, "
                        f"~{hands_to_erosion(int(st.get('buffer_chips') or 0))} passive hands to erase buffer)"
                    )
                elif qual_protect:
                    print(
                        f"[cemini-lobby] qualification protect ON "
                        f"rank={st.get('rank')} chips={st.get('chips')} "
                        f"buffer=+{st.get('buffer_chips')} vs #{st.get('cutoff_chips')}"
                    )
                elif st.get("rank") is not None:
                    print(
                        f"[cemini-lobby] protect OFF "
                        f"rank={st.get('rank')} buffer=+{st.get('buffer_chips')}"
                    )
            except Exception as exc:
                print(f"[cemini-lobby] qual status skip: {exc}", file=sys.stderr)

        refresh_qualification(force=True)

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
                in_queue_only = False
                table = tables[0]
                if not table.get("competitionId"):
                    table = {**table, "competitionId": competition_id}
                deadline_ms = table.get("actionDeadlineAt") or 0
                deadline_s = (
                    max(0.0, (deadline_ms / 1000.0) - time.time()) if deadline_ms else 10.0
                )
                ctx = _safe_research_context(table, retrieve_fn)
                if qual_protect or lead_protect:
                    ctx["qualification_protect"] = qual_protect
                    ctx["survival_mode"] = True
                if lead_protect:
                    ctx["lead_protect"] = True
                villain_mem = villain_memory_for_table(state, table)
                if villain_mem:
                    ctx["session_villain_memory"] = villain_mem
                    mem_margins = exploit_from_memory(villain_mem)
                    if mem_margins:
                        hud = ctx.setdefault("opponent_hud", {})
                        base = hud.get("margins") or {}
                        hud["margins"] = {**base, **{
                            k: base.get(k, 0.0) + v for k, v in mem_margins.items()
                        }}
                try:
                    action = decide_fn(table, deadline_s=deadline_s, research_context=ctx)
                except TypeError:
                    action = decide_fn(table, deadline_s=deadline_s)
                action = _normalize_action_name(action)
                action = maybe_sanitize_action(action)
                payload = {"tableId": table["tableId"], **action}
                try:
                    client.post("/texas/action", payload)
                    hands_acted += 1
                    state["hands_played"] = state.get("hands_played", 0) + 1
                    update_session_memory(state, table)
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
                now = time.time()
                refresh_qualification()
                if in_queue_only and (now - last_lobby_log_at) >= LOBBY_LOG_INTERVAL_S:
                    _log_lobby_queue(client, competition_id)
                    last_lobby_log_at = now
                ensure_joined(force=False)
                time.sleep(POLL_INTERVAL + rng.uniform(-POLL_JITTER, POLL_JITTER))
    finally:
        client.close()


def _apply_prod_defense_defaults() -> None:
    """Enable anti-profiling defaults for live lobby unless operator overrides."""
    os.environ.setdefault("CEMINI_SANITIZE_OUTPUT", "1")
    os.environ.setdefault("CEMINI_MIX_POSTFLOP", "1")


def main(argv: Optional[list[str]] = None) -> int:
    _apply_prod_defense_defaults()
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
