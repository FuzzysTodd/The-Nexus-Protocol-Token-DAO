/**
 * @license
 * SPDX-License-Identifier: Apache-2.0
 * The Nexus Protocol DAO - Multi-Asset Treasury, Outflow vs. Subscriptions Analytics & Wyoming DAO LLC Bill Desk
 */

import React, { useState, useMemo } from 'react';
import {
  ResponsiveContainer,
  ComposedChart,
  Bar,
  Line,
  Area,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip as RechartsTooltip,
  Legend,
} from 'recharts';
import { useNexusDao } from '../context/NexusDaoContext';
import { TreasuryCharts } from './TreasuryCharts';
import {
  calculateMonthlyBillsVsOutflowAnalytics,
  WyomingLlcDigitalBill,
  WyomingLlcPaymentRail,
  WyomingSubscriptionCategory,
} from '../dao/logic';
import {
  Wallet,
  ShieldCheck,
  AlertTriangle,
  PauseCircle,
  PlayCircle,
  CheckCircle,
  Send,
  BarChart3,
  Building2,
  CreditCard,
  Receipt,
  Plus,
  Sparkles,
  FileText,
  CheckCircle2,
  ArrowUpRight,
  Layers,
  Globe,
} from 'lucide-react';

type OutflowChartMode = 'composed' | 'stacked' | 'google_focus';

export const TreasuryManager: React.FC = () => {
  const {
    treasuryAssets,
    isTreasuryPaused,
    toggleTreasuryPause,
    largeTransfers,
    requestTransfer,
    confirmLargeTransfer,
    executeLargeTransfer,
    operatorRole,
    daoBills,
    withdrawals,
    wyomingLlcProfile,
    wyomingLlcBills,
    payWyomingLlcBill,
    payAllPendingWyomingLlcBills,
    createWyomingLlcBill,
  } = useNexusDao();

  const [selectedAsset, setSelectedAsset] = useState('ETH');
  const [transferAmount, setTransferAmount] = useState('');
  const [transferRecipient, setTransferRecipient] = useState('');
  const [showTransferModal, setShowTransferModal] = useState(false);

  // Outflow vs Bills & Subscriptions Chart State
  const [outflowTimeframe, setOutflowTimeframe] = useState<6 | 12>(6);
  const [outflowChartMode, setOutflowChartMode] = useState<OutflowChartMode>('composed');

  // Wyoming DAO LLC Digital Bill Desk State
  const [selectedBillCategory, setSelectedBillCategory] = useState<string>('ALL');
  const [showCreateBillModal, setShowCreateBillModal] = useState(false);
  const [inspectedBill, setInspectedBill] = useState<WyomingLlcDigitalBill | null>(null);
  const [billToast, setBillToast] = useState<string | null>(null);

  // New Wyoming LLC Digital Bill Form State
  const [newBillVendor, setNewBillVendor] = useState('Google Cloud Platform & Gemini Ultra API');
  const [newBillCategory, setNewBillCategory] = useState<WyomingSubscriptionCategory>('GOOGLE_CLOUD_WORKSPACE');
  const [newBillDescription, setNewBillDescription] = useState(
    'Google Cloud compute, Vertex AI endpoints & corporate workspace subscription billed to Wyoming DAO LLC'
  );
  const [newBillCost, setNewBillCost] = useState('490.00');
  const [newBillCycle, setNewBillCycle] = useState<'MONTHLY' | 'ANNUAL_PRORATED' | 'USAGE_METERED'>('MONTHLY');
  const [newBillRail, setNewBillRail] = useState<WyomingLlcPaymentRail>('WYOMING_LLC_VIRTUAL_CARD');
  const [newBillMerchantId, setNewBillMerchantId] = useState('GOOGLE-CLOUD-WY-99401');
  const [newBillTaxClass, setNewBillTaxClass] = useState('IRC § 162 Cloud & SaaS Subscription Expense');

  const triggerBillToast = (msg: string) => {
    setBillToast(msg);
    setTimeout(() => setBillToast(null), 4000);
  };

  const totalTreasuryUsd = treasuryAssets.reduce((sum, a) => {
    const num = parseFloat(a.usdValue.replace(/[^0-9.-]+/g, '')) || 0;
    return sum + num;
  }, 0);

  const isGuardianOrOwner =
    operatorRole === 'Owner (FuzzysTodd)' || operatorRole === 'Super Delegate';

  // Compute Monthly Bill Payments & Subscription Costs vs. DAO Treasury Outflow
  const outflowAnalytics = useMemo(() => {
    return calculateMonthlyBillsVsOutflowAnalytics(
      daoBills,
      wyomingLlcBills,
      withdrawals,
      outflowTimeframe
    );
  }, [daoBills, wyomingLlcBills, withdrawals, outflowTimeframe]);

  const filteredWyomingBills = useMemo(() => {
    if (selectedBillCategory === 'ALL') return wyomingLlcBills;
    return wyomingLlcBills.filter((b) => b.category === selectedBillCategory);
  }, [wyomingLlcBills, selectedBillCategory]);

  const pendingWyomingBillsCount = wyomingLlcBills.filter(
    (b) => b.status === 'PENDING_DISBURSEMENT'
  ).length;

  const formatUsdCompact = (val: number) => {
    if (val >= 1_000_000) return `$${(val / 1_000_000).toFixed(2)}M`;
    if (val >= 1_000) return `$${(val / 1_000).toFixed(1)}k`;
    return `$${val.toLocaleString()}`;
  };

  const handleTransferSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    if (!transferAmount || !transferRecipient.trim()) return;
    requestTransfer(selectedAsset, transferAmount, transferRecipient.trim());
    setTransferAmount('');
    setTransferRecipient('');
    setShowTransferModal(false);
  };

  const handlePaySingleWyomingBill = (billId: string) => {
    const res = payWyomingLlcBill(billId);
    if (res && res.success) {
      triggerBillToast(
        `Paid ${res.updatedBill.vendor} ($${res.updatedBill.monthlyCostUsd.toFixed(2)}) via ${res.updatedBill.wyomingEntityName}!`
      );
    } else if (res && res.error) {
      triggerBillToast(res.error);
    }
  };

  const handlePayAllWyomingBills = () => {
    const count = payAllPendingWyomingLlcBills();
    if (count > 0) {
      triggerBillToast(
        `Batch settled ${count} digital subscriptions via ${wyomingLlcProfile.legalName}!`
      );
    } else {
      triggerBillToast('All eligible Wyoming DAO LLC subscriptions are already settled for this cycle.');
    }
  };

  const handleCreateWyomingBillSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    if (!newBillVendor.trim() || !newBillCost) return;

    const created = createWyomingLlcBill({
      vendor: newBillVendor.trim(),
      category: newBillCategory,
      description: newBillDescription.trim() || 'Commercial SaaS subscription billed through Wyoming DAO LLC',
      monthlyCostUsd: parseFloat(newBillCost) || 100.0,
      billingCycle: newBillCycle,
      paymentRail: newBillRail,
      accountOrMerchantId: newBillMerchantId.trim() || 'WY-MERCH-001',
      nextBillingDate: '2026-12-01',
      taxDeductibleClass: newBillTaxClass.trim() || 'IRC § 162 Ordinary & Necessary Business Expense',
      autoRenew: true,
    });

    setShowCreateBillModal(false);
    triggerBillToast(
      `Digital Bill ${created.invoiceNumber} (${created.vendor}) created under ${wyomingLlcProfile.legalName}!`
    );
  };

  const applySubscriptionPreset = (preset: 'google_cloud' | 'google_workspace' | 'openai_anthropic' | 'aws_infra') => {
    if (preset === 'google_cloud') {
      setNewBillVendor('Google Cloud Platform (GCP) & Gemini API');
      setNewBillCategory('GOOGLE_CLOUD_WORKSPACE');
      setNewBillDescription('Google Cloud Kubernetes, BigQuery indexing & Gemini 2.5 Pro API subscription');
      setNewBillCost('1250.00');
      setNewBillRail('WYOMING_LLC_VIRTUAL_CARD');
      setNewBillMerchantId('GCP-WY-LLC-882190');
      setNewBillTaxClass('IRC § 162 Cloud Infrastructure & AI API Expense');
    } else if (preset === 'google_workspace') {
      setNewBillVendor('Google Workspace Enterprise & Google Domains');
      setNewBillCategory('GOOGLE_CLOUD_WORKSPACE');
      setNewBillDescription('Corporate DAO email seats, Google Drive Vault & DNS domain registration');
      setNewBillCost('480.00');
      setNewBillRail('WYOMING_LLC_VIRTUAL_CARD');
      setNewBillMerchantId('GWS-WY-LLC-441092');
      setNewBillTaxClass('IRC § 162 Enterprise SaaS & Productivity');
    } else if (preset === 'openai_anthropic') {
      setNewBillVendor('Enterprise AI Compute & LLM Swarm Subscription');
      setNewBillCategory('AI_LLM_COMPUTE');
      setNewBillDescription('High-concurrency autonomous agent inference & code verification tier');
      setNewBillCost('950.00');
      setNewBillRail('USDC_ONCHAIN_BRIDGE');
      setNewBillMerchantId('AI-SWARM-WY-77310');
      setNewBillTaxClass('IRC § 174 R&D Autonomous Agent Compute');
    } else if (preset === 'aws_infra') {
      setNewBillVendor('AWS Nitro Enclaves & Dedicated Validator Nodes');
      setNewBillCategory('DEVOPS_GITHUB_SAAS');
      setNewBillDescription('HSM key signing enclaves and multi-region failover nodes');
      setNewBillCost('1120.00');
      setNewBillRail('CIRCLE_MINT_ACH');
      setNewBillMerchantId('AWS-NITRO-WY-55190');
      setNewBillTaxClass('IRC § 162 Validator & Security Infrastructure');
    }
  };

  return (
    <div className="space-y-6">
      {/* Toast Notification */}
      {billToast && (
        <div className="fixed bottom-6 right-6 z-50 bg-emerald-950 border border-emerald-500 text-emerald-200 px-4 py-3 rounded-xl shadow-2xl flex items-center gap-2.5 text-xs font-mono">
          <Sparkles className="w-4 h-4 text-emerald-400 shrink-0" />
          <span>{billToast}</span>
        </div>
      )}

      {/* Treasury Hero Banner */}
      <div className="rounded-2xl bg-gradient-to-r from-slate-900 via-teal-950/30 to-slate-900 border border-slate-800 p-6 shadow-xl">
        <div className="flex flex-col md:flex-row md:items-center justify-between gap-4">
          <div>
            <div className="flex flex-wrap items-center gap-2">
              <span className="px-2.5 py-0.5 rounded-full text-xs font-semibold bg-teal-500/20 text-teal-400 border border-teal-500/40 flex items-center gap-1.5">
                <Wallet className="w-3.5 h-3.5" />
                NexusDAOTreasury Vault
              </span>
              <span className="px-2.5 py-0.5 rounded-full text-xs font-semibold bg-cyan-500/15 text-cyan-300 border border-cyan-500/30 flex items-center gap-1.5">
                <Building2 className="w-3.5 h-3.5" />
                {wyomingLlcProfile.legalName} ({wyomingLlcProfile.filingId})
              </span>
              <span className="text-xs text-slate-500 font-mono">Contract: NexusDAOTreasury.sol</span>
            </div>
            <h2 className="text-xl font-bold text-slate-100 mt-1">
              Multi-Asset Protocol Treasury & Wyoming DAO LLC Commercial Desk
            </h2>
            <p className="text-xs text-slate-400 max-w-3xl mt-1">
              Holds protocol reserves with Timelock-gated execution and settles recurring Google Cloud, Google Workspace, and SaaS operational subscriptions directly through the registered Wyoming DAO LLC legal entity.
            </p>
          </div>

          <div className="flex flex-wrap items-center gap-2">
            {isGuardianOrOwner && (
              <button
                onClick={toggleTreasuryPause}
                className={`px-3.5 py-2 rounded-xl text-xs font-bold transition flex items-center gap-1.5 cursor-pointer ${
                  isTreasuryPaused
                    ? 'bg-emerald-600 hover:bg-emerald-500 text-white shadow-lg'
                    : 'bg-red-950/80 hover:bg-red-900 border border-red-800 text-red-300'
                }`}
              >
                {isTreasuryPaused ? (
                  <>
                    <PlayCircle className="w-3.5 h-3.5" />
                    Unpause Treasury
                  </>
                ) : (
                  <>
                    <PauseCircle className="w-3.5 h-3.5" />
                    Emergency Pause
                  </>
                )}
              </button>
            )}

            <button
              onClick={() => setShowCreateBillModal(true)}
              className="px-3.5 py-2 rounded-xl bg-slate-800 hover:bg-slate-700 border border-cyan-500/40 text-cyan-300 font-bold text-xs transition flex items-center gap-1.5 cursor-pointer"
            >
              <Plus className="w-3.5 h-3.5" />
              New Wyoming LLC Digital Bill
            </button>

            <button
              onClick={() => setShowTransferModal(true)}
              className="px-4 py-2 rounded-xl bg-gradient-to-r from-teal-600 to-cyan-600 hover:from-teal-500 hover:to-cyan-500 text-white font-bold text-xs shadow-lg transition flex items-center gap-1.5 cursor-pointer"
            >
              <Send className="w-3.5 h-3.5" />
              Request Transfer
            </button>
          </div>
        </div>

        {/* Total Value */}
        <div className="mt-5 pt-4 border-t border-slate-800/80 flex flex-wrap items-center justify-between gap-4">
          <div>
            <span className="text-[10px] uppercase font-bold text-slate-400">Total Treasury Reserve Value</span>
            <div className="text-2xl font-black text-slate-100 font-mono mt-0.5">
              ${totalTreasuryUsd.toLocaleString()} USD
            </div>
          </div>
          <div className="flex flex-wrap items-center gap-4 text-xs font-mono text-slate-400">
            <div>
              Legal Wrapper: <span className="text-emerald-400 font-semibold">Wyo. Stat. § 17-31-101</span>
            </div>
            <div>
              Executor: <span className="text-cyan-400 font-semibold">NexusDAOTimelock</span>
            </div>
            <div>
              Multisig Threshold: <span className="text-amber-400 font-semibold">50 ETH / 100k ERC20</span>
            </div>
            <div>
              Status:{' '}
              <span className={isTreasuryPaused ? 'text-red-400 font-bold' : 'text-emerald-400 font-bold'}>
                {isTreasuryPaused ? 'PAUSED' : 'ACTIVE'}
              </span>
            </div>
          </div>
        </div>
      </div>

      {/* Asset Cards Grid */}
      <div className="grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-6 gap-3">
        {treasuryAssets.map((asset) => (
          <div
            key={asset.symbol}
            className="p-4 rounded-2xl bg-slate-900/90 border border-slate-800 space-y-2 hover:border-slate-700 transition"
          >
            <div className="flex items-center justify-between">
              <span className="text-xs font-bold text-slate-200">{asset.symbol}</span>
              <span className="text-[10px] text-slate-500 font-mono">{asset.name}</span>
            </div>
            <div className="text-sm font-bold text-slate-100 font-mono">{asset.balance}</div>
            <div className="text-xs text-teal-400 font-mono">{asset.usdValue}</div>
          </div>
        ))}
      </div>

      {/* NEW: RECHARTS MONTHLY BILL PAYMENTS & SUBSCRIPTION COSTS VS. DAO TREASURY OUTFLOW */}
      <div
        className="rounded-2xl bg-slate-900/90 border border-slate-800 p-5 space-y-5 shadow-xl"
        data-testid="treasury-bills-outflow-chart"
      >
        <div className="flex flex-col lg:flex-row lg:items-center justify-between gap-4 border-b border-slate-800 pb-4">
          <div>
            <div className="flex items-center gap-2">
              <span className="p-1.5 rounded-lg bg-emerald-950 text-emerald-400 border border-emerald-800">
                <BarChart3 className="w-4 h-4" />
              </span>
              <h3 className="text-base font-bold text-slate-100">
                Monthly Bill Payments & Subscription Costs vs. DAO Treasury Outflow
              </h3>
              <span className="px-2 py-0.5 rounded text-[10px] font-mono font-semibold bg-cyan-950 text-cyan-300 border border-cyan-800">
                Wyoming DAO LLC + Circle Gateway
              </span>
            </div>
            <p className="text-xs text-slate-400 mt-1">
              Comparative trajectory of Google Cloud/Workspace & SaaS subscriptions paid via{' '}
              <strong className="text-slate-200">{wyomingLlcProfile.legalName}</strong> and Circle DAO operational bills relative to total monthly protocol treasury outflow.
            </p>
          </div>

          {/* Chart Mode & Timeframe Controls */}
          <div className="flex flex-wrap items-center gap-2">
            <div className="flex items-center bg-slate-950 p-1 rounded-xl border border-slate-800 text-xs">
              <button
                onClick={() => setOutflowChartMode('composed')}
                className={`px-3 py-1.5 rounded-lg font-medium transition cursor-pointer ${
                  outflowChartMode === 'composed'
                    ? 'bg-slate-800 text-cyan-400 font-bold'
                    : 'text-slate-400 hover:text-slate-200'
                }`}
              >
                Outflow Comparison
              </button>
              <button
                onClick={() => setOutflowChartMode('stacked')}
                className={`px-3 py-1.5 rounded-lg font-medium transition cursor-pointer ${
                  outflowChartMode === 'stacked'
                    ? 'bg-slate-800 text-emerald-400 font-bold'
                    : 'text-slate-400 hover:text-slate-200'
                }`}
              >
                Stacked Breakdown
              </button>
              <button
                onClick={() => setOutflowChartMode('google_focus')}
                className={`px-3 py-1.5 rounded-lg font-medium transition cursor-pointer ${
                  outflowChartMode === 'google_focus'
                    ? 'bg-slate-800 text-amber-400 font-bold'
                    : 'text-slate-400 hover:text-slate-200'
                }`}
              >
                Google & LLC Subscriptions
              </button>
            </div>

            <div className="flex items-center bg-slate-950 p-1 rounded-xl border border-slate-800 text-xs font-mono">
              {([6, 12] as const).map((months) => (
                <button
                  key={months}
                  onClick={() => setOutflowTimeframe(months)}
                  className={`px-2.5 py-1.5 rounded-lg font-semibold transition cursor-pointer ${
                    outflowTimeframe === months
                      ? 'bg-cyan-950 text-cyan-300 border border-cyan-800/80'
                      : 'text-slate-400 hover:text-slate-200'
                  }`}
                >
                  {months}M
                </button>
              ))}
            </div>
          </div>
        </div>

        {/* KPI Metrics Strip */}
        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-3">
          <div className="p-3.5 rounded-xl bg-slate-950/80 border border-slate-800/90">
            <div className="flex items-center justify-between text-[10px] uppercase font-bold text-slate-400">
              <span>Monthly Bills & Subscriptions</span>
              <CreditCard className="w-3.5 h-3.5 text-cyan-400" />
            </div>
            <div className="text-lg font-black text-cyan-400 font-mono mt-1">
              ${outflowAnalytics.currentMonthCombinedBillsSubsUsd.toLocaleString()} / mo
            </div>
            <div className="text-[11px] text-slate-400 font-mono mt-0.5">
              LLC Subs: <strong className="text-slate-200">${outflowAnalytics.currentMonthSubscriptionsUsd.toLocaleString()}</strong> • DAO Bills:{' '}
              <strong className="text-slate-200">${outflowAnalytics.currentMonthBillsUsd.toLocaleString()}</strong>
            </div>
          </div>

          <div className="p-3.5 rounded-xl bg-slate-950/80 border border-slate-800/90">
            <div className="flex items-center justify-between text-[10px] uppercase font-bold text-slate-400">
              <span>Google Cloud & Workspace (WY LLC)</span>
              <Globe className="w-3.5 h-3.5 text-emerald-400" />
            </div>
            <div className="text-lg font-black text-emerald-400 font-mono mt-1">
              ${outflowAnalytics.currentMonthGoogleSpendUsd.toLocaleString()} / mo
            </div>
            <div className="text-[11px] text-slate-400 font-mono mt-0.5">
              Paid via <strong className="text-emerald-300">WY-DAO-2026-001489210</strong>
            </div>
          </div>

          <div className="p-3.5 rounded-xl bg-slate-950/80 border border-slate-800/90">
            <div className="flex items-center justify-between text-[10px] uppercase font-bold text-slate-400">
              <span>Total Monthly Treasury Outflow</span>
              <ArrowUpRight className="w-3.5 h-3.5 text-indigo-400" />
            </div>
            <div className="text-lg font-black text-slate-100 font-mono mt-1">
              ${outflowAnalytics.currentMonthTotalOutflowUsd.toLocaleString()} / mo
            </div>
            <div className="text-[11px] text-slate-400 font-mono mt-0.5">
              Withdrawals & Transfers: <strong className="text-slate-300">${outflowAnalytics.currentMonthWithdrawalsUsd.toLocaleString()}</strong>
            </div>
          </div>

          <div className="p-3.5 rounded-xl bg-slate-950/80 border border-slate-800/90">
            <div className="flex items-center justify-between text-[10px] uppercase font-bold text-slate-400">
              <span>Bills Share of Total Outflow</span>
              <Layers className="w-3.5 h-3.5 text-amber-400" />
            </div>
            <div className="text-lg font-black text-amber-400 font-mono mt-1">
              {outflowAnalytics.billShareOfOutflowPct}% of Outflow
            </div>
            <div className="text-[11px] text-slate-400 font-mono mt-0.5">
              Budget Utilization: <strong className="text-emerald-400">{outflowAnalytics.budgetUtilizationPct}%</strong> of ceiling
            </div>
          </div>
        </div>

        {/* Recharts ComposedChart Visualization */}
        <div className="w-full h-80 pt-2">
          <ResponsiveContainer width="100%" height="100%">
            <ComposedChart
              data={outflowAnalytics.points}
              margin={{ top: 10, right: 20, left: 10, bottom: 10 }}
            >
              <defs>
                <linearGradient id="gradTotalOutflow" x1="0" y1="0" x2="0" y2="1">
                  <stop offset="5%" stopColor="#6366f1" stopOpacity={0.35} />
                  <stop offset="95%" stopColor="#6366f1" stopOpacity={0.02} />
                </linearGradient>
                <linearGradient id="gradWyomingSubs" x1="0" y1="0" x2="0" y2="1">
                  <stop offset="5%" stopColor="#10b981" stopOpacity={0.45} />
                  <stop offset="95%" stopColor="#10b981" stopOpacity={0.05} />
                </linearGradient>
              </defs>

              <CartesianGrid strokeDasharray="3 3" stroke="#1e293b" vertical={false} />

              <XAxis
                dataKey="month"
                stroke="#64748b"
                tick={{ fill: '#94a3b8', fontSize: 11 }}
                tickLine={{ stroke: '#334155' }}
              />

              <YAxis
                yAxisId="left"
                stroke="#64748b"
                tick={{ fill: '#94a3b8', fontSize: 11 }}
                tickLine={{ stroke: '#334155' }}
                tickFormatter={formatUsdCompact}
                width={65}
              />

              <YAxis
                yAxisId="right"
                orientation="right"
                stroke="#64748b"
                tick={{ fill: '#94a3b8', fontSize: 11 }}
                tickLine={{ stroke: '#334155' }}
                tickFormatter={(v) => `${v}%`}
                domain={[0, 100]}
                width={48}
                hide={outflowChartMode !== 'stacked'}
              />

              <RechartsTooltip
                content={({ active, payload, label }) => {
                  if (active && payload && payload.length) {
                    const pt = payload[0].payload;
                    return (
                      <div className="rounded-xl bg-slate-950/95 border border-slate-700 p-3.5 shadow-2xl text-xs space-y-2 min-w-[250px]">
                        <div className="flex items-center justify-between border-b border-slate-800 pb-1.5 font-bold text-slate-100">
                          <span>{label} Treasury Outflow Breakdown</span>
                          <span className="text-[10px] font-mono text-cyan-400">{pt.isoMonth}</span>
                        </div>

                        <div className="space-y-1 font-mono">
                          <div className="flex items-center justify-between text-emerald-400">
                            <span>Wyoming LLC Subscriptions:</span>
                            <span className="font-bold">${pt.wyomingLlcSubscriptionsUsd.toLocaleString()}</span>
                          </div>
                          <div className="flex items-center justify-between text-[11px] text-slate-400 pl-2">
                            <span>↳ Google Cloud & Workspace:</span>
                            <span className="text-emerald-300">${pt.googleEcosystemSpendUsd.toLocaleString()}</span>
                          </div>
                          <div className="flex items-center justify-between text-cyan-400">
                            <span>DAO Operational Bills (Circle):</span>
                            <span className="font-bold">${pt.daoOperationalBillsUsd.toLocaleString()}</span>
                          </div>
                          <div className="flex items-center justify-between text-amber-300 border-t border-slate-800/80 pt-1">
                            <span>Combined Bills & Subscriptions:</span>
                            <span className="font-bold">${pt.combinedBillsAndSubsUsd.toLocaleString()}</span>
                          </div>
                          <div className="flex items-center justify-between text-indigo-300">
                            <span>Treasury Withdrawals & Transfers:</span>
                            <span>${pt.treasuryWithdrawalsUsd.toLocaleString()}</span>
                          </div>
                          <div className="flex items-center justify-between text-slate-100 border-t border-slate-800 pt-1 font-bold">
                            <span>Total DAO Treasury Outflow:</span>
                            <span>${pt.totalTreasuryOutflowUsd.toLocaleString()}</span>
                          </div>
                        </div>

                        <div className="pt-1 border-t border-slate-800/80 flex items-center justify-between text-[11px] text-slate-400">
                          <span>Bills & Subs Share of Outflow:</span>
                          <span className="font-mono font-bold text-amber-400">{pt.billToOutflowRatioPct}%</span>
                        </div>
                      </div>
                    );
                  }
                  return null;
                }}
              />

              <Legend wrapperStyle={{ paddingTop: '10px', fontSize: '11px', color: '#94a3b8' }} />

              {outflowChartMode === 'composed' && (
                <>
                  <Area
                    yAxisId="left"
                    type="monotone"
                    dataKey="totalTreasuryOutflowUsd"
                    fill="url(#gradTotalOutflow)"
                    stroke="#6366f1"
                    strokeWidth={2}
                    name="Total DAO Treasury Outflow (USD)"
                  />
                  <Bar
                    yAxisId="left"
                    dataKey="wyomingLlcSubscriptionsUsd"
                    fill="#10b981"
                    radius={[4, 4, 0, 0]}
                    barSize={18}
                    name="Wyoming LLC Subscriptions (Google & SaaS)"
                  />
                  <Bar
                    yAxisId="left"
                    dataKey="daoOperationalBillsUsd"
                    fill="#06b6d4"
                    radius={[4, 4, 0, 0]}
                    barSize={18}
                    name="DAO Operational Bills (Circle USDC)"
                  />
                  <Line
                    yAxisId="left"
                    type="monotone"
                    dataKey="monthlyBudgetCeilingUsd"
                    stroke="#f59e0b"
                    strokeWidth={1.5}
                    strokeDasharray="5 5"
                    dot={false}
                    name="Monthly Outflow Budget Ceiling"
                  />
                </>
              )}

              {outflowChartMode === 'stacked' && (
                <>
                  <Bar
                    yAxisId="left"
                    dataKey="wyomingLlcSubscriptionsUsd"
                    stackId="outflow"
                    fill="#10b981"
                    name="Wyoming LLC Subscriptions (Google & SaaS)"
                  />
                  <Bar
                    yAxisId="left"
                    dataKey="daoOperationalBillsUsd"
                    stackId="outflow"
                    fill="#06b6d4"
                    name="DAO Operational Bills (Circle USDC)"
                  />
                  <Bar
                    yAxisId="left"
                    dataKey="treasuryWithdrawalsUsd"
                    stackId="outflow"
                    fill="#6366f1"
                    radius={[4, 4, 0, 0]}
                    name="Protocol Withdrawals & Liquidity Outflow"
                  />
                  <Line
                    yAxisId="right"
                    type="monotone"
                    dataKey="billToOutflowRatioPct"
                    stroke="#f59e0b"
                    strokeWidth={2.5}
                    name="Bills & Subs Share (%)"
                  />
                </>
              )}

              {outflowChartMode === 'google_focus' && (
                <>
                  <Area
                    yAxisId="left"
                    type="monotone"
                    dataKey="combinedBillsAndSubsUsd"
                    fill="url(#gradWyomingSubs)"
                    stroke="#10b981"
                    strokeWidth={2}
                    name="Combined Monthly Bills & Subscriptions"
                  />
                  <Bar
                    yAxisId="left"
                    dataKey="googleEcosystemSpendUsd"
                    fill="#f59e0b"
                    radius={[4, 4, 0, 0]}
                    barSize={20}
                    name="Google Cloud, Workspace & Gemini API (WY LLC)"
                  />
                  <Bar
                    yAxisId="left"
                    dataKey="daoOperationalBillsUsd"
                    fill="#06b6d4"
                    radius={[4, 4, 0, 0]}
                    barSize={20}
                    name="DAO Infrastructure Bills (RPC / Oracle / GPU)"
                  />
                </>
              )}
            </ComposedChart>
          </ResponsiveContainer>
        </div>
      </div>

      {/* NEW: WYOMING DAO LLC DIGITAL BILL & SUBSCRIPTION PAYMENT DESK */}
      <div
        className="rounded-2xl bg-slate-900/90 border border-slate-800 p-5 space-y-5 shadow-xl"
        data-testid="wyoming-llc-bill-desk"
      >
        {/* Legal Entity Header */}
        <div className="flex flex-col lg:flex-row lg:items-center justify-between gap-4 border-b border-slate-800 pb-4">
          <div className="space-y-1">
            <div className="flex flex-wrap items-center gap-2">
              <span className="px-2.5 py-0.5 rounded-full text-xs font-bold bg-emerald-500/15 text-emerald-400 border border-emerald-500/30 flex items-center gap-1.5">
                <Building2 className="w-3.5 h-3.5" />
                {wyomingLlcProfile.legalName}
              </span>
              <span className="text-xs font-mono text-cyan-400 bg-cyan-950/80 border border-cyan-800/60 px-2 py-0.5 rounded">
                Filing ID: {wyomingLlcProfile.filingId}
              </span>
              <span className="text-xs font-mono text-slate-400">
                {wyomingLlcProfile.statutoryAuthority}
              </span>
            </div>
            <h3 className="text-base font-bold text-slate-100">
              Wyoming DAO LLC Digital Bill & Subscription Payment Desk (Google & Commercial SaaS)
            </h3>
            <p className="text-xs text-slate-400">
              Pay Google Cloud, Google Workspace, Gemini API, GitHub Enterprise, and any recurring commercial cost subscription directly through the DAO&apos;s legally recognized Wyoming LLC wrapper ({wyomingLlcProfile.registeredOffice}).
            </p>
          </div>

          <div className="flex flex-wrap items-center gap-2 shrink-0">
            <button
              onClick={handlePayAllWyomingBills}
              disabled={pendingWyomingBillsCount === 0}
              className="px-4 py-2 rounded-xl bg-emerald-600 hover:bg-emerald-500 disabled:opacity-40 text-white font-bold text-xs shadow-lg transition flex items-center gap-1.5 cursor-pointer"
            >
              <CheckCircle2 className="w-3.5 h-3.5" />
              Pay All Pending LLC Bills ({pendingWyomingBillsCount})
            </button>
            <button
              onClick={() => setShowCreateBillModal(true)}
              className="px-4 py-2 rounded-xl bg-gradient-to-r from-cyan-600 to-teal-600 hover:from-cyan-500 hover:to-teal-500 text-white font-bold text-xs shadow-lg transition flex items-center gap-1.5 cursor-pointer"
            >
              <Plus className="w-3.5 h-3.5" />
              + Create Digital Bill / Subscription
            </button>
          </div>
        </div>

        {/* Entity Credentials & Category Filter Bar */}
        <div className="flex flex-col md:flex-row md:items-center justify-between gap-3 bg-slate-950/80 p-3 rounded-xl border border-slate-800/80 text-xs">
          <div className="flex flex-wrap items-center gap-4 font-mono text-[11px] text-slate-400">
            <span>
              Virtual Card: <strong className="text-emerald-400">{wyomingLlcProfile.virtualCardPrefix}</strong>
            </span>
            <span>
              EIN: <strong className="text-slate-200">{wyomingLlcProfile.einMasked}</strong>
            </span>
            <span>
              Settled Cycle: <strong className="text-cyan-400">{outflowAnalytics.wyomingLlcPaidCount}/{outflowAnalytics.wyomingLlcTotalCount} Active</strong>
            </span>
          </div>

          <div className="flex flex-wrap items-center gap-1">
            {[
              { id: 'ALL', label: 'All Subscriptions' },
              { id: 'GOOGLE_CLOUD_WORKSPACE', label: 'Google Cloud & Workspace' },
              { id: 'AI_LLM_COMPUTE', label: 'AI & TPU Compute' },
              { id: 'DEVOPS_GITHUB_SAAS', label: 'GitHub & DevOps' },
              { id: 'WYOMING_LEGAL_FILING', label: 'Wyoming Legal & Filing' },
            ].map((cat) => (
              <button
                key={cat.id}
                onClick={() => setSelectedBillCategory(cat.id)}
                className={`px-2.5 py-1 rounded-lg text-[11px] font-semibold transition cursor-pointer ${
                  selectedBillCategory === cat.id
                    ? 'bg-cyan-600 text-white'
                    : 'text-slate-400 hover:text-slate-200 bg-slate-900'
                }`}
              >
                {cat.label}
              </button>
            ))}
          </div>
        </div>

        {/* Digital Bills Grid */}
        <div className="grid grid-cols-1 md:grid-cols-2 gap-3.5">
          {filteredWyomingBills.map((bill) => (
            <div
              key={bill.id}
              className="p-4 rounded-xl bg-slate-950/90 border border-slate-800 hover:border-slate-700 transition flex flex-col justify-between gap-3"
            >
              <div className="space-y-2">
                <div className="flex items-start justify-between gap-2">
                  <div>
                    <div className="flex flex-wrap items-center gap-1.5">
                      <span className="text-[10px] font-mono font-bold px-2 py-0.5 rounded bg-cyan-950 text-cyan-300 border border-cyan-800/70">
                        {bill.invoiceNumber}
                      </span>
                      <span className="text-[10px] font-mono px-2 py-0.5 rounded bg-slate-900 text-slate-300 border border-slate-800">
                        {bill.category.replace(/_/g, ' ')}
                      </span>
                    </div>
                    <h4 className="text-sm font-bold text-slate-100 mt-1.5">{bill.vendor}</h4>
                  </div>

                  <span
                    className={`px-2 py-0.5 rounded text-[10px] font-mono font-bold uppercase shrink-0 ${
                      bill.status === 'PAID_CURRENT_CYCLE'
                        ? 'bg-emerald-950 text-emerald-400 border border-emerald-800'
                        : bill.status === 'REQUIRES_GUARDIAN'
                        ? 'bg-amber-950 text-amber-400 border border-amber-800'
                        : 'bg-cyan-950 text-cyan-300 border border-cyan-800'
                    }`}
                  >
                    {bill.status.replace(/_/g, ' ')}
                  </span>
                </div>

                <p className="text-xs text-slate-400">{bill.description}</p>

                <div className="grid grid-cols-3 gap-2 pt-1 text-[11px] font-mono">
                  <div className="p-2 rounded-lg bg-slate-900/90 border border-slate-800/80">
                    <div className="text-[9px] uppercase text-slate-500">Monthly Cost</div>
                    <div className="text-xs font-bold text-emerald-400">
                      ${bill.monthlyCostUsd.toFixed(2)} USD
                    </div>
                  </div>
                  <div className="p-2 rounded-lg bg-slate-900/90 border border-slate-800/80">
                    <div className="text-[9px] uppercase text-slate-500">Payment Rail</div>
                    <div className="text-[11px] text-slate-200 truncate">
                      {bill.paymentRail.replace(/_/g, ' ')}
                    </div>
                  </div>
                  <div className="p-2 rounded-lg bg-slate-900/90 border border-slate-800/80">
                    <div className="text-[9px] uppercase text-slate-500">Merchant Acct</div>
                    <div className="text-[11px] text-cyan-300 truncate">{bill.accountOrMerchantId}</div>
                  </div>
                </div>
              </div>

              <div className="pt-2.5 border-t border-slate-800/80 flex items-center justify-between gap-2">
                <div className="text-[10px] font-mono text-slate-400 truncate">
                  {bill.taxDeductibleClass}
                </div>

                <div className="flex items-center gap-2 shrink-0">
                  <button
                    onClick={() => setInspectedBill(bill)}
                    aria-label={`Inspect digital bill for ${bill.vendor}`}
                    className="px-2.5 py-1.5 rounded-lg bg-slate-900 hover:bg-slate-800 border border-slate-700 text-slate-300 text-[11px] font-semibold flex items-center gap-1 transition cursor-pointer"
                  >
                    <FileText className="w-3 h-3 text-cyan-400" />
                    Digital Bill
                  </button>

                  {bill.status !== 'PAID_CURRENT_CYCLE' && (
                    <button
                      onClick={() => handlePaySingleWyomingBill(bill.id)}
                      aria-label={`Pay ${bill.vendor} via WY LLC`}
                      className="px-3 py-1.5 rounded-lg bg-emerald-600 hover:bg-emerald-500 text-white text-[11px] font-bold flex items-center gap-1 transition cursor-pointer"
                    >
                      <Receipt className="w-3 h-3" />
                      Pay via WY LLC
                    </button>
                  )}
                </div>
              </div>
            </div>
          ))}
        </div>
      </div>

      {/* Visual Asset Allocation & Historical Balance Trends (Recharts) */}
      <TreasuryCharts assets={treasuryAssets} />

      {/* Large Transfers Co-Signing Queue */}
      <div className="rounded-2xl bg-slate-900/90 border border-slate-800 p-5 space-y-4">
        <div className="flex items-center justify-between border-b border-slate-800 pb-3">
          <div className="flex items-center gap-2">
            <ShieldCheck className="w-4 h-4 text-amber-400" />
            <h3 className="text-sm font-bold text-slate-200">
              Large Transfer Multisig Queue ({largeTransfers.length})
            </h3>
          </div>
          <span className="text-xs text-slate-400">
            Rule: Transfers &gt; 50 ETH require Guardian Co-Sign
          </span>
        </div>

        {largeTransfers.length === 0 ? (
          <div className="text-xs text-slate-500 text-center py-6">
            No large transfer requests pending.
          </div>
        ) : (
          <div className="space-y-3">
            {largeTransfers.map((req) => (
              <div
                key={req.nonce}
                className="p-4 rounded-xl bg-slate-950 border border-slate-800 flex flex-col md:flex-row md:items-center justify-between gap-3"
              >
                <div className="space-y-1">
                  <div className="flex items-center gap-2">
                    <span className="text-xs font-bold text-amber-400 font-mono">Nonce #{req.nonce}</span>
                    <span className="text-sm font-bold text-slate-100 font-mono">{req.amount}</span>
                    <span
                      className={`px-2 py-0.5 rounded text-[10px] font-bold font-mono uppercase ${
                        req.status === 'Pending_Guardian'
                          ? 'bg-amber-950 text-amber-400 border border-amber-800'
                          : req.status === 'Confirmed'
                          ? 'bg-cyan-950 text-cyan-400 border border-cyan-800'
                          : 'bg-emerald-950 text-emerald-400 border border-emerald-800'
                      }`}
                    >
                      {req.status.replace('_', ' ')}
                    </span>
                  </div>
                  <div className="text-xs text-slate-400 font-mono">
                    Recipient: <strong className="text-slate-300">{req.recipient}</strong> • Requested by:{' '}
                    {req.requestedBy.slice(0, 8)}... at {req.requestedAt}
                  </div>
                </div>

                <div className="flex items-center gap-2">
                  {req.status === 'Pending_Guardian' && (
                    <button
                      onClick={() => confirmLargeTransfer(req.nonce)}
                      disabled={!isGuardianOrOwner}
                      className="px-3.5 py-1.5 rounded-xl bg-amber-600 hover:bg-amber-500 text-white font-bold text-xs transition disabled:opacity-40 cursor-pointer"
                    >
                      Co-Sign as Guardian
                    </button>
                  )}

                  {req.status === 'Confirmed' && (
                    <button
                      onClick={() => executeLargeTransfer(req.nonce)}
                      className="px-3.5 py-1.5 rounded-xl bg-emerald-600 hover:bg-emerald-500 text-white font-bold text-xs transition cursor-pointer"
                    >
                      Execute Transfer
                    </button>
                  )}

                  {req.status === 'Executed' && (
                    <span className="text-xs text-emerald-400 font-medium flex items-center gap-1">
                      <CheckCircle className="w-3.5 h-3.5" /> Executed
                    </span>
                  )}
                </div>
              </div>
            ))}
          </div>
        )}
      </div>

      {/* MODAL: CREATE WYOMING DAO LLC DIGITAL BILL / SUBSCRIPTION */}
      {showCreateBillModal && (
        <div className="fixed inset-0 z-50 bg-black/80 backdrop-blur-sm flex items-center justify-center p-4">
          <div className="w-full max-w-xl rounded-2xl bg-slate-900 border border-slate-700 p-6 shadow-2xl space-y-4">
            <div className="flex items-center justify-between border-b border-slate-800 pb-3">
              <div>
                <div className="flex items-center gap-2">
                  <Building2 className="w-4 h-4 text-emerald-400" />
                  <h3 className="text-base font-bold text-slate-100">
                    Create Wyoming DAO LLC Digital Bill / Subscription
                  </h3>
                </div>
                <p className="text-xs text-slate-400 mt-0.5">
                  Billed through {wyomingLlcProfile.legalName} ({wyomingLlcProfile.filingId})
                </p>
              </div>
              <button
                onClick={() => setShowCreateBillModal(false)}
                className="text-slate-400 hover:text-slate-200 text-sm font-mono cursor-pointer"
              >
                ✕
              </button>
            </div>

            {/* Quick Presets for Google & Cloud Subscriptions */}
            <div className="space-y-1.5">
              <span className="text-[11px] font-semibold text-slate-400">
                1-Click Subscription Templates:
              </span>
              <div className="flex flex-wrap gap-1.5">
                <button
                  type="button"
                  onClick={() => applySubscriptionPreset('google_cloud')}
                  className="px-2.5 py-1 rounded-lg bg-cyan-950/90 hover:bg-cyan-900 border border-cyan-800 text-cyan-300 text-[11px] font-semibold cursor-pointer"
                >
                  Google Cloud & Gemini API
                </button>
                <button
                  type="button"
                  onClick={() => applySubscriptionPreset('google_workspace')}
                  className="px-2.5 py-1 rounded-lg bg-emerald-950/90 hover:bg-emerald-900 border border-emerald-800 text-emerald-300 text-[11px] font-semibold cursor-pointer"
                >
                  Google Workspace & Domains
                </button>
                <button
                  type="button"
                  onClick={() => applySubscriptionPreset('openai_anthropic')}
                  className="px-2.5 py-1 rounded-lg bg-purple-950/90 hover:bg-purple-900 border border-purple-800 text-purple-300 text-[11px] font-semibold cursor-pointer"
                >
                  AI Swarm Compute
                </button>
                <button
                  type="button"
                  onClick={() => applySubscriptionPreset('aws_infra')}
                  className="px-2.5 py-1 rounded-lg bg-amber-950/90 hover:bg-amber-900 border border-amber-800 text-amber-300 text-[11px] font-semibold cursor-pointer"
                >
                  AWS Validator Enclave
                </button>
              </div>
            </div>

            <form onSubmit={handleCreateWyomingBillSubmit} className="space-y-3 text-xs">
              <div>
                <label className="block text-slate-300 font-semibold mb-1">
                  Subscription Vendor / Service Provider
                </label>
                <input
                  type="text"
                  value={newBillVendor}
                  onChange={(e) => setNewBillVendor(e.target.value)}
                  className="w-full px-3 py-2 rounded-xl bg-slate-950 border border-slate-800 text-slate-100 focus:border-cyan-500 focus:outline-none"
                  placeholder="e.g. Google Cloud Platform, Google Workspace, GitHub, etc."
                  required
                />
              </div>

              <div className="grid grid-cols-1 sm:grid-cols-3 gap-3">
                <div>
                  <label className="block text-slate-300 font-semibold mb-1">Category</label>
                  <select
                    value={newBillCategory}
                    onChange={(e) => setNewBillCategory(e.target.value as WyomingSubscriptionCategory)}
                    className="w-full px-2.5 py-2 rounded-xl bg-slate-950 border border-slate-800 text-slate-200 focus:border-cyan-500 focus:outline-none"
                  >
                    <option value="GOOGLE_CLOUD_WORKSPACE">GOOGLE_CLOUD_WORKSPACE</option>
                    <option value="AI_LLM_COMPUTE">AI_LLM_COMPUTE</option>
                    <option value="DEVOPS_GITHUB_SAAS">DEVOPS_GITHUB_SAAS</option>
                    <option value="ENTERPRISE_SECURITY">ENTERPRISE_SECURITY</option>
                    <option value="WYOMING_LEGAL_FILING">WYOMING_LEGAL_FILING</option>
                    <option value="CUSTOM_SUBSCRIPTION">CUSTOM_SUBSCRIPTION</option>
                  </select>
                </div>

                <div>
                  <label className="block text-slate-300 font-semibold mb-1">Monthly Cost (USD)</label>
                  <input
                    type="number"
                    step="0.01"
                    value={newBillCost}
                    onChange={(e) => setNewBillCost(e.target.value)}
                    className="w-full px-3 py-2 rounded-xl bg-slate-950 border border-slate-800 font-mono text-emerald-400 focus:border-cyan-500 focus:outline-none"
                    required
                  />
                </div>

                <div>
                  <label className="block text-slate-300 font-semibold mb-1">Billing Cycle</label>
                  <select
                    value={newBillCycle}
                    onChange={(e) => setNewBillCycle(e.target.value as any)}
                    className="w-full px-2.5 py-2 rounded-xl bg-slate-950 border border-slate-800 text-slate-200 focus:border-cyan-500 focus:outline-none"
                  >
                    <option value="MONTHLY">MONTHLY</option>
                    <option value="USAGE_METERED">USAGE_METERED</option>
                    <option value="ANNUAL_PRORATED">ANNUAL_PRORATED</option>
                  </select>
                </div>
              </div>

              <div className="grid grid-cols-1 sm:grid-cols-2 gap-3">
                <div>
                  <label className="block text-slate-300 font-semibold mb-1">
                    Wyoming LLC Payment Rail
                  </label>
                  <select
                    value={newBillRail}
                    onChange={(e) => setNewBillRail(e.target.value as WyomingLlcPaymentRail)}
                    className="w-full px-2.5 py-2 rounded-xl bg-slate-950 border border-slate-800 text-slate-200 focus:border-cyan-500 focus:outline-none"
                  >
                    <option value="WYOMING_LLC_VIRTUAL_CARD">Wyoming LLC Virtual Card (4852-9910)</option>
                    <option value="CIRCLE_MINT_ACH">Circle Mint Commercial ACH</option>
                    <option value="USDC_ONCHAIN_BRIDGE">USDC On-Chain Settlement Bridge</option>
                    <option value="FEDWIRE_COMMERCIAL">Commercial Fedwire Settlement</option>
                  </select>
                </div>

                <div>
                  <label className="block text-slate-300 font-semibold mb-1">
                    Account / Merchant Billing ID
                  </label>
                  <input
                    type="text"
                    value={newBillMerchantId}
                    onChange={(e) => setNewBillMerchantId(e.target.value)}
                    className="w-full px-3 py-2 rounded-xl bg-slate-950 border border-slate-800 font-mono text-slate-200 focus:border-cyan-500 focus:outline-none"
                    required
                  />
                </div>
              </div>

              <div>
                <label className="block text-slate-300 font-semibold mb-1">Description</label>
                <input
                  type="text"
                  value={newBillDescription}
                  onChange={(e) => setNewBillDescription(e.target.value)}
                  className="w-full px-3 py-2 rounded-xl bg-slate-950 border border-slate-800 text-slate-200 focus:border-cyan-500 focus:outline-none"
                />
              </div>

              <div className="flex items-center justify-end gap-2 pt-3 border-t border-slate-800">
                <button
                  type="button"
                  onClick={() => setShowCreateBillModal(false)}
                  className="px-4 py-2 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-300 font-semibold cursor-pointer"
                >
                  Cancel
                </button>
                <button
                  type="submit"
                  className="px-5 py-2 rounded-xl bg-gradient-to-r from-emerald-600 to-teal-600 hover:from-emerald-500 hover:to-teal-500 text-white font-bold shadow-lg cursor-pointer"
                >
                  Issue Wyoming LLC Digital Bill
                </button>
              </div>
            </form>
          </div>
        </div>
      )}

      {/* MODAL: INSPECT DIGITAL BILL & WYOMING LLC LEGAL RECEIPT */}
      {inspectedBill && (
        <div className="fixed inset-0 z-50 bg-black/80 backdrop-blur-sm flex items-center justify-center p-4">
          <div className="w-full max-w-xl rounded-2xl bg-slate-900 border border-slate-700 p-6 shadow-2xl space-y-4 text-xs">
            <div className="flex items-center justify-between border-b border-slate-800 pb-3">
              <div className="flex items-center gap-2">
                <Receipt className="w-5 h-5 text-emerald-400" />
                <div>
                  <h3 className="text-sm font-bold text-white">
                    Wyoming DAO LLC Official Digital Bill & Attestation
                  </h3>
                  <p className="text-[11px] text-slate-400 font-mono">
                    {inspectedBill.wyomingEntityName} • {inspectedBill.wyomingFilingId}
                  </p>
                </div>
              </div>
              <button
                onClick={() => setInspectedBill(null)}
                className="px-2.5 py-1 rounded bg-slate-800 text-slate-300 hover:text-white font-mono cursor-pointer"
              >
                Close
              </button>
            </div>

            <div className="bg-slate-950 border border-slate-800 rounded-xl p-4 space-y-2.5 font-mono">
              <div className="flex justify-between border-b border-slate-800/80 pb-2">
                <span className="text-slate-400">Invoice Number:</span>
                <span className="text-cyan-400 font-bold">{inspectedBill.invoiceNumber}</span>
              </div>
              <div className="flex justify-between border-b border-slate-800/80 pb-2">
                <span className="text-slate-400">Billed Legal Entity:</span>
                <span className="text-slate-100 font-bold">{inspectedBill.wyomingEntityName}</span>
              </div>
              <div className="flex justify-between border-b border-slate-800/80 pb-2">
                <span className="text-slate-400">Statutory Authority:</span>
                <span className="text-emerald-300">{wyomingLlcProfile.statutoryAuthority}</span>
              </div>
              <div className="flex justify-between border-b border-slate-800/80 pb-2">
                <span className="text-slate-400">Vendor / Payee:</span>
                <span className="text-slate-100">{inspectedBill.vendor}</span>
              </div>
              <div className="flex justify-between border-b border-slate-800/80 pb-2">
                <span className="text-slate-400">Merchant Account ID:</span>
                <span className="text-cyan-300">{inspectedBill.accountOrMerchantId}</span>
              </div>
              <div className="flex justify-between border-b border-slate-800/80 pb-2">
                <span className="text-slate-400">Payment Rail:</span>
                <span className="text-slate-200">{inspectedBill.paymentRail}</span>
              </div>
              <div className="flex justify-between border-b border-slate-800/80 pb-2">
                <span className="text-slate-400">Subscription Amount:</span>
                <span className="text-emerald-400 font-bold">
                  ${inspectedBill.monthlyCostUsd.toFixed(2)} USD ({inspectedBill.billingCycle})
                </span>
              </div>
              <div className="flex justify-between border-b border-slate-800/80 pb-2">
                <span className="text-slate-400">Tax Classification:</span>
                <span className="text-amber-300">{inspectedBill.taxDeductibleClass}</span>
              </div>
              <div className="flex justify-between">
                <span className="text-slate-400">Status:</span>
                <span className="text-emerald-400 font-bold">{inspectedBill.status}</span>
              </div>
              {inspectedBill.digitalReceiptHash && (
                <div className="pt-2 border-t border-slate-800">
                  <div className="text-slate-500 text-[10px] mb-1">
                    256-Bit Cryptographic Settlement Receipt Hash:
                  </div>
                  <div className="text-[10px] text-emerald-400 break-all bg-slate-900 p-2 rounded border border-emerald-900/50">
                    {inspectedBill.digitalReceiptHash}
                  </div>
                </div>
              )}
            </div>

            <div className="flex items-center justify-end gap-2">
              {inspectedBill.status !== 'PAID_CURRENT_CYCLE' && (
                <button
                  onClick={() => {
                    handlePaySingleWyomingBill(inspectedBill.id);
                    setInspectedBill(null);
                  }}
                  className="px-4 py-2 rounded-xl bg-emerald-600 hover:bg-emerald-500 text-white font-bold cursor-pointer"
                >
                  Settle Digital Bill Now (${inspectedBill.monthlyCostUsd.toFixed(2)})
                </button>
              )}
              <button
                onClick={() => setInspectedBill(null)}
                className="px-4 py-2 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-200 font-semibold cursor-pointer"
              >
                Done
              </button>
            </div>
          </div>
        </div>
      )}

      {/* TRANSFER REQUEST MODAL */}
      {showTransferModal && (
        <div className="fixed inset-0 z-50 bg-black/80 backdrop-blur-sm flex items-center justify-center p-4">
          <div className="w-full max-w-md rounded-2xl bg-slate-900 border border-slate-800 p-6 shadow-2xl space-y-4">
            <div className="flex items-center justify-between border-b border-slate-800 pb-3">
              <div>
                <h3 className="text-base font-bold text-slate-100">Request Treasury Transfer</h3>
                <p className="text-xs text-slate-400">
                  Gated by NexusDAOTimelock / Guardian Co-sign
                </p>
              </div>
              <button
                onClick={() => setShowTransferModal(false)}
                className="text-slate-400 hover:text-slate-200"
              >
                ✕
              </button>
            </div>

            <form onSubmit={handleTransferSubmit} className="space-y-4">
              <div>
                <label className="block text-xs font-semibold text-slate-300 mb-1">Select Asset</label>
                <select
                  value={selectedAsset}
                  onChange={(e) => setSelectedAsset(e.target.value)}
                  className="w-full px-3 py-2 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-200 focus:border-teal-500 focus:outline-none"
                >
                  {treasuryAssets.map((a) => (
                    <option key={a.symbol} value={a.symbol}>
                      {a.symbol} ({a.balance})
                    </option>
                  ))}
                </select>
              </div>

              <div>
                <label className="block text-xs font-semibold text-slate-300 mb-1">Transfer Amount</label>
                <input
                  type="number"
                  step="any"
                  value={transferAmount}
                  onChange={(e) => setTransferAmount(e.target.value)}
                  placeholder="e.g. 25.0"
                  className="w-full px-3 py-2 rounded-xl bg-slate-950 border border-slate-800 text-xs font-mono text-slate-200 focus:border-teal-500 focus:outline-none"
                  required
                />
                {parseFloat(transferAmount) > 50 && selectedAsset === 'ETH' && (
                  <div className="mt-1 text-[11px] text-amber-400 flex items-center gap-1">
                    <AlertTriangle className="w-3 h-3" />
                    Amount exceeds 50 ETH. Will queue for Guardian Co-Signature.
                  </div>
                )}
              </div>

              <div>
                <label className="block text-xs font-semibold text-slate-300 mb-1">Recipient Address</label>
                <input
                  type="text"
                  value={transferRecipient}
                  onChange={(e) => setTransferRecipient(e.target.value)}
                  placeholder="0x..."
                  className="w-full px-3 py-2 rounded-xl bg-slate-950 border border-slate-800 text-xs font-mono text-slate-200 focus:border-teal-500 focus:outline-none"
                  required
                />
              </div>

              <div className="flex items-center justify-end gap-3 pt-2">
                <button
                  type="button"
                  onClick={() => setShowTransferModal(false)}
                  className="px-4 py-2 rounded-xl bg-slate-800 text-slate-300 text-xs font-semibold hover:bg-slate-700 transition"
                >
                  Cancel
                </button>
                <button
                  type="submit"
                  className="px-5 py-2 rounded-xl bg-gradient-to-r from-teal-600 to-cyan-600 hover:from-teal-500 hover:to-cyan-500 text-white font-bold text-xs shadow-lg transition"
                >
                  Submit Request
                </button>
              </div>
            </form>
          </div>
        </div>
      )}
    </div>
  );
};
