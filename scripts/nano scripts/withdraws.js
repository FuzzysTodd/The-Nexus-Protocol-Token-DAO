const { ethers } = require("ethers");
const fs = require("fs");
const path = require("path");
const express = require("express");

const CONTRACT = process.env.NEXUS_BUILDER_FUND_ADDRESS;
const RPC_URL_PRIMARY = process.env.RPC_URL_PRIMARY || process.env.RPC_URL;
const RPC_URL_FALLBACK = process.env.RPC_URL_FALLBACK || null;

const DASHBOARD_SIGNAL_FILE = path.join(__dirname, "expert-registry-signal.json");

const ABI = [
  "function pendingReward(uint256 builderId) view returns (uint256)",
  "function claimReward() external",
  "function getBuilder(uint256 id) view returns (tuple(address wallet, uint256 shares, string handle, string component, bool active))",
  "function builderCount() view returns (uint256)",
  "function ngttBalance() view returns (uint256)",
  "function rewardConfig() view returns (address placementWallet, uint256 placementBps, address ngttToken, uint256 ngttRewardPerEthWei)"
];

function log(...args) {
  console.log("[NEXUS]", ...args);
}

async function createProvider() {
  try {
    const p = new ethers.providers.JsonRpcProvider(RPC_URL_PRIMARY);
    await p.getNetwork();
    log("Connected to PRIMARY RPC");
    return p;
  } catch (err) {
    log("PRIMARY RPC failed:", err.message);
    if (!RPC_URL_FALLBACK) throw new Error("No fallback RPC configured");
    const p = new ethers.providers.JsonRpcProvider(RPC_URL_FALLBACK);
    await p.getNetwork();
    log("Connected to FALLBACK RPC");
    return p;
  }
}

function readExpertSignal() {
  try {
    if (!fs.existsSync(DASHBOARD_SIGNAL_FILE)) return { exists: false };
    return JSON.parse(fs.readFileSync(DASHBOARD_SIGNAL_FILE, "utf8"));
  } catch {
    return { exists: false };
  }
}

async function getWithdrawStatus() {
  const provider = await createProvider();
  const fund = new ethers.Contract(CONTRACT, ABI, provider);

  const expertSignal = readExpertSignal();
  const builderCount = Number(await fund.builderCount());
  const builders = [];

  for (let id = 0; id < builderCount; id++) {
    const b = await fund.getBuilder(id);
    const pending = await fund.pendingReward(id);
    builders.push({
      id,
      wallet: b.wallet,
      shares: Number(b.shares),
      handle: b.handle,
      component: b.component,
      active: b.active,
      pendingEthWei: pending.toString()
    });
  }

  const ngttBalance = await fund.ngttBalance();
  const rewardConfig = await fund.rewardConfig();

  return {
    expertSignal,
    builders,
    ngttBalance: ngttBalance.toString(),
    rewardConfig: {
      placementWallet: rewardConfig.placementWallet,
      placementBps: Number(rewardConfig.placementBps),
      ngttToken: rewardConfig.ngttToken,
      ngttRewardPerEthWei: rewardConfig.ngttRewardPerEthWei.toString()
    }
  };
}

async function claimReward(privateKey) {
  const provider = await createProvider();
  const signer = new ethers.Wallet(privateKey, provider);
  const fund = new ethers.Contract(CONTRACT, ABI, signer);

  try {
    const tx = await fund.claimReward();
    const receipt = await tx.wait();
    return { success: true, txHash: tx.hash };
  } catch (err) {
    return { success: false, error: err.message };
  }
}

const app = express();
app.use(express.json());

app.get("/withdraws", async (req, res) => {
  try {
    res.json(await getWithdrawStatus());
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
});

app.post("/withdraws/claim", async (req, res) => {
  const { privateKey } = req.body;
  if (!privateKey) return res.status(400).json({ error: "privateKey required" });
  res.json(await claimReward(privateKey));
});

const PORT = process.env.WITHDRAWS_PORT || 8789;
app.listen(PORT, () => log(`Withdraws API running on port ${PORT}`));
