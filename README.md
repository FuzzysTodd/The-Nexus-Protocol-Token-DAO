# The Nexus Protocol Token DAO

Welcome to The Nexus Protocol! 👋

## 🚀 New Here? Start With The User Guide!

**[📖 Open the User Guide →](user-guide.html)**

The User Guide is your friendly, no-jargon walkthrough of everything Nexus Protocol has to offer - from absolute beginner to advanced user.

## Quick Links

### For Users
- **[🚀 Marketing & Campaign Page](marketing.html)** - Official digital campaign landing page for NGTT
- **[User Guide](user-guide.html)** - Start here! Beginner-friendly walkthrough
- **[Games Arcade](games.html)** - Play Nexus browser games and browse the age-group catalog
- **[Web3 Directory](chimera.html)** - Dashboard for Web3 ecosystems and governance
- **[Withdrawal Manager](withdraw.html)** - Connect your wallet, add any contracts you own, and withdraw ETH proceeds

### For Developers
- **[Technical Documentation](README.xml)** - Architecture and smart contract details
- **[Governance Structure](GOVERNANCE.md)** - Authority and DAO operating mandate
- **[Marketing Strategy](MARKETING_STRATEGY.md)** - Comprehensive Harvard-level digital marketing & legal strategy
- **[Smart Contracts](contracts/)** - Solidity contracts including NGTT token
- **[Public DAO Pages](.github/workflows/public-pages.yml)** - Free GitHub Pages deployment for static DAO surfaces and report snapshots

### For Marketing & Growth
- **[📣 Marketing Path](MARKETING_PATH.md)** - Canonical go-to-market strategy, brand guide, launch roadmap, and phase-by-phase conclusions
- **[🛠 Marketing Implementation Plan](docs/MARKETING_IMPLEMENTATION_PLAN.md)** - Execution checklist, owners, deliverables, and launch cadence
- **[💎 Revenue Guide](CRYPTO_REVENUE_GUIDE.md)** - Complete documentation of all 10 NGTT revenue streams

## What is Nexus Protocol?

Nexus Protocol is a real project combining:
- **Decentralized Finance (DeFi)** tools and protocols
- **Smart Contract** management interfaces
- **DAO Governance** structures
- **NGTT Token** ecosystem with multiple reward mechanisms

Think of it as a Swiss Army knife for Web3 - your gateway to managing crypto assets, participating in DAOs, and exploring blockchain technology.

## Key Components

### 🎯 NGTT Token
The Nexus Game Theory Token is the ecosystem's utility token with governance rights, reward distribution, and staking capabilities.

### 🎮 Games Arcade
A polished browser arcade for playable Nexus mini-games, strategy drills, and the age-group game catalog.

### 💼 Withdrawal Manager
A simple web interface to manage withdrawals from your smart contracts using MetaMask.

### 🌐 Web3 Directory
Your dashboard to navigate various DeFi protocols including Uniswap, Aave, Chainlink, Nouns DAO, and more.

### 📋 Governance System
Structured authority with Owner (FuzzysTodd), Master Project Controller (MPC), and Super Delegates.

## Marketing Path

The Nexus Protocol's marketing strategy is fully documented in **[MARKETING_PATH.md](MARKETING_PATH.md)**.

The marketing path moves participants through five phases:

| Phase | Goal |
|---|---|
| **Awareness** | Discovery via social media, content, influencers, GitHub |
| **Acquisition** | DEX listing, airdrop, onboarding funnel, token purchase |
| **Activation** | First game played, first NGTT earned, wallet connected |
| **Retention** | DAO governance, MCP groups, boost events, dividend cycles |
| **Revenue** | All 10 streams from `CRYPTO_REVENUE_GUIDE.md` — passive + active |

See [`MARKETING_PATH.md`](MARKETING_PATH.md) for the complete go-to-market strategy, launch roadmap, brand guide, KPIs, and phase-by-phase conclusions.

## Getting Started (Quick Version)

1. **Install MetaMask** - Download from [metamask.io](https://metamask.io)
2. **Get Test ETH** - Use testnets (Sepolia/Goerli) with free faucets
3. **Explore** - Open the [User Guide](user-guide.html), [Games Arcade](games.html), or [Web3 Directory](chimera.html)

### GitHub Codespaces

This repository includes a `.devcontainer/devcontainer.json` configuration for Codespaces.

After creating a Codespace:
- Python 3.11 and Node.js 20 are available
- `requirements-dev.txt` dependencies are installed automatically
- `playwright-tool` npm dependencies are installed automatically

Then run:

```bash
# Optional lint check (may report pre-existing repository issues):
flake8 .

# Main validation:
pytest -q
```

## 🤖 Personal DAO Bots — Zero AI Credits

The DAO now runs its own deterministic bots that handle routine repo upkeep
with **plain Node.js — no paid models, no AI credits**:

| Bot | Duty | Command |
|---|---|---|
| **Health Bot** | Validates JSON configs, verifies npm script targets, detects junk files, confirms git identity is set so commits never prompt | `npm run bots:health` |
| **File-Accounting Bot** | Accounts for every tracked file — especially loose root files — in `reports/file-accounting.json` / `.md`; the DAO file set stays complete | `npm run bots:accounting` |
| **Registry Sync Bot** | Feeds the dashboard's Agents & Bots tab from the MCP registries (`reports/agents.json`) | `npm run bots:sync` |

Run all three at once with `npm run bots:all`. The financial-ops bots keep
their human-gated approval model — no bot can move treasury funds or sign
anything on its own.

## 🚀 The Agent Fleet — Running Locally at No Charge

`npm run agents:run` (or `node bots/fleet-runner.js`) runs **eight
maintenance/reporting/intel commands** from your file sets locally — no GitHub
Actions charges and no model API calls for these commands (your hardware,
electricity, and any on-chain gas are separate). The 4 Python tools need a
Python interpreter (python3 / python / py -3 — auto-detected):

| Fleet member | What it does | Output |
|---|---|---|
| Health Bot | Repo health checks | `reports/health-report.json` |
| File-Accounting Bot | Full-tree file accounting | `reports/file-accounting.*` |
| Registry Sync Bot | Dashboard agent data | `reports/agents.json` |
| **Intel Bot** | **Internet access: public market prices + repo stats (no API keys, $0)** | `reports/intel.json` |
| Financial Ops Reporter | Financial-ops REPORT — the reporting side of the fin-ops bots only | `ops/reports/financial-ops-report.*` |
| Repo Assessor | Read-only repo assessment | `reports/repo-assessment.json` |
| Asset Finder | Token/contract inventory | `reports/asset-finder.txt` |
| Telemetry Monitor | Read-only local hardware snapshot | `reports/telemetry-snapshot.txt` |

### Internet access — free

The Intel Bot gives the fleet real internet access at no cost: it fetches
public, no-key APIs (Coinbase spot prices, GitHub repo stats). It records
failures gracefully — a daily run never dies because the internet was down.

### Thinking models — local GPUs (free of API credits) vs paid APIs

The Intel Bot has an optional thinking step with three modes, resolved
automatically:

1. **Local GPU (`NEXUS_THINK=local` — free of API credits).** Run
   [Ollama](https://ollama.com) on the GPU machine. The bot auto-detects it
   at `http://localhost:11434` and reasons on your own hardware — you pay only
   electricity. Set `NEXUS_THINK=local` explicitly; if the server is down it
   reports UNAVAILABLE and never falls back to a paid provider. The fleet's
   GPU machine has an RTX 5060 Ti 8GB + RTX 5060 8GB (device ID 0x2d05) —
   16GB pooled across both cards. Verified picks (October 2026):

   | Ollama pull | VRAM | Best for |
   |---|---|---|
   | `qwen3:14b` (Q4_K_M) | ~9 GB — splits across BOTH cards | all-round reasoning |
   | `gpt-oss:20b` | ~12 GB — splits across both cards | agent work, long context, fast |
   | `qwen3:8b` / `llama3.1:8b` | ~5 GB — fits on ONE card | fastest, leaves the other card free |
   | `deepseek-r1:14b` | ~9 GB — splits across both cards | visible chain-of-thought |

   Ollama automatically splits a model's layers across both GPUs when it
   doesn't fit on one — so `qwen3:14b` runs fine on this machine using both
   cards. To keep one card free, use an 8B model instead. A GPU
   accelerates model inference speed; it does not automatically make every
   bot smarter or speed up arbitrary Python/Node/git work. "Always
   available" means the server waits and reasons when triggered — it does not
   burn GPU cycles continuously.

2. **Remote hooks (your GPU box serving the whole fleet).** Start with
   loopback only. To serve other machines on your network, run Ollama bound to
   the LAN behind a firewall that blocks internet exposure, and point each
   fleet machine's `NEXUS_MODEL_URL` at
   `http://<gpu-machine-ip>:11434/v1/chat/completions`. An unauthenticated
   model server must never be reachable from the internet.

3. **Paid remote API (`NEXUS_THINK=remote`).** Requires BOTH
   `NEXUS_THINK=remote` AND `NEXUS_MODEL_API_KEY` — a stray key alone can
   never trigger a paid call. Billed by your provider per call.

The honest bottom line: thinking on your own GPUs costs electricity, not API
credits; paid APIs cost per call; continuous around-the-clock inference has
no free version in any form. Also note: this is the maintenance/reporting
fleet plus one optional reasoning step — the 11 MCP registry agents remain
definitions, and this is not yet an MCP-connected persistent reasoning
service.

### Fedora 44 quickstart — GPU machine (RTX 5060 Ti 8GB + RTX 5060 8GB)

The one-command path (idempotent — safe to re-run, and it sets up your
repo `.env` too):

```bash
./scripts/setup-fedora.sh
```

It does everything below. The manual equivalent, for reference:

```bash
# 1. NVIDIA driver (RPM Fusion). RTX 50-series needs the open kernel module —
#    the current akmod-nvidia branch builds it automatically for Blackwell.
sudo dnf install \
  https://mirrors.rpmfusion.org/free/fedora/rpmfusion-free-release-$(rpm -E %fedora).noarch.rpm \
  https://mirrors.rpmfusion.org/nonfree/fedora/rpmfusion-nonfree-release-$(rpm -E %fedora).noarch.rpm
sudo dnf install akmod-nvidia xorg-x11-drv-nvidia-cuda
# Wait for the module build to finish (a few minutes), then verify, then reboot:
modinfo -F version nvidia
sudo reboot

# 2. Ollama — official installer writes a systemd service on 127.0.0.1:11434
curl -fsSL https://ollama.com/install.sh | sh
# (Fedora dnf5 workaround if that errors on the repo step: 
#  curl -fsSL https://ollama.com/install.sh | sed s/--add-repo/addrepo/ | sh )
sudo systemctl enable --now ollama

# 3. Pull the model — qwen3:14b splits across both cards
#    (use an 8B model like llama3.1:8b to keep one card free)
ollama pull qwen3:14b

# 4. In your repo checkout's .env (copy from .env.example):
#    NEXUS_THINK=local
#    NEXUS_MODEL_NAME=qwen3:14b

# 5. Verify: nvidia-smi shows both cards, then
npm run agents:run   # status line should say: thinking: local-gpu

# 6. Daily run — cron (systemd timer works too):
crontab -e
# add:  30 6 * * * cd /path/to/The-Nexus-Protocol-Token-DAO && ./scripts/bots-daily.sh
```

(The script prints your exact cron line at the end — paste it into `crontab -e`.)

Notes: with Secure Boot enabled, the rebuilt NVIDIA module needs MOK
enrollment/signing — if `nvidia-smi` fails after a kernel update, check
`sudo akmods` output. Keep Ollama on loopback (default) unless other fleet
machines need it — then bind to the LAN behind a firewall, never the internet.

The full classification lives in `reports/fleet-manifest.json`:

- **Run locally by the fleet runner:** the 8 tools above — deterministic code
  (verified: local file reads, local git, local hardware queries, and public
  no-key internet APIs only; no paid services).
- **Definition-only:** the 11 MCP registry agents — they execute only when
  wired to an engine, and incur no charges until then. This runner does NOT
  implement their duties.
- **Human-gated:** the 3 financial-ops bots — by design they never move funds
  autonomously; only their reporting side runs above.
- **Reference library:** the 87 skill definitions in `skills/` — no charges
  until an agent consults them.

The daily scripts (`scripts/bots-daily.sh` / `.cmd`) run this whole fleet on
schedule. They commit and push ONLY the fleet outputs (`reports/` +
`ops/reports/`), refuse to run over your staged work or manual report edits,
and retry any locally-committed-but-unpushed reports.

Note: the git hooks (below) are READ-ONLY checks — they validate but never
refresh reports; report generation happens in the fleet runner / daily
scripts.

While GitHub Actions is blocked by the account's billing lock, run them
without Actions:

### Mode 1 — Automatic, via git hooks (recommended)

One-time per machine: `npm run hooks:install` (or `bash scripts/install-hooks.sh`).
After that, the bots run **on every commit and push automatically** — quiet
on success, zero friction, zero credits:

| Hook | Runs |
|---|---|
| `pre-commit` | Health Bot + File-Accounting Bot |
| `pre-push` | All three bots, reports refreshed before they hit GitHub |

In a hurry, bypass once with `git commit --no-verify` / `git push --no-verify`.
Remove anytime with `git config --unset core.hooksPath`.

### Mode 2 — Daily, via Task Scheduler / cron

Replaces the scheduled workflow. One-time setup (Windows, elevated prompt,
adjust the path to your clone):

```
schtasks /Create /TN "Nexus DAO Bots" /TR "C:\path\to\repo\scripts\bots-daily.cmd" /SC DAILY /ST 06:00
```

Linux/macOS cron instead:

```
0 6 * * *  cd /path/to/repo && bash scripts/bots-daily.sh >> .bots-daily.log 2>&1
```

Both run all three bots, commit updated reports under your pre-configured
identity, and push — git push is **not** affected by the Actions billing lock.

### When Actions comes back

`.github/workflows/dao-bots.yml` stays in the repo and resumes automatically
once the billing issue is resolved — no changes needed. The bots are the
same either way.

## 🧾 One-Time Identity Setup (never re-enter your info)

Run once per machine/clone — after that every commit and pull in this repo
carries your identity automatically (for prompt-free pushes, log in once with
`gh auth login`):

```bash
npm run identity        # runs scripts/setup-identity.sh
```

This sets your git name/email (repo-local only, and it never overwrites an
identity you already configured) and frictionless pull/rebase behavior.
It's idempotent — safe to re-run anytime.

## 📁 DAO File Accounting

`dao-data-source-manifest.json` is the source of truth for the DAO's file set.
Its `fileAccounting` policy requires **every tracked file — including all
loose root files — to appear in the accounting inventory** with a category,
purpose, and disposition. The File-Accounting Bot enforces this and fails CI
if anything is unaccounted for:

- Inventory (JSON): `reports/file-accounting.json`
- Human-readable table: `reports/file-accounting.md`

## 🤖 MCP Agents & Their Duties

Every AI/automation agent's domain, tools, and authority level is defined in
[`mcp/nexus-agent-registry.json`](mcp/nexus-agent-registry.json) — 11 agents
crypto-core through treasury-ops. The dashboard's **Agents & Bots** tab renders
them live via the Registry Sync Bot, so duties are always current.

## Important Notes

⚠️ **Audit Status** - This is a real project, but repository components and on-chain flows may not all be audited for production use.

- Always do your own research (DYOR)
- Start with testnets for learning
- Never invest more than you can afford to lose
- Blockchain transactions are permanent and irreversible

## Repository Structure

```
├── user-guide.html          # Start here! User-friendly walkthrough
├── games.html               # Browser arcade and game catalog
├── games.js                 # Arcade gameplay logic
├── chimera.html             # Web3 directory dashboard
├── withdraw.html            # Contract withdrawal manager
├── logical.js               # Frontend helper library
├── MARKETING_PATH.md        # 📣 Canonical marketing strategy & conclusions
├── CRYPTO_REVENUE_GUIDE.md  # 💎 Complete revenue stream documentation
├── GOVERNANCE.md            # Authority structure
├── README.xml               # Technical documentation
├── contracts/               # Smart contracts (Solidity)
│   └── NexusGameTheoryToken.sol
├── nexus/                   # Python modules
│   ├── telemetry_monitor.py
│   ├── family_renaissance.py
│   └── test_*.py           # Test suites
└── [Protocol Bundles]       # Uniswap, Aave, Nouns DAO, etc.
```

## Testing & Validation

The repository includes comprehensive testing:

```bash
# Run linting
pip install -r requirements-dev.txt
flake8 .

# Run all tests
pytest -q
```

Current status: ✅ **193 tests passing**

## Owner & Authority

**Owner & Primary Authority:** FuzzysTodd  
**Wallet:** `0x33ffc308e693a5b49e0ee0241f41f03ccef495f2`  
**GitHub:** [@FuzzysTodd](https://github.com/FuzzysTodd)

See [GOVERNANCE.md](GOVERNANCE.md) for complete authority structure.

## Public Addresses

- **Owner wallet:** `0x33ffc308e693a5b49e0ee0241f41f03ccef495f2` ([Etherscan](https://etherscan.io/address/0x33ffc308e693a5b49e0ee0241f41f03ccef495f2))
- **GitHub owner:** [@FuzzysTodd](https://github.com/FuzzysTodd)
- **Canonical repository:** [FuzzysTodd/The-Nexus-Protocol-Token-DOA](https://github.com/FuzzysTodd/The-Nexus-Protocol-Token-DOA)
- **Official deployed contract addresses:** No additional official deployed contract addresses are published in this repository at this time.

## Contributing

Contributions are welcome! 

1. Check the [User Guide](user-guide.html) to understand the project
2. Read the [Technical Documentation](README.xml)
3. Open issues or pull requests on GitHub

## Security & Standards

- **Nexus Encryption Standard (NES)** - Project-owned security and signing standard
- See [docs/NEXUS_ENCRYPTION_STANDARD.md](docs/NEXUS_ENCRYPTION_STANDARD.md)

## License

Repository-authored content maintained by FuzzysTodd and The-Nexus-Protocol-Token-DOA. Third-party code and dependencies remain subject to their own licenses.

---

**Ready to start?** 🚀 **[Open the User Guide →](user-guide.html)**

