/**
 * @license
 * SPDX-License-Identifier: Apache-2.0
 * The Nexus Protocol DAO - Builder Fund & 10 Revenue Streams Center
 */

import React, { useState } from 'react';
import { useNexusDao } from '../context/NexusDaoContext';
import { REVENUE_STREAMS } from '../data/nexusContracts';
import {
  Coins,
  Cpu,
  Layers,
  Sparkles,
  ArrowUpRight,
  CheckCircle,
  TrendingUp,
  Activity,
  Zap,
} from 'lucide-react';

export const BuilderFundRevenue: React.FC = () => {
  const {
    account,
    builderFeeUsdCents,
    builderFundEth,
    builderFundSatoshis,
    builderClaimableEth,
    recordApiUsage,
    claimBuilderRewards,
    activeRevenueStreams,
    harvestAllStreams,
    harvestSingleStream,
    toggleStreamAutoCompound,
  } = useNexusDao();

  const [callCountInput, setCallCountInput] = useState<number>(500);
  const [harvestNotification, setHarvestNotification] = useState<string | null>(null);

  const handleSimulateApiTraffic = () => {
    if (callCountInput <= 0) return;
    recordApiUsage(callCountInput);
  };

  const handleHarvestAll = () => {
    const amount = harvestAllStreams();
    setHarvestNotification(`Harvested $${amount.toLocaleString()} USD across all 10 streams into Treasury Vault!`);
    setTimeout(() => setHarvestNotification(null), 6000);
  };

  const handleHarvestSingle = (id: number, name: string) => {
    const amount = harvestSingleStream(id);
    setHarvestNotification(`Harvested $${amount.toFixed(2)} from ${name}!`);
    setTimeout(() => setHarvestNotification(null), 6000);
  };

  const totalAccumulatedAllStreams = activeRevenueStreams.reduce((sum, s) => sum + s.totalAccumulatedUsd, 0);
  const totalDailyInflowAllStreams = activeRevenueStreams.reduce((sum, s) => sum + s.dailyInflowUsd, 0);
  const totalAccruedClaimableAllStreams = activeRevenueStreams.reduce((sum, s) => sum + s.accruedClaimableUsd, 0);

  return (
    <div className="space-y-6" data-testid="builder-fund-revenue-view">
      {/* Hero Banner */}
      <div className="rounded-2xl bg-gradient-to-r from-slate-900 via-amber-950/30 to-slate-900 border border-slate-800 p-6 shadow-xl">
        <div className="flex flex-col lg:flex-row lg:items-center justify-between gap-4">
          <div>
            <div className="flex items-center gap-2">
              <span className="px-2.5 py-0.5 rounded-full text-xs font-semibold bg-amber-500/20 text-amber-400 border border-amber-500/40 flex items-center gap-1.5">
                <Coins className="w-3.5 h-3.5" />
                NexusBuilderFund & 10 Activated Revenue Streams
              </span>
              <span className="text-xs text-slate-500 font-mono">10/10 Streams Operational & Continuous Streaming</span>
            </div>
            <h2 className="text-xl font-bold text-slate-100 mt-1">
              Activated Protocol Revenue & Developer Payout Engine
            </h2>
            <p className="text-xs text-slate-400 max-w-2xl mt-1">
              Real-time cashflow from automated token reflection taxes, game theory fee sinks, Uniswap v3 LP rewards, Wyoming LLC property rents, and Protocol Guild oracle settlements.
            </p>
          </div>

          <div className="flex flex-wrap items-center gap-3">
            <button
              onClick={handleHarvestAll}
              className="px-4 py-2.5 rounded-xl bg-gradient-to-r from-emerald-600 to-teal-600 hover:from-emerald-500 hover:to-teal-500 text-white font-bold text-xs shadow-lg transition flex items-center gap-1.5"
            >
              <Zap className="w-4 h-4 fill-current" />
              Harvest All 10 Streams (${totalAccruedClaimableAllStreams.toLocaleString()})
            </button>

            <button
              onClick={claimBuilderRewards}
              disabled={builderClaimableEth <= 0}
              className="px-4 py-2.5 rounded-xl bg-gradient-to-r from-amber-600 to-yellow-600 hover:from-amber-500 hover:to-yellow-500 text-slate-950 font-bold text-xs shadow-lg transition flex items-center gap-1.5 disabled:opacity-40"
            >
              <Sparkles className="w-4 h-4 fill-current" />
              Claim Builder Comp ({builderClaimableEth.toFixed(4)} ETH)
            </button>
          </div>
        </div>

        {/* Global Revenue Metrics Strip */}
        <div className="grid grid-cols-2 sm:grid-cols-4 gap-3 mt-5 pt-4 border-t border-slate-800/80">
          <div className="p-3 rounded-xl bg-slate-950/60 border border-slate-800/80">
            <div className="text-[10px] uppercase font-bold text-slate-400">Total Streamed Revenue</div>
            <div className="text-base font-bold text-emerald-400 font-mono mt-0.5">
              ${totalAccumulatedAllStreams.toLocaleString()} USD
            </div>
            <div className="text-[11px] text-slate-500 font-mono">Cumulative across 10 streams</div>
          </div>

          <div className="p-3 rounded-xl bg-slate-950/60 border border-slate-800/80">
            <div className="text-[10px] uppercase font-bold text-slate-400">24h Daily Inflow Velocity</div>
            <div className="text-base font-bold text-cyan-400 font-mono mt-0.5">
              +${totalDailyInflowAllStreams.toLocaleString()}/day
            </div>
            <div className="text-[11px] text-slate-500 font-mono">Continuous liquidity routing</div>
          </div>

          <div className="p-3 rounded-xl bg-slate-950/60 border border-slate-800/80">
            <div className="text-[10px] uppercase font-bold text-slate-400">Pending Accrued to Harvest</div>
            <div className="text-base font-bold text-amber-300 font-mono mt-0.5">
              ${totalAccruedClaimableAllStreams.toLocaleString()} USD
            </div>
            <div className="text-[11px] text-slate-500 font-mono">Ready for vault distribution</div>
          </div>

          <div className="p-3 rounded-xl bg-slate-950/60 border border-slate-800/80">
            <div className="text-[10px] uppercase font-bold text-slate-400">Builder Satoshis / BTC</div>
            <div className="text-base font-bold text-yellow-400 font-mono mt-0.5">
              {builderFundSatoshis.toLocaleString()} Sats
            </div>
            <div className="text-[11px] text-slate-500 font-mono">{(builderFundSatoshis / 100_000_000).toFixed(4)} BTC Pool</div>
          </div>
        </div>
      </div>

      {harvestNotification && (
        <div className="p-3 rounded-xl bg-emerald-950/80 border border-emerald-800 text-xs text-emerald-300 flex items-center justify-between shadow-lg">
          <span className="flex items-center gap-2 font-medium">
            <CheckCircle className="w-4 h-4 text-emerald-400" />
            {harvestNotification}
          </span>
          <span className="text-[10px] text-emerald-400 font-mono">On-Chain Event Logged</span>
        </div>
      )}

      {/* Oracle Simulation Trigger */}
      <div className="rounded-2xl bg-slate-900/90 border border-slate-800 p-5 space-y-3">
        <div className="flex items-center justify-between border-b border-slate-800 pb-2">
          <div className="flex items-center gap-2">
            <Activity className="w-4 h-4 text-cyan-400" />
            <h3 className="text-xs font-bold text-slate-200 uppercase tracking-wider">
              Chainlink Automation & Oracle REST Ingestion
            </h3>
          </div>
          <span className="text-[11px] text-slate-400">Simulate off-chain developer usage on-chain</span>
        </div>

        <div className="flex flex-col sm:flex-row items-center gap-3">
          <div className="flex-1 w-full">
            <label className="block text-[11px] text-slate-400 mb-1">
              Logged API Calls / Contract Invocations to Settle
            </label>
            <input
              type="number"
              value={callCountInput}
              onChange={(e) => setCallCountInput(Number(e.target.value))}
              placeholder="e.g. 500"
              className="w-full px-3 py-2 rounded-xl bg-slate-950 border border-slate-800 text-xs font-mono text-slate-200 focus:border-amber-500 focus:outline-none"
            />
          </div>

          <button
            onClick={handleSimulateApiTraffic}
            className="w-full sm:w-auto mt-auto px-5 py-2.5 rounded-xl bg-gradient-to-r from-amber-600 to-yellow-600 hover:from-amber-500 hover:to-yellow-500 text-slate-950 font-bold text-xs shadow-md transition flex items-center justify-center gap-2 shrink-0"
          >
            <Zap className="w-3.5 h-3.5 fill-current" />
            Trigger recordUsage() Settlement
          </button>
        </div>
      </div>

      {/* The 10 Activated Revenue Streams Interactive Grid */}
      <div className="rounded-2xl bg-slate-900/90 border border-slate-800 p-6 space-y-4">
        <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-2 border-b border-slate-800 pb-3">
          <div>
            <h3 className="text-base font-bold text-slate-200">
              The 10 Activated Canonical Revenue Streams
            </h3>
            <p className="text-xs text-slate-400">
              All 10 streams actively generating continuous yields with configurable auto-compounding and instant manual harvests.
            </p>
          </div>
          <span className="text-xs px-2.5 py-1 rounded-full bg-emerald-950 text-emerald-400 border border-emerald-800/80 font-mono font-semibold flex items-center gap-1.5">
            <span className="w-2 h-2 rounded-full bg-emerald-400 animate-pulse" />
            10 / 10 Active
          </span>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-2 gap-3.5">
          {activeRevenueStreams.map((s) => (
            <div
              key={s.id}
              className="p-4 rounded-xl bg-slate-950 border border-slate-800 space-y-3 hover:border-slate-700 transition"
            >
              <div className="flex items-start justify-between gap-2">
                <div className="flex items-center gap-2">
                  <span className="w-6 h-6 rounded-lg bg-amber-950/80 text-amber-400 flex items-center justify-center font-bold text-xs font-mono border border-amber-800/40">
                    {s.id}
                  </span>
                  <div>
                    <h4 className="text-xs font-bold text-slate-100">{s.name}</h4>
                    <span className="text-[10px] text-slate-500 font-mono">{s.destinationContract}</span>
                  </div>
                </div>

                <div className="flex items-center gap-1.5 shrink-0">
                  <span
                    className={`px-2 py-0.5 rounded text-[10px] font-bold ${
                      s.type.includes('Passive')
                        ? 'bg-teal-950 text-teal-400 border border-teal-800/60'
                        : 'bg-indigo-950 text-indigo-400 border border-indigo-800/60'
                    }`}
                  >
                    {s.type}
                  </span>
                  <span className="text-xs font-bold font-mono text-emerald-400">{s.apy}</span>
                </div>
              </div>

              <p className="text-xs text-slate-400 leading-relaxed">{s.description}</p>

              <div className="grid grid-cols-3 gap-2 pt-2 border-t border-slate-900 text-xs font-mono">
                <div>
                  <span className="text-[10px] text-slate-500 uppercase">Accumulated</span>
                  <div className="text-slate-200 font-bold">${s.totalAccumulatedUsd.toLocaleString()}</div>
                </div>
                <div>
                  <span className="text-[10px] text-slate-500 uppercase">Daily Inflow</span>
                  <div className="text-cyan-400 font-bold">+${s.dailyInflowUsd.toLocaleString()}</div>
                </div>
                <div>
                  <span className="text-[10px] text-slate-500 uppercase">Claimable</span>
                  <div className="text-emerald-400 font-bold">${s.accruedClaimableUsd.toFixed(2)}</div>
                </div>
              </div>

              <div className="pt-2 border-t border-slate-900 flex items-center justify-between text-xs">
                <button
                  onClick={() => toggleStreamAutoCompound(s.id)}
                  className={`text-[11px] font-mono px-2 py-1 rounded-lg border transition ${
                    s.autoCompoundEnabled
                      ? 'bg-emerald-950/60 text-emerald-400 border-emerald-800'
                      : 'bg-slate-900 text-slate-400 border-slate-800'
                  }`}
                >
                  {s.autoCompoundEnabled ? 'Auto-Compounding: ON' : 'Auto-Compounding: OFF'}
                </button>

                <button
                  onClick={() => handleHarvestSingle(s.id, s.name)}
                  disabled={s.accruedClaimableUsd <= 0}
                  className="px-3 py-1 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-200 font-bold text-xs transition disabled:opacity-40"
                >
                  Harvest (${s.accruedClaimableUsd.toFixed(2)})
                </button>
              </div>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
};
