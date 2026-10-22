#!/usr/bin/env bash
# =============================================================================
# setup-fedora.sh — one-time Fedora 44 GPU-machine setup for the Nexus fleet
# =============================================================================
# Sets up the GPU machine (RTX 5060 Ti 8GB + RTX 5060 8GB) to run local-GPU thinking for the
# DAO bot fleet at zero API-credit cost:
#
#   1. RPM Fusion repos + NVIDIA driver (open kernel module — required for
#      Blackwell / RTX 50-series) + CUDA bits
#   2. Ollama as a systemd service on 127.0.0.1:11434
#   3. The qwen3:14b model (~9 GB — Ollama splits it across both cards)
#   4. Your repo .env pointing at local thinking
#   5. Prints the cron line for the daily fleet run
#
# Safe to re-run: every step checks whether it is already done.
# Run as your normal user (sudo is used only where needed):
#
#   ./scripts/setup-fedora.sh
#
# ==============================================================================
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
MODEL="${NEXUS_MODEL_NAME:-qwen3:14b}"

log()  { printf '\n\033[1;32m==>\033[0m %s\n' "$*"; }
warn() { printf '\n\033[1;33m[warn]\033[0m %s\n' "$*"; }

# --- helpers -----------------------------------------------------------------
have()  { command -v "$1" >/dev/null 2>&1; }
pkg()   { rpm -q "$1" >/dev/null 2>&1; }
sudoc() {
  if [ "$(id -u)" -eq 0 ]; then "$@"; else sudo "$@"; fi
}

# --- 0. preflight ------------------------------------------------------------
log "Checking we are on Fedora…"
if ! grep -qi 'fedora' /etc/os-release 2>/dev/null; then
  warn "This script is written for Fedora. /etc/os-release does not say Fedora."
  warn "Continuing anyway — but the dnf commands below may not fit your distro."
fi

if ! have nvidia-smi; then
  log "No NVIDIA driver detected yet — normal on a fresh install."
fi

# --- 1. RPM Fusion + NVIDIA driver --------------------------------------------
log "Step 1/5: RPM Fusion repos + NVIDIA driver (open kernel module for RTX 50-series)"
if pkg akmod-nvidia && pkg xorg-x11-drv-nvidia-cuda; then
  echo "    NVIDIA packages already installed — skipping."
else
  sudoc dnf install -y \
    "https://mirrors.rpmfusion.org/free/fedora/rpmfusion-free-release-$(rpm -E %fedora).noarch.rpm" \
    "https://mirrors.rpmfusion.org/nonfree/fedora/rpmfusion-nonfree-release-$(rpm -E %fedora).noarch.rpm"
  sudoc dnf install -y akmod-nvidia xorg-x11-drv-nvidia-cuda
  echo "    Driver packages installed."
fi

if have nvidia-smi && nvidia-smi >/dev/null 2>&1; then
  echo "    Driver is loaded and working:"
  nvidia-smi --query-gpu=name,memory.total --format=csv,noheader || true
else
  log "Waiting for the akmod kernel-module build to finish (this can take a few minutes)…"
  sudoc akmods --force || true
  if modinfo -F version nvidia >/dev/null 2>&1; then
    echo "    Kernel module built: nvidia $(modinfo -F version nvidia)"
    warn "REBOOT before continuing, then re-run this script to verify."
  else
    warn "Kernel module not built yet. Run:  sudo akmods --force   then reboot."
    warn "If you use Secure Boot, the module must be MOK-signed to load —"
    warn "check 'sudo akmods' output for signing instructions."
  fi
fi

# --- 2. Ollama ----------------------------------------------------------------
log "Step 2/5: Ollama (systemd service on 127.0.0.1:11434)"
if have ollama; then
  echo "    Ollama already installed: $(ollama --version 2>/dev/null || echo 'present')"
else
  curl -fsSL https://ollama.com/install.sh | sh
  # Fedora dnf5 workaround if the installer errors on the repo step:
  #   curl -fsSL https://ollama.com/install.sh | sed s/--add-repo/addrepo/ | sh
fi
sudoc systemctl enable --now ollama
sleep 2
if curl -s -m 3 http://127.0.0.1:11434/api/tags >/dev/null; then
  echo "    Ollama service is up."
else
  warn "Ollama did not answer on 127.0.0.1:11434 — check: systemctl status ollama"
fi

# --- 3. model -----------------------------------------------------------------
log "Step 3/5: Pulling the ${MODEL} model (splits across both 8GB cards if needed)"
ollama pull "${MODEL}"

# --- 4. repo .env -------------------------------------------------------------
log "Step 4/5: Repo .env at ${REPO_ROOT}/.env"
if [ -f "${REPO_ROOT}/.env" ]; then
  if grep -q '^NEXUS_THINK=local' "${REPO_ROOT}/.env" 2>/dev/null; then
    echo "    .env already has NEXUS_THINK=local — nothing to do."
  else
    warn ".env exists but NEXUS_THINK is not set to local. Add/adjust these lines:"
    echo "      NEXUS_THINK=local"
    echo "      NEXUS_MODEL_NAME=${MODEL}"
  fi
else
  cp "${REPO_ROOT}/.env.example" "${REPO_ROOT}/.env"
  # shellcheck disable=SC2016  (single-quoted values, appended verbatim)
  cat >> "${REPO_ROOT}/.env" <<EOF

# --- added by setup-fedora.sh ---
NEXUS_THINK=local
NEXUS_MODEL_NAME=${MODEL}
EOF
  echo "    Created .env from .env.example with NEXUS_THINK=local."
  warn "Add your git push credentials/remote settings to .env if needed — never commit .env."
fi

# --- 5. verify + daily run ----------------------------------------------------
log "Step 5/5: Verification"
echo "    nvidia-smi:"
nvidia-smi --query-gpu=name,memory.total,driver_version --format=csv,noheader || warn "nvidia-smi not working yet — see Step 1 notes."
echo
echo "    Verify the fleet sees local thinking:"
echo "      cd ${REPO_ROOT} && npm run agents:run"
echo "    The status line should end with: thinking: local-gpu"
echo
echo "    Daily fleet run — add to YOUR crontab (crontab -e):"
echo "      30 6 * * * cd ${REPO_ROOT} && ./scripts/bots-daily.sh"
echo
echo "Done. Thinking now runs on your GPUs — electricity only, no API credits,"
echo "and a stopped Ollama reports 'unavailable' instead of ever paying a provider."
