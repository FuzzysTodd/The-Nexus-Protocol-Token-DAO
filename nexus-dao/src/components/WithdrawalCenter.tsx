/**
 * @license
 * SPDX-License-Identifier: Apache-2.0
 * The Nexus Protocol DAO - Multi-Rail Withdrawal & Payout Center (dashwall.py / withdraw.js)
 */

import React, { useState } from 'react';
import { useNexusDao } from '../context/NexusDaoContext';
import { WithdrawalRail, evaluateWithdrawalTier, WithdrawalRequest } from '../dao/logic';
import {
  ArrowDownToLine,
  ShieldCheck,
  Clock,
  CheckCircle,
  AlertTriangle,
  Building,
  Landmark,
  Coins,
  CreditCard,
  Send,
  ExternalLink,
  ShieldAlert,
  FileText,
  Search,
  Filter,
  CheckCircle2,
  XCircle,
  AlertCircle,
  History,
  Download,
  Copy,
  ChevronRight,
  UserCheck,
  X,
  FileSpreadsheet,
} from 'lucide-react';

export const WithdrawalCenter: React.FC = () => {
  const {
    account,
    operatorRole,
    withdrawals,
    requestWithdrawal,
    approveWithdrawalRequest,
    executeWithdrawalRequest,
    cancelWithdrawalRequest,
  } = useNexusDao();

  const [selectedAsset, setSelectedAsset] = useState<string>('USDC');
  const [selectedRail, setSelectedRail] = useState<WithdrawalRail>('CIRCLE_MINT_ACH');
  const [amountInput, setAmountInput] = useState<string>('25000');
  const [recipientAddressOrIban, setRecipientAddressOrIban] = useState<string>('US893847291048294');
  const [recipientName, setRecipientName] = useState<string>('Nexus Wyoming LLC Holding Corp');
  const [routingOrSwift, setRoutingOrSwift] = useState<string>('121000358');
  const [memoInput, setMemoInput] = useState<string>('Infrastructure & Developer Grant Settlement');
  const [showSuccessToast, setShowSuccessToast] = useState<string | null>(null);

  // Status tracking table states
  const [statusFilter, setStatusFilter] = useState<'ALL' | 'PENDING' | 'APPROVED' | 'REJECTED'>('ALL');
  const [searchQuery, setSearchQuery] = useState<string>('');
  const [railFilter, setRailFilter] = useState<string>('ALL');
  const [activeAuditRequest, setActiveAuditRequest] = useState<WithdrawalRequest | null>(null);
  const [rejectingRequestId, setRejectingRequestId] = useState<string | null>(null);
  const [rejectReasonInput, setRejectReasonInput] = useState<string>('Sanctions / AML KYC pre-flight screening unverified on beneficiary registry.');
  const [copyFeedback, setCopyFeedback] = useState<string | null>(null);

  const numAmount = parseFloat(amountInput) || 0;
  const usdEquivalent = selectedAsset === 'ETH' ? numAmount * 2600 : numAmount;
  const tierInfo = evaluateWithdrawalTier(usdEquivalent, selectedRail);

  const isGuardianOrOwner =
    operatorRole === 'Owner (FuzzysTodd)' || operatorRole === 'Super Delegate';

  const handleWithdrawalSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    if (numAmount <= 0 || !recipientAddressOrIban.trim() || !recipientName.trim()) return;

    const req = requestWithdrawal({
      asset: selectedAsset,
      amount: numAmount,
      rail: selectedRail,
      recipientAddressOrIban: recipientAddressOrIban.trim(),
      recipientName: recipientName.trim(),
      bankRoutingOrSwift: routingOrSwift.trim(),
      memo: memoInput.trim(),
    });

    setShowSuccessToast(req.id);
    setTimeout(() => setShowSuccessToast(null), 8000);
  };

  const handleConfirmRejection = () => {
    if (!rejectingRequestId) return;
    cancelWithdrawalRequest(rejectingRequestId, rejectReasonInput);
    setRejectingRequestId(null);
  };

  const handleExportAuditLogs = () => {
    const dataStr = 'data:text/json;charset=utf-8,' + encodeURIComponent(JSON.stringify(withdrawals, null, 2));
    const downloadAnchor = document.createElement('a');
    downloadAnchor.setAttribute('href', dataStr);
    downloadAnchor.setAttribute('download', `nexus-withdrawal-audit-${Date.now()}.json`);
    document.body.appendChild(downloadAnchor);
    downloadAnchor.click();
    downloadAnchor.remove();
    setCopyFeedback('Exported JSON audit log file');
    setTimeout(() => setCopyFeedback(null), 3000);
  };

  const handleCopyAuditSummary = () => {
    const summary = withdrawals.map((w) => ({
      id: w.id,
      status: w.status,
      asset: w.asset,
      amount: w.amount,
      usd: w.usdEquivalent,
      recipient: w.recipientName,
      rail: w.rail,
      auditEventsCount: w.auditTrail?.length || 0,
      rejectionReason: w.rejectionReason || null,
      txHash: w.txHash || null,
    }));
    navigator.clipboard.writeText(JSON.stringify(summary, null, 2));
    setCopyFeedback('Copied audit log summary to clipboard');
    setTimeout(() => setCopyFeedback(null), 3000);
  };

  // Metrics
  const totalSettledUsd = withdrawals
    .filter((w) => w.status === 'SETTLED')
    .reduce((sum, w) => sum + w.usdEquivalent, 0);

  const totalPendingUsd = withdrawals
    .filter((w) => w.status === 'PENDING_GUARDIAN' || w.status === 'TIMELOCK_QUEUED' || w.status === 'PROCESSING')
    .reduce((sum, w) => sum + w.usdEquivalent, 0);

  const pendingCount = withdrawals.filter(
    (w) => w.status === 'PENDING_GUARDIAN' || w.status === 'PROCESSING'
  ).length;

  const approvedCount = withdrawals.filter(
    (w) => w.status === 'TIMELOCK_QUEUED' || w.status === 'SETTLED'
  ).length;

  const rejectedCount = withdrawals.filter((w) => w.status === 'REJECTED').length;

  // Filtered withdrawals for status tracking table
  const filteredWithdrawals = withdrawals.filter((w) => {
    // Status filter
    if (statusFilter === 'PENDING' && w.status !== 'PENDING_GUARDIAN' && w.status !== 'PROCESSING') {
      return false;
    }
    if (statusFilter === 'APPROVED' && w.status !== 'TIMELOCK_QUEUED' && w.status !== 'SETTLED') {
      return false;
    }
    if (statusFilter === 'REJECTED' && w.status !== 'REJECTED') {
      return false;
    }

    // Rail filter
    if (railFilter !== 'ALL' && w.rail !== railFilter) {
      return false;
    }

    // Search query
    if (searchQuery.trim()) {
      const q = searchQuery.toLowerCase();
      const matchId = w.id.toLowerCase().includes(q);
      const matchName = w.recipientName.toLowerCase().includes(q);
      const matchAddr = w.recipientAddressOrIban.toLowerCase().includes(q);
      const matchMemo = w.memo.toLowerCase().includes(q);
      const matchAsset = w.asset.toLowerCase().includes(q);
      const matchReason = w.rejectionReason?.toLowerCase().includes(q);
      if (!matchId && !matchName && !matchAddr && !matchMemo && !matchAsset && !matchReason) {
        return false;
      }
    }

    return true;
  });

  return (
    <div className="space-y-6" data-testid="withdrawal-center-view">
      {/* Hero Banner */}
      <div className="rounded-2xl bg-gradient-to-r from-slate-900 via-indigo-950/30 to-slate-900 border border-slate-800 p-6 shadow-xl">
        <div className="flex flex-col lg:flex-row lg:items-center justify-between gap-4">
          <div>
            <div className="flex items-center gap-2">
              <span className="px-2.5 py-0.5 rounded-full text-xs font-semibold bg-indigo-500/20 text-indigo-400 border border-indigo-500/40 flex items-center gap-1.5">
                <ArrowDownToLine className="w-3.5 h-3.5" />
                Multi-Rail Withdrawal Engine
              </span>
              <span className="text-xs text-slate-500 font-mono">dashwall.py • withdraw.js • NexusDAOTreasury</span>
            </div>
            <h2 className="text-xl font-bold text-slate-100 mt-1">
              Multi-Rail Capital Withdrawal & Payout Center
            </h2>
            <p className="text-xs text-slate-400 max-w-2xl mt-1">
              Automated corporate payout infrastructure supporting on-chain crypto, Circle Mint ACH (US), SEPA Instant (EU), and Fedwire/SWIFT with automated AML screening and Timelock safety ceilings.
            </p>
          </div>

          <div className="flex flex-wrap items-center gap-3">
            <div className="px-3.5 py-2 rounded-xl bg-slate-950/80 border border-slate-800 text-left">
              <div className="text-[10px] uppercase font-bold text-slate-500">Total Settled Payouts</div>
              <div className="text-sm font-bold text-emerald-400 font-mono mt-0.5">
                ${totalSettledUsd.toLocaleString()} USD
              </div>
            </div>
            <div className="px-3.5 py-2 rounded-xl bg-slate-950/80 border border-slate-800 text-left">
              <div className="text-[10px] uppercase font-bold text-slate-500">Queued in Timelock</div>
              <div className="text-sm font-bold text-amber-400 font-mono mt-0.5">
                ${totalPendingUsd.toLocaleString()} USD
              </div>
            </div>
          </div>
        </div>

        {/* Withdrawal Rail Selector Cards */}
        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-3 mt-5 pt-4 border-t border-slate-800/80">
          <div
            onClick={() => setSelectedRail('CIRCLE_MINT_ACH')}
            className={`p-3.5 rounded-xl border transition cursor-pointer ${
              selectedRail === 'CIRCLE_MINT_ACH'
                ? 'bg-slate-800/90 border-cyan-400 shadow-md'
                : 'bg-slate-950/60 border-slate-800/80 hover:border-slate-700'
            }`}
          >
            <div className="flex items-center justify-between">
              <span className="text-xs font-bold text-slate-200 flex items-center gap-1.5">
                <Landmark className="w-3.5 h-3.5 text-cyan-400" />
                Circle Mint ACH
              </span>
              <span className="text-[10px] px-2 py-0.5 rounded font-bold bg-emerald-950 text-emerald-400">
                0% Fee
              </span>
            </div>
            <div className="text-xs text-slate-400 mt-1">Direct US Bank Clearing</div>
            <div className="text-[10px] text-slate-500 font-mono mt-1">ETA: 1-2 Hours • Max $500k/day</div>
          </div>

          <div
            onClick={() => setSelectedRail('SEPA_EU')}
            className={`p-3.5 rounded-xl border transition cursor-pointer ${
              selectedRail === 'SEPA_EU'
                ? 'bg-slate-800/90 border-cyan-400 shadow-md'
                : 'bg-slate-950/60 border-slate-800/80 hover:border-slate-700'
            }`}
          >
            <div className="flex items-center justify-between">
              <span className="text-xs font-bold text-slate-200 flex items-center gap-1.5">
                <Building className="w-3.5 h-3.5 text-indigo-400" />
                SEPA Instant (EU)
              </span>
              <span className="text-[10px] px-2 py-0.5 rounded font-bold bg-slate-800 text-slate-300">
                €12 Fee
              </span>
            </div>
            <div className="text-xs text-slate-400 mt-1">European IBAN Bank Payout</div>
            <div className="text-[10px] text-slate-500 font-mono mt-1">ETA: Instant • Euro Clearing</div>
          </div>

          <div
            onClick={() => setSelectedRail('CRYPTO_ONCHAIN')}
            className={`p-3.5 rounded-xl border transition cursor-pointer ${
              selectedRail === 'CRYPTO_ONCHAIN'
                ? 'bg-slate-800/90 border-cyan-400 shadow-md'
                : 'bg-slate-950/60 border-slate-800/80 hover:border-slate-700'
            }`}
          >
            <div className="flex items-center justify-between">
              <span className="text-xs font-bold text-slate-200 flex items-center gap-1.5">
                <Coins className="w-3.5 h-3.5 text-teal-400" />
                Crypto On-Chain
              </span>
              <span className="text-[10px] px-2 py-0.5 rounded font-bold bg-slate-800 text-slate-300">
                Gas Only
              </span>
            </div>
            <div className="text-xs text-slate-400 mt-1">ETH, Base, Arbitrum EVM</div>
            <div className="text-[10px] text-slate-500 font-mono mt-1">ETA: 1 Block (~12s)</div>
          </div>

          <div
            onClick={() => setSelectedRail('FEDWIRE_SWIFT')}
            className={`p-3.5 rounded-xl border transition cursor-pointer ${
              selectedRail === 'FEDWIRE_SWIFT'
                ? 'bg-slate-800/90 border-cyan-400 shadow-md'
                : 'bg-slate-950/60 border-slate-800/80 hover:border-slate-700'
            }`}
          >
            <div className="flex items-center justify-between">
              <span className="text-xs font-bold text-slate-200 flex items-center gap-1.5">
                <CreditCard className="w-3.5 h-3.5 text-amber-400" />
                Fedwire / SWIFT
              </span>
              <span className="text-[10px] px-2 py-0.5 rounded font-bold bg-slate-800 text-slate-300">
                $25 Fee
              </span>
            </div>
            <div className="text-xs text-slate-400 mt-1">International Cross-Border</div>
            <div className="text-[10px] text-slate-500 font-mono mt-1">ETA: Same Day Fedwire</div>
          </div>
        </div>
      </div>

      {/* Main Grid: Request Form & Quick Queue */}
      <div className="grid grid-cols-1 lg:grid-cols-12 gap-6">
        {/* Left: Withdrawal Request Form */}
        <div className="lg:col-span-5 rounded-2xl bg-slate-900/90 border border-slate-800 p-5 space-y-4">
          <div className="flex items-center justify-between border-b border-slate-800 pb-3">
            <div className="flex items-center gap-2">
              <Send className="w-4 h-4 text-cyan-400" />
              <h3 className="text-sm font-bold text-slate-200">Initiate Withdrawal Request</h3>
            </div>
            <span className="text-[10px] font-mono text-slate-400">
              Tier {tierInfo.tier} Policy
            </span>
          </div>

          <form onSubmit={handleWithdrawalSubmit} className="space-y-3.5">
            <div className="grid grid-cols-2 gap-3">
              <div>
                <label className="block text-xs font-semibold text-slate-300 mb-1">Asset</label>
                <select
                  value={selectedAsset}
                  onChange={(e) => setSelectedAsset(e.target.value)}
                  className="w-full px-3 py-2 rounded-xl bg-slate-950 border border-slate-800 text-xs font-mono text-slate-200 focus:border-cyan-500 focus:outline-none"
                >
                  <option value="USDC">USDC (Circle)</option>
                  <option value="ETH">ETH (Ether)</option>
                  <option value="EUR">EUR (Euro SEPA)</option>
                  <option value="USD">USD (Fedwire)</option>
                  <option value="USDT">USDT (Tether)</option>
                  <option value="NGTT">NGTT (Token)</option>
                </select>
              </div>

              <div>
                <label className="block text-xs font-semibold text-slate-300 mb-1">Amount</label>
                <input
                  type="number"
                  step="any"
                  value={amountInput}
                  onChange={(e) => setAmountInput(e.target.value)}
                  placeholder="e.g. 25000"
                  className="w-full px-3 py-2 rounded-xl bg-slate-950 border border-slate-800 text-xs font-mono text-slate-100 focus:border-cyan-500 focus:outline-none"
                  required
                />
              </div>
            </div>

            <div>
              <label className="block text-xs font-semibold text-slate-300 mb-1">
                Recipient Legal Entity / Beneficiary Name
              </label>
              <input
                type="text"
                value={recipientName}
                onChange={(e) => setRecipientName(e.target.value)}
                placeholder="e.g. Nexus European Holdings GmbH"
                className="w-full px-3 py-2 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-200 focus:border-cyan-500 focus:outline-none"
                required
              />
            </div>

            <div>
              <label className="block text-xs font-semibold text-slate-300 mb-1">
                {selectedRail === 'CRYPTO_ONCHAIN'
                  ? 'Recipient Ethereum Address (0x...)'
                  : selectedRail === 'SEPA_EU'
                  ? 'IBAN Number (e.g. DE89...)'
                  : 'Account / IBAN Number'}
              </label>
              <input
                type="text"
                value={recipientAddressOrIban}
                onChange={(e) => setRecipientAddressOrIban(e.target.value)}
                placeholder={selectedRail === 'CRYPTO_ONCHAIN' ? '0x...' : 'US893847291048294'}
                className="w-full px-3 py-2 rounded-xl bg-slate-950 border border-slate-800 text-xs font-mono text-slate-200 focus:border-cyan-500 focus:outline-none"
                required
              />
            </div>

            {selectedRail !== 'CRYPTO_ONCHAIN' && (
              <div>
                <label className="block text-xs font-semibold text-slate-300 mb-1">
                  Routing / SWIFT BIC Code
                </label>
                <input
                  type="text"
                  value={routingOrSwift}
                  onChange={(e) => setRoutingOrSwift(e.target.value)}
                  placeholder="e.g. 121000358 or DBEUSTM1XXX"
                  className="w-full px-3 py-2 rounded-xl bg-slate-950 border border-slate-800 text-xs font-mono text-slate-200 focus:border-cyan-500 focus:outline-none"
                />
              </div>
            )}

            <div>
              <label className="block text-xs font-semibold text-slate-300 mb-1">Payment Memo / Invoice Ref</label>
              <input
                type="text"
                value={memoInput}
                onChange={(e) => setMemoInput(e.target.value)}
                placeholder="e.g. Q4 Infrastructure Retainer"
                className="w-full px-3 py-2 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-200 focus:border-cyan-500 focus:outline-none"
                required
              />
            </div>

            {/* Tier Rules Summary Box */}
            <div className="p-3 rounded-xl bg-slate-950/90 border border-slate-800 text-xs font-mono space-y-1.5">
              <div className="flex items-center justify-between text-slate-300">
                <span>Equivalent USD Value:</span>
                <span className="font-bold text-slate-100">${usdEquivalent.toLocaleString()} USD</span>
              </div>
              <div className="flex items-center justify-between text-slate-400">
                <span>Timelock Delay:</span>
                <span className={tierInfo.requiresTimelock ? 'text-amber-400 font-semibold' : 'text-emerald-400'}>
                  {tierInfo.requiresTimelock ? `${tierInfo.timelockDelaySeconds / 3600} Hours` : 'None (Instant Rail)'}
                </span>
              </div>
              <div className="flex items-center justify-between text-slate-400">
                <span>Dual Guardian Co-Sign:</span>
                <span className={tierInfo.requiresGuardianCosign ? 'text-amber-400 font-semibold' : 'text-slate-400'}>
                  {tierInfo.requiresGuardianCosign ? 'Mandatory (2 Signatures)' : 'Bypassed'}
                </span>
              </div>
              <div className="flex items-center justify-between text-slate-400">
                <span>Est. Processing Fee:</span>
                <span className="text-emerald-400 font-bold">${tierInfo.feeUsd.toFixed(2)} USD</span>
              </div>
              <div className="flex items-center justify-between text-slate-400">
                <span>Est. Settlement Arrival:</span>
                <span className="text-cyan-400">{tierInfo.estimatedSettlement}</span>
              </div>
            </div>

            <button
              type="submit"
              className="w-full py-2.5 rounded-xl bg-gradient-to-r from-indigo-600 to-cyan-600 hover:from-indigo-500 hover:to-cyan-500 text-white font-bold text-xs shadow-lg transition flex items-center justify-center gap-2"
            >
              <Send className="w-3.5 h-3.5" />
              Submit Withdrawal Authorization
            </button>
          </form>

          {showSuccessToast && (
            <div className="p-2.5 rounded-xl bg-emerald-950/60 border border-emerald-800 text-xs text-emerald-300 flex items-center gap-2">
              <CheckCircle className="w-4 h-4 text-emerald-400 shrink-0" />
              <span>Withdrawal request <strong>{showSuccessToast}</strong> created and forwarded to Approvals Queue.</span>
            </div>
          )}
        </div>

        {/* Right: Quick Action Cards for Pending Actionables */}
        <div className="lg:col-span-7 rounded-2xl bg-slate-900/90 border border-slate-800 p-5 space-y-4 flex flex-col justify-between">
          <div>
            <div className="flex flex-wrap items-center justify-between gap-2 border-b border-slate-800 pb-3">
              <div className="flex items-center gap-2">
                <ShieldCheck className="w-4 h-4 text-amber-400" />
                <h3 className="text-sm font-bold text-slate-200">
                  Priority Actionables ({withdrawals.filter((w) => w.status !== 'SETTLED' && w.status !== 'REJECTED').length} Pending Execution)
                </h3>
              </div>
              <span className="text-xs text-slate-400 font-mono">
                Operator Role: <strong className="text-cyan-400">{operatorRole}</strong>
              </span>
            </div>

            <div className="space-y-3 mt-3">
              {withdrawals
                .filter((w) => w.status !== 'SETTLED' && w.status !== 'REJECTED')
                .map((w) => (
                  <div
                    key={w.id}
                    className="p-3.5 rounded-xl bg-slate-950 border border-slate-800 flex flex-col sm:flex-row sm:items-center justify-between gap-3 hover:border-slate-700 transition"
                  >
                    <div className="space-y-1">
                      <div className="flex items-center gap-2 flex-wrap">
                        <span className="text-xs font-bold text-slate-100 font-mono">{w.id}</span>
                        <span className="text-sm font-bold text-emerald-400 font-mono">
                          {w.amount.toLocaleString()} {w.asset}
                        </span>
                        <span className="text-xs text-slate-400 font-mono">
                          (~${w.usdEquivalent.toLocaleString()} USD)
                        </span>
                        <span className="px-2 py-0.5 rounded text-[10px] font-bold font-mono bg-slate-800 text-cyan-400">
                          {w.rail.replace(/_/g, ' ')}
                        </span>
                        <span
                          className={`px-2 py-0.5 rounded text-[10px] font-bold font-mono uppercase ${
                            w.status === 'TIMELOCK_QUEUED'
                              ? 'bg-amber-950 text-amber-400 border border-amber-800'
                              : 'bg-indigo-950 text-indigo-400 border border-indigo-800'
                          }`}
                        >
                          {w.status.replace(/_/g, ' ')}
                        </span>
                      </div>
                      <div className="text-xs text-slate-300">
                        Beneficiary: <strong>{w.recipientName}</strong>
                      </div>
                      <div className="text-[11px] text-slate-500 font-mono">
                        {w.memo} • Requested by {w.requestedBy.slice(0, 8)}...
                      </div>
                    </div>

                    <div className="flex items-center gap-2 shrink-0">
                      {w.status === 'PENDING_GUARDIAN' && (
                        <button
                          onClick={() => approveWithdrawalRequest(w.id)}
                          disabled={!isGuardianOrOwner}
                          className="px-3 py-1.5 rounded-lg bg-amber-600 hover:bg-amber-500 text-white font-bold text-xs transition disabled:opacity-40"
                        >
                          Co-Sign
                        </button>
                      )}

                      {w.status === 'TIMELOCK_QUEUED' && (
                        <button
                          onClick={() => executeWithdrawalRequest(w.id)}
                          className="px-3 py-1.5 rounded-lg bg-emerald-600 hover:bg-emerald-500 text-white font-bold text-xs transition"
                        >
                          Execute Payout
                        </button>
                      )}

                      <button
                        onClick={() => setRejectingRequestId(w.id)}
                        className="px-2.5 py-1.5 rounded-lg bg-slate-800 hover:bg-red-950 hover:text-red-300 text-slate-400 text-xs transition"
                      >
                        Reject
                      </button>

                      <button
                        onClick={() => setActiveAuditRequest(w)}
                        className="px-2.5 py-1.5 rounded-lg bg-slate-900 border border-slate-700 hover:border-cyan-400 text-cyan-400 text-xs font-mono transition flex items-center gap-1"
                        title="View audit logs"
                      >
                        <History className="w-3.5 h-3.5" />
                        Audit
                      </button>
                    </div>
                  </div>
                ))}

              {withdrawals.filter((w) => w.status !== 'SETTLED' && w.status !== 'REJECTED').length === 0 && (
                <div className="p-6 text-center text-slate-500 text-xs font-mono bg-slate-950 rounded-xl border border-slate-800">
                  No pending withdrawals currently awaiting guardian co-signing or timelock release. All actions logged in status table below.
                </div>
              )}
            </div>
          </div>

          <div className="pt-2 text-[11px] text-slate-500 flex items-center justify-between border-t border-slate-800/80">
            <span>Corporate multi-rail policy enforced: Tier 1 Instant / Tier 2 24h Timelock / Tier 3 Dual Guardian</span>
            <span className="text-emerald-400 font-mono">TRM Labs AML Guard Active</span>
          </div>
        </div>
      </div>

      {/* FULL STATUS TRACKING & AUDIT LOGS TABLE */}
      <div className="rounded-2xl bg-slate-900/90 border border-slate-800 p-5 space-y-4 shadow-xl">
        {/* Table Title and Filter Tabs */}
        <div className="flex flex-col md:flex-row md:items-center justify-between gap-4 border-b border-slate-800 pb-4">
          <div className="flex items-center gap-2.5">
            <div className="p-2 rounded-xl bg-cyan-950/80 text-cyan-400 border border-cyan-800/50">
              <FileSpreadsheet className="w-5 h-5" />
            </div>
            <div>
              <h3 className="text-base font-bold text-slate-100 flex items-center gap-2">
                Withdrawal Status Tracking & Audit Logs
                <span className="text-xs px-2 py-0.5 rounded-full font-mono font-semibold bg-slate-800 text-cyan-400">
                  {filteredWithdrawals.length} Records
                </span>
              </h3>
              <p className="text-xs text-slate-400">
                End-to-end multi-rail withdrawal status auditing across pending, approved, and rejected payouts with immutable event logs.
              </p>
            </div>
          </div>

          {/* Export / Quick Copy Buttons */}
          <div className="flex items-center gap-2">
            {copyFeedback && (
              <span className="text-[11px] text-emerald-400 font-mono animate-pulse">
                {copyFeedback}
              </span>
            )}
            <button
              onClick={handleCopyAuditSummary}
              className="px-3 py-1.5 rounded-xl bg-slate-950 border border-slate-800 hover:border-slate-700 text-slate-300 text-xs font-medium transition flex items-center gap-1.5"
              title="Copy audit log summary JSON"
            >
              <Copy className="w-3.5 h-3.5 text-cyan-400" />
              Copy Summary
            </button>
            <button
              onClick={handleExportAuditLogs}
              className="px-3 py-1.5 rounded-xl bg-slate-950 border border-slate-800 hover:border-slate-700 text-slate-300 text-xs font-medium transition flex items-center gap-1.5"
              title="Download complete withdrawal audit JSON"
            >
              <Download className="w-3.5 h-3.5 text-indigo-400" />
              Export Audit JSON
            </button>
          </div>
        </div>

        {/* Filter Controls Bar */}
        <div className="flex flex-col lg:flex-row lg:items-center justify-between gap-3 pt-1">
          {/* Status Tabs: ALL, PENDING, APPROVED, REJECTED */}
          <div className="flex items-center gap-1 bg-slate-950 p-1 rounded-xl border border-slate-800">
            <button
              onClick={() => setStatusFilter('ALL')}
              className={`px-3 py-1.5 rounded-lg text-xs font-semibold transition flex items-center gap-1.5 ${
                statusFilter === 'ALL'
                  ? 'bg-slate-800 text-cyan-400 shadow-sm'
                  : 'text-slate-400 hover:text-slate-200'
              }`}
            >
              <span>All Logs</span>
              <span className="text-[10px] px-1.5 py-0.2 rounded-full bg-slate-900 font-mono">
                {withdrawals.length}
              </span>
            </button>

            <button
              onClick={() => setStatusFilter('PENDING')}
              className={`px-3 py-1.5 rounded-lg text-xs font-semibold transition flex items-center gap-1.5 ${
                statusFilter === 'PENDING'
                  ? 'bg-amber-950 text-amber-300 border border-amber-800/60 shadow-sm'
                  : 'text-slate-400 hover:text-slate-200'
              }`}
            >
              <Clock className="w-3.5 h-3.5 text-amber-400" />
              <span>Pending</span>
              <span className="text-[10px] px-1.5 py-0.2 rounded-full bg-slate-900 font-mono text-amber-400">
                {pendingCount}
              </span>
            </button>

            <button
              onClick={() => setStatusFilter('APPROVED')}
              className={`px-3 py-1.5 rounded-lg text-xs font-semibold transition flex items-center gap-1.5 ${
                statusFilter === 'APPROVED'
                  ? 'bg-emerald-950 text-emerald-300 border border-emerald-800/60 shadow-sm'
                  : 'text-slate-400 hover:text-slate-200'
              }`}
            >
              <CheckCircle2 className="w-3.5 h-3.5 text-emerald-400" />
              <span>Approved</span>
              <span className="text-[10px] px-1.5 py-0.2 rounded-full bg-slate-900 font-mono text-emerald-400">
                {approvedCount}
              </span>
            </button>

            <button
              onClick={() => setStatusFilter('REJECTED')}
              className={`px-3 py-1.5 rounded-lg text-xs font-semibold transition flex items-center gap-1.5 ${
                statusFilter === 'REJECTED'
                  ? 'bg-rose-950 text-rose-300 border border-rose-800/60 shadow-sm'
                  : 'text-slate-400 hover:text-slate-200'
              }`}
            >
              <XCircle className="w-3.5 h-3.5 text-rose-400" />
              <span>Rejected</span>
              <span className="text-[10px] px-1.5 py-0.2 rounded-full bg-slate-900 font-mono text-rose-400">
                {rejectedCount}
              </span>
            </button>
          </div>

          {/* Search & Rail Selectors */}
          <div className="flex flex-wrap items-center gap-2">
            <div className="relative min-w-[220px]">
              <Search className="w-3.5 h-3.5 text-slate-500 absolute left-3 top-1/2 -translate-y-1/2" />
              <input
                type="text"
                value={searchQuery}
                onChange={(e) => setSearchQuery(e.target.value)}
                placeholder="Search ID, entity, IBAN, memo..."
                className="w-full pl-8 pr-3 py-1.5 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-200 placeholder-slate-500 focus:outline-none focus:border-cyan-500"
              />
              {searchQuery && (
                <button
                  onClick={() => setSearchQuery('')}
                  className="absolute right-2.5 top-1/2 -translate-y-1/2 text-slate-500 hover:text-slate-300 text-xs"
                >
                  ×
                </button>
              )}
            </div>

            <select
              value={railFilter}
              onChange={(e) => setRailFilter(e.target.value)}
              className="px-3 py-1.5 rounded-xl bg-slate-950 border border-slate-800 text-xs font-mono text-slate-300 focus:outline-none focus:border-cyan-500"
            >
              <option value="ALL">All Rails</option>
              <option value="CIRCLE_MINT_ACH">Circle Mint ACH</option>
              <option value="SEPA_EU">SEPA Instant EU</option>
              <option value="CRYPTO_ONCHAIN">Crypto On-Chain</option>
              <option value="FEDWIRE_SWIFT">Fedwire / SWIFT</option>
            </select>
          </div>
        </div>

        {/* The Tracking Table */}
        <div className="overflow-x-auto rounded-xl border border-slate-800 bg-slate-950/70">
          <table className="w-full text-left text-xs">
            <thead>
              <tr className="border-b border-slate-800 bg-slate-900/80 text-[11px] uppercase tracking-wider text-slate-400 font-semibold">
                <th className="px-4 py-3">Request ID & Time</th>
                <th className="px-4 py-3">Rail & Beneficiary</th>
                <th className="px-4 py-3">Amount & USD Value</th>
                <th className="px-4 py-3">Status & AML Screening</th>
                <th className="px-4 py-3">Dual Signatures</th>
                <th className="px-4 py-3">Latest Audit Event</th>
                <th className="px-4 py-3 text-right">Actions</th>
              </tr>
            </thead>
            <tbody className="divide-y divide-slate-800/80">
              {filteredWithdrawals.map((w) => {
                const latestAudit = w.auditTrail && w.auditTrail.length > 0
                  ? w.auditTrail[w.auditTrail.length - 1]
                  : null;

                const isPending = w.status === 'PENDING_GUARDIAN' || w.status === 'PROCESSING';
                const isApproved = w.status === 'TIMELOCK_QUEUED' || w.status === 'SETTLED';
                const isRejected = w.status === 'REJECTED';

                return (
                  <tr
                    key={w.id}
                    className="hover:bg-slate-900/60 transition group"
                  >
                    {/* ID & Time */}
                    <td className="px-4 py-3.5 whitespace-nowrap">
                      <div className="font-mono font-bold text-slate-100 flex items-center gap-1.5">
                        <span>{w.id}</span>
                        {isRejected && <XCircle className="w-3.5 h-3.5 text-rose-400 shrink-0" />}
                        {w.status === 'SETTLED' && <CheckCircle className="w-3.5 h-3.5 text-emerald-400 shrink-0" />}
                        {w.status === 'TIMELOCK_QUEUED' && <Clock className="w-3.5 h-3.5 text-amber-400 shrink-0" />}
                      </div>
                      <div className="text-[11px] text-slate-500 font-mono mt-0.5">{w.requestedAt}</div>
                      <div className="text-[10px] text-slate-600 font-mono">By: {w.requestedBy.slice(0, 8)}...</div>
                    </td>

                    {/* Rail & Beneficiary */}
                    <td className="px-4 py-3.5">
                      <div className="font-semibold text-slate-200">{w.recipientName}</div>
                      <div className="text-[11px] text-slate-400 font-mono break-all mt-0.5">
                        {w.recipientAddressOrIban}
                      </div>
                      <div className="flex items-center gap-2 mt-1">
                        <span className="px-1.5 py-0.2 rounded text-[10px] font-mono font-semibold bg-slate-900 text-cyan-400 border border-slate-800">
                          {w.rail.replace(/_/g, ' ')}
                        </span>
                        {w.bankRoutingOrSwift && (
                          <span className="text-[10px] text-slate-500 font-mono">
                            BIC/Routing: {w.bankRoutingOrSwift}
                          </span>
                        )}
                      </div>
                      <div className="text-[11px] text-slate-500 italic mt-0.5">Memo: {w.memo}</div>
                    </td>

                    {/* Amount & USD Value */}
                    <td className="px-4 py-3.5 whitespace-nowrap font-mono">
                      <div className="font-bold text-emerald-400 text-sm">
                        {w.amount.toLocaleString()} {w.asset}
                      </div>
                      <div className="text-[11px] text-slate-400">
                        ${w.usdEquivalent.toLocaleString()} USD
                      </div>
                      <div className="text-[10px] text-slate-500">
                        Fee: ${w.feeUsd.toFixed(2)} USD
                      </div>
                    </td>

                    {/* Status & Compliance */}
                    <td className="px-4 py-3.5 whitespace-nowrap">
                      <div>
                        {w.status === 'PENDING_GUARDIAN' && (
                          <span className="inline-flex items-center gap-1.5 px-2.5 py-1 rounded-full text-xs font-bold font-mono bg-amber-950/80 text-amber-300 border border-amber-800">
                            <span className="w-1.5 h-1.5 rounded-full bg-amber-400 animate-pulse" />
                            PENDING GUARDIAN
                          </span>
                        )}
                        {w.status === 'PROCESSING' && (
                          <span className="inline-flex items-center gap-1.5 px-2.5 py-1 rounded-full text-xs font-bold font-mono bg-cyan-950/80 text-cyan-300 border border-cyan-800">
                            <span className="w-1.5 h-1.5 rounded-full bg-cyan-400 animate-pulse" />
                            PROCESSING RAIL
                          </span>
                        )}
                        {w.status === 'TIMELOCK_QUEUED' && (
                          <span className="inline-flex items-center gap-1.5 px-2.5 py-1 rounded-full text-xs font-bold font-mono bg-indigo-950/80 text-indigo-300 border border-indigo-800">
                            <Clock className="w-3 h-3 text-indigo-400" />
                            TIMELOCK QUEUED
                          </span>
                        )}
                        {w.status === 'SETTLED' && (
                          <span className="inline-flex items-center gap-1.5 px-2.5 py-1 rounded-full text-xs font-bold font-mono bg-emerald-950/80 text-emerald-300 border border-emerald-800">
                            <CheckCircle2 className="w-3 h-3 text-emerald-400" />
                            SETTLED ON-CHAIN
                          </span>
                        )}
                        {w.status === 'REJECTED' && (
                          <span className="inline-flex items-center gap-1.5 px-2.5 py-1 rounded-full text-xs font-bold font-mono bg-rose-950/80 text-rose-300 border border-rose-800">
                            <XCircle className="w-3 h-3 text-rose-400" />
                            REJECTED / VOID
                          </span>
                        )}
                      </div>

                      {/* AML Screening Tag */}
                      <div className="flex items-center gap-1.5 mt-1 text-[11px] font-mono">
                        {w.amlCheckPassed ? (
                          <span className="text-emerald-400 flex items-center gap-1">
                            <CheckCircle2 className="w-3 h-3" />
                            TRM Labs: Clean (Risk {w.riskScore}/100)
                          </span>
                        ) : (
                          <span className="text-rose-400 font-bold flex items-center gap-1">
                            <AlertTriangle className="w-3 h-3" />
                            AML Flagged (Risk {w.riskScore}/100)
                          </span>
                        )}
                      </div>

                      {w.rejectionReason && (
                        <div className="text-[10px] text-rose-400/90 font-mono max-w-xs truncate mt-0.5" title={w.rejectionReason}>
                          Reason: {w.rejectionReason}
                        </div>
                      )}
                    </td>

                    {/* Dual Signatures & Timelock */}
                    <td className="px-4 py-3.5 whitespace-nowrap text-xs font-mono">
                      <div className="flex items-center gap-1.5">
                        <span className="text-slate-400 text-[11px]">Signatures:</span>
                        <span
                          className={`font-bold px-1.5 py-0.2 rounded text-[11px] ${
                            w.guardianApproval2
                              ? 'bg-emerald-950 text-emerald-300 border border-emerald-800'
                              : w.guardianApproval1
                              ? 'bg-amber-950 text-amber-300 border border-amber-800'
                              : 'bg-slate-800 text-slate-400'
                          }`}
                        >
                          {w.guardianApproval2 ? '2 / 2' : w.guardianApproval1 ? '1 / 2' : '0 / 2'}
                        </span>
                      </div>
                      <div className="text-[10px] text-slate-500 mt-1">
                        {w.timelockEtaTimestamp
                          ? 'Timelock Active (24h Delay)'
                          : isRejected
                          ? 'Cancelled before Timelock'
                          : 'Instant Fast Rail'}
                      </div>
                    </td>

                    {/* Latest Audit Event */}
                    <td className="px-4 py-3.5 max-w-[240px]">
                      {latestAudit ? (
                        <div className="space-y-0.5">
                          <div className="flex items-center gap-1 text-[10px] font-bold font-mono text-cyan-400 uppercase">
                            <span className="w-1.5 h-1.5 rounded-full bg-cyan-400" />
                            {latestAudit.action.replace(/_/g, ' ')}
                          </div>
                          <div className="text-[11px] text-slate-300 line-clamp-2" title={latestAudit.note}>
                            {latestAudit.note}
                          </div>
                          <div className="text-[10px] text-slate-500 font-mono">
                            {latestAudit.timestamp}
                          </div>
                        </div>
                      ) : (
                        <span className="text-slate-500 text-[11px] font-mono">No audit trail yet</span>
                      )}
                    </td>

                    {/* Actions */}
                    <td className="px-4 py-3.5 whitespace-nowrap text-right">
                      <div className="flex items-center justify-end gap-1.5">
                        <button
                          onClick={() => setActiveAuditRequest(w)}
                          className="px-2.5 py-1.5 rounded-lg bg-slate-900 border border-slate-700 hover:border-cyan-400 text-cyan-300 text-xs font-mono transition flex items-center gap-1 shadow-sm"
                          title="Inspect detailed event audit logs"
                        >
                          <History className="w-3.5 h-3.5" />
                          <span>Audit ({w.auditTrail?.length || 0})</span>
                        </button>

                        {w.status === 'PENDING_GUARDIAN' && (
                          <button
                            onClick={() => approveWithdrawalRequest(w.id)}
                            disabled={!isGuardianOrOwner}
                            className="px-2.5 py-1.5 rounded-lg bg-amber-600 hover:bg-amber-500 text-white font-bold text-xs transition disabled:opacity-40"
                          >
                            Co-Sign
                          </button>
                        )}

                        {w.status === 'TIMELOCK_QUEUED' && (
                          <button
                            onClick={() => executeWithdrawalRequest(w.id)}
                            className="px-2.5 py-1.5 rounded-lg bg-emerald-600 hover:bg-emerald-500 text-white font-bold text-xs transition"
                          >
                            Execute
                          </button>
                        )}

                        {w.status !== 'SETTLED' && w.status !== 'REJECTED' && (
                          <button
                            onClick={() => setRejectingRequestId(w.id)}
                            className="px-2 py-1.5 rounded-lg bg-slate-900 border border-slate-800 hover:bg-rose-950 hover:border-rose-700 text-slate-400 hover:text-rose-300 text-xs transition"
                            title="Reject request with audit reason"
                          >
                            Reject
                          </button>
                        )}
                      </div>
                    </td>
                  </tr>
                );
              })}

              {filteredWithdrawals.length === 0 && (
                <tr>
                  <td colSpan={7} className="px-4 py-8 text-center text-slate-500 text-xs font-mono">
                    No withdrawals found matching the selected filter criteria.
                  </td>
                </tr>
              )}
            </tbody>
          </table>
        </div>
      </div>

      {/* DETAILED AUDIT TRAIL MODAL */}
      {activeAuditRequest && (
        <div className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-slate-950/80 backdrop-blur-sm animate-in fade-in duration-150">
          <div className="w-full max-w-2xl rounded-2xl bg-slate-900 border border-slate-700 shadow-2xl p-6 space-y-4 max-h-[90vh] overflow-y-auto">
            <div className="flex items-center justify-between border-b border-slate-800 pb-3">
              <div className="flex items-center gap-2">
                <History className="w-5 h-5 text-cyan-400" />
                <div>
                  <h3 className="text-base font-bold text-slate-100 flex items-center gap-2">
                    Audit Trail: {activeAuditRequest.id}
                    <span
                      className={`px-2 py-0.5 rounded text-[10px] font-mono font-bold uppercase ${
                        activeAuditRequest.status === 'SETTLED'
                          ? 'bg-emerald-950 text-emerald-400 border border-emerald-800'
                          : activeAuditRequest.status === 'REJECTED'
                          ? 'bg-rose-950 text-rose-400 border border-rose-800'
                          : 'bg-amber-950 text-amber-400 border border-amber-800'
                      }`}
                    >
                      {activeAuditRequest.status.replace(/_/g, ' ')}
                    </span>
                  </h3>
                  <div className="text-xs text-slate-400 font-mono">
                    {activeAuditRequest.amount.toLocaleString()} {activeAuditRequest.asset} (${activeAuditRequest.usdEquivalent.toLocaleString()} USD) • {activeAuditRequest.rail}
                  </div>
                </div>
              </div>
              <button
                onClick={() => setActiveAuditRequest(null)}
                className="p-1 rounded-lg text-slate-400 hover:text-slate-100 hover:bg-slate-800 transition"
              >
                <X className="w-5 h-5" />
              </button>
            </div>

            {/* Beneficiary & Compliance Brief */}
            <div className="p-3.5 rounded-xl bg-slate-950 border border-slate-800 text-xs font-mono space-y-1.5">
              <div className="flex justify-between text-slate-300">
                <span>Beneficiary:</span>
                <span className="font-bold text-slate-100">{activeAuditRequest.recipientName}</span>
              </div>
              <div className="flex justify-between text-slate-400">
                <span>Destination:</span>
                <span className="break-all">{activeAuditRequest.recipientAddressOrIban}</span>
              </div>
              <div className="flex justify-between text-slate-400">
                <span>Payment Memo:</span>
                <span className="italic">{activeAuditRequest.memo}</span>
              </div>
              <div className="flex justify-between text-slate-400">
                <span>AML Risk Assessment:</span>
                <span className={activeAuditRequest.amlCheckPassed ? 'text-emerald-400' : 'text-rose-400 font-bold'}>
                  {activeAuditRequest.amlCheckPassed ? 'TRM Labs Sanction Check: Clean (Score ' + activeAuditRequest.riskScore + '/100)' : 'AML Sanctions Warning (Score ' + activeAuditRequest.riskScore + '/100)'}
                </span>
              </div>
              {activeAuditRequest.txHash && (
                <div className="flex justify-between text-cyan-400">
                  <span>Settlement Tx Hash:</span>
                  <span>{activeAuditRequest.txHash}</span>
                </div>
              )}
              {activeAuditRequest.rejectionReason && (
                <div className="flex justify-between text-rose-400">
                  <span>Rejection Reason:</span>
                  <span>{activeAuditRequest.rejectionReason}</span>
                </div>
              )}
            </div>

            {/* Audit Event Timeline */}
            <div>
              <h4 className="text-xs uppercase font-bold text-slate-400 tracking-wider mb-2 flex items-center gap-1.5">
                <Clock className="w-3.5 h-3.5 text-cyan-400" />
                Immutable Event Timeline ({activeAuditRequest.auditTrail?.length || 0} events)
              </h4>

              <div className="relative pl-6 space-y-4 border-l border-slate-800 ml-3">
                {activeAuditRequest.auditTrail?.map((evt, idx) => (
                  <div key={evt.id || idx} className="relative group">
                    <span
                      className={`absolute -left-[31px] top-1 w-3 h-3 rounded-full border-2 border-slate-900 ${
                        evt.action === 'REJECTED_CANCELLED'
                          ? 'bg-rose-500 ring-2 ring-rose-500/20'
                          : evt.action === 'EXECUTED_SETTLED'
                          ? 'bg-emerald-500 ring-2 ring-emerald-500/20'
                          : evt.action === 'TIMELOCK_ENQUEUED'
                          ? 'bg-indigo-500 ring-2 ring-indigo-500/20'
                          : evt.action === 'GUARDIAN_APPROVED'
                          ? 'bg-amber-500 ring-2 ring-amber-500/20'
                          : 'bg-cyan-500 ring-2 ring-cyan-500/20'
                      }`}
                    />
                    <div className="p-3 rounded-xl bg-slate-950/80 border border-slate-800 text-xs space-y-1">
                      <div className="flex items-center justify-between flex-wrap gap-1">
                        <span className="font-mono font-bold text-xs uppercase text-slate-200">
                          {evt.action.replace(/_/g, ' ')}
                        </span>
                        <span className="text-[10px] text-slate-500 font-mono">{evt.timestamp}</span>
                      </div>
                      <p className="text-slate-300 text-xs">{evt.note}</p>
                      <div className="text-[10px] text-slate-500 font-mono">
                        Operator: <span className="text-cyan-400">{evt.operator}</span>
                        {evt.txHash && <span className="ml-2 text-emerald-400">• Tx: {evt.txHash}</span>}
                      </div>
                    </div>
                  </div>
                ))}
              </div>
            </div>

            <div className="pt-2 border-t border-slate-800 flex justify-end">
              <button
                onClick={() => setActiveAuditRequest(null)}
                className="px-4 py-2 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-200 text-xs font-semibold transition"
              >
                Close Audit Viewer
              </button>
            </div>
          </div>
        </div>
      )}

      {/* REJECTION REASON MODAL */}
      {rejectingRequestId && (
        <div className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-slate-950/80 backdrop-blur-sm animate-in fade-in duration-150">
          <div className="w-full max-w-lg rounded-2xl bg-slate-900 border border-rose-900/60 shadow-2xl p-6 space-y-4">
            <div className="flex items-center justify-between border-b border-slate-800 pb-3">
              <div className="flex items-center gap-2 text-rose-400 font-bold text-sm">
                <AlertCircle className="w-4 h-4 text-rose-500" />
                <span>Reject & Void Withdrawal Authorization</span>
              </div>
              <button
                onClick={() => setRejectingRequestId(null)}
                className="text-slate-400 hover:text-slate-100"
              >
                <X className="w-4 h-4" />
              </button>
            </div>

            <p className="text-xs text-slate-300">
              Rejecting withdrawal <strong>{rejectingRequestId}</strong> will cancel processing, record an immutable audit entry with your operator identity, and notify compliance officers.
            </p>

            <div>
              <label className="block text-xs font-semibold text-slate-300 mb-1">
                Select or Customize Audit Rejection Reason:
              </label>
              <select
                onChange={(e) => setRejectReasonInput(e.target.value)}
                className="w-full px-3 py-2 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-200 mb-2 focus:outline-none focus:border-rose-500"
              >
                <option value="Sanctions / AML KYC pre-flight screening unverified on beneficiary registry.">
                  Sanctions / AML KYC unverified
                </option>
                <option value="SWIFT routing BIC / IBAN failed checksum validation on clearing house.">
                  SWIFT BIC / IBAN checksum validation failed
                </option>
                <option value="Requested payout amount exceeds quarterly operational allowance.">
                  Exceeds quarterly operational allowance
                </option>
                <option value="Beneficiary entity corporate certificate mismatch with state registry.">
                  Beneficiary legal entity mismatch
                </option>
                <option value="Administrative cancellation requested by initiating signer.">
                  Administrative cancellation by initiating signer
                </option>
              </select>

              <textarea
                rows={3}
                value={rejectReasonInput}
                onChange={(e) => setRejectReasonInput(e.target.value)}
                placeholder="Specify precise compliance or governance rejection rationale..."
                className="w-full px-3 py-2 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-200 focus:outline-none focus:border-rose-500"
              />
            </div>

            <div className="flex items-center justify-end gap-2 pt-2 border-t border-slate-800">
              <button
                onClick={() => setRejectingRequestId(null)}
                className="px-3 py-2 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-300 text-xs font-medium transition"
              >
                Cancel
              </button>
              <button
                onClick={handleConfirmRejection}
                className="px-4 py-2 rounded-xl bg-rose-600 hover:bg-rose-500 text-white text-xs font-bold transition shadow-lg flex items-center gap-1.5"
              >
                <XCircle className="w-4 h-4" />
                Confirm Rejection & Record Audit
              </button>
            </div>
          </div>
        </div>
      )}
    </div>
  );
};
