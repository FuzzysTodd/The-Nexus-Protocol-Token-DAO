/**
 * @license
 * SPDX-License-Identifier: Apache-2.0
 * The Nexus Protocol DAO - Payable Contract Studio & Production Engine
 * Generates custom Solidity 0.8.20 contracts with payable methods, fallbacks,
 * value routing, and direct export to the DAO Chunk Poster.
 */

import React, { useState } from 'react';
import { useNexusDao } from '../context/NexusDaoContext';
import {
  PayableContractConfig,
  PayableTemplateType,
  PayableBeneficiary,
  PayableFunctionDef,
  SimulatedPayableContract,
} from '../dao/logic';
import { NEXUS_METADATA } from '../data/nexusContracts';
import {
  Coins,
  FileCode,
  Sparkles,
  Send,
  Plus,
  Trash2,
  CheckCircle2,
  Copy,
  ExternalLink,
  Shield,
  Layers,
  ArrowUpRight,
  TrendingUp,
  Cpu,
  RefreshCw,
  Sliders,
  DollarSign,
  AlertCircle,
  Database,
  Terminal,
} from 'lucide-react';

export const PayableContractStudio: React.FC = () => {
  const {
    account,
    payableContracts,
    selectedPayableContract,
    setSelectedPayableContract,
    createPayableContract,
    executePayableMethod,
    exportPayableContractToWorkbench,
  } = useNexusDao();

  // Mode: 'produce' (create new contract) | 'simulate' (interact with deployed)
  const [activeMode, setActiveMode] = useState<'produce' | 'simulate'>('produce');

  // Form state for producing contract
  const [contractName, setContractName] = useState('NexusPayableVaultV1');
  const [template, setTemplate] = useState<PayableTemplateType>('income-splitter');
  const [allowFallback, setAllowFallback] = useState(true);
  const [emergencyWithdraw, setEmergencyWithdraw] = useState(true);

  // Beneficiaries for income splitter
  const [beneficiaries, setBeneficiaries] = useState<PayableBeneficiary[]>([
    { address: '0x95aD61b0a150d79219dCF64E1E6Cc01f0B64C4cE', label: 'DAO Treasury', bps: 4000 },
    { address: '0x256B0E270f209633e7208Eab8A64bB7A6A95B6Ea', label: 'Builder Fund', bps: 3000 },
    { address: '0x88Cc63901b0b5A4B4B9A7A0F11C8281b3127814b', label: 'Agent Swarm Bounties', bps: 2000 },
    { address: '0x388C818CA8B9251b393131C08a73683246A16699', label: 'Staking Reserve', bps: 1000 },
  ]);

  // Functions list
  const [functions, setFunctions] = useState<PayableFunctionDef[]>([
    {
      name: 'depositPayable',
      description: 'Accepts payable ETH and routes into protocol pool',
      payable: true,
      minDepositWei: 1000000000000000n, // 0.001 ETH
      maxDepositWei: 10000000000000000000n, // 10 ETH
      hasReentrancyGuard: true,
      emitsEvent: 'CustomDeposit',
    },
    {
      name: 'distributePool',
      description: 'Splits accumulated contract ETH across beneficiaries',
      payable: false,
      minDepositWei: 0n,
      maxDepositWei: 0n,
      hasReentrancyGuard: true,
      emitsEvent: 'SplitDistributed',
    },
  ]);

  // New function draft modal/fields
  const [newFnName, setNewFnName] = useState('');
  const [newFnDesc, setNewFnDesc] = useState('');
  const [newFnPayable, setNewFnPayable] = useState(true);
  const [newFnMinEth, setNewFnMinEth] = useState('0.001');
  const [newFnMaxEth, setNewFnMaxEth] = useState('10.0');

  // Simulator interaction states
  const [selectedMethod, setSelectedMethod] = useState<string>('depositPayable');
  const [msgValueEth, setMsgValueEth] = useState<string>('0.05');
  const [isExecuting, setIsExecuting] = useState(false);
  const [lastReceipt, setLastReceipt] = useState<{
    txHash: string;
    gasUsed: number;
    logs: string[];
    valueEth: string;
    splits?: Array<{ recipient: string; amountWei: bigint }>;
  } | null>(null);

  const [copiedCode, setCopiedCode] = useState(false);
  const [toastMessage, setToastMessage] = useState<string | null>(null);

  const showToast = (msg: string) => {
    setToastMessage(msg);
    setTimeout(() => setToastMessage(null), 3500);
  };

  // Helper to compute total bps
  const totalBps = beneficiaries.reduce((sum, b) => sum + b.bps, 0);

  // Template presets handler
  const handleSelectTemplate = (t: PayableTemplateType) => {
    setTemplate(t);
    if (t === 'income-splitter') {
      setContractName('NexusIncomeSplitterV2');
      setFunctions([
        {
          name: 'depositPayable',
          description: 'Deposits ETH into splitter pool to be routed to beneficiaries',
          payable: true,
          minDepositWei: 1000000000000000n,
          maxDepositWei: 50000000000000000000n,
          hasReentrancyGuard: true,
          emitsEvent: 'CustomDeposit',
        },
        {
          name: 'distributePool',
          description: 'Splits contract ETH across all configured beneficiaries',
          payable: false,
          minDepositWei: 0n,
          maxDepositWei: 0n,
          hasReentrancyGuard: true,
          emitsEvent: 'SplitDistributed',
        },
      ]);
    } else if (t === 'agent-bounty-vault') {
      setContractName('NexusAgentBountyVaultV2');
      setFunctions([
        {
          name: 'createBounty',
          description: 'Locks payable ETH bounty for autonomous MCP agents with task id',
          payable: true,
          minDepositWei: 10000000000000000n,
          maxDepositWei: 20000000000000000000n,
          hasReentrancyGuard: true,
          emitsEvent: 'BountyCreated',
        },
        {
          name: 'claimBounty',
          description: 'Releases bounty reward to claiming agent after validation',
          payable: false,
          minDepositWei: 0n,
          maxDepositWei: 0n,
          hasReentrancyGuard: true,
          emitsEvent: 'BountyClaimed',
        },
      ]);
    } else if (t === 'game-wager-pool') {
      setContractName('NexusGameTheoryWagerV2');
      setFunctions([
        {
          name: 'placeWager',
          description: 'Enters player into game theory round with payable ETH deposit',
          payable: true,
          minDepositWei: 1000000000000000n,
          maxDepositWei: 5000000000000000000n,
          hasReentrancyGuard: true,
          emitsEvent: 'WagerPlaced',
        },
        {
          name: 'settleRound',
          description: 'Settles game round payout to winning address',
          payable: false,
          minDepositWei: 0n,
          maxDepositWei: 0n,
          hasReentrancyGuard: true,
          emitsEvent: 'RewardPaid',
        },
      ]);
    } else if (t === 'micro-fee-accumulator') {
      setContractName('NexusMicroFeeAccumulatorV1');
      setFunctions([
        {
          name: 'recordMicroFee',
          description: 'Records sub-cent Satoshi/Wei micro-fee payment from financial signals bus',
          payable: true,
          minDepositWei: 1000000000000n, // 1 Gwei
          maxDepositWei: 1000000000000000000n,
          hasReentrancyGuard: false,
          emitsEvent: 'MicroFeeAccumulated',
        },
        {
          name: 'sweepToTreasury',
          description: 'Sweeps accumulated micro-fees to DAO treasury',
          payable: false,
          minDepositWei: 0n,
          maxDepositWei: 0n,
          hasReentrancyGuard: true,
          emitsEvent: 'SweepToTreasury',
        },
      ]);
    } else {
      setContractName('NexusCustomPayableSandbox');
      setFunctions([
        {
          name: 'customPayableMethod',
          description: 'User-defined payable entry point with reentrancy protection',
          payable: true,
          minDepositWei: 0n,
          maxDepositWei: 10000000000000000000n,
          hasReentrancyGuard: true,
          emitsEvent: 'CustomDeposit',
        },
      ]);
    }
  };

  const handleAddBeneficiary = () => {
    setBeneficiaries([
      ...beneficiaries,
      {
        address: '0x' + Array.from({ length: 40 }, () => Math.floor(Math.random() * 16).toString(16)).join(''),
        label: `Sub-Stream #${beneficiaries.length + 1}`,
        bps: 1000,
      },
    ]);
  };

  const handleRemoveBeneficiary = (idx: number) => {
    setBeneficiaries(beneficiaries.filter((_, i) => i !== idx));
  };

  const handleUpdateBeneficiary = (idx: number, field: keyof PayableBeneficiary, val: any) => {
    setBeneficiaries(
      beneficiaries.map((b, i) => (i === idx ? { ...b, [field]: val } : b))
    );
  };

  const handleAddFunction = () => {
    if (!newFnName.trim()) return;
    const minWei = BigInt(Math.floor(parseFloat(newFnMinEth || '0') * 1e18));
    const maxWei = BigInt(Math.floor(parseFloat(newFnMaxEth || '0') * 1e18));

    setFunctions([
      ...functions,
      {
        name: newFnName.trim(),
        description: newFnDesc.trim() || 'Custom payable function',
        payable: newFnPayable,
        minDepositWei: minWei,
        maxDepositWei: maxWei,
        hasReentrancyGuard: true,
        emitsEvent: 'CustomDeposit',
      },
    ]);

    setNewFnName('');
    setNewFnDesc('');
  };

  const handleDeployContract = () => {
    const config: PayableContractConfig = {
      contractName: contractName.trim() || 'NexusPayableVault',
      template,
      ownerAddress: NEXUS_METADATA.ownerAddress,
      beneficiaries,
      functions,
      allowFallbackPayable: allowFallback,
      enableEmergencyWithdraw: emergencyWithdraw,
    };

    const deployed = createPayableContract(config);
    showToast(`Successfully produced and deployed ${deployed.config.contractName} to local simulator!`);
    setActiveMode('simulate');
  };

  const handleExecuteSimulated = async () => {
    if (!selectedPayableContract) return;
    setIsExecuting(true);

    try {
      const valueWei = BigInt(Math.floor(parseFloat(msgValueEth || '0') * 1e18));
      const res = await executePayableMethod(
        selectedPayableContract.id,
        selectedMethod,
        valueWei
      );

      setLastReceipt({
        txHash: res.txHash,
        gasUsed: res.gasUsed,
        logs: res.logs,
        valueEth: msgValueEth,
        splits: res.distributedSplits,
      });

      showToast(`Payable call executed! ${res.logs[0] || 'Success'}`);
    } catch (err: any) {
      showToast(`Execution error: ${err.message || 'Unknown'}`);
    } finally {
      setIsExecuting(false);
    }
  };

  const handleExportToWorkbench = () => {
    if (!selectedPayableContract) return;
    exportPayableContractToWorkbench(selectedPayableContract.id);
    showToast(`Contract ${selectedPayableContract.config.contractName} exported to Contract Workbench as verified chunks!`);
  };

  const handleCopyCode = () => {
    if (!selectedPayableContract) return;
    navigator.clipboard.writeText(selectedPayableContract.solidityCode);
    setCopiedCode(true);
    setTimeout(() => setCopiedCode(false), 2000);
  };

  return (
    <div className="space-y-6">
      {/* Toast Notification */}
      {toastMessage && (
        <div className="fixed bottom-6 right-6 z-50 bg-cyan-950 border border-cyan-500 text-cyan-200 px-4 py-2.5 rounded-lg shadow-2xl flex items-center gap-2 text-xs font-mono animate-bounce">
          <Sparkles className="w-4 h-4 text-cyan-400" />
          <span>{toastMessage}</span>
        </div>
      )}

      {/* Top Banner Header */}
      <div className="rounded-xl border border-slate-800 bg-gradient-to-r from-slate-900 via-cyan-950/20 to-slate-900 p-5 shadow-lg">
        <div className="flex flex-col md:flex-row md:items-center justify-between gap-4">
          <div className="space-y-1">
            <div className="flex items-center gap-2 text-xs font-mono text-cyan-400 uppercase tracking-wider">
              <Coins className="w-4 h-4 text-cyan-400" />
              <span>Payable Contract Production Studio</span>
              <span className="text-slate-600">•</span>
              <span className="text-amber-400 font-semibold">{NEXUS_METADATA.standard}</span>
            </div>
            <h1 className="text-xl md:text-2xl font-bold text-slate-100 flex items-center gap-2">
              Produce Custom Contracts with Payables & Value Routing
            </h1>
            <p className="text-xs text-slate-400 max-w-3xl">
              Author, template, compile, and execute simulated Solidity 0.8.20 payable contracts with{' '}
              <code className="text-cyan-300 font-mono">receive() external payable</code>, reentrancy guards,
              custom <code className="text-cyan-300 font-mono">msg.value</code> handlers, and 1-click chunking
              to the DAO Governor.
            </p>
          </div>

          <div className="flex items-center gap-2 self-start md:self-auto">
            <button
              onClick={() => setActiveMode('produce')}
              className={`px-3.5 py-2 rounded-lg text-xs font-semibold flex items-center gap-1.5 transition ${
                activeMode === 'produce'
                  ? 'bg-cyan-600 text-white shadow-lg shadow-cyan-900/40'
                  : 'bg-slate-800 text-slate-300 hover:bg-slate-700'
              }`}
            >
              <Plus className="w-3.5 h-3.5" />
              Contract Producer
            </button>
            <button
              onClick={() => setActiveMode('simulate')}
              className={`px-3.5 py-2 rounded-lg text-xs font-semibold flex items-center gap-1.5 transition ${
                activeMode === 'simulate'
                  ? 'bg-emerald-600 text-white shadow-lg shadow-emerald-900/40'
                  : 'bg-slate-800 text-slate-300 hover:bg-slate-700'
              }`}
            >
              <Terminal className="w-3.5 h-3.5" />
              Simulator & Tester ({payableContracts.length})
            </button>
          </div>
        </div>
      </div>

      {/* Main Content Areas */}
      {activeMode === 'produce' ? (
        <div className="grid grid-cols-1 lg:grid-cols-12 gap-6">
          {/* Left Configuration Form */}
          <div className="lg:col-span-6 space-y-5">
            <div className="bg-slate-900/80 border border-slate-800 rounded-xl p-5 space-y-4">
              <div className="flex items-center justify-between border-b border-slate-800 pb-3">
                <div className="flex items-center gap-2 font-semibold text-sm text-slate-200">
                  <Sliders className="w-4 h-4 text-cyan-400" />
                  <span>Contract Architecture & Template</span>
                </div>
                <span className="text-[11px] font-mono text-cyan-400 bg-cyan-950/60 px-2 py-0.5 rounded border border-cyan-800/60">
                  Solidity ^0.8.20
                </span>
              </div>

              {/* Template selector pills */}
              <div className="space-y-1.5">
                <label className="text-xs font-medium text-slate-300">Preset Payable Architecture</label>
                <div className="grid grid-cols-2 gap-2">
                  {[
                    { id: 'income-splitter', label: 'Income Splitter & Distributor', desc: 'Auto-splits msg.value to beneficiaries' },
                    { id: 'agent-bounty-vault', label: 'Agent Bounty Vault', desc: 'Payable bounties for MCP swarm agents' },
                    { id: 'game-wager-pool', label: 'Game Theory Wager Pool', desc: 'Payable session entrance with skill multipliers' },
                    { id: 'micro-fee-accumulator', label: 'Micro-Fee Accumulator', desc: 'Sub-cent Satoshi/Wei streams from Port 8790' },
                    { id: 'custom-payable', label: 'Custom Payable Sandbox', desc: 'Blank canvas for custom payable methods' },
                  ].map((tpl) => (
                    <button
                      key={tpl.id}
                      type="button"
                      onClick={() => handleSelectTemplate(tpl.id as PayableTemplateType)}
                      className={`text-left p-2.5 rounded-lg border transition ${
                        template === tpl.id
                          ? 'border-cyan-500 bg-cyan-950/40 text-cyan-200 ring-1 ring-cyan-500'
                          : 'border-slate-800 bg-slate-950/40 text-slate-400 hover:border-slate-700'
                      }`}
                    >
                      <div className="text-xs font-semibold text-slate-200">{tpl.label}</div>
                      <div className="text-[10px] text-slate-400 truncate">{tpl.desc}</div>
                    </button>
                  ))}
                </div>
              </div>

              {/* Contract name */}
              <div className="space-y-1.5">
                <label className="text-xs font-medium text-slate-300">Contract Name</label>
                <input
                  type="text"
                  value={contractName}
                  onChange={(e) => setContractName(e.target.value)}
                  className="w-full bg-slate-950 border border-slate-700 rounded-lg px-3 py-2 text-xs font-mono text-cyan-300 focus:outline-none focus:border-cyan-500"
                  placeholder="e.g. NexusPayableVault"
                />
              </div>

              {/* Toggles */}
              <div className="grid grid-cols-2 gap-3 pt-2">
                <label className="flex items-center gap-2 text-xs text-slate-300 cursor-pointer">
                  <input
                    type="checkbox"
                    checked={allowFallback}
                    onChange={(e) => setAllowFallback(e.target.checked)}
                    className="rounded border-slate-700 bg-slate-950 text-cyan-500 focus:ring-0"
                  />
                  <span>
                    Include <code className="text-cyan-400 font-mono">receive() payable</code>
                  </span>
                </label>
                <label className="flex items-center gap-2 text-xs text-slate-300 cursor-pointer">
                  <input
                    type="checkbox"
                    checked={emergencyWithdraw}
                    onChange={(e) => setEmergencyWithdraw(e.target.checked)}
                    className="rounded border-slate-700 bg-slate-950 text-cyan-500 focus:ring-0"
                  />
                  <span>
                    Emergency Withdraw (<code className="text-cyan-400 font-mono">onlyOwner</code>)
                  </span>
                </label>
              </div>

              {/* Beneficiaries Section for Income Splitter */}
              {template === 'income-splitter' && (
                <div className="space-y-3 pt-3 border-t border-slate-800">
                  <div className="flex items-center justify-between">
                    <div>
                      <div className="text-xs font-semibold text-slate-200 flex items-center gap-1.5">
                        <TrendingUp className="w-3.5 h-3.5 text-cyan-400" />
                        <span>Beneficiary Distribution Basis Points</span>
                      </div>
                      <div className="text-[10px] text-slate-400">
                        Total: <span className={totalBps === 10000 ? 'text-emerald-400 font-bold' : 'text-amber-400 font-bold'}>{totalBps} / 10,000 bps ({totalBps / 100}%)</span>
                      </div>
                    </div>
                    <button
                      type="button"
                      onClick={handleAddBeneficiary}
                      className="text-[11px] text-cyan-400 hover:text-cyan-300 flex items-center gap-1 font-medium"
                    >
                      <Plus className="w-3 h-3" /> Add Beneficiary
                    </button>
                  </div>

                  <div className="space-y-2 max-h-56 overflow-y-auto pr-1">
                    {beneficiaries.map((b, idx) => (
                      <div key={idx} className="bg-slate-950/70 border border-slate-800 rounded-lg p-2.5 flex items-center gap-2">
                        <div className="flex-1 space-y-1">
                          <input
                            type="text"
                            value={b.label}
                            onChange={(e) => handleUpdateBeneficiary(idx, 'label', e.target.value)}
                            className="w-full bg-transparent text-[11px] font-semibold text-slate-200 focus:outline-none border-b border-transparent focus:border-cyan-500"
                            placeholder="Beneficiary Label"
                          />
                          <input
                            type="text"
                            value={b.address}
                            onChange={(e) => handleUpdateBeneficiary(idx, 'address', e.target.value)}
                            className="w-full bg-transparent text-[10px] font-mono text-slate-400 focus:outline-none border-b border-transparent focus:border-cyan-500"
                            placeholder="0xRecipientAddress"
                          />
                        </div>
                        <div className="w-24 text-right">
                          <div className="text-[10px] text-slate-400">Share (bps)</div>
                          <input
                            type="number"
                            value={b.bps}
                            onChange={(e) => handleUpdateBeneficiary(idx, 'bps', parseInt(e.target.value) || 0)}
                            className="w-full bg-slate-900 border border-slate-700 rounded px-1.5 py-0.5 text-xs font-mono text-cyan-300 text-right focus:outline-none focus:border-cyan-500"
                          />
                        </div>
                        <button
                          type="button"
                          onClick={() => handleRemoveBeneficiary(idx)}
                          className="text-slate-500 hover:text-rose-400 p-1"
                        >
                          <Trash2 className="w-3.5 h-3.5" />
                        </button>
                      </div>
                    ))}
                  </div>
                </div>
              )}

              {/* Custom Functions List */}
              <div className="space-y-3 pt-3 border-t border-slate-800">
                <div className="text-xs font-semibold text-slate-200 flex items-center justify-between">
                  <div className="flex items-center gap-1.5">
                    <FileCode className="w-3.5 h-3.5 text-cyan-400" />
                    <span>Configured Contract Functions ({functions.length})</span>
                  </div>
                </div>

                <div className="space-y-2">
                  {functions.map((fn, idx) => (
                    <div key={idx} className="bg-slate-950/70 border border-slate-800 rounded-lg p-2.5 flex items-center justify-between text-xs">
                      <div>
                        <div className="font-mono text-cyan-300 font-semibold flex items-center gap-1.5">
                          <span>{fn.name}()</span>
                          {fn.payable && (
                            <span className="text-[9px] bg-amber-950 text-amber-400 px-1.5 py-0.2 rounded border border-amber-800/60 uppercase">
                              payable
                            </span>
                          )}
                          {fn.hasReentrancyGuard && (
                            <span className="text-[9px] bg-emerald-950 text-emerald-400 px-1.5 py-0.2 rounded border border-emerald-800/60">
                              nonReentrant
                            </span>
                          )}
                        </div>
                        <div className="text-[10px] text-slate-400">{fn.description}</div>
                      </div>

                      <button
                        type="button"
                        onClick={() => setFunctions(functions.filter((_, i) => i !== idx))}
                        className="text-slate-500 hover:text-rose-400 p-1"
                      >
                        <Trash2 className="w-3.5 h-3.5" />
                      </button>
                    </div>
                  ))}
                </div>

                {/* Add new function form */}
                <div className="bg-slate-950/50 border border-slate-800/80 rounded-lg p-3 space-y-2">
                  <div className="text-[11px] font-semibold text-slate-300">Add Custom Payable Method</div>
                  <div className="grid grid-cols-2 gap-2">
                    <input
                      type="text"
                      value={newFnName}
                      onChange={(e) => setNewFnName(e.target.value)}
                      placeholder="e.g. fundAgentVault"
                      className="bg-slate-900 border border-slate-700 rounded px-2 py-1 text-xs font-mono text-slate-200 focus:outline-none focus:border-cyan-500"
                    />
                    <input
                      type="text"
                      value={newFnDesc}
                      onChange={(e) => setNewFnDesc(e.target.value)}
                      placeholder="Function description"
                      className="bg-slate-900 border border-slate-700 rounded px-2 py-1 text-xs text-slate-200 focus:outline-none focus:border-cyan-500"
                    />
                  </div>
                  <div className="flex items-center justify-between text-xs pt-1">
                    <label className="flex items-center gap-1.5 text-slate-300">
                      <input
                        type="checkbox"
                        checked={newFnPayable}
                        onChange={(e) => setNewFnPayable(e.target.checked)}
                        className="rounded border-slate-700 bg-slate-950 text-cyan-500"
                      />
                      <span>Mark as <code className="text-amber-400 font-mono">payable</code></span>
                    </label>

                    <button
                      type="button"
                      onClick={handleAddFunction}
                      className="px-2.5 py-1 bg-cyan-700 text-white rounded text-[11px] font-medium hover:bg-cyan-600 flex items-center gap-1"
                    >
                      <Plus className="w-3 h-3" /> Add Function
                    </button>
                  </div>
                </div>
              </div>

              {/* Deploy / Generate button */}
              <div className="pt-2">
                <button
                  type="button"
                  onClick={handleDeployContract}
                  className="w-full py-2.5 bg-gradient-to-r from-cyan-600 to-blue-600 hover:from-cyan-500 hover:to-blue-500 text-white font-semibold rounded-lg text-xs shadow-lg shadow-cyan-900/40 flex items-center justify-center gap-2 transition"
                >
                  <Sparkles className="w-4 h-4" />
                  Produce & Deploy Contract to Local Simulator
                </button>
              </div>
            </div>
          </div>

          {/* Right Live Solidity Preview */}
          <div className="lg:col-span-6 space-y-4">
            <div className="bg-slate-900/80 border border-slate-800 rounded-xl p-5 space-y-3">
              <div className="flex items-center justify-between border-b border-slate-800 pb-3">
                <div className="flex items-center gap-2 font-semibold text-sm text-slate-200">
                  <Terminal className="w-4 h-4 text-cyan-400" />
                  <span>Real-Time Solidity 0.8.20 Source Preview</span>
                </div>
                <div className="text-[11px] font-mono text-slate-400">
                  Authority: <span className="text-cyan-400">@FuzzysTodd</span>
                </div>
              </div>

              {/* Preview Code View */}
              <div className="bg-slate-950 border border-slate-800 rounded-lg p-3 font-mono text-[11px] text-slate-300 max-h-[540px] overflow-y-auto overflow-x-auto space-y-1">
                <pre className="text-emerald-400/90 leading-relaxed whitespace-pre font-mono">
                  {`// SPDX-License-Identifier: MIT
// Standard: NES v1.0 (Nexus Encryption Standard)
// Canonical Authority: @FuzzysTodd (tenkrypt.cb.id)
// Target: Solidity ^0.8.20

pragma solidity ^0.8.20;

abstract contract ReentrancyGuard {
    uint256 private constant _NOT_ENTERED = 1;
    uint256 private constant _ENTERED = 2;
    uint256 private _status = 1;
    modifier nonReentrant() {
        require(_status != 2, "Reentrant call");
        _status = 2;
        _;
        _status = 1;
    }
}

contract ${contractName} is ReentrancyGuard {
    uint256 public totalReceived;
    uint256 public totalDistributed;

    event DirectEthReceived(address indexed sender, uint256 amount);
    event CustomDeposit(address indexed sender, uint256 amount, uint256 timestamp);

${allowFallback ? `    receive() external payable {
        totalReceived += msg.value;
        emit DirectEthReceived(msg.sender, msg.value);
    }\n` : ''}
${functions.map(f => `    function ${f.name}() external ${f.payable ? 'payable ' : ''}${f.hasReentrancyGuard ? 'nonReentrant ' : ''}{
${f.minDepositWei > 0n ? `        require(msg.value >= ${f.minDepositWei}, "Below min");\n` : ''}        totalReceived += msg.value;
        emit ${f.emitsEvent}(msg.sender, msg.value, block.timestamp);
    }`).join('\n\n')}

    function getContractBalance() external view returns (uint256) {
        return address(this).balance;
    }
}`}
                </pre>
              </div>

              <div className="flex items-center justify-between text-xs text-slate-400 pt-1">
                <div className="flex items-center gap-1.5">
                  <CheckCircle2 className="w-3.5 h-3.5 text-emerald-400" />
                  <span>Verified ReentrancyGuard & Payable Fallback</span>
                </div>
                <span className="font-mono text-cyan-400">100% Deterministic AST</span>
              </div>
            </div>
          </div>
        </div>
      ) : (
        /* Simulator & Tester Mode */
        <div className="grid grid-cols-1 lg:grid-cols-12 gap-6">
          {/* Left Column: Contract Selector & Overview */}
          <div className="lg:col-span-5 space-y-4">
            <div className="bg-slate-900/80 border border-slate-800 rounded-xl p-5 space-y-4">
              <div className="flex items-center justify-between border-b border-slate-800 pb-3">
                <div className="flex items-center gap-2 font-semibold text-sm text-slate-200">
                  <Database className="w-4 h-4 text-cyan-400" />
                  <span>Deployed Payable Contracts</span>
                </div>
                <span className="text-xs font-mono text-cyan-400 bg-cyan-950/60 px-2 py-0.5 rounded border border-cyan-800/60">
                  {payableContracts.length} Registered
                </span>
              </div>

              {/* Contract List */}
              <div className="space-y-2">
                {payableContracts.map((c) => (
                  <button
                    key={c.id}
                    type="button"
                    onClick={() => {
                      setSelectedPayableContract(c);
                      setSelectedMethod(c.config.functions[0]?.name || 'depositPayable');
                    }}
                    className={`w-full text-left p-3 rounded-lg border transition ${
                      selectedPayableContract?.id === c.id
                        ? 'border-cyan-500 bg-cyan-950/40 text-cyan-200'
                        : 'border-slate-800 bg-slate-950/50 text-slate-400 hover:border-slate-700'
                    }`}
                  >
                    <div className="flex items-center justify-between">
                      <span className="text-xs font-bold text-slate-200 font-mono">{c.config.contractName}</span>
                      <span className="text-[10px] font-mono bg-slate-800 px-1.5 py-0.5 rounded text-emerald-400">
                        {(Number(c.balanceWei) / 1e18).toFixed(4)} ETH
                      </span>
                    </div>
                    <div className="text-[10px] text-slate-400 font-mono truncate mt-0.5">
                      {c.deployedAddress}
                    </div>
                    <div className="flex items-center gap-2 mt-1.5 text-[10px] text-slate-500">
                      <span>Template: {c.config.template}</span>
                      <span>•</span>
                      <span>Executions: {c.executionCount}</span>
                    </div>
                  </button>
                ))}
              </div>

              {/* Selected contract metadata */}
              {selectedPayableContract && (
                <div className="bg-slate-950/80 border border-slate-800 rounded-lg p-3 space-y-2 text-xs">
                  <div className="flex items-center justify-between text-slate-400 text-[11px]">
                    <span>Total Received:</span>
                    <span className="font-mono text-cyan-400">
                      {(Number(selectedPayableContract.totalReceivedWei) / 1e18).toFixed(4)} ETH
                    </span>
                  </div>
                  <div className="flex items-center justify-between text-slate-400 text-[11px]">
                    <span>Total Distributed:</span>
                    <span className="font-mono text-emerald-400">
                      {(Number(selectedPayableContract.totalDistributedWei) / 1e18).toFixed(4)} ETH
                    </span>
                  </div>
                  <div className="flex items-center justify-between text-slate-400 text-[11px]">
                    <span>Contract Balance:</span>
                    <span className="font-mono text-amber-400 font-bold">
                      {(Number(selectedPayableContract.balanceWei) / 1e18).toFixed(4)} ETH
                    </span>
                  </div>

                  <div className="pt-2 flex items-center gap-2">
                    <button
                      type="button"
                      onClick={handleExportToWorkbench}
                      className="flex-1 py-1.5 bg-cyan-700 hover:bg-cyan-600 text-white rounded text-[11px] font-semibold flex items-center justify-center gap-1.5 transition"
                    >
                      <ArrowUpRight className="w-3.5 h-3.5" />
                      Export to Chunk Poster
                    </button>
                    <button
                      type="button"
                      onClick={handleCopyCode}
                      className="px-2.5 py-1.5 bg-slate-800 hover:bg-slate-700 text-slate-300 rounded text-[11px] flex items-center gap-1 transition"
                    >
                      {copiedCode ? <CheckCircle2 className="w-3.5 h-3.5 text-emerald-400" /> : <Copy className="w-3.5 h-3.5" />}
                      {copiedCode ? 'Copied' : 'Copy'}
                    </button>
                  </div>
                </div>
              )}
            </div>
          </div>

          {/* Right Column: Interactive Payable Caller */}
          <div className="lg:col-span-7 space-y-4">
            <div className="bg-slate-900/80 border border-slate-800 rounded-xl p-5 space-y-4">
              <div className="flex items-center justify-between border-b border-slate-800 pb-3">
                <div className="flex items-center gap-2 font-semibold text-sm text-slate-200">
                  <Terminal className="w-4 h-4 text-emerald-400" />
                  <span>Execute Payable Transaction Simulator</span>
                </div>
                <div className="text-[11px] font-mono text-slate-400">
                  Caller: <span className="text-cyan-400">{account.slice(0, 8)}...{account.slice(-6)}</span>
                </div>
              </div>

              {selectedPayableContract ? (
                <div className="space-y-4">
                  {/* Method choice */}
                  <div className="space-y-1.5">
                    <label className="text-xs font-medium text-slate-300">Target Function</label>
                    <div className="grid grid-cols-2 gap-2">
                      {selectedPayableContract.config.functions.map((fn) => (
                        <button
                          key={fn.name}
                          type="button"
                          onClick={() => setSelectedMethod(fn.name)}
                          className={`text-left p-2.5 rounded-lg border text-xs transition ${
                            selectedMethod === fn.name
                              ? 'border-cyan-500 bg-cyan-950/40 text-cyan-200'
                              : 'border-slate-800 bg-slate-950/40 text-slate-400 hover:border-slate-700'
                          }`}
                        >
                          <div className="font-mono font-semibold text-slate-200 flex items-center justify-between">
                            <span>{fn.name}()</span>
                            {fn.payable && (
                              <span className="text-[9px] bg-amber-950 text-amber-400 px-1 rounded">
                                PAYABLE
                              </span>
                            )}
                          </div>
                          <div className="text-[10px] text-slate-400 truncate mt-0.5">{fn.description}</div>
                        </button>
                      ))}

                      {selectedPayableContract.config.allowFallbackPayable && (
                        <button
                          type="button"
                          onClick={() => setSelectedMethod('receive')}
                          className={`text-left p-2.5 rounded-lg border text-xs transition ${
                            selectedMethod === 'receive'
                              ? 'border-cyan-500 bg-cyan-950/40 text-cyan-200'
                              : 'border-slate-800 bg-slate-950/40 text-slate-400 hover:border-slate-700'
                          }`}
                        >
                          <div className="font-mono font-semibold text-slate-200 flex items-center justify-between">
                            <span>receive() fallback</span>
                            <span className="text-[9px] bg-amber-950 text-amber-400 px-1 rounded">
                              DIRECT
                            </span>
                          </div>
                          <div className="text-[10px] text-slate-400 truncate mt-0.5">Direct plain ETH transfer</div>
                        </button>
                      )}
                    </div>
                  </div>

                  {/* msg.value input */}
                  <div className="space-y-1.5">
                    <div className="flex items-center justify-between">
                      <label className="text-xs font-medium text-slate-300 flex items-center gap-1.5">
                        <Coins className="w-3.5 h-3.5 text-amber-400" />
                        <span>Payable Value (msg.value in ETH)</span>
                      </label>
                      <span className="text-[11px] text-slate-400 font-mono">
                        ~${(parseFloat(msgValueEth || '0') * 3150).toLocaleString()} USD
                      </span>
                    </div>

                    <input
                      type="number"
                      step="0.001"
                      value={msgValueEth}
                      onChange={(e) => setMsgValueEth(e.target.value)}
                      className="w-full bg-slate-950 border border-slate-700 rounded-lg px-3 py-2 text-sm font-mono text-cyan-300 focus:outline-none focus:border-cyan-500"
                      placeholder="0.05"
                    />

                    {/* Quick value presets */}
                    <div className="flex items-center gap-2 pt-1">
                      {['0.01', '0.05', '0.1', '0.5', '1.0'].map((val) => (
                        <button
                          key={val}
                          type="button"
                          onClick={() => setMsgValueEth(val)}
                          className="px-2 py-0.5 bg-slate-800 hover:bg-slate-700 text-[10px] font-mono text-slate-300 rounded"
                        >
                          +{val} ETH
                        </button>
                      ))}
                      <button
                        type="button"
                        onClick={() => setMsgValueEth('0')}
                        className="px-2 py-0.5 bg-slate-800/60 hover:bg-slate-800 text-[10px] font-mono text-slate-400 rounded"
                      >
                        0 ETH (call only)
                      </button>
                    </div>
                  </div>

                  {/* Execute Button */}
                  <button
                    type="button"
                    disabled={isExecuting}
                    onClick={handleExecuteSimulated}
                    className="w-full py-2.5 bg-emerald-600 hover:bg-emerald-500 disabled:opacity-50 text-white font-semibold rounded-lg text-xs shadow-lg shadow-emerald-900/40 flex items-center justify-center gap-2 transition"
                  >
                    {isExecuting ? <RefreshCw className="w-4 h-4 animate-spin" /> : <Send className="w-4 h-4" />}
                    <span>Simulate Payable Call: {selectedMethod}{parseFloat(msgValueEth || '0') > 0 ? `{value: ${msgValueEth} ETH}` : ''}()</span>
                  </button>

                  {/* Receipt and Log Output */}
                  {lastReceipt && (
                    <div className="bg-slate-950 border border-slate-800 rounded-lg p-3 space-y-2 text-xs">
                      <div className="flex items-center justify-between text-[11px] font-semibold text-emerald-400 border-b border-slate-800 pb-1.5">
                        <div className="flex items-center gap-1.5">
                          <CheckCircle2 className="w-3.5 h-3.5" />
                          <span>Simulated On-Chain Execution Receipt</span>
                        </div>
                        <span className="font-mono text-slate-400">Gas: {lastReceipt.gasUsed.toLocaleString()}</span>
                      </div>

                      <div className="text-[10px] font-mono text-slate-400">
                        TxHash: <span className="text-cyan-300">{lastReceipt.txHash}</span>
                      </div>

                      {lastReceipt.splits && lastReceipt.splits.length > 0 && (
                        <div className="space-y-1 pt-1 border-t border-slate-800/80">
                          <div className="text-[10px] font-semibold text-slate-300">Beneficiary Splits Distributed:</div>
                          {lastReceipt.splits.map((s, i) => (
                            <div key={i} className="flex items-center justify-between text-[10px] font-mono text-slate-400 bg-slate-900/60 px-2 py-0.5 rounded">
                              <span>{s.recipient.slice(0, 10)}...{s.recipient.slice(-6)}</span>
                              <span className="text-emerald-400 font-semibold">
                                +{(Number(s.amountWei) / 1e18).toFixed(6)} ETH
                              </span>
                            </div>
                          ))}
                        </div>
                      )}

                      <div className="space-y-0.5 text-[10px] font-mono text-slate-500 pt-1">
                        {lastReceipt.logs.map((log, i) => (
                          <div key={i}>&gt; {log}</div>
                        ))}
                      </div>
                    </div>
                  )}
                </div>
              ) : (
                <div className="text-center py-12 text-slate-500 text-xs">
                  No payable contract selected. Select one from the left or switch to Producer mode to generate one.
                </div>
              )}
            </div>
          </div>
        </div>
      )}
    </div>
  );
};
