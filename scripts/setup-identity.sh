#!/usr/bin/env bash
# setup-identity.sh — One-time setup so Todd never has to enter his info again.
#
# Run once per machine/clone:   bash scripts/setup-identity.sh
# After this, every commit, merge, and pull in this repo is attributed to
# Todd automatically — no prompts, no re-entry.
#
# What it does:
#   1. Sets git user.name / user.email (repo-local, so it never leaks to other projects).
#   2. Sets pull/merge behavior so `git pull` never asks merge-style questions.
#   3. Configures credential caching so pushes don't re-ask for credentials.
#   4. Verifies the GitHub CLI (gh) login if present.
#
# Safe to re-run — it is idempotent.

set -euo pipefail

# ── Todd's identity (repo-local only) ─────────────────────────────────────────
GIT_NAME="Todd Stephens"
GIT_EMAIL="157565446+FuzzysTodd@users.noreply.github.com"   # GitHub noreply — keeps your real email private

echo "▸ Configuring git identity (this repo only): $GIT_NAME <$GIT_EMAIL>"
git config user.name  "$GIT_NAME"
git config user.email "$GIT_EMAIL"

# ── Frictionless pulls / merges / pushes ──────────────────────────────────────
echo "▸ Configuring frictionless pull & push behavior"
git config pull.rebase    true       # pull = rebase, avoids merge-commit prompts
git config pull.autostash true       # auto-stash dirty worktree before pull
git config push.default   current    # push the branch you're on, no questions
git config rebase.autoStash true
git config merge.ff        only      # fast-forward only: never surprised by merge commits

# Credential caching (Linux/macOS agent; Windows Git for Windows handles this natively)
if command -v pass >/dev/null 2>&1 || [[ "$OSTYPE" != msys* ]]; then
  git config credential.helper "cache --timeout=86400" 2>/dev/null || true
fi

# ── Verify ────────────────────────────────────────────────────────────────────
echo ""
echo "✅ Identity configured for this repo:"
git config user.name
git config user.email
echo ""

if command -v gh >/dev/null 2>&1; then
  echo "▸ GitHub CLI detected — you are authenticated as:"
  gh api user --jq '.login' || echo "  (run 'gh auth login' once to enable push without password prompts)"
fi

echo ""
echo "Done. Every future commit and pull in this repo now carries your identity"
echo "automatically — nothing to enter, ever again."
