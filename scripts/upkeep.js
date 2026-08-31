// upkeep.js — Nexus Builder Fund Chainlink Automation / cron job
// Runs as a Chainlink-compatible job or simple cron: `node upkeep.js`

const { ethers } = require("ethers");
const fetch = require("node-fetch");

// ---- Configuration ----

const STATS_URL  = process.env.STATS_URL || "http://localhost:8788/api/v1/builder-fund/stats";
const CONTRACT   = process.env.NEXUS_BUILDER_FUND_ADDRESS;
const ORACLE_KEY = process.env.ORACLE_PRIVATE_KEY;
const RPC_URL    = process.env.RPC_URL;

const MIN_CALLS_THRESHOLD = Number(process.env.NEXUS_MIN_CALLS_THRESHOLD || 10);
const MAX_ENDPOINTS_PER_RUN = Number(process.env.NEXUS_MAX_ENDPOINTS_PER_RUN || 50);

const ABI = [
  "function recordUsage(bytes32 endpoint, uint256 callCount) external",
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

async function fetchStats() {
  log("Fetching stats from", STATS_URL);
  const res = await fetch(STATS_URL, { timeout: 10_000 }).catch((err) => {
    throw new Error(`Failed to fetch stats: ${err.message}`);
  });

  if (!res.ok) {
    throw new Error(`Stats endpoint returned ${res.status} ${res.statusText}`);
  }

  const json = await res.json();
  if (!json || typeof json !== "object") {
    throw new Error("Stats endpoint returned non-JSON or invalid payload");
  }

  if (!json.byEndpoint || typeof json.byEndpoint !== "object") {
    throw new Error("Stats payload missing byEndpoint field");
  }

  log("Stats snapshotAt:", json.snapshotAt || "(unknown)");
  log("Total calls:", json.totalCalls || 0);

  return json;
}

function selectEndpoints(byEndpoint) {
  const entries = Object.entries(byEndpoint);
  const selected = [];

  for (const [endpoint, count] of entries) {
    const numericCount = Number(count || 0);
    if (Number.isNaN(numericCount)) {
      log(`Skipping endpoint ${endpoint}: non-numeric count`, count);
      continue;
    }
    if (numericCount < MIN_CALLS_THRESHOLD) {
      log(`Skipping endpoint ${endpoint}: count ${numericCount} < threshold ${MIN_CALLS_THRESHOLD}`);
      continue;
    }
    selected.push([endpoint, numericCount]);
    if (selected.length >= MAX_ENDPOINTS_PER_RUN) {
      log(`Reached MAX_ENDPOINTS_PER_RUN=${MAX_ENDPOINTS_PER_RUN}, remaining endpoints will be processed in future runs.`);
      break;
    }
  }

  log(`Selected ${selected.length} endpoint(s) for settlement.`);
  return selected;
}

async function createFundContract() {
  requireEnv("NEXUS_BUILDER_FUND_ADDRESS", CONTRACT);
  requireEnv("ORACLE_PRIVATE_KEY", ORACLE_KEY);
  requireEnv("RPC_URL", RPC_URL);

  const provider = new ethers.providers.JsonRpcProvider(RPC_URL);
  const signer   = new ethers.Wallet(ORACLE_KEY, provider);
  const fund     = new ethers.Contract(CONTRACT, ABI, signer);

  const network = await provider.getNetwork();
  log("Connected to network:", network.name || network.chainId);

  return fund;
}

async function recordUsageBatch(fund, endpoints) {
  for (const [endpoint, count] of endpoints) {
    try {
      const hash = ethers.utils.keccak256(ethers.utils.toUtf8Bytes(endpoint));
      log(`Recording ${count} calls for endpoint "${endpoint}" (hash=${hash})`);

      const tx = await fund.recordUsage(hash, count);
      log("Submitted tx:", tx.hash);

      const receipt = await tx.wait();
      log(`Confirmed tx for ${endpoint}: status=${receipt.status}, gasUsed=${receipt.gasUsed.toString()}`);
    } catch (err) {
      logError(err, `recordUsage(${endpoint}, ${count})`);
    }
  }
}

// ---- Entry Point ----

async function run() {
  log("Nexus Builder Fund upkeep starting…");

  try {
    const stats = await fetchStats();
    const endpoints = selectEndpoints(stats.byEndpoint);

    if (endpoints.length === 0) {
      log("No endpoints above threshold; nothing to settle this run.");
      return;
    }

    const fund = await createFundContract();
    await recordUsageBatch(fund, endpoints);

    log("Nexus Builder Fund upkeep completed.");
  } catch (err) {
    logError(err, "upkeep run");
  }
}

if (require.main === module) {
  run().catch((err) => logError(err, "top-level"));
}
