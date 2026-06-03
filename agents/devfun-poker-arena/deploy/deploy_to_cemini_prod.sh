#!/usr/bin/env bash
# Deploy dev.fun poker lobby loop to cemini-prod and enable systemd service.
#
# Usage (from repo root or this directory):
#   ./agents/devfun-poker-arena/deploy/deploy_to_cemini_prod.sh
#
# Requires: ssh cemini-prod, local .arena-credentials in agent dir
set -euo pipefail

HOST="${CEMINI_PROD_HOST:-cemini-prod}"
REMOTE_DIR="/opt/devfun-poker-arena"
SERVICE="cemini-devfun-poker-lobby.service"

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
AGENT_DIR="$(cd "${SCRIPT_DIR}/.." && pwd)"
CREDS="${AGENT_DIR}/.arena-credentials"

echo "==> Deploying from ${AGENT_DIR} to ${HOST}:${REMOTE_DIR}"

if [[ ! -f "${CREDS}" ]]; then
  echo "ERROR: missing ${CREDS} — register locally first (run_cemini.py)." >&2
  exit 1
fi

if [[ ! -f "${AGENT_DIR}/private/opponent_hud_exploit.py" ]]; then
  echo "WARN: ${AGENT_DIR}/private/opponent_hud_exploit.py missing — prod HUD exploits disabled." >&2
fi

echo "==> Rsync agent tree (exclude venv/creds/state)"
rsync -avz --delete \
  --exclude '.venv/' \
  --exclude 'venv/' \
  --exclude 'venv-pokerskill/' \
  --exclude '.git/' \
  --exclude '__pycache__/' \
  --exclude '.arena-credentials' \
  --exclude '.arena-credentials.*' \
  --exclude '.arena-poker-state' \
  --exclude '.env' \
  "${AGENT_DIR}/" "${HOST}:${REMOTE_DIR}/"

echo "==> Copy credentials + env"
LOCAL_ID="$(python3 -c "import json; print(json.load(open('${CREDS}'))['agentId'])")"
REMOTE_ID="$(ssh -q "${HOST}" python3 -c "import json; print(json.load(open('${REMOTE_DIR}/.arena-credentials'))['agentId'])" 2>/dev/null || echo "")"

if [[ -n "${REMOTE_ID}" && "${LOCAL_ID}" != "${REMOTE_ID}" && "${CEMINI_FORCE_CREDS:-0}" != "1" ]]; then
  echo "    SKIP creds copy — agentId mismatch (local=${LOCAL_ID} prod=${REMOTE_ID})."
  echo "    Prod key kept. To overwrite anyway: CEMINI_FORCE_CREDS=1 $0"
elif [[ "${CEMINI_SKIP_CREDS:-0}" == "1" ]]; then
  echo "    SKIP creds copy (CEMINI_SKIP_CREDS=1) — prod key unchanged."
else
  scp -q "${CREDS}" "${HOST}:${REMOTE_DIR}/.arena-credentials"
  echo "    Copied .arena-credentials (agentId=${LOCAL_ID})"
fi
if [[ -f "${AGENT_DIR}/.env" ]]; then
  scp -q "${AGENT_DIR}/.env" "${HOST}:${REMOTE_DIR}/.env"
else
  scp -q "${SCRIPT_DIR}/.env.production.example" "${HOST}:${REMOTE_DIR}/.env"
fi

echo "==> Remote venv + systemd"
ssh "${HOST}" bash -s <<'REMOTE'
set -euo pipefail
REMOTE_DIR="/opt/devfun-poker-arena"
PY=/usr/bin/python3.11

chmod 600 "${REMOTE_DIR}/.arena-credentials" "${REMOTE_DIR}/.env" 2>/dev/null || true

if [[ ! -x "${REMOTE_DIR}/venv/bin/python" ]]; then
  echo "Creating venv with ${PY}..."
  "${PY}" -m venv "${REMOTE_DIR}/venv"
fi

"${REMOTE_DIR}/venv/bin/pip" install -q --upgrade pip
"${REMOTE_DIR}/venv/bin/pip" install -q httpx python-dotenv treys pokerkit

install -m 644 "${REMOTE_DIR}/deploy/cemini-devfun-poker-lobby.service" \
  /etc/systemd/system/cemini-devfun-poker-lobby.service
install -m 644 "${REMOTE_DIR}/deploy/cemini-devfun-poker-monitor.service" \
  /etc/systemd/system/cemini-devfun-poker-monitor.service
install -m 644 "${REMOTE_DIR}/deploy/cemini-devfun-poker-monitor.timer" \
  /etc/systemd/system/cemini-devfun-poker-monitor.timer
install -m 644 "${REMOTE_DIR}/deploy/cemini-devfun-poker-export.service" \
  /etc/systemd/system/cemini-devfun-poker-export.service
install -m 644 "${REMOTE_DIR}/deploy/cemini-devfun-poker-export.timer" \
  /etc/systemd/system/cemini-devfun-poker-export.timer

mkdir -p "${REMOTE_DIR}/reports/analyze"
mkdir -p "${REMOTE_DIR}/reports/exports/playground-s1-live"

systemctl daemon-reload
systemctl enable cemini-devfun-poker-lobby.service
systemctl enable cemini-devfun-poker-monitor.timer
systemctl enable cemini-devfun-poker-export.timer
systemctl restart cemini-devfun-poker-lobby.service
systemctl start cemini-devfun-poker-monitor.service
systemctl start cemini-devfun-poker-export.service
sleep 2
systemctl --no-pager status cemini-devfun-poker-lobby.service || true
systemctl --no-pager status cemini-devfun-poker-monitor.timer || true
systemctl --no-pager status cemini-devfun-poker-export.timer || true
REMOTE

echo ""
echo "Done. Tail logs:"
echo "  ssh ${HOST} journalctl -u ${SERVICE} -f"
echo "  ssh ${HOST} journalctl -u cemini-devfun-poker-monitor.service -f"
echo "  ssh ${HOST} journalctl -u cemini-devfun-poker-export.service -f"
echo "  ssh ${HOST} ls -lt ${REMOTE_DIR}/reports/analyze/ | head"
echo "  ssh ${HOST} wc -l ${REMOTE_DIR}/reports/exports/playground-s1-live/*.jsonl"
