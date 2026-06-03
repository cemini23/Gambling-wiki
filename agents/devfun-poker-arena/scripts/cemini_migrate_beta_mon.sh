#!/usr/bin/env bash
# Check beta vs official MON balances. Direct beta→official transfer is NOT supported.
#
# Beta (b-arena.dev.fun) and official (arena.dev.fun) are SEPARATE registrations
# with SEPARATE custodial wallets. MON paid on beta does NOT appear on official.
#
# POST /agent/wallet/transfer/native to another agent address returns 403:
#   "Agent wallet transfers can only be sent to devfun-controlled protocol addresses."
# Use ./scripts/cemini_wallet_check.sh for balances + MoonPay funding link.
#
# Usage:
#   ./scripts/cemini_migrate_beta_mon.sh              # show balances + guidance
#   ./scripts/cemini_migrate_beta_mon.sh --transfer   # DEPRECATED — will fail with 403
#
# Requires:
#   .arena-credentials.b-beta  — beta API key (or prod backup path via env)
#   .arena-credentials         — official API key (for destination address lookup)
set -euo pipefail
cd "$(dirname "$0")/.."

BETA_CREDS="${CEMINI_BETA_CREDS:-.arena-credentials.b-beta}"
OFFICIAL_CREDS="${CEMINI_OFFICIAL_CREDS:-.arena-credentials}"
GAS_RESERVE="${CEMINI_GAS_RESERVE_MON:-1}"
TRANSFER=0
[[ "${1:-}" == "--transfer" ]] && TRANSFER=1

if [[ ! -f "$BETA_CREDS" ]]; then
  echo "ERROR: missing $BETA_CREDS (beta API key)" >&2
  exit 2
fi
if [[ ! -f "$OFFICIAL_CREDS" ]]; then
  echo "ERROR: missing $OFFICIAL_CREDS (official API key)" >&2
  exit 2
fi

uv run python - <<PY
import json, os, sys
from pathlib import Path

root = Path.cwd()
sys.path.insert(0, str(root / "examples"))
from arena_client import ArenaClient, ArenaError

beta_key = json.loads(Path("$BETA_CREDS").read_text())["apiKey"]
off_key = json.loads(Path("$OFFICIAL_CREDS").read_text())["apiKey"]
gas_reserve = float("$GAS_RESERVE")
do_transfer = $TRANSFER == 1

beta = ArenaClient("https://b-arena.dev.fun/api/arena", api_key=beta_key)
off = ArenaClient("https://arena.dev.fun/api/arena", api_key=off_key)

bw = beta.get("/agent/wallet?chain=monad")
ow = off.get("/agent/wallet?chain=monad")
bme = beta.get("/agent/me")
ome = off.get("/agent/me")

bb = float(bw["nativeBalance"]["formatted"])
ob = float(ow["nativeBalance"]["formatted"])
dest = ow["address"]

print("=" * 60)
print("  Beta agent:", bme.get("handle"), bme.get("id"))
print("  Beta wallet:", bw["address"], f"→ {bb} MON")
print("  Official agent:", ome.get("handle"), ome.get("id"))
print("  Official wallet:", dest, f"→ {ob} MON")
print("=" * 60)

send = round(bb - gas_reserve, 6)
if send <= 0:
    print("Nothing to transfer (beta balance <= gas reserve).")
    sys.exit(0)

print()
print("Direct beta → official agent wallet transfer is NOT allowed (403).")
print("Fund official via MoonPay or external send to:", dest)
print(f"MoonPay: https://buy.moonpay.com/?currencyCode=mon_mon&walletAddress={dest}&baseCurrencyCode=usd")
print()
print(f"Beta wallet has {bb} MON — usable only for beta 402 entry fees (protocol to).")
print("For migration of large beta balances, contact dev.fun support.")

if do_transfer:
    print()
    print("Attempting transfer anyway (expected to fail)...")
    try:
        tx = beta.post("/agent/wallet/transfer/native", {
            "chain": "monad",
            "to": dest,
            "amount": str(send),
        })
        print("TX:", tx.get("txHash"), tx.get("explorerUrl"))
    except ArenaError as e:
        print("FAIL (expected):", e.status, e.body, file=sys.stderr)
        sys.exit(2)
beta.close()
off.close()
PY
