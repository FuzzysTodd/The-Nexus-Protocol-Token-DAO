// register-expert-builders.js — Nexus Protocol Expert Registry
// Deterministic wallet derivation + RPC fallback + dashboard signaling.
// DRY_RUN=true prints everything without broadcasting.

const { ethers } = require("ethers");
const fs = require("fs");
const path = require("path");

// ---- Configuration ----

const CONTRACT = process.env.NEXUS_BUILDER_FUND_ADDRESS;
const ADMIN_KEY = process.env.ADMIN_PRIVATE_KEY;

// Primary + fallback RPC
const RPC_URL_PRIMARY  = process.env.RPC_URL_PRIMARY || process.env.RPC_URL;
const RPC_URL_FALLBACK = process.env.RPC_URL_FALLBACK || null;

// Deterministic wallet seed
const MNEMONIC = process.env.NEXUS_MASTER_MNEMONIC;

// Dashboard signaling file (withdraws.js listens for updates)
const DASHBOARD_SIGNAL_FILE = path.join(__dirname, "expert-registry-signal.json");

const DRY_RUN = process.env.DRY_RUN === "true";

// Expert registry definition
const EXPERTS = [
  { index: 0, shares: 200, handle: "nexus-solidity-defi-expert",        component: "Solidity-DeFi-Core",          codeSpace: "contracts/NexusBuilderFund.sol" },
  { index: 1, shares: 150, handle: "nexus-solidity-amm-expert",         component: "Solidity-AMM-Staking",        codeSpace: "contracts/NexusLPStaking.sol" },
  { index: 2, shares: 150, handle: "nexus-solidity-rwa-expert",         component: "Solidity-RWA-Compliance",     codeSpace: "contracts/NexusRWA.sol" },
  { index: 3, shares: 120, handle: "nexus-solidity-nft-frac-expert",    component: "Solidity-NFT-Fractionalization", codeSpace: "contracts/NexusFractionalize.sol" },
  { index: 4, shares: 180, handle: "nexus-solidity-options-expert",     component: "Solidity-Options-DeFi",       codeSpace: "contracts/NexusOptionsVault.sol" },
  { index: 5, shares: 160, handle: "nexus-solidity-vault-expert",       component: "Solidity-Vault-Yield",        codeSpace: "contracts/NexusFractalVault.sol" },
  { index: 6, shares: 100, handle: "nexus-nodejs-signalbus-expert",     component: "NodeJS-WebSocket-Infra",      codeSpace: "nexus-signal-bus.js" },
  { index: 7, shares: 80,  handle: "nexus-python-qa-expert",            component: "Python-QA-Validation",        codeSpace: "nexus/e2e_soundness.py" },
  { index: 8, shares: 90,  handle: "nexus-web3-ux-expert",              component: "Frontend-Web3-UX",            codeSpace: "web3-interface.html" },
  { index: 9, shares: 70,  handle: "nexus-builderfund-ux-expert",       component: "Frontend-DApp-UX",            codeSpace: "builder-fund.html" },
];

// ABI for 4‑param overload
const ABI = [
  "function registerBuilder(address wallet, uint256 shares, string handle, string component) external",
];

// ---- Helpers ----

function requireEnv(name, value) {
  if (!value) throw new Error(`Missing required environment variable: ${name}`);
}

function log(...args) {
  const ts = new Date().toISOString();
  console.log(`[${ts}]`, ...args);
}

function logError(err, context = "") {
  const ts = new Date().toISOString();
  console.error(`[${ts}] ERROR ${context}:`, err && err.stack ? err.stack : err);
}

function deriveWallet(index) {
  requireEnv("NEXUS_MASTER_MNEMONIC", MNEMONIC);
  const root = ethers.HDNodeWallet.fromPhrase(MNEMONIC);
  const derived = root.derivePath(`m/44'/60'/0'/0/${index}`);
  return derived.address;
}

async function createProvider() {
  requireEnv("RPC_URL_PRIMARY", RPC_URL_PRIMARY);

  try {
    const provider = new ethers.providers.JsonRpcProvider(RPC_URL_PRIMARY);
    const network = await provider.getNetwork();
    log("Connected to PRIMARY network:", network.name || network.chainId);
    return provider;
  } catch (err) {
    logError(err, "PRIMARY RPC failed");

    if (!RPC_URL_FALLBACK) throw new Error("No RPC_URL_FALLBACK configured");

    log("Attempting FALLBACK RPC…");
    const provider = new ethers.providers.JsonRpcProvider(RPC_URL_FALLBACK);
    const network = await provider.getNetwork();
    log("Connected to FALLBACK network:", network.name || network.chainId);
    return provider;
  }
}

// ---- Dashboard Signaling ----

function signalDashboard(expert, wallet, txHash = null) {
  const payload = {
    timestamp: new Date().toISOString(),
    expert,
    wallet,
    txHash,
    dryRun: DRY_RUN,
  };

  fs.writeFileSync(DASHBOARD_SIGNAL_FILE, JSON.stringify(payload, null, 2));
  log("Dashboard signal updated:", DASHBOARD_SIGNAL_FILE);
}

// ---- Core Logic ----

async function createFundContract() {
  requireEnv("NEXUS_BUILDER_FUND_ADDRESS", CONTRACT);
  requireEnv("ADMIN_PRIVATE_KEY", ADMIN_KEY);

  const provider = await createProvider();
  const signer   = new ethers.Wallet(ADMIN_KEY, provider);
  const fund     = new ethers.Contract(CONTRACT, ABI, signer);

  return fund;
}

async function registerExperts(fund) {
  for (const expert of EXPERTS) {
    const { index, shares, handle, component, codeSpace } = expert;
    const wallet = deriveWallet(index);

    log(`Expert: ${handle}`);
    log(`Component: ${component}`);
    log(`Code space: ${codeSpace}`);
    log(`Derived wallet (index ${index}): ${wallet}`);
    log(`Shares: ${shares}`);

    // Dashboard signal for preview
    signalDashboard(expert, wallet, null);

    if (DRY_RUN) {
      log(`DRY_RUN=true → Skipping transaction for ${handle}`);
      continue;
    }

    try {
      const tx = await fund.registerBuilder(wallet, shares, handle, component);
      log("Submitted tx:", tx.hash);

      const receipt = await tx.wait();
      log(`Confirmed tx for ${handle}: status=${receipt.status}, gasUsed=${receipt.gasUsed.toString()}`);

      // Dashboard signal with tx hash
      signalDashboard(expert, wallet, tx.hash);

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
