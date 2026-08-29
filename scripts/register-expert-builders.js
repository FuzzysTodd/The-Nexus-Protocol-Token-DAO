// register-expert-builders.js — Nexus Protocol Expert Registry
// Registers all 10 expert components into NexusBuilderFund.sol
// Supports DRY_RUN=true for preview mode.

const { ethers } = require("ethers");
const fs = require("fs");

// ---- Configuration ----

const CONTRACT = process.env.NEXUS_BUILDER_FUND_ADDRESS;
const ADMIN_KEY = process.env.ADMIN_PRIVATE_KEY;
const RPC_URL   = process.env.RPC_URL;

const DRY_RUN = process.env.DRY_RUN === "true";

// Expert registry definition (from protocol spec)
const EXPERTS = [
  { wallet: "0xExpertWallet1", shares: 200, handle: "nexus-solidity-defi-expert", component: "Solidity-DeFi-Core", codeSpace: "contracts/NexusBuilderFund.sol" },
  { wallet: "0xExpertWallet2", shares: 150, handle: "nexus-solidity-amm-expert", component: "Solidity-AMM-Staking", codeSpace: "contracts/NexusLPStaking.sol" },
  { wallet: "0xExpertWallet3", shares: 150, handle: "nexus-solidity-rwa-expert", component: "Solidity-RWA-Compliance", codeSpace: "contracts/NexusRWA.sol" },
  { wallet: "0xExpertWallet4", shares: 120, handle: "nexus-solidity-nft-frac-expert", component: "Solidity-NFT-Fractionalization", codeSpace: "contracts/NexusFractionalize.sol" },
  { wallet: "0xExpertWallet5", shares: 180, handle: "nexus-solidity-options-expert", component: "Solidity-Options-DeFi", codeSpace: "contracts/NexusOptionsVault.sol" },
  { wallet: "0xExpertWallet6", shares: 160, handle: "nexus-solidity-vault-expert", component: "Solidity-Vault-Yield", codeSpace: "contracts/NexusFractalVault.sol" },
  { wallet: "0xExpertWallet7", shares: 100, handle: "nexus-nodejs-signalbus-expert", component: "NodeJS-WebSocket-Infra", codeSpace: "nexus-signal-bus.js" },
  { wallet: "0xExpertWallet8", shares: 80,  handle: "nexus-python-qa-expert", component: "Python-QA-Validation", codeSpace: "nexus/e2e_soundness.py" },
  { wallet: "0xExpertWallet9", shares: 90,  handle: "nexus-web3-ux-expert", component: "Frontend-Web3-UX", codeSpace: "web3-interface.html" },
  { wallet: "0xExpertWallet10", shares: 70, handle: "nexus-builderfund-ux-expert", component: "Frontend-DApp-UX", codeSpace: "builder-fund.html" },
];

// ABI for registerBuilder (4‑param overload)
const ABI = [
  "function registerBuilder(address wallet, uint256 shares, string handle, string component) external",
];

// ---- Helpers ----

function requireEnv(name, value) {
  if (!value) {
    throw new Error(`Missing required environment variable: ${name}`);
  }
}

function log(...args) {
  const ts = new Date().toISOString();
  console.log(`[${ts}]`, ...args);
}

function logError(err, context = "") {
  const ts = new Date().toISOString();
  console.error(`[${ts}] ERROR ${context}:`, err && err.stack ? err.stack : err);
}

// ---- Core Logic ----

async function createFundContract() {
  requireEnv("NEXUS_BUILDER_FUND_ADDRESS", CONTRACT);
  requireEnv("ADMIN_PRIVATE_KEY", ADMIN_KEY);
  requireEnv("RPC_URL", RPC_URL);

  const provider = new ethers.providers.JsonRpcProvider(RPC_URL);
  const signer   = new ethers.Wallet(ADMIN_KEY, provider);
  const fund     = new ethers.Contract(CONTRACT, ABI, signer);

  const network = await provider.getNetwork();
  log("Connected to network:", network.name || network.chainId);

  return fund;
}

async function registerExperts(fund) {
  for (const expert of EXPERTS) {
    const { wallet, shares, handle, component, codeSpace } = expert;

    log(`Registering expert: ${handle} (${component}) — ${shares} shares`);
    log(`Code space: ${codeSpace}`);

    if (DRY_RUN) {
      log(`DRY_RUN=true → Skipping transaction for ${handle}`);
      continue;
    }

    try {
      const tx = await fund.registerBuilder(wallet, shares, handle, component);
      log("Submitted tx:", tx.hash);

      const receipt = await tx.wait();
      log(`Confirmed tx for ${handle}: status=${receipt.status}, gasUsed=${receipt.gasUsed.toString()}`);
    } catch (err) {
      logError(err, `registerBuilder(${handle})`);
    }
  }
}

// ---- Entry Point ----

async function run() {
  log("Nexus Expert Registry — starting…");
  log(`DRY_RUN: ${DRY_RUN}`);

  try {
    const fund = await createFundContract();
    await registerExperts(fund);

    log("Nexus Expert Registry — completed.");
  } catch (err) {
    logError(err, "expert registry run");
  }
}

if (require.main === module) {
  run().catch((err) => logError(err, "top-level"));
}
