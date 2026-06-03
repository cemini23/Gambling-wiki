#!/usr/bin/env bash
# Cemini HL analyst loop: analyze → LLM brief → preflight → deploy
#
# Self-play (EP VPIP, regression spots) is a DEPLOY GATE — not the trainer.
# RL / overnight sweeps on egress are separate; do not conflate with this loop.
#
# Usage:
#   ./examples/cemini_hl_loop.sh                    # analyze + brief (stop for patch)
#   ./examples/cemini_hl_loop.sh --from-prod        # fetch latest prod analyze
#   ./examples/cemini_hl_loop.sh --report path.txt  # skip fetch, build brief only
#   ./examples/cemini_hl_loop.sh --preflight-only   # after you patched decide()
#   ./examples/cemini_hl_loop.sh --deploy           # preflight + rsync prod
#   ./examples/cemini_hl_loop.sh --full             # longer self-play gate (600 hands)
#
# After step 2, open reports/hl-loop/latest_brief.md in Cursor and patch
# examples/cemini_decide.py per prompts/cemini_hl_analyst_prompt.md
set -euo pipefail

cd "$(dirname "$0")/.."
AGENT_DIR="$(pwd)"

HOST="${CEMINI_PROD_HOST:-cemini-prod}"
REMOTE_DIR="/opt/devfun-poker-arena"
MATCH="${ARENA_LOBBY_COMPETITION_ID:-cmpy2qy65002ud9ej6b7jjq0l}"
TOP="${HL_ANALYZE_TOP:-15}"
ROUND="${HL_ROUND:-1}"
REPORTS="${AGENT_DIR}/reports/hl-loop"
ANALYZE_DIR="${AGENT_DIR}/reports/analyze"
LATEST_REPORT="${REPORTS}/latest_analyze.txt"
BRIEF="${REPORTS}/latest_brief.md"

FROM_PROD=0
REPORT_ARG=""
PREFLIGHT_ONLY=0
DEPLOY=0
FULL_GATE=0
SKIP_BRIEF=0

usage() {
  sed -n '2,18p' "$0"
}

while [[ $# -gt 0 ]]; do
  case "$1" in
    --from-prod) FROM_PROD=1; shift ;;
    --report) REPORT_ARG="${2:-}"; shift 2 ;;
    --preflight-only) PREFLIGHT_ONLY=1; shift ;;
    --deploy) DEPLOY=1; PREFLIGHT_ONLY=1; shift ;;
    --full) FULL_GATE=1; shift ;;
    --skip-brief) SKIP_BRIEF=1; shift ;;
    --round) ROUND="${2:-1}"; shift 2 ;;
    --match) MATCH="${2:-}"; shift 2 ;;
    -h|--help) usage; exit 0 ;;
    *) echo "Unknown arg: $1" >&2; usage; exit 2 ;;
  esac
done

mkdir -p "${REPORTS}" "${ANALYZE_DIR}"

step_ok() {
  echo ""
  echo "✓ $1"
}

step_fail() {
  echo ""
  echo "✗ $1" >&2
  exit 1
}

# ── Step 1: ANALYZE ─────────────────────────────────────────────────────────
fetch_analyze() {
  if [[ -n "${REPORT_ARG}" ]]; then
    cp -f "${REPORT_ARG}" "${LATEST_REPORT}"
    step_ok "Using analyze report: ${REPORT_ARG}"
    return
  fi

  if [[ "${FROM_PROD}" -eq 1 ]]; then
    echo "==> [1/4] Fetch analyze from ${HOST} (competition ${MATCH})"
    ssh "${HOST}" bash -s <<REMOTE
set -euo pipefail
cd "${REMOTE_DIR}"
export ARENA_LOBBY_COMPETITION_ID="${MATCH}"
./venv/bin/python examples/arena_monitor.py analyze --match "${MATCH}" --top "${TOP}" \
  --reports-dir "${REMOTE_DIR}/reports"
REMOTE
    REMOTE_LATEST="$(ssh "${HOST}" "ls -t ${REMOTE_DIR}/reports/analyze/*.txt 2>/dev/null | head -1")"
    if [[ -z "${REMOTE_LATEST}" ]]; then
      step_fail "No analyze report on prod"
    fi
    scp -q "${HOST}:${REMOTE_LATEST}" "${LATEST_REPORT}"
    step_ok "Prod analyze → ${LATEST_REPORT}"
    return
  fi

  echo "==> [1/4] Local analyze (competition ${MATCH})"
  if [[ ! -f "${AGENT_DIR}/.arena-credentials" ]] && [[ -z "${ARENA_API_KEY:-}" ]]; then
    step_fail "No .arena-credentials — use --from-prod or --report path.txt"
  fi
  uv run python examples/analyze.py --match "${MATCH}" --top "${TOP}" --out "${LATEST_REPORT}"
  step_ok "Local analyze → ${LATEST_REPORT}"
}

if [[ "${PREFLIGHT_ONLY}" -eq 0 ]]; then
  fetch_analyze

  # ── Step 2: BRIEF (LLM patch packet) ────────────────────────────────────────
  if [[ "${SKIP_BRIEF}" -eq 0 ]]; then
    echo ""
    echo "==> [2/4] Build HL analyst brief (OSINT shape → ${BRIEF})"
    uv run python examples/cemini_hl_brief.py \
      --report "${LATEST_REPORT}" \
      --out "${BRIEF}" \
      --round "${ROUND}" \
      --match "${MATCH}"
    step_ok "Brief ready — patch cemini_decide.py in Cursor, then re-run with --preflight-only"

    echo ""
    echo "────────────────────────────────────────────────────────────"
    echo "  NEXT: Open ${BRIEF}"
    echo "  Patch ONE leak in examples/cemini_decide.py"
    echo "  Then:  ./examples/cemini_hl_loop.sh --preflight-only"
    echo "  Deploy: ./examples/cemini_hl_loop.sh --deploy"
    echo "────────────────────────────────────────────────────────────"
    exit 0
  fi
fi

# ── Step 3: PREFLIGHT (gate) ──────────────────────────────────────────────────
echo ""
echo "==> [3/4] Preflight gate (pytest + EP VPIP self-play + dry-run)"
if [[ "${FULL_GATE}" -eq 1 ]]; then
  ./scripts/cemini_preflight.sh --full
else
  ./scripts/cemini_preflight.sh
fi
step_ok "Preflight PASS"

# ── Step 4: DEPLOY (optional) ─────────────────────────────────────────────────
if [[ "${DEPLOY}" -eq 1 ]]; then
  echo ""
  echo "==> [4/4] Deploy to ${HOST}"
  ./deploy/deploy_to_cemini_prod.sh
  step_ok "Deployed — monitor: ssh ${HOST} journalctl -u cemini-devfun-poker-lobby -f"
  echo ""
  echo "Re-analyze after ~50 hands:"
  echo "  ./examples/cemini_hl_loop.sh --from-prod --round $((ROUND + 1))"
else
  echo ""
  echo "==> [4/4] Deploy skipped (pass --deploy to rsync prod)"
fi

echo ""
echo "HL LOOP OK"
