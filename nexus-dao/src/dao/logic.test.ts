import test from 'node:test';
import assert from 'node:assert/strict';
import {
  calculateGameReward,
  calculateProfitDistribution,
  checkQuorum,
  getTimelockStatus,
  requiresGuardianCosign,
  convertUsdCentsToSatoshis,
  convertUsdCentsToWei,
  assembleChunks,
  chunkContractSource,
  parseContractSignatures,
  computeGP22ModernizationState,
  solveSignalDegradation,
  evaluateAnomaly,
  calculateTokenSupremacy,
  calculatePayableSplit,
  generatePayableSolidityContract,
  simulatePayableExecution,
  getPredefinedCopilotFolders,
  evaluateTriggerCondition,
  executeMassAgentRub,
  getPredefinedCircleWallets,
  getPredefinedDaoBills,
  processDaoBillPayment,
  executeAutomatedBillOrchestrationCycle,
  calculateTreasuryAllocation,
  generateHistoricalTreasuryTrends,
  calculateTreasuryMetricsSummary,
  getPredefinedForexPairs,
  executeForexSwap,
  getInitialActiveRevenueStreams,
  harvestAllRevenueStreams,
  evaluateWithdrawalTier,
  getInitialWithdrawalRequests,
  filterWithdrawalsByStatusCategory,
  getInitialFinancialApprovals,
  SIGNAL_CHANNEL_PRESETS,
  validateSignalBroadcast,
  generateProofHash,
  computeExpectedTransmittal,
  generateSignalProofFuzz,
  getInitialCorrectiveActions,
  getISOQualityMetrics,
  getRepositoryMappedStructure,
  evaluateDAOComplianceScore,
  type MCPGroupState,
  type ContractChunk,
  type GP22Checkpoints,
} from './logic';

test('calculateGameReward computes skill-adjusted reward with age group bonus', () => {
  // Base 100 tokens, skill 50 -> skillMultiplier = 100 + 50/10 = 105 -> 105 tokens
  const rewardAdult = calculateGameReward(100n, 50, 3);
  assert.equal(rewardAdult, 105n);

  // Age group <= 2 gets 20% bonus: 105 * 120 / 100 = 126
  const rewardChild = calculateGameReward(100n, 50, 2);
  assert.equal(rewardChild, 126n);

  // Zero base reward returns 0
  assert.equal(calculateGameReward(0n, 100, 1), 0n);
});

test('calculateProfitDistribution splits pool across active groups by games played', () => {
  const groups: MCPGroupState[] = [
    {
      id: 1,
      name: 'Alpha Swarm',
      members: ['0xAlice', '0xBob'],
      gamesPlayed: 30,
      totalTokens: 0n,
      profitShare: 0n,
      active: true,
    },
    {
      id: 2,
      name: 'Beta Swarm',
      members: ['0xCharlie'],
      gamesPlayed: 70,
      totalTokens: 0n,
      profitShare: 0n,
      active: true,
    },
    {
      id: 3,
      name: 'Inactive Swarm',
      members: ['0xDave'],
      gamesPlayed: 100,
      totalTokens: 0n,
      profitShare: 0n,
      active: false,
    },
  ];

  const pool = 1000n;
  const result = calculateProfitDistribution(pool, groups);

  // Group 1 got 30/100 = 300
  assert.equal(result.groupShares.get(1), 300n);
  // Group 2 got 70/100 = 700
  assert.equal(result.groupShares.get(2), 700n);
  // Alice and Bob split 300 evenly: 150 each
  assert.equal(result.memberShares.get('0xalice'), 150n);
  assert.equal(result.memberShares.get('0xbob'), 150n);
  // Charlie gets all 700
  assert.equal(result.memberShares.get('0xcharlie'), 700n);
  assert.equal(result.totalDistributed, 1000n);
});

test('checkQuorum verifies 4% threshold for 1B NGTT supply', () => {
  const totalSupply = 1_000_000_000n; // 1 Billion NGTT
  // 4% is 40,000,000
  const pass = checkQuorum(45_000_000n, totalSupply);
  assert.equal(pass.hasQuorum, true);
  assert.equal(pass.requiredVotes, 40_000_000n);
  assert.equal(pass.percentageReached, 4.5);

  const fail = checkQuorum(30_000_000n, totalSupply);
  assert.equal(fail.hasQuorum, false);
  assert.equal(fail.percentageReached, 3.0);
});

test('getTimelockStatus tracks delay readiness', () => {
  const delay = 172800; // 2 days
  const queuedAt = 1000;

  // Before delay
  const pending = getTimelockStatus(queuedAt, delay, queuedAt + 86400); // 1 day elapsed
  assert.equal(pending.isReady, false);
  assert.equal(pending.remainingSeconds, 86400);
  assert.equal(pending.percentElapsed, 50);

  // After delay
  const ready = getTimelockStatus(queuedAt, delay, queuedAt + 172800);
  assert.equal(ready.isReady, true);
  assert.equal(ready.remainingSeconds, 0);
  assert.equal(ready.percentElapsed, 100);
});

test('requiresGuardianCosign flags transfers over multisig threshold', () => {
  const threshold = 50n;
  assert.equal(requiresGuardianCosign(51n, threshold), true);
  assert.equal(requiresGuardianCosign(50n, threshold), false);
  assert.equal(requiresGuardianCosign(10n, threshold), false);
});

test('convertUsdCentsToSatoshis and Wei accurately calculate rates', () => {
  // 100 cents = $1.00. At BTC = $100,000, $1 = 0.00001 BTC = 1000 satoshis
  const sats = convertUsdCentsToSatoshis(100, 100_000);
  assert.equal(sats, 1000);

  // 100 cents = $1.00. At ETH = $2,500, $1 = 0.0004 ETH = 4e14 wei
  const wei = convertUsdCentsToWei(100, 2500);
  assert.equal(wei, 400000000000000n);
});

test('chunkContractSource and assembleChunks seamlessly split and recombine', () => {
  const sampleSolidity = `// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

contract TestContract {
    uint256 public value;
    function setValue(uint256 v) external {
        value = v;
    }
}`;

  const chunks = chunkContractSource(sampleSolidity, 3);
  assert.equal(chunks.length > 1, true);

  const assembled = assembleChunks(chunks);
  assert.equal(assembled.success, true);
  assert.equal(assembled.content, sampleSolidity);
  assert.equal(assembled.missingChunks.length, 0);

  // Test missing chunk detection
  const missingOne = [chunks[0], chunks[2]]; // missing chunk 2
  const assembledIncomplete = assembleChunks(missingOne);
  assert.equal(assembledIncomplete.success, false);
  assert.deepEqual(assembledIncomplete.missingChunks, [2]);
});

test('parseContractSignatures extracts contract details and methods', () => {
  const sampleSolidity = `
contract NexusTreasury is AccessControl, ReentrancyGuard {
    event TransferLogged(address to, uint256 amt);
    function withdraw(address to, uint256 amount) external returns (bool) {}
    function getBalance() external view returns (uint256) {}
}
`;
  const parsed = parseContractSignatures(sampleSolidity);
  assert.equal(parsed.contractName, 'NexusTreasury');
  assert.deepEqual(parsed.inherits, ['AccessControl', 'ReentrancyGuard']);
  assert.equal(parsed.functions.length, 2);
  assert.equal(parsed.functions[0].name, 'withdraw');
  assert.equal(parsed.functions[0].isMutating, true);
  assert.equal(parsed.functions[1].name, 'getBalance');
  assert.equal(parsed.functions[1].isMutating, false);
});

test('computeGP22ModernizationState tracks checkpoints and tier transitions', () => {
  const initialCheckpoints: GP22Checkpoints = {
    tier2_artifacts_generated: true,
    tier2_vote_submitted: true,
    tier2_quorum_met: true,
    tier2_routing_activated: false,
    tier3_proposal_generated: false,
    tier3_vote_submitted: false,
    tier3_quorum_met: false,
    tier3_routing_activated: false,
    pr_merged: false,
    ci_cd_triggered: false,
    modernization_logged: false,
  };

  const state1 = computeGP22ModernizationState(initialCheckpoints);
  assert.equal(state1.currentTier, 2);
  assert.equal(state1.completedCount, 3);
  assert.equal(state1.isReadyForTier4Execution, false);

  // Activate Tier 2 routing & complete Tier 3 + CI/CD
  const readyCheckpoints: GP22Checkpoints = {
    ...initialCheckpoints,
    tier2_routing_activated: true,
    tier3_proposal_generated: true,
    tier3_vote_submitted: true,
    tier3_quorum_met: true,
    tier3_routing_activated: true,
    pr_merged: true,
    ci_cd_triggered: true,
  };

  const state2 = computeGP22ModernizationState(readyCheckpoints);
  assert.equal(state2.currentTier, 4);
  assert.equal(state2.isReadyForTier4Execution, true);
  assert.equal(state2.canExecuteOnChain, true);
});

test('solveSignalDegradation repairs noisy and drifted financial signals', () => {
  const cleanSignal = [100, 100, 100, 100, 100];
  const cleanResult = solveSignalDegradation(cleanSignal);
  assert.equal(cleanResult.classification, 'CLEAN');
  assert.equal(cleanResult.correctionsApplied, 0);

  // Spiked/noisy signal
  const noisySignal = [100, 280, 100, 100, 100];
  const repaired = solveSignalDegradation(noisySignal);
  assert.equal(repaired.classification, 'SPIKED');
  assert.equal(repaired.correctionsApplied > 0, true);
  // Spiked index 1 should be pulled towards 100
  assert.equal(repaired.repairedSignal[1] < 280, true);
});

test('evaluateAnomaly flags abnormal GPU temperatures, power draw, and gas surges', () => {
  const normalReading = {
    id: 'node-01',
    powerDrawWatts: 180,
    temperatureCelsius: 65,
    fanSpeedRpm: 1800,
    gasPriceGwei: 22,
  };
  const normalReport = evaluateAnomaly(normalReading);
  assert.equal(normalReport.isAnomaly, false);

  const criticalReading = {
    id: 'node-02',
    powerDrawWatts: 340,
    temperatureCelsius: 88,
    fanSpeedRpm: 3200,
    gasPriceGwei: 120,
  };
  const criticalReport = evaluateAnomaly(criticalReading);
  assert.equal(criticalReport.isAnomaly, true);
  assert.equal(criticalReport.reasons.length >= 2, true);
});

test('calculateTokenSupremacy confirms 3-Engine GREATEST tier alignment', () => {
  const result = calculateTokenSupremacy();
  assert.equal(result.tier, 'GREATEST');
  assert.equal(result.score >= 99.0, true);
  assert.equal(result.engineVerdicts.monsterBall, 'DOMINANT');
  assert.equal(result.engineVerdicts.superLogical, 'CRITICAL_PROOF');
  assert.equal(result.engineVerdicts.threeAlgebra, 'VERIFIED_EXPONENTIAL');
});

test('calculatePayableSplit splits total Wei across beneficiaries according to basis points with no residue loss', () => {
  const beneficiaries = [
    { address: '0xAlice', label: 'Builder Alpha', bps: 6000 }, // 60%
    { address: '0xBob', label: 'Builder Beta', bps: 4000 },   // 40%
  ];
  const totalWei = 1_000_000_000_000_000_000n; // 1 ETH
  const splits = calculatePayableSplit(totalWei, beneficiaries);
  
  assert.equal(splits.length, 2);
  assert.equal(splits[0].amountWei, 600_000_000_000_000_000n);
  assert.equal(splits[1].amountWei, 400_000_000_000_000_000n);
  assert.equal(splits[0].amountWei + splits[1].amountWei, totalWei);
});

test('generatePayableSolidityContract generates valid Solidity with payable modifier and fallback', () => {
  const code = generatePayableSolidityContract({
    contractName: 'NexusCustomVault',
    template: 'income-splitter',
    ownerAddress: '0x123',
    beneficiaries: [{ address: '0xabc', label: 'Treasury', bps: 10000 }],
    functions: [
      {
        name: 'depositPayable',
        description: 'Deposits ETH into vault',
        payable: true,
        minDepositWei: 1000n,
        maxDepositWei: 1000000000000000000n,
        hasReentrancyGuard: true,
        emitsEvent: 'CustomDeposit',
      },
    ],
    allowFallbackPayable: true,
    enableEmergencyWithdraw: true,
  });

  assert.equal(code.includes('contract NexusCustomVault is Ownable, ReentrancyGuard'), true);
  assert.equal(code.includes('receive() external payable'), true);
  assert.equal(code.includes('function depositPayable() external payable nonReentrant'), true);
  assert.equal(code.includes('require(msg.value >= 1000, "Deposit below minimum");'), true);
  assert.equal(code.includes('NES v1.0'), true);
});

test('simulatePayableExecution validates min/max deposits and updates contract balance', () => {
  const contract = {
    id: 'test-contract-1',
    config: {
      contractName: 'TestPayable',
      template: 'custom-payable' as const,
      ownerAddress: '0xOwner',
      beneficiaries: [],
      functions: [
        {
          name: 'fundPool',
          description: 'Funds the pool',
          payable: true,
          minDepositWei: 10000000000000000n, // 0.01 ETH
          maxDepositWei: 5000000000000000000n, // 5 ETH
          hasReentrancyGuard: true,
          emitsEvent: 'CustomDeposit',
        },
      ],
      allowFallbackPayable: true,
      enableEmergencyWithdraw: true,
    },
    solidityCode: '',
    balanceWei: 50000000000000000n, // 0.05 ETH initial
    deployedAddress: '0xMockContract',
    createdAt: Date.now(),
    totalReceivedWei: 50000000000000000n,
    totalDistributedWei: 0n,
    executionCount: 1,
  };

  // Deposit below min reverts
  const failRes = simulatePayableExecution(contract, 'fundPool', 100n, '0xUser');
  assert.equal(failRes.success, false);
  assert.equal(failRes.error?.includes('minimum'), true);

  // Valid deposit succeeds and increases balance
  const passRes = simulatePayableExecution(contract, 'fundPool', 20000000000000000n, '0xUser');
  assert.equal(passRes.success, true);
  assert.equal(passRes.newContractBalanceWei, 70000000000000000n);
  assert.equal(passRes.gasUsed > 21000, true);
});

test('evaluateTriggerCondition accurately triggers Copilot workflow folders', () => {
  const folders = getPredefinedCopilotFolders();
  const massRubFolder = folders.find((f) => f.id === 'wf-mass-rub-001')!;
  const sweepFolder = folders.find((f) => f.id === 'wf-payable-sweep-002')!;
  const oracleFolder = folders.find((f) => f.id === 'wf-oracle-hedge-003')!;

  // Manual trigger fires mass rub
  assert.equal(evaluateTriggerCondition(massRubFolder, { manualTriggerFired: true }), true);
  assert.equal(evaluateTriggerCondition(massRubFolder, { manualTriggerFired: false }), false);

  // Satoshi buffer threshold
  assert.equal(evaluateTriggerCondition(sweepFolder, { satoshiBuffer: 150_000n }), true);
  assert.equal(evaluateTriggerCondition(sweepFolder, { satoshiBuffer: 50_000n }), false);

  // Oracle threshold
  assert.equal(evaluateTriggerCondition(oracleFolder, { oracleDeviationPct: 0.8 }), true);
  assert.equal(evaluateTriggerCondition(oracleFolder, { oracleDeviationPct: 0.2 }), false);
});

test('executeMassAgentRub coordinates simultaneous swarm dispatch with 432Hz resonance', () => {
  const folders = getPredefinedCopilotFolders();
  const agents = [
    { id: 'mcp-fin-011', name: 'Smart Contract Auditor', role: 'Security' },
    { id: 'mcp-fin-012', name: 'ML Anomaly Predictor', role: 'ML Analytics' },
    { id: 'mcp-fin-013', name: 'Particle Signal Solver', role: 'Consensus' },
    { id: 'mcp-fin-014', name: 'Satoshi Sweeper', role: 'Micro-Payments' },
    { id: 'mcp-fin-015', name: 'Arbitrage Scanner', role: 'Liquidity' },
    { id: 'dao-accounting-bot.js', name: 'DAO Accounting Engine', role: 'Ledger' },
  ];

  const rubResult = executeMassAgentRub(folders, agents, 200_000_000_000_000_000n);

  assert.equal(rubResult.totalAgentsActivated, 6);
  assert.equal(rubResult.swarmHarmonicFrequencyHz, 432.08);
  assert.equal(rubResult.consensusScore >= 99.0, true);
  assert.equal(rubResult.agentDispatches.length, 6);
  assert.equal(rubResult.routedPayableWei > 0n, true);
});

test('processDaoBillPayment executes gasless Circle payment, deducts wallet balance and marks bill paid', () => {
  const wallets = getPredefinedCircleWallets();
  const bills = getPredefinedDaoBills();
  const wallet = wallets[0]; // MCP-Fin-014 ($24,500 USDC)
  const bill = bills[0]; // Alchemy ($450 USDC)

  const initialBalance = wallet.usdcBalance;
  const result = processDaoBillPayment(bill, wallet, 2500.0);

  assert.equal(result.success, true);
  assert.equal(result.receipt !== undefined, true);
  assert.equal(result.receipt?.amountUsdc, 450.0);
  assert.equal(result.receipt?.gatewayFeeUsdc, 0.0);
  assert.equal(result.receipt?.status, 'SETTLED');
  assert.equal(result.updatedBill.status, 'PAID');
  assert.equal(result.updatedWallet.usdcBalance, initialBalance - 450.0);
});

test('processDaoBillPayment flags bills exceeding policy limit for Guardian cosign', () => {
  const wallets = getPredefinedCircleWallets();
  const wallet = wallets[0];
  const largeBill = {
    id: 'bill-large-001',
    vendor: 'Institutional Security Audit Firm',
    category: 'SECURITY_AUDIT' as const,
    description: 'Formal verification of entire 1B NGTT codebase',
    amountUsdc: 15000.0,
    recipientAddress: '0x9999a1b2c3d4e5f678901234567890abcdef1234',
    recipientChain: 'BASE' as const,
    frequency: 'ON_DEMAND' as const,
    dueDate: 'Immediate',
    status: 'PENDING' as const,
    autoPayEnabled: true,
    assignedAgent: 'mcp-fin-011',
  };

  const result = processDaoBillPayment(largeBill, wallet, 2500.0);
  assert.equal(result.success, false);
  assert.equal(result.updatedBill.status, 'NEEDS_GUARDIAN');
  assert.equal(result.error?.includes('exceeds auto-pay policy limit'), true);
});

test('executeAutomatedBillOrchestrationCycle pays all eligible bills across MCP agent fleet', () => {
  const wallets = getPredefinedCircleWallets();
  const bills = getPredefinedDaoBills();
  const initialState = {
    isOnline: true,
    autoPayPolicyLimitUsdc: 2500.0,
    totalBillsPaidCount: 0,
    totalUsdcPaid: 0.0,
    lastOrchestrationCycle: 'Never',
    activeAgentsCount: 4,
    nextScheduledRun: 'Immediate',
  };

  const cycle = executeAutomatedBillOrchestrationCycle(bills, wallets, initialState);
  assert.equal(cycle.processedReceipts.length, 6);
  assert.equal(cycle.updatedOrchestratorState.totalBillsPaidCount, 6);
  assert.equal(cycle.updatedOrchestratorState.totalUsdcPaid, 3535.0);
  assert.equal(cycle.updatedBills.every((b) => b.status === 'PAID'), true);
});

test('calculateTreasuryAllocation computes percentages, total value, and stablecoin share', () => {
  const sampleAssets = [
    { symbol: 'ETH', name: 'Ether', balance: '142.50 ETH', usdValue: '$370,500' },
    { symbol: 'USDC', name: 'USD Coin', balance: '450,000.00 USDC', usdValue: '$450,000' },
    { symbol: 'USDT', name: 'Tether USD', balance: '250,000.00 USDT', usdValue: '$250,000' },
    { symbol: 'NGTT', name: 'Nexus Token', balance: '150,000,000.00 NGTT', usdValue: '$1,500,000' },
  ];

  const result = calculateTreasuryAllocation(sampleAssets);
  // Total: 370500 + 450000 + 250000 + 1500000 = 2,570,500
  assert.equal(result.totalUsd, 2570500);
  assert.equal(result.items.length, 4);

  // Dominant asset is NGTT ($1.5M)
  assert.equal(result.dominantAsset?.symbol, 'NGTT');
  // NGTT share: 1,500,000 / 2,570,500 * 100 ~ 58.3%
  assert.equal(result.dominantAsset?.percentage, 58.4);

  // Stablecoins: USDC ($450k) + USDT ($250k) = $700,000 -> 700k / 2570.5k ~ 27.2%
  assert.equal(result.stablecoinSharePct, 27.2);

  // Colors are assigned
  assert.equal(result.items.every((it) => !!it.color), true);
});

test('generateHistoricalTreasuryTrends produces points ending with live asset values', () => {
  const sampleAssets = [
    { symbol: 'ETH', name: 'Ether', balance: '100 ETH', usdValue: '$250,000' },
    { symbol: 'USDC', name: 'USD Coin', balance: '500,000 USDC', usdValue: '$500,000' },
    { symbol: 'NGTT', name: 'Nexus Token', balance: '10,000,000 NGTT', usdValue: '$1,000,000' },
  ];

  const nowMs = 1793910000000;
  const trend7D = generateHistoricalTreasuryTrends('7D', sampleAssets, nowMs);
  assert.equal(trend7D.length, 7);

  // Latest point matches current total: 250k + 500k + 1000k = 1,750,000
  const latestPoint = trend7D[trend7D.length - 1];
  assert.equal(latestPoint.totalUsd, 1750000);
  assert.equal(latestPoint.ETH, 250000);
  assert.equal(latestPoint.USDC, 500000);
  assert.equal(latestPoint.NGTT, 1000000);

  // First point represents historical initial level
  assert.equal(trend7D[0].totalUsd < latestPoint.totalUsd, true);

  const trend30D = generateHistoricalTreasuryTrends('30D', sampleAssets, nowMs);
  assert.equal(trend30D.length, 10);
  assert.equal(trend30D[trend30D.length - 1].totalUsd, 1750000);
});

test('calculateTreasuryMetricsSummary correctly computes net changes and peaks', () => {
  const points = [
    { date: '2026-10-01', label: 'Oct 1', timestamp: 1, totalUsd: 1000000, netInflowUsd: 0 },
    { date: '2026-10-15', label: 'Oct 15', timestamp: 2, totalUsd: 1300000, netInflowUsd: 300000 },
    { date: '2026-11-01', label: 'Nov 1', timestamp: 3, totalUsd: 1250000, netInflowUsd: -50000 },
  ];

  const summary = calculateTreasuryMetricsSummary(points);
  assert.equal(summary.startUsd, 1000000);
  assert.equal(summary.currentUsd, 1250000);
  assert.equal(summary.netChangeUsd, 250000);
  assert.equal(summary.percentageChange, 25.0);
  assert.equal(summary.peakUsd, 1300000);
  assert.equal(summary.troughUsd, 1000000);
  assert.equal(summary.averageGrowthPerStep, 125000);
});

test('executeForexSwap accurately calculates rates, spreads, and settlements', () => {
  const pairs = getPredefinedForexPairs();
  const eurUsd = pairs.find((p) => p.symbol === 'EUR/USD')!;

  // Buy 10,000 EUR
  const trade = executeForexSwap(eurUsd, 'BUY', 10000);
  assert.equal(trade.pair, 'EUR/USD');
  assert.equal(trade.side, 'BUY');
  assert.equal(trade.amountBase, 10000);
  assert.equal(trade.rate, eurUsd.ask);
  assert.equal(trade.totalUsd, Math.round(10000 * eurUsd.ask * 100) / 100);
  assert.equal(trade.status, 'SETTLED');
  assert.equal(trade.feeUsd > 0, true);
});

test('harvestAllRevenueStreams claims accrued USD across all 10 activated streams', () => {
  const streams = getInitialActiveRevenueStreams();
  assert.equal(streams.length, 10);
  assert.equal(streams.every((s) => s.status === 'STREAMING'), true);

  const totalBefore = streams.reduce((sum, s) => sum + s.accruedClaimableUsd, 0);
  const result = harvestAllRevenueStreams(streams);

  assert.equal(result.harvestedTotalUsd, Math.round(totalBefore * 100) / 100);
  assert.equal(result.updatedStreams.every((s) => s.accruedClaimableUsd === 0), true);
  assert.equal(result.updatedStreams[0].lastHarvest.includes('Just now'), true);
});

test('evaluateWithdrawalTier applies timelock and dual guardian thresholds based on amount', () => {
  // Small withdrawal (< $25k) -> Tier 1, no timelock, no guardian cosign
  const t1 = evaluateWithdrawalTier(15000, 'CRYPTO_ONCHAIN');
  assert.equal(t1.tier, 1);
  assert.equal(t1.requiresTimelock, false);
  assert.equal(t1.requiresGuardianCosign, false);
  assert.equal(t1.feeUsd, 5.0);

  // Medium withdrawal ($25k - $100k) -> Tier 2, 24h timelock, guardian cosign
  const t2 = evaluateWithdrawalTier(50000, 'CIRCLE_MINT_ACH');
  assert.equal(t2.tier, 2);
  assert.equal(t2.requiresTimelock, true);
  assert.equal(t2.requiresGuardianCosign, true);
  assert.equal(t2.timelockDelaySeconds, 86400);

  // Large withdrawal (> $100k) -> Tier 3, 48h timelock, dual guardian
  const t3 = evaluateWithdrawalTier(250000, 'FEDWIRE_SWIFT');
  assert.equal(t3.tier, 3);
  assert.equal(t3.requiresTimelock, true);
  assert.equal(t3.requiresGuardianCosign, true);
  assert.equal(t3.timelockDelaySeconds, 172800);
});

test('getInitialFinancialApprovals loads dual-signature queued operations', () => {
  const approvals = getInitialFinancialApprovals();
  assert.equal(approvals.length >= 4, true);

  const sepaAppr = approvals.find((a) => a.id === 'appr-ops-01')!;
  assert.equal(sepaAppr.type, 'WITHDRAWAL');
  assert.equal(sepaAppr.requiredSignatures, 2);
  assert.equal(sepaAppr.signatures.length, 1);
  assert.equal(sepaAppr.status, 'PENDING_GUARDIAN');
});

test('Withdrawal status tracking correctly filters pending, approved, and rejected records with audit trails', () => {
  const withdrawals = getInitialWithdrawalRequests();

  // Audit trails must exist on all withdrawals
  for (const w of withdrawals) {
    assert.equal(Array.isArray(w.auditTrail), true, `Withdrawal ${w.id} must have auditTrail`);
    assert.equal(w.auditTrail.length > 0, true, `Withdrawal ${w.id} must contain audit entries`);
    assert.equal(w.auditTrail[0].action, 'INITIATED', `First audit action should be INITIATED`);
  }

  // Filter Pending
  const pending = filterWithdrawalsByStatusCategory(withdrawals, 'PENDING');
  assert.equal(pending.length >= 1, true);
  assert.equal(pending.every((w) => w.status === 'PENDING_GUARDIAN' || w.status === 'PROCESSING'), true);

  // Filter Approved
  const approved = filterWithdrawalsByStatusCategory(withdrawals, 'APPROVED');
  assert.equal(approved.length >= 2, true);
  assert.equal(approved.every((w) => w.status === 'TIMELOCK_QUEUED' || w.status === 'SETTLED'), true);

  // Filter Rejected
  const rejected = filterWithdrawalsByStatusCategory(withdrawals, 'REJECTED');
  assert.equal(rejected.length >= 1, true);
  assert.equal(rejected.every((w) => w.status === 'REJECTED'), true);
  assert.equal(rejected[0].id, 'wdr-2026-099');
  assert.equal(typeof rejected[0].rejectionReason === 'string', true);
  assert.equal(rejected[0].auditTrail.some((a) => a.action === 'REJECTED_CANCELLED'), true);
});

test('SIGNAL_CHANNEL_PRESETS contains calibrated default values, units, and boundaries', () => {
  assert.equal(typeof SIGNAL_CHANNEL_PRESETS['oracle.price.eth_usd'], 'object');
  assert.equal(SIGNAL_CHANNEL_PRESETS['oracle.price.eth_usd'].defaultValue, 3150.25);
  assert.equal(SIGNAL_CHANNEL_PRESETS['oracle.price.eth_usd'].unit, 'USD');
  assert.equal(SIGNAL_CHANNEL_PRESETS['oracle.price.btc_usd'].defaultValue, 88450.0);
  assert.equal(SIGNAL_CHANNEL_PRESETS['forex.eur_usd.spot'].defaultValue, 1.0845);
  assert.equal(SIGNAL_CHANNEL_PRESETS['arbitrage.dex_spread'].defaultValue, 14.8);
  assert.equal(SIGNAL_CHANNEL_PRESETS['arbitrage.dex_spread'].unit, 'bps');
  assert.equal(SIGNAL_CHANNEL_PRESETS['builder.microfee.logged'].unit, 'ETH');
});

test('validateSignalBroadcast validates values within calibrated protocol envelopes', () => {
  // Nominal ETH price
  const validEth = validateSignalBroadcast('oracle.price.eth_usd', 3150.25);
  assert.equal(validEth.isValid, true);
  assert.equal(validEth.status, 'VALID');
  assert.equal(validEth.deviationPercent, 0);

  // Out of bounds high (e.g. 50,000 ETH)
  const highEth = validateSignalBroadcast('oracle.price.eth_usd', 50000);
  assert.equal(highEth.isValid, false);
  assert.equal(highEth.status, 'OUT_OF_BOUNDS');

  // Out of bounds low (e.g. 100 ETH)
  const lowEth = validateSignalBroadcast('oracle.price.eth_usd', 100);
  assert.equal(lowEth.isValid, false);
  assert.equal(lowEth.status, 'OUT_OF_BOUNDS');

  // Invalid numbers
  const nanVal = validateSignalBroadcast('oracle.price.eth_usd', NaN);
  assert.equal(nanVal.isValid, false);
  assert.equal(nanVal.status, 'INVALID_NUMBER');

  // Extreme deviation within envelope
  const extremeValidEth = validateSignalBroadcast('oracle.price.eth_usd', 6000);
  assert.equal(extremeValidEth.isValid, true);
  assert.equal(extremeValidEth.status, 'EXTREME_DEVIATION');
});

test('computeExpectedTransmittal builds verified cryptographic payload with proof hash', () => {
  const transmittal = computeExpectedTransmittal(
    'oracle.price.eth_usd',
    3150.25,
    'USD',
    'Chainlink v0.8 Aggregator Sync',
    42
  );

  assert.equal(transmittal.channel, 'oracle.price.eth_usd');
  assert.equal(transmittal.payloadValue, 3150.25);
  assert.equal(transmittal.unit, 'USD');
  assert.equal(transmittal.validationStatus, 'PASSED');
  assert.equal(transmittal.fuzzResilienceTier, 'A_RATED');
  assert.equal(transmittal.proofHash.startsWith('0x'), true);
  assert.equal(transmittal.proofHash.length, 66); // 0x + 64 hex chars
  assert.equal(transmittal.signatureProof.startsWith('NES-v1.0-ECDSA:0x'), true);
  assert.equal(transmittal.deliveryRail, 'ws://nexus-event-bus.cb.id:8790/v1/broadcast');
  assert.equal(transmittal.expectedLatencyMs > 0, true);
});

test('generateSignalProofFuzz generates perturbation vectors and verifies resilience', () => {
  const fuzzResult = generateSignalProofFuzz('oracle.price.eth_usd', 3150.25);

  assert.equal(fuzzResult.channel, 'oracle.price.eth_usd');
  assert.equal(fuzzResult.vectors.length, 7);
  assert.equal(fuzzResult.resilienceScore >= 70, true);

  // Nominal vector must pass
  const nominal = fuzzResult.vectors.find((v) => v.id === 'v1')!;
  assert.equal(nominal.isValid, true);
  assert.equal(nominal.fuzzStatus, 'VERIFIED');
  assert.equal(nominal.proofHash.startsWith('0x'), true);

  // Positive and negative jitter vectors must pass
  const posJitter = fuzzResult.vectors.find((v) => v.id === 'v2')!;
  const negJitter = fuzzResult.vectors.find((v) => v.id === 'v3')!;
  assert.equal(posJitter.isValid, true);
  assert.equal(negJitter.isValid, true);
});

test('getInitialCorrectiveActions returns ISO 9001 and IEEE 1012 compliant CAR items with cryptographic digests', () => {
  const cars = getInitialCorrectiveActions();
  assert.equal(cars.length >= 5, true);

  for (const car of cars) {
    assert.equal(car.id.startsWith('CAR-'), true, `CAR ID must start with CAR- prefix: ${car.id}`);
    assert.equal(typeof car.title, 'string');
    assert.equal(typeof car.standardReference, 'string');
    assert.equal(car.cryptographicDigest.startsWith('0x'), true, `Cryptographic digest must be hex: ${car.id}`);
    assert.equal(car.cryptographicDigest.length, 66, `Cryptographic digest must be 32-byte (66 chars): ${car.id}`);
    assert.equal(['CRITICAL', 'HIGH', 'MEDIUM', 'LOW'].includes(car.severity), true);
    assert.equal(['IMPLEMENTED', 'VERIFIED', 'IN_PROGRESS', 'SCHEDULED'].includes(car.status), true);
  }

  const isoOracleCar = cars.find((c) => c.id === 'CAR-ISO-01')!;
  assert.equal(isoOracleCar.standardReference.includes('ISO 9001:2015'), true);
  assert.equal(isoOracleCar.status, 'VERIFIED');

  const ieeeFuzzCar = cars.find((c) => c.id === 'CAR-IEEE-02')!;
  assert.equal(ieeeFuzzCar.standardReference.includes('IEEE 1012-2016'), true);
  assert.equal(ieeeFuzzCar.status, 'VERIFIED');
});

test('getISOQualityMetrics provides institutional audit benchmarks across ISO 9001, IEEE, and SOC 2', () => {
  const metrics = getISOQualityMetrics();
  assert.equal(metrics.length >= 4, true);

  for (const m of metrics) {
    assert.equal(m.metricId.startsWith('QM-'), true);
    assert.equal(m.score >= m.target, true, `Score ${m.score} should meet target ${m.target} for ${m.metricId}`);
    assert.equal(m.score <= 100, true);
    assert.equal(['COMPLIANT', 'EXEMPLARY', 'MONITORING'].includes(m.status), true);
  }

  const ieeeMetric = metrics.find((m) => m.metricId === 'QM-IEEE-02')!;
  assert.equal(ieeeMetric.standard, 'IEEE 1012');
  assert.equal(ieeeMetric.score >= 95, true);
});

test('getRepositoryMappedStructure maps all core DAO architectural modules with test coverage', () => {
  const modules = getRepositoryMappedStructure();
  assert.equal(modules.length >= 7, true);

  for (const mod of modules) {
    assert.equal(mod.id.startsWith('mod-'), true);
    assert.equal(mod.linesOfCode > 0, true);
    assert.equal(mod.testCoveragePercent >= 90.0, true, `Module ${mod.id} test coverage below 90% threshold`);
    assert.equal(['TIER_1_CONSENSUS', 'TIER_2_ORCHESTRATION', 'TIER_3_INTERFACE'].includes(mod.securityTier), true);
    assert.equal(mod.complianceTags.length > 0, true);
  }

  const coreLogic = modules.find((m) => m.id === 'mod-core-logic')!;
  assert.equal(coreLogic.securityTier, 'TIER_1_CONSENSUS');
  assert.equal(coreLogic.path, 'src/dao/logic.ts');
});

test('evaluateDAOComplianceScore calculates overall institutional rating and verification ratio', () => {
  const cars = getInitialCorrectiveActions();
  const metrics = getISOQualityMetrics();

  const evaluation = evaluateDAOComplianceScore(cars, metrics);
  assert.equal(evaluation.overallScore >= 95.0, true);
  assert.equal(evaluation.rating, 'AAA_INSTITUTIONAL');
  assert.equal(evaluation.verifiedRatio, 100);
  assert.equal(evaluation.pendingCount, 0);
  assert.equal(evaluation.summary.includes('ISO 9001:2015'), true);
  assert.equal(evaluation.summary.includes('IEEE 1012-2016'), true);
});





