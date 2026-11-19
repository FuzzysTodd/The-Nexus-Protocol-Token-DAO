#!/usr/bin/env bash
# setup-identity.sh — One-time setup so Todd never has to re-enter his info.
#
# Run once per machine/clone:   bash scripts/setup-identity.sh
#   (or:                        npm run identity)
#
# What it does:
#   1. Sets git user.name / user.email for THIS REPO ONLY — but never
#      overwrites an identity you have already configured.
#   2. Sets pull/merge behavior so `git pull` doesn't ask merge-style
#      questions (repo-local only).
#   3. Verifies the GitHub CLI (gh) login if present.
#
# Notes:
#   - Commit identity is separate from authentication. This script covers
#     identity; pushing without password prompts comes from `gh auth login`
#     or your OS credential manager.
#   - Safe to re-run — it is idempotent.

set -euo pipefail

REPO_IDENTITY_EMAIL="157565446+FuzzysTodd@users.noreply.github.com"   # GitHub noreply — keeps your real email private

# ── 1. Identity (never overwrite an existing one) ──────────────────────────────
if git config user.name >/dev/null 2>&1 && git config user.email >/dev/null 2>&1; then
  echo "▸ Git identity already configured — keeping it:"
  echo "    $(git config user.name) <$(git config user.email)>"
else
  echo "▸ Configuring git identity (this repo only): Todd Stephens <$REPO_IDENTITY_EMAIL>"
  git config user.name  "Todd Stephens"
  git config user.email "$REPO_IDENTITY_EMAIL"
fi

# ── 2. Frictionless pulls (repo-local only) ───────────────────────────────────
echo "▸ Configuring frictionless pull behavior"
git config pull.rebase     true   # pull = rebase, avoids merge-commit prompts
git config pull.autostash  true   # auto-stash dirty worktree before pull
git config rebase.autoStash true
git config push.default    current  # push the branch you're on, no questions

# ── 3. Verify ──────────────────────────────────────────────────────────────────
echo ""
echo "✅ Identity configured for this repo:"
echo "    $(git config user.name) <$(git config user.email)>"
echo ""

if command -v gh >/dev/null 2>&1; then
  if gh api user --jq '.login' >/dev/null 2>&1; then
    echo "▸ GitHub CLI authenticated as: $(gh api user --jq '.login')"
    echo "  Pushes will not prompt for credentials."
  else
    echo "▸ GitHub CLI present but not logged in — run 'gh auth login' once"
    echo "  so pushes don't prompt for credentials."
  fi
else
  echo "▸ Tip: install + 'gh auth login' once to make pushes prompt-free."
fi

echo ""
echo "Done. Commits and pulls in this repo now carry your identity automatically."
