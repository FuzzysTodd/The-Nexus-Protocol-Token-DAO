#!/usr/bin/env bash
# ═══════════════════════════════════════════════════════════════════════════════
# Nexus Protocol — Remote Stack Launcher (Self-Hosted / VPS / Codespaces)
#
# Starts all Nexus services in NEXUS_ENV=remote mode on any Linux host.
# No cloud-vendor lock-in required.
#
# Supported targets:
#   ✦ Any VPS / dedicated server (Ubuntu, Debian, etc.)
#   ✦ GitHub Codespaces (ports auto-forwarded via devcontainer.json)
#   ✦ Any SSH-accessible Linux host
#   ✦ Docker via docker-compose.yml in project root
#
# Services:
#   Port   Service
#   3000   Dashboard + Static HTML    (server.js)
#   8787   Approval Service REST      (approval-service-server.js)
#   8788   Financial Ops REST         (financial-ops-rest-server.js)
#   8789   Withdrawals API            (scripts/withdraws.js)
#   8790   Signal Bus WebSocket       (nexus-signal-bus.js)
#
# Usage:
#   bash scripts/start-remote.sh              # start all (detached)
#   bash scripts/start-remote.sh stop         # stop all
#   bash scripts/start-remote.sh status       # show running PIDs
#   bash scripts/start-remote.sh systemd      # install as systemd --user units
#   bash scripts/start-remote.sh docker       # start via docker-compose
#
# Required env vars (set in .env or export before running):
#   NEXUS_RPC_URL              wss://... (Infura/Alchemy/public endpoint)
#   NEXUS_WS_RPC_URL           wss://... (websocket RPC for signal bus)
#   NEXUS_GOVERNOR_ADDRESS     0x...
#   NEXUS_TREASURY_ADDRESS     0x...
#   NEXUS_TOKEN_ADDRESS        0x...
#   NEXUS_HOST_URL             https://your-domain.com  (optional)
# ═══════════════════════════════════════════════════════════════════════════════
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

# Log and PID dirs — prefer /var/log/nexus on production VPS, else ~/.nexus/
if [ -w /var/log ] 2>/dev/null && mkdir -p /var/log/nexus /var/run/nexus 2>/dev/null; then
  LOG_DIR="/var/log/nexus"
  PID_DIR="/var/run/nexus"
else
  LOG_DIR="$HOME/.nexus/logs"
  PID_DIR="$HOME/.nexus/pids"
fi
mkdir -p "$LOG_DIR" "$PID_DIR"

# Load .env if present
if [ -f "$ROOT/.env" ]; then
  set -a
  # shellcheck disable=SC1090
  source "$ROOT/.env"
  set +a
fi

export NEXUS_ENV=remote
export PORT="${PORT:-3000}"
export APPROVAL_SERVICE_PORT="${APPROVAL_SERVICE_PORT:-8787}"
export FINANCIAL_OPS_REST_PORT="${FINANCIAL_OPS_REST_PORT:-8788}"
export WITHDRAWS_PORT="${WITHDRAWS_PORT:-8789}"
export NEXUS_SIGNAL_BUS_PORT="${NEXUS_SIGNAL_BUS_PORT:-8790}"

if [ -z "${NEXUS_RPC_URL:-}" ]; then
  echo "⚠  NEXUS_RPC_URL is not set — Signal Bus will start in stub mode."
  echo "   Set NEXUS_RPC_URL=wss://... to connect to a live Ethereum node."
fi

# ── Helpers ────────────────────────────────────────────────────────────────────
start_service () {
  local name="$1" script="$2"
  local logfile="$LOG_DIR/${name}.log" pidfile="$PID_DIR/${name}.pid"

  if [ -f "$pidfile" ] && kill -0 "$(cat "$pidfile")" 2>/dev/null; then
    echo "  ↩ $name already running (PID $(cat "$pidfile"))"
    return
  fi

  node "$ROOT/$script" >> "$logfile" 2>&1 &
  echo $! > "$pidfile"
  echo "  ✓ $name started  (PID $!)  → $logfile"
}

stop_service () {
  local name="$1" pidfile="$PID_DIR/${name}.pid"
  if [ -f "$pidfile" ]; then
    local pid; pid=$(cat "$pidfile")
    kill -0 "$pid" 2>/dev/null && kill "$pid" && echo "  ✓ $name stopped (PID $pid)" || echo "  ↩ $name not running"
    rm -f "$pidfile"
  else
    echo "  ↩ $name not running (no PID file)"
  fi
}

status_service () {
  local name="$1" pidfile="$PID_DIR/${name}.pid"
  if [ -f "$pidfile" ] && kill -0 "$(cat "$pidfile")" 2>/dev/null; then
    echo "  ✓ $name  running  (PID $(cat "$pidfile"))"
  else
    echo "  ○ $name  stopped"
  fi
}

# ── systemd --user unit installer ─────────────────────────────────────────────
install_systemd () {
  local unit_dir="$HOME/.config/systemd/user"
  mkdir -p "$unit_dir"

  declare -A SERVICES=(
    ["nexus-dashboard"]="server.js"
    ["nexus-approval"]="approval-service-server.js"
    ["nexus-financial"]="financial-ops-rest-server.js"
    ["nexus-signal-bus"]="nexus-signal-bus.js"
  )

  for unit_name in "${!SERVICES[@]}"; do
    local script="${SERVICES[$unit_name]}"
    cat > "$unit_dir/${unit_name}.service" << EOF
[Unit]
Description=Nexus Protocol — ${unit_name}
After=network.target

[Service]
Type=simple
WorkingDirectory=${ROOT}
ExecStart=$(command -v node) ${ROOT}/${script}
Restart=on-failure
RestartSec=5s
Environment=NEXUS_ENV=remote
EnvironmentFile=-${ROOT}/.env
StandardOutput=append:${LOG_DIR}/${unit_name}.log
StandardError=append:${LOG_DIR}/${unit_name}.error.log

[Install]
WantedBy=default.target
EOF
    echo "  ✓ Installed $unit_dir/${unit_name}.service"
  done

  systemctl --user daemon-reload
  for unit_name in "${!SERVICES[@]}"; do
    systemctl --user enable --now "${unit_name}.service"
    echo "  ✓ Enabled + started ${unit_name}.service"
  done
  echo ""
  echo "  Services auto-restart on login / reboot."
  echo "  View logs:  journalctl --user -u nexus-dashboard -f"
}

# ── Main ───────────────────────────────────────────────────────────────────────
CMD="${1:-start}"

HOST_URL="${NEXUS_HOST_URL:-http://localhost}"

case "$CMD" in
  start)
    echo "🚀 Starting Nexus Protocol remote stack (NEXUS_ENV=remote)…"
    start_service "nexus-dashboard"  "server.js"
    start_service "nexus-approval"   "approval-service-server.js"
    start_service "nexus-financial"  "financial-ops-rest-server.js"
    start_service "nexus-signal-bus" "nexus-signal-bus.js"
    echo ""
    echo "Endpoints:"
    echo "  Dashboard   → ${HOST_URL}:${PORT}"
    echo "  Approval    → ${HOST_URL}:${APPROVAL_SERVICE_PORT}"
    echo "  Financial   → ${HOST_URL}:${FINANCIAL_OPS_REST_PORT}"
    echo "  Signal Bus  → ws://$(echo "$HOST_URL" | sed 's|https://|wss://|;s|http://|ws://|'):${NEXUS_SIGNAL_BUS_PORT}"
    echo ""
    echo "Static dashboards also available at:"
    echo "  https://fuzzystodd.github.io/The-Nexus-Protocol-Token-DAO"
    echo ""
    echo "Logs: $LOG_DIR/"
    echo "Stop: bash scripts/start-remote.sh stop"
    ;;
  stop)
    echo "🛑 Stopping Nexus Protocol remote stack…"
    stop_service "nexus-dashboard"
    stop_service "nexus-approval"
    stop_service "nexus-financial"
    stop_service "nexus-signal-bus"
    ;;
  status)
    echo "📊 Nexus Protocol remote stack status:"
    status_service "nexus-dashboard"
    status_service "nexus-approval"
    status_service "nexus-financial"
    status_service "nexus-signal-bus"
    ;;
  systemd)
    echo "⚙  Installing systemd --user units…"
    install_systemd
    ;;
  docker)
    echo "🐳 Starting via docker-compose…"
    docker-compose -f "$ROOT/docker-compose.yml" up -d
    echo "  Dashboard → http://localhost:${PORT}"
    ;;
  *)
    echo "Usage: $0 [start|stop|status|systemd|docker]"
    exit 1
    ;;
esac
