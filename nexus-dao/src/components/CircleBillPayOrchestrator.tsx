/**
 * @license
 * SPDX-License-Identifier: Apache-2.0
 * The Nexus Protocol DAO - Circle Wallets & Autonomous Bill Pay Orchestrator
 * Brings the orchestrator online to pay all DAO operational bills automatically
 * using developer-controlled Circle Wallets and the MCP Agent Fleet.
 */

import React, { useState } from 'react';
import { useNexusDao } from '../context/NexusDaoContext';
import { BillCategory, DaoBill } from '../dao/logic';
import { NEXUS_METADATA } from '../data/nexusContracts';
import {
  Wallet,
  Zap,
  Server,
  CheckCircle2,
  Clock,
  ShieldCheck,
  CreditCard,
  Plus,
  Coins,
  RefreshCw,
  ExternalLink,
  Sliders,
  DollarSign,
  AlertTriangle,
  Play,
  Copy,
  Receipt,
  Radio,
  Sparkles,
  Building2,
  Globe,
  FileText,
} from 'lucide-react';

export const CircleBillPayOrchestrator: React.FC = () => {
  const {
    account,
    circleWallets,
    daoBills,
    billPaymentReceipts,
    orchestratorState,
    toggleOrchestratorOnline,
    setOrchestratorPolicyLimit,
    payDaoBill,
    payAllDaoBillsAutonomous,
    createCustomBill,
    wyomingLlcProfile,
    wyomingLlcBills,
    payWyomingLlcBill,
    payAllPendingWyomingLlcBills,
  } = useNexusDao();

  const [isProcessingAll, setIsProcessingAll] = useState(false);
  const [processingBillId, setProcessingBillId] = useState<string | null>(null);
  const [processingLlcBillId, setProcessingLlcBillId] = useState<string | null>(null);
  const [toastMessage, setToastMessage] = useState<string | null>(null);
  const [showAddModal, setShowAddModal] = useState(false);
  const [copiedAddr, setCopiedAddr] = useState<string | null>(null);

  // New bill state
  const [vendor, setVendor] = useState('');
  const [category, setCategory] = useState<BillCategory>('INFRASTRUCTURE');
  const [description, setDescription] = useState('');
  const [amountUsdc, setAmountUsdc] = useState('350.00');
  const [recipientAddress, setRecipientAddress] = useState('0x');
  const [assignedAgent, setAssignedAgent] = useState('mcp-fin-014');

  const showToast = (msg: string) => {
    setToastMessage(msg);
    setTimeout(() => setToastMessage(null), 3500);
  };

  const handlePayAll = async () => {
    setIsProcessingAll(true);
    try {
      const count = await payAllDaoBillsAutonomous();
      showToast(`Orchestrator online: Automatically settled ${count} DAO operational bills via Circle Wallets!`);
    } catch (err: any) {
      showToast(`Error: ${err.message || 'Payment execution failed'}`);
    } finally {
      setIsProcessingAll(false);
    }
  };

  const handlePaySingleBill = async (billId: string) => {
    setProcessingBillId(billId);
    try {
      const success = await payDaoBill(billId);
      if (success) {
        showToast('Bill settled gasless via Circle Agent Wallet!');
      } else {
        showToast('Payment stopped: Exceeds policy limit or insufficient balance.');
      }
    } finally {
      setProcessingBillId(null);
    }
  };

  const handleCreateBill = (e: React.FormEvent) => {
    e.preventDefault();
    if (!vendor.trim() || !amountUsdc) return;

    createCustomBill({
      vendor: vendor.trim(),
      category,
      description: description.trim() || 'DAO operational infrastructure expense',
      amountUsdc: parseFloat(amountUsdc) || 100.0,
      recipientAddress: recipientAddress.trim(),
      recipientChain: 'BASE',
      frequency: 'MONTHLY',
      dueDate: 'Due in 30 days',
      autoPayEnabled: true,
      assignedAgent,
    });

    setShowAddModal(false);
    setVendor('');
    setDescription('');
    showToast('New recurring DAO bill registered in orchestrator ledger!');
  };

  const handleCopy = (addr: string) => {
    navigator.clipboard.writeText(addr);
    setCopiedAddr(addr);
    setTimeout(() => setCopiedAddr(null), 2000);
  };

  const pendingBills = daoBills.filter((b) => b.status === 'PENDING');
  const pendingTotalUsdc = pendingBills.reduce((sum, b) => sum + b.amountUsdc, 0);
  const totalCircleUsdc = circleWallets.reduce((sum, w) => sum + w.usdcBalance, 0);

  return (
    <div className="space-y-6">
      {/* Toast Notification */}
      {toastMessage && (
        <div className="fixed bottom-6 right-6 z-50 bg-emerald-950 border border-emerald-500 text-emerald-200 px-4 py-2.5 rounded-lg shadow-2xl flex items-center gap-2 text-xs font-mono animate-bounce">
          <Sparkles className="w-4 h-4 text-emerald-400" />
          <span>{toastMessage}</span>
        </div>
      )}

      {/* Top Banner: Orchestrator Online & Command Bar */}
      <div className="relative overflow-hidden rounded-xl border border-emerald-500/30 bg-gradient-to-r from-slate-950 via-slate-900 to-emerald-950/40 p-6 shadow-2xl">
        <div className="relative z-10 flex flex-col lg:flex-row lg:items-center justify-between gap-6">
          <div className="space-y-2">
            <div className="flex items-center gap-2 text-xs font-mono text-emerald-400">
              <Zap className="w-4 h-4 text-emerald-400" />
              <span>Circle Agent Wallets & Autonomous Bill Pay Orchestrator</span>
              <span className="text-slate-600">•</span>
              <span className="text-amber-400 font-semibold">{NEXUS_METADATA.standard}</span>
              <span className="text-slate-600">•</span>
              <span className="text-cyan-400 font-mono">Circle Gateway Gasless Nanopayments</span>
            </div>

            <h1 className="text-2xl md:text-3xl font-bold text-slate-100 flex items-center gap-3">
              <span>DAO Autonomous Bill Pay Engine</span>
              <span
                className={`text-xs font-mono px-2.5 py-1 rounded-full border ${
                  orchestratorState.isOnline
                    ? 'bg-emerald-950 border-emerald-500 text-emerald-300 animate-pulse'
                    : 'bg-slate-800 border-slate-700 text-slate-400'
                }`}
              >
                {orchestratorState.isOnline ? 'ORCHESTRATOR ONLINE' : 'ORCHESTRATOR OFFLINE'}
              </span>
            </h1>

            <p className="text-xs text-slate-400 max-w-3xl">
              Developer-controlled Circle Wallets allow the MCP agent fleet to settle all DAO operational bills in
              complete automation. Zero gas fees via Circle Gateway, cryptographic agent receipts, and autonomous
              threshold safety policies.
            </p>

            {/* Live Metrics */}
            <div className="flex flex-wrap items-center gap-4 pt-1 text-xs font-mono text-slate-300">
              <div className="flex items-center gap-1.5 bg-slate-900/80 px-2.5 py-1 rounded border border-slate-800">
                <Wallet className="w-3.5 h-3.5 text-cyan-400" />
                <span>Circle Reserves: <strong className="text-cyan-300">${totalCircleUsdc.toLocaleString()} USDC</strong></span>
              </div>
              <div className="flex items-center gap-1.5 bg-slate-900/80 px-2.5 py-1 rounded border border-slate-800">
                <Server className="w-3.5 h-3.5 text-emerald-400" />
                <span>Active Paying Agents: <strong className="text-emerald-300">{circleWallets.length} Online</strong></span>
              </div>
              <div className="flex items-center gap-1.5 bg-slate-900/80 px-2.5 py-1 rounded border border-slate-800">
                <CheckCircle2 className="w-3.5 h-3.5 text-blue-400" />
                <span>Settled to Date: <strong className="text-blue-300">${orchestratorState.totalUsdcPaid.toLocaleString()} USDC ({orchestratorState.totalBillsPaidCount} bills)</strong></span>
              </div>
            </div>
          </div>

          {/* Master Actions */}
          <div className="flex flex-col items-stretch lg:items-end gap-2.5 min-w-[280px]">
            <button
              onClick={handlePayAll}
              disabled={isProcessingAll || pendingBills.length === 0}
              className="relative group px-6 py-4 rounded-xl font-bold text-sm text-slate-950 shadow-2xl transition-all duration-300 transform active:scale-95 disabled:opacity-50 bg-gradient-to-r from-emerald-400 via-teal-300 to-cyan-400 hover:from-emerald-300 hover:to-cyan-300"
            >
              <div className="flex items-center justify-center gap-2.5">
                <Play className={`w-5 h-5 ${isProcessingAll ? 'animate-spin' : 'group-hover:scale-110 transition-transform'}`} />
                <span className="tracking-wide uppercase font-mono text-xs md:text-sm">
                  {isProcessingAll ? 'Autonomous Settling...' : `Pay All Bills (${pendingBills.length})`}
                </span>
              </div>
              <div className="text-[10px] font-mono text-slate-900/80 text-center mt-1">
                Auto-Settle ${pendingTotalUsdc.toFixed(2)} USDC via Circle Agent Fleet
              </div>
            </button>

            <div className="flex items-center justify-between w-full text-[11px] font-mono text-slate-400 px-1">
              <button
                onClick={toggleOrchestratorOnline}
                className={`flex items-center gap-1 font-semibold ${
                  orchestratorState.isOnline ? 'text-emerald-400 hover:text-emerald-300' : 'text-slate-400 hover:text-slate-200'
                }`}
              >
                <Radio className={`w-3.5 h-3.5 ${orchestratorState.isOnline ? 'animate-pulse text-emerald-400' : ''}`} />
                {orchestratorState.isOnline ? 'Orchestrator Active' : 'Bring Online'}
              </button>
              <button
                onClick={() => setShowAddModal(true)}
                className="text-cyan-400 hover:text-cyan-300 flex items-center gap-1 font-semibold"
              >
                <Plus className="w-3.5 h-3.5" />
                + Add DAO Bill
              </button>
            </div>
          </div>
        </div>
      </div>

      {/* Circle Developer & Agent Wallets Grid */}
      <div className="space-y-3">
        <div className="flex items-center justify-between">
          <div className="flex items-center gap-2 text-sm font-semibold text-slate-200">
            <Wallet className="w-4 h-4 text-cyan-400" />
            <span>Circle Developer-Controlled & Agent Wallets ({circleWallets.length})</span>
          </div>
          <span className="text-[11px] text-slate-400 font-mono">
            Powered by Circle USDC Gateway • Gasless x402 Settle
          </span>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4">
          {circleWallets.map((wallet) => (
            <div
              key={wallet.id}
              className="bg-slate-900/80 border border-slate-800 rounded-xl p-4 space-y-3 hover:border-slate-700 transition"
            >
              <div className="flex items-center justify-between">
                <span className="text-[10px] font-mono bg-cyan-950 text-cyan-300 px-2 py-0.5 rounded border border-cyan-800/60 font-semibold">
                  {wallet.chain}
                </span>
                <span className="text-[10px] font-mono text-emerald-400 flex items-center gap-1 font-semibold">
                  <span className="w-1.5 h-1.5 rounded-full bg-emerald-400 animate-pulse" />
                  {wallet.status}
                </span>
              </div>

              <div>
                <div className="text-xs font-bold text-slate-200 truncate">{wallet.name}</div>
                <div className="text-[10px] text-slate-400 font-mono">Agent: {wallet.agentId}</div>
              </div>

              <div className="bg-slate-950/70 p-2.5 rounded-lg border border-slate-800/80 space-y-1">
                <div className="text-[10px] text-slate-500 uppercase">USDC Balance</div>
                <div className="text-lg font-bold font-mono text-emerald-400">
                  ${wallet.usdcBalance.toLocaleString('en-US', { minimumFractionDigits: 2 })}
                </div>
                <div className="text-[10px] text-slate-400 flex items-center justify-between pt-0.5">
                  <span>Daily Cap:</span>
                  <span className="font-mono text-slate-300">${wallet.dailyLimitUsdc.toLocaleString()}</span>
                </div>
              </div>

              <div className="flex items-center justify-between text-[10px] font-mono text-slate-400 pt-1">
                <span className="truncate mr-1">{wallet.address.slice(0, 10)}...{wallet.address.slice(-6)}</span>
                <button
                  onClick={() => handleCopy(wallet.address)}
                  className="text-cyan-400 hover:text-cyan-300 p-1 flex items-center gap-0.5"
                >
                  <Copy className="w-3 h-3" />
                  {copiedAddr === wallet.address ? 'Copied' : ''}
                </button>
              </div>
            </div>
          ))}
        </div>
      </div>

      {/* Main Split: DAO Operational Bills Ledger & Auto-Pay Policy / Receipts */}
      <div className="grid grid-cols-1 lg:grid-cols-12 gap-6">
        {/* Left Column: DAO Operational Bills Ledger */}
        <div className="lg:col-span-7 space-y-4">
          <div className="flex items-center justify-between">
            <div className="flex items-center gap-2 text-sm font-semibold text-slate-200">
              <CreditCard className="w-4 h-4 text-emerald-400" />
              <span>DAO Operational Bills Ledger ({daoBills.length})</span>
            </div>
            <span className="text-[11px] font-mono text-slate-400">
              Pending: <strong className="text-amber-300">${pendingTotalUsdc.toFixed(2)} USDC</strong>
            </span>
          </div>

          <div className="space-y-3">
            {daoBills.map((bill) => (
              <div
                key={bill.id}
                className="bg-slate-900/70 border border-slate-800 rounded-xl p-4 space-y-3 hover:border-slate-700 transition"
              >
                <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-2 border-b border-slate-800 pb-2.5">
                  <div>
                    <div className="flex items-center gap-2">
                      <span className="text-xs font-bold text-slate-200">{bill.vendor}</span>
                      <span className="text-[9px] font-mono bg-slate-800 text-slate-300 px-1.5 py-0.5 rounded">
                        {bill.category}
                      </span>
                    </div>
                    <div className="text-[11px] text-slate-400 mt-0.5">{bill.description}</div>
                  </div>

                  <div className="flex items-center gap-2 self-start sm:self-auto">
                    <span
                      className={`text-[10px] font-mono px-2 py-0.5 rounded font-bold uppercase ${
                        bill.status === 'PAID'
                          ? 'bg-emerald-950 text-emerald-400 border border-emerald-800/60'
                          : bill.status === 'NEEDS_GUARDIAN'
                          ? 'bg-purple-950 text-purple-400 border border-purple-800/60'
                          : 'bg-amber-950 text-amber-400 border border-amber-800/60'
                      }`}
                    >
                      {bill.status}
                    </span>

                    {bill.status === 'PENDING' && (
                      <button
                        onClick={() => handlePaySingleBill(bill.id)}
                        disabled={processingBillId === bill.id}
                        className="px-2.5 py-1 bg-emerald-600 hover:bg-emerald-500 disabled:opacity-50 text-white font-mono text-[10px] font-semibold rounded flex items-center gap-1 transition"
                      >
                        {processingBillId === bill.id ? (
                          <RefreshCw className="w-3 h-3 animate-spin" />
                        ) : (
                          <Play className="w-2.5 h-2.5" />
                        )}
                        Pay Now
                      </button>
                    )}
                  </div>
                </div>

                <div className="grid grid-cols-2 sm:grid-cols-4 gap-2 text-[10px] font-mono text-slate-400">
                  <div className="bg-slate-950/60 p-2 rounded border border-slate-800/80">
                    <div className="text-slate-500 uppercase">Amount</div>
                    <div className="text-xs font-bold text-emerald-300">
                      ${bill.amountUsdc.toFixed(2)} USDC
                    </div>
                  </div>
                  <div className="bg-slate-950/60 p-2 rounded border border-slate-800/80">
                    <div className="text-slate-500 uppercase">Frequency</div>
                    <div className="text-slate-300">{bill.frequency}</div>
                  </div>
                  <div className="bg-slate-950/60 p-2 rounded border border-slate-800/80">
                    <div className="text-slate-500 uppercase">Assigned Agent</div>
                    <div className="text-cyan-300 truncate">{bill.assignedAgent}</div>
                  </div>
                  <div className="bg-slate-950/60 p-2 rounded border border-slate-800/80">
                    <div className="text-slate-500 uppercase">Schedule</div>
                    <div className="text-amber-300 truncate">{bill.dueDate}</div>
                  </div>
                </div>

                {bill.lastPaidAt && (
                  <div className="text-[10px] font-mono text-slate-500 flex items-center justify-between border-t border-slate-800/80 pt-2">
                    <span>Last Settled: {bill.lastPaidAt}</span>
                    <span className="text-cyan-400 truncate">Tx: {bill.lastTxId}</span>
                  </div>
                )}
              </div>
            ))}
          </div>
        </div>

        {/* Right Column: Policy Thresholds & Real-Time Receipts */}
        <div className="lg:col-span-5 space-y-4">
          {/* Policy Limits Card */}
          <div className="bg-slate-900/80 border border-slate-800 rounded-xl p-5 space-y-4">
            <div className="flex items-center justify-between border-b border-slate-800 pb-3">
              <div className="flex items-center gap-2 font-semibold text-sm text-slate-200">
                <Sliders className="w-4 h-4 text-cyan-400" />
                <span>Autonomous Payment Policy</span>
              </div>
              <span className="text-[10px] font-mono text-emerald-400 bg-emerald-950/60 px-2 py-0.5 rounded border border-emerald-800/60">
                Circle Policy Rules
              </span>
            </div>

            <div className="space-y-2">
              <div className="flex items-center justify-between text-xs">
                <span className="text-slate-300">Auto-Approve Threshold:</span>
                <span className="font-mono text-emerald-400 font-bold">
                  ${orchestratorState.autoPayPolicyLimitUsdc.toLocaleString()} USDC
                </span>
              </div>
              <input
                type="range"
                min="500"
                max="10000"
                step="500"
                value={orchestratorState.autoPayPolicyLimitUsdc}
                onChange={(e) => setOrchestratorPolicyLimit(parseFloat(e.target.value))}
                className="w-full accent-emerald-500 bg-slate-950"
              />
              <div className="flex justify-between text-[10px] text-slate-500 font-mono">
                <span>$500 USDC</span>
                <span>$5,000 USDC</span>
                <span>$10,000 USDC</span>
              </div>
              <p className="text-[10px] text-slate-400 pt-1">
                Bills under this threshold are settled automatically by the assigned MCP agent wallet without human delay.
                Bills exceeding this limit require 3-of-5 Guardian multisig sign-off.
              </p>
            </div>
          </div>

          {/* Settled Receipts Stream */}
          <div className="bg-slate-900/80 border border-slate-800 rounded-xl p-5 space-y-3">
            <div className="flex items-center justify-between border-b border-slate-800 pb-2.5">
              <div className="flex items-center gap-2 font-semibold text-xs text-slate-200">
                <Receipt className="w-4 h-4 text-emerald-400" />
                <span>Circle Payment Receipts ({billPaymentReceipts.length})</span>
              </div>
              <span className="text-[10px] font-mono text-slate-400">Gasless Settled</span>
            </div>

            <div className="space-y-2 max-h-72 overflow-y-auto pr-1">
              {billPaymentReceipts.map((receipt) => (
                <div
                  key={receipt.paymentId}
                  className="bg-slate-950/80 p-2.5 rounded-lg border border-slate-800 text-[11px] font-mono space-y-1"
                >
                  <div className="flex items-center justify-between">
                    <span className="font-bold text-slate-200 truncate">{receipt.vendor}</span>
                    <span className="text-emerald-400 font-bold">
                      ${receipt.amountUsdc.toFixed(2)} USDC
                    </span>
                  </div>
                  <div className="flex items-center justify-between text-[10px] text-slate-400">
                    <span>Tx: {receipt.circleTxId.slice(0, 14)}...</span>
                    <span className="text-emerald-400">Fee: $0.00 (Gasless)</span>
                  </div>
                  <div className="text-[9px] text-slate-500 truncate">
                    Signature: {receipt.agentSignature}
                  </div>
                  <div className="text-[9px] text-slate-500 text-right">
                    {receipt.timestamp}
                  </div>
                </div>
              ))}
            </div>
          </div>
        </div>
      </div>

      {/* Wyoming DAO LLC Digital Bill & Subscription Payment Desk Integration */}
      <div className="bg-slate-900/80 border border-indigo-500/30 rounded-xl p-5 space-y-4">
        <div className="flex flex-col md:flex-row md:items-center justify-between gap-3 border-b border-slate-800 pb-3">
          <div>
            <div className="flex items-center gap-2 text-sm font-bold text-slate-100">
              <Building2 className="w-4 h-4 text-indigo-400" />
              <span>Wyoming DAO LLC Digital Subscription & Google Cloud Billing Rail</span>
              <span className="text-[10px] font-mono bg-indigo-950/90 text-indigo-300 px-2 py-0.5 rounded border border-indigo-800/60">
                {wyomingLlcProfile.statutoryAuthority}
              </span>
            </div>
            <p className="text-xs text-slate-400 mt-0.5">
              Legal Entity: <strong className="text-slate-200">{wyomingLlcProfile.legalName}</strong> ({wyomingLlcProfile.filingId}) • Settle Google Cloud, Google Workspace, Gemini API, and SaaS cost subscriptions directly through the Wyoming DAO LLC banking & USDC bridge.
            </p>
          </div>
          <button
            onClick={() => {
              const settled = payAllPendingWyomingLlcBills();
              showToast(
                settled > 0
                  ? `Settled ${settled} digital subscription bills via ${wyomingLlcProfile.legalName}!`
                  : 'All Wyoming DAO LLC digital subscription bills are already settled.'
              );
            }}
            className="px-3.5 py-2 bg-indigo-600 hover:bg-indigo-500 text-white font-mono text-xs font-semibold rounded-lg flex items-center gap-1.5 transition self-start md:self-auto"
          >
            <CheckCircle2 className="w-3.5 h-3.5" />
            Settle All Pending LLC Subscriptions
          </button>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-3">
          {wyomingLlcBills.map((llcBill) => (
            <div
              key={llcBill.id}
              className="bg-slate-950/80 border border-slate-800 rounded-lg p-3.5 flex flex-col justify-between gap-2.5"
            >
              <div className="space-y-1">
                <div className="flex items-center justify-between gap-2">
                  <span className="text-[10px] font-mono text-indigo-400 font-bold">{llcBill.invoiceNumber}</span>
                  <span
                    className={`text-[9px] font-mono px-1.5 py-0.5 rounded font-bold ${
                      llcBill.status === 'PAID_CURRENT_CYCLE'
                        ? 'bg-emerald-950 text-emerald-400 border border-emerald-800/60'
                        : 'bg-amber-950 text-amber-300 border border-amber-800/60'
                    }`}
                  >
                    {llcBill.status.replace(/_/g, ' ')}
                  </span>
                </div>
                <div className="text-xs font-bold text-slate-100">{llcBill.vendor}</div>
                <div className="text-[11px] text-slate-400 line-clamp-2">{llcBill.description}</div>
              </div>

              <div className="flex items-center justify-between pt-2 border-t border-slate-800/80 text-[11px] font-mono">
                <div>
                  <span className="text-emerald-400 font-bold">${llcBill.monthlyCostUsd.toLocaleString('en-US', { minimumFractionDigits: 2 })}</span>
                  <span className="text-slate-500 text-[10px] ml-1">({llcBill.billingCycle})</span>
                </div>
                {llcBill.status !== 'PAID_CURRENT_CYCLE' ? (
                  <button
                    onClick={() => {
                      setProcessingLlcBillId(llcBill.id);
                      const res = payWyomingLlcBill(llcBill.id);
                      setProcessingLlcBillId(null);
                      if (res.success) {
                        showToast(`Paid ${llcBill.vendor} ($${llcBill.monthlyCostUsd.toFixed(2)}) via Wyoming DAO LLC!`);
                      }
                    }}
                    disabled={processingLlcBillId === llcBill.id}
                    aria-label={`Pay ${llcBill.vendor} via WY LLC`}
                    className="px-2.5 py-1 bg-indigo-600 hover:bg-indigo-500 text-white rounded text-[10px] font-semibold transition"
                  >
                    Pay via WY LLC
                  </button>
                ) : (
                  <span className="text-[10px] text-emerald-400 flex items-center gap-1">
                    <FileText className="w-3 h-3" />
                    Settled
                  </span>
                )}
              </div>
            </div>
          ))}
        </div>
      </div>

      {/* Modal: Add New DAO Bill */}
      {showAddModal && (
        <div className="fixed inset-0 z-50 bg-black/80 backdrop-blur-sm flex items-center justify-center p-4">
          <div className="bg-slate-900 border border-slate-700 rounded-xl max-w-lg w-full p-6 space-y-4 shadow-2xl">
            <div className="flex items-center justify-between border-b border-slate-800 pb-3">
              <div className="flex items-center gap-2 font-bold text-sm text-slate-100">
                <CreditCard className="w-4 h-4 text-emerald-400" />
                <span>Register New DAO Operational Bill</span>
              </div>
              <button
                onClick={() => setShowAddModal(false)}
                className="text-slate-400 hover:text-slate-200 text-sm font-mono"
              >
                ✕
              </button>
            </div>

            <form onSubmit={handleCreateBill} className="space-y-3 text-xs">
              <div className="space-y-1">
                <label className="text-slate-300 font-medium">Vendor / Service Name</label>
                <input
                  type="text"
                  value={vendor}
                  onChange={(e) => setVendor(e.target.value)}
                  className="w-full bg-slate-950 border border-slate-700 rounded-lg px-3 py-1.5 text-slate-200 focus:outline-none focus:border-emerald-500"
                  placeholder="e.g. QuickNode Dedicated RPC Cluster"
                  required
                />
              </div>

              <div className="grid grid-cols-2 gap-3">
                <div className="space-y-1">
                  <label className="text-slate-300 font-medium">Category</label>
                  <select
                    value={category}
                    onChange={(e) => setCategory(e.target.value as BillCategory)}
                    className="w-full bg-slate-950 border border-slate-700 rounded-lg px-2.5 py-1.5 text-slate-200 focus:outline-none focus:border-emerald-500"
                  >
                    <option value="INFRASTRUCTURE">INFRASTRUCTURE</option>
                    <option value="ORACLE">ORACLE</option>
                    <option value="SECURITY_AUDIT">SECURITY_AUDIT</option>
                    <option value="STORAGE">STORAGE</option>
                    <option value="COMPLIANCE">COMPLIANCE</option>
                    <option value="COMPUTE_GPU">COMPUTE_GPU</option>
                  </select>
                </div>

                <div className="space-y-1">
                  <label className="text-slate-300 font-medium">Amount (USDC)</label>
                  <input
                    type="number"
                    step="0.01"
                    value={amountUsdc}
                    onChange={(e) => setAmountUsdc(e.target.value)}
                    className="w-full bg-slate-950 border border-slate-700 rounded-lg px-3 py-1.5 font-mono text-emerald-300 focus:outline-none focus:border-emerald-500"
                    placeholder="350.00"
                    required
                  />
                </div>
              </div>

              <div className="space-y-1">
                <label className="text-slate-300 font-medium">Recipient Address</label>
                <input
                  type="text"
                  value={recipientAddress}
                  onChange={(e) => setRecipientAddress(e.target.value)}
                  className="w-full bg-slate-950 border border-slate-700 rounded-lg px-3 py-1.5 font-mono text-slate-200 focus:outline-none focus:border-emerald-500"
                  placeholder="0xRecipientAddress"
                  required
                />
              </div>

              <div className="space-y-1">
                <label className="text-slate-300 font-medium">Assigned Paying Agent</label>
                <select
                  value={assignedAgent}
                  onChange={(e) => setAssignedAgent(e.target.value)}
                  className="w-full bg-slate-950 border border-slate-700 rounded-lg px-2.5 py-1.5 text-slate-200 focus:outline-none focus:border-emerald-500"
                >
                  <option value="mcp-fin-014">mcp-fin-014 (Treasury Sweeper)</option>
                  <option value="dao-accounting-bot.js">dao-accounting-bot.js (Accounting)</option>
                  <option value="mcp-fin-011">mcp-fin-011 (Security Auditor)</option>
                  <option value="mcp-fin-015">mcp-fin-015 (Arbitrage Engine)</option>
                </select>
              </div>

              <div className="space-y-1">
                <label className="text-slate-300 font-medium">Description</label>
                <textarea
                  value={description}
                  onChange={(e) => setDescription(e.target.value)}
                  className="w-full bg-slate-950 border border-slate-700 rounded-lg px-3 py-1.5 text-slate-200 focus:outline-none focus:border-emerald-500 h-16"
                  placeholder="Describe the operational service provided to the DAO"
                />
              </div>

              <div className="flex items-center justify-end gap-2 pt-2 border-t border-slate-800">
                <button
                  type="button"
                  onClick={() => setShowAddModal(false)}
                  className="px-3 py-1.5 bg-slate-800 hover:bg-slate-700 text-slate-300 rounded text-xs"
                >
                  Cancel
                </button>
                <button
                  type="submit"
                  className="px-4 py-1.5 bg-emerald-600 hover:bg-emerald-500 text-white font-semibold rounded text-xs shadow-md shadow-emerald-900/40"
                >
                  Save Bill to Orchestrator
                </button>
              </div>
            </form>
          </div>
        </div>
      )}
    </div>
  );
};
