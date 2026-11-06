# Nexus Protocol — Resilience & Deployment Checklist

## Scope
This checklist implements repository resilience and operational redundancy
using **GitHub-native and self-hosted tooling only** — no Azure dependency.

---

## 1. GitHub Repository Controls

- [ ] Enable branch protection on `main` and `MASTER`
- [ ] Require pull request reviews and status checks before merge
- [ ] Require signed commits; prevent force pushes on protected branches
- [ ] Keep linear history; block direct pushes to protected branches
- [ ] Add immutable release tags with signed release process
- [ ] Enable Dependabot alerts and auto-merge for patch-level deps
- [ ] Confirm `dao-source-manifest-validation.yml` is active in CI

---

## 2. Self-Hosted Deployment Controls

### Process Management
- [ ] Install PM2: `npm install -g pm2`
- [ ] Start all services: `pm2 start ecosystem.config.js`
- [ ] Persist across reboots: `pm2 save && pm2 startup`
- [ ] Verify all 4 services show `online` in `pm2 status`

### Docker (alternative to PM2)
- [ ] Copy `.env.example` → `.env` and fill in secrets
- [ ] Build and start: `docker-compose up -d`
- [ ] Confirm health checks pass: `docker-compose ps`

### Bare systemd (VPS without Docker)
- [ ] Run `bash scripts/start-remote.sh systemd`
- [ ] Confirm units enabled: `systemctl --user status nexus-dashboard`

---

## 3. Static Dashboard Hosting (GitHub Pages — free)

- [ ] Go to **Settings → Pages** in the GitHub repo
- [ ] Set source to **GitHub Actions**
- [ ] Confirm `.github/workflows/deploy-pages.yml` is present
- [ ] Push to `main` or `MASTER` to trigger deployment
- [ ] Verify live URL: `https://fuzzystodd.github.io/The-Nexus-Protocol-Token-DAO`

---

## 4. Vercel Deployment (optional zero-config CDN — free tier)

- [ ] Install Vercel CLI: `npm install -g vercel`
- [ ] Run `vercel --prod` from repo root
- [ ] Confirm `vercel.json` routes all dashboard pages correctly
- [ ] Set `NEXUS_ENV=remote` in Vercel project environment variables

---

## 5. Validation & Metadata Controls

All DAO source entries must include:
- `type`
- `locator`
- `trust`
- `scope`
- `notes`
- `metadata.validationStatus`
- `metadata.addedBy`
- `metadata.addedAt`
- optional `metadata.provenanceHash` (SHA-256)

Secrets must never appear in source locators or notes.
Canonical repo: `FuzzysTodd/The-Nexus-Protocol-Token-DAO`
Owner authority: `@FuzzysTodd`

---

## 6. Monitoring & Logs (no third-party required)

| What | How |
|---|---|
| Service health | `GET http://localhost:3000/api/status` |
| PM2 process logs | `pm2 logs` |
| Approval audit trail | `.approval-service-state.json` |
| systemd logs | `journalctl --user -u nexus-dashboard -f` |
| Docker logs | `docker-compose logs -f` |
| GitHub Actions runs | Repo → Actions tab |

---

## Rollout Order

1. Enable GitHub Pages (Settings → Pages → GitHub Actions source)
2. Push `main` / `MASTER` → `deploy-pages.yml` runs → static site live
3. On a VPS/server: clone repo, copy `.env.example` → `.env`, run `pm2 start ecosystem.config.js`
4. Optionally deploy to Vercel for CDN edge delivery
5. Enforce manifest validation in CI (already configured in `nexus-ci.yml`)
