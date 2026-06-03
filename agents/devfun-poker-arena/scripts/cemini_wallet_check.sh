#!/usr/bin/env bash
# Compare beta vs official agent wallets; print funding link for official.
#
# Beta (b-arena.dev.fun) and official (arena.dev.fun) register SEPARATE agents with
# SEPARATE custodial Monad wallets. MON on beta does NOT appear on official.
#
# Outbound agent transfers only go to dev.fun protocol addresses (402 entry fees) —
# NOT to another agent wallet. See LESSONS.md L4.
set -euo pipefail
cd "$(dirname "$0")/.."

BETA_CREDS="${CEMINI_BETA_CREDS:-.arena-credentials.b-beta}"
OFFICIAL_CREDS="${CEMINI_OFFICIAL_CREDS:-.arena-credentials}"

if [[ ! -f "$BETA_CREDS" ]] && [[ -z "${CEMINI_SKIP_SSH:-}" ]]; then
  if ssh -o ConnectTimeout=5 cemini-prod test -f /opt/devfun-poker-arena/.arena-credentials.b-beta 2>/dev/null; then
    mkdir -p "$(dirname "$BETA_CREDS")"
    ssh cemini-prod cat /opt/devfun-poker-arena/.arena-credentials.b-beta > "$BETA_CREDS"
    echo "(fetched beta creds from cemini-prod → $BETA_CREDS)"
  fi
fi

if [[ ! -f "$OFFICIAL_CREDS" ]]; then
  echo "ERROR: missing $OFFICIAL_CREDS" >&2
  exit 2
fi
if [[ ! -f "$BETA_CREDS" ]]; then
  echo "WARN: missing $BETA_CREDS — skipping beta balance" >&2
fi

uv run python - <<PY
import json, os, sys
from pathlib import Path

root = Path.cwd()
sys.path.insert(0, str(root / "examples"))
from arena_client import ArenaClient

def load(p):
    return json.loads(Path(p).read_text())["apiKey"]

def snapshot(base, key, label):
    c = ArenaClient(base, api_key=key)
    me = c.get("/agent/me")
    w = c.get("/agent/wallet?chain=monad")
    c.close()
    bal = float(w["nativeBalance"]["formatted"])
    return {
        "label": label,
        "base": base,
        "handle": me.get("handle"),
        "id": me.get("id"),
        "address": w["address"],
        "mon": bal,
    }

rows = []
if Path("$OFFICIAL_CREDS").exists():
    rows.append(snapshot(
        "https://arena.dev.fun/api/arena",
        load("$OFFICIAL_CREDS"),
        "official",
    ))
if Path("$BETA_CREDS").exists():
    rows.append(snapshot(
        "https://b-arena.dev.fun/api/arena",
        load("$BETA_CREDS"),
        "beta",
    ))

print("=" * 64)
for r in rows:
    print(f"{r['label'].upper():8}  {r['handle']}  ({r['id']})")
    print(f"         API: {r['base']}")
    print(f"         Wallet: {r['address']}")
    print(f"         Balance: {r['mon']} MON")
    print("-" * 64)

if len(rows) == 2 and rows[0]["mon"] == 0 and rows[1]["mon"] > 0:
    print()
    print("⚠  MON is on BETA but official wallet is empty.")
    print("   Agent-to-agent transfer returns 403 (protocol addresses only).")
    print("   Fund OFFICIAL via MoonPay or send MON to:")
    print(f"   {rows[0]['address']}")
    print()
    print(f"   MoonPay: https://buy.moonpay.com/?currencyCode=mon_mon&walletAddress={rows[0]['address']}&baseCurrencyCode=usd")
    print()
    print("   Beta MON can only pay beta competition entry fees (402 → protocol to).")
    print("   For manual migration of large beta balances, contact dev.fun support.")

official = next((r for r in rows if r["label"] == "official"), None)
if official and official["mon"] < 0.01:
    print()
    print("Note: paid official competitions (e.g. Tournament) need ~0.01 MON + gas in the OFFICIAL wallet.")
    print("Playground S1 join is chip-based (409 if stack < table buy-in), not MON entry.")
PY
