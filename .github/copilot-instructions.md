# Copilot Instructions for The Nexus Protocol Token DAO

## Project Overview

This repository contains **The Nexus Protocol Token DAO** — a Web3/DeFi project combining:
- **NGTT (Nexus Game Theory Token)** — an ERC-20 token with governance, staking, and reward mechanics
- **Smart contracts** written in Solidity (^0.8.20), using OpenZeppelin libraries
- **Frontend interfaces** built with plain HTML/CSS/JavaScript (no framework)
- **DAO governance** structures documented in `GOVERNANCE.md`
- **Reference protocol implementations** (Uniswap, Aave, Olympus, Compound, etc.) for study and integration

Repository owner and primary authority: **@FuzzysTodd** (wallet `0x33ffc308e693a5b49e0ee0241f41f03ccef495f2`).

---

## Repository Structure

| Path | Purpose |
|------|---------|
| `contracts/` | Primary Solidity smart contracts (NGTT token, etc.) |
| `docs/` | Architecture docs, NEXUS_ENCRYPTION_STANDARD, governance notes |
| `nexus/` | Python assessment and tooling scripts |
| `mcp/` | MCP agent configuration files (JSON) |
| `playwright-tool/` | Playwright-based Web3 automation and test scripts |
| `ops/` | Operational reports and financial-ops data |
| `.github/workflows/` | CI/CD workflows |
| `*.html` / `*.js` | Frontend pages (index, marketing, games, withdraw, governance, chimera) |
| `Aave-V3/`, `Uniswap-V3/`, etc. | Third-party protocol reference implementations (do not modify) |

---

## Code Standards

### Solidity Smart Contracts
- Target **Solidity `^0.8.20`** for all contracts.
- Use **OpenZeppelin** libraries for standard token/access/security primitives.
- Follow the **Nexus Encryption Standard (NES)** — see `docs/NEXUS_ENCRYPTION_STANDARD.md` — for security, signing, and message-protection conventions.
- Always add `ReentrancyGuard` to functions that transfer ETH or tokens.
- Emit events for every state-changing action.
- Document all public and external functions with NatSpec (`@notice`, `@param`, `@return`).
- Run `solhint` and `slither` before committing contract changes if available.

### JavaScript / Frontend
- Plain ES6+ JavaScript — no bundler or framework required.
- Keep each HTML page self-contained with inline or co-located `<script>` tags.
- Use `ethers.js` (loaded via CDN) for all Web3 interactions.
- Never hard-code private keys or mnemonics in any file.
- Validate all user inputs before passing to contract calls.

### Python
- Target Python 3.10+.
- Follow PEP 8 style guidelines.
- Use `flake8` for linting (config in `.flake8`).

### General
- Prefer minimal, targeted changes — small PRs are easier to review.
- Do not modify files inside third-party reference directories (`Aave-V3/`, `Uniswap-V3/`, `Olympus-DAO/`, etc.) unless specifically instructed.
- Never commit secrets, private keys, or wallet mnemonics.
- When the owner explicitly grants permission, AI may update workspace instruction files and Copilot customization files such as `.github/copilot-instructions.md`, `.github/instructions/*.instructions.md`, and `.github/agents/*.agent.md` to keep guidance accurate.
- Keep instruction-file edits minimal, scoped, and documented in the same change.
- When an operation is blocked, unavailable, or partially broken, AI may use safe workarounds or alternate paths to complete the task if they do not bypass owner approval, weaken security, or create irreversible side effects.
- The owner grants AI authority to deeply analyze, coordinate, and optimize the total DAO across interdependent systems, workflows, and publications, including complex multi-step orchestration, provided the same approval and safety boundaries remain in force.

---

## Build & Test

### Smart Contracts
```bash
# Install dependencies (Hardhat or Foundry project)
npm install

# Compile
npx hardhat compile

# Run tests
npx hardhat test

# Lint Solidity
npx solhint 'contracts/**/*.sol'
```

### Frontend
No build step is required. Open HTML files directly in a browser or serve with a static server:
```bash
npx serve .
```

### Python scripts
```bash
pip install -r requirements.txt   # if present
flake8 nexus/ *.py
python nexus/<script>.py
```

### Playwright automation
```bash
cd playwright-tool
npm install
npx playwright test
```

---

## Governance & Authority

- All contract deployments, token actions, and treasury movements require sign-off from **@FuzzysTodd**.
- Governance rules are defined in `GOVERNANCE.md` — do not alter them without explicit approval.
- DAO improvement proposals follow the process in `docs/`.

---

## Security Guidelines

- Flag any use of `tx.origin`, unchecked external calls, or missing access controls in smart contracts.
- Use `SafeERC20` for token transfers where applicable.
- Prefer `call` over `transfer`/`send` for ETH transfers (post-EIP-1884).
- All financial or token-distribution logic must be covered by unit tests before merging.

---

## Helpful References

- [GOVERNANCE.md](../GOVERNANCE.md) — DAO authority and operating mandate
- [docs/NEXUS_ENCRYPTION_STANDARD.md](../docs/NEXUS_ENCRYPTION_STANDARD.md) — NES security conventions
- [MARKETING_PATH.md](../MARKETING_PATH.md) — Go-to-market strategy
- [CRYPTO_REVENUE_GUIDE.md](../CRYPTO_REVENUE_GUIDE.md) — NGTT revenue streams
