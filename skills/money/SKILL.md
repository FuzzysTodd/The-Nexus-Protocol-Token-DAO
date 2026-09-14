---
name: money
description: financial crypto expert
---

…y, Hardhat devnet

Contracts (contracts/):
  NexusToken.sol        — ERC-20Votes + ERC-20Permit + AccessControl (1B NGTT cap)
  NexusTreasury.sol     — Multi-sig treasury (N-of-M guardian confirms, 10 ETH threshold)
  NexusGovernor.sol     — OpenZeppelin Governor v5 + TimelockController (4% quorum, 7-day voting)
  NexusLPStaking.sol    — MasterChef-style LP staking for NGTT rewards
  NexusRWARegistry.sol  — ERC-721 real-world asset registry with valuation + fractionalisation
  NexusFractalVault.sol — ERC-4626 auto-compounding vault (mcp-010 keeper bot)

Networking:
  nexus-p2p-node.js     — TCP + WebSocket P2P mesh node with GossipSub topics (ports 9000/9001/8791)
  nexus-signal-relay.js — MCP agent <-> nexus-signal-bus bridge with SSE + polling (port 8792)

Tooling:
  hardhat.config.ts     — Hardhat v3 config: hardhat/localhost/nexus-devnet/sepolia/mainnet
  nexus-node-runner.ps1 — GPU-enabled full-stack launcher (RTX 5060 Ti, sm_120, CUDA 13.3)

Agent wiring:
  mcp-001 GameTheory  → token:GameCompleted
  mcp-002 TokenEcon   → token:ProfitDistributed / Transfer
  mcp-003 Governance  → governor:* proposals + votes
  mcp-004 AI Pipeline → all events (GPU feed)
  mcp-005 GPU Render  → nexus-devnet Hardhat node
  mcp-006 VPN Node    → p2p-node traffic routing
  mcp-009 Cloud-Local → p2p-node sync + recovery
  mcp-010 FinAnalytics→ FractalVault harvests + treasury flows
  mcp-fin-012 Scanner → withdrawal + ERC20 transfer events
  mcp-fin-013 Reporter→ ProposalExecuted + HarvestReinvested

All JS files pass node --check.  Solhint import-path warnings expected (npm install pending).
