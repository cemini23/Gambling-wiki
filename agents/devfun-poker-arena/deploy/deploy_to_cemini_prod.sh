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

echo "==> Rsync agent tree (exclude venv/creds/state)"
rsync -avz --delete \
  --exclude '.venv/' \
  --exclude 'venv/' \
  --exclude '.git/' \
  --exclude '__pycache__/' \
  --exclude '.arena-credentials' \
  --exclude '.arena-credentials.*' \
  --exclude '.arena-poker-state' \
  --exclude '.env' \
  "${AGENT_DIR}/" "${HOST}:${REMOTE_DIR}/"

echo "==> Copy credentials + env"
scp -q "${CREDS}" "${HOST}:${REMOTE_DIR}/.arena-credentials"
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

systemctl daemon-reload
systemctl enable cemini-devfun-poker-lobby.service
systemctl restart cemini-devfun-poker-lobby.service
sleep 2
systemctl --no-pager status cemini-devfun-poker-lobby.service || true
REMOTE

echo ""
echo "Done. Tail logs: ssh ${HOST} journalctl -u ${SERVICE} -f"
