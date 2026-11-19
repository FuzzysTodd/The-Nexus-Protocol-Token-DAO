/**
 * @license
 * SPDX-License-Identifier: Apache-2.0
 * The Nexus Protocol DAO - Treasury Asset Allocation & Historical Trends
 */

import React, { useState, useMemo } from 'react';
import {
  ResponsiveContainer,
  PieChart,
  Pie,
  Cell,
  Tooltip as RechartsTooltip,
  AreaChart,
  Area,
  XAxis,
  YAxis,
  CartesianGrid,
  Legend,
} from 'recharts';
import {
  calculateTreasuryAllocation,
  generateHistoricalTreasuryTrends,
  calculateTreasuryMetricsSummary,
  TreasuryAssetInput,
  TreasuryTimeframe,
  TreasuryAllocationItem,
} from '../dao/logic';
import {
  PieChart as PieIcon,
  TrendingUp,
  Layers,
  ArrowUpRight,
  ShieldAlert,
  Sparkles,
  BarChart3,
  Calendar,
  Filter,
} from 'lucide-react';

interface TreasuryChartsProps {
  assets: TreasuryAssetInput[];
}

type ChartViewMode = 'stacked' | 'total' | 'single';

export const TreasuryCharts: React.FC<TreasuryChartsProps> = ({ assets }) => {
  const [timeframe, setTimeframe] = useState<TreasuryTimeframe>('30D');
  const [viewMode, setViewMode] = useState<ChartViewMode>('stacked');
  const [selectedAssetSymbol, setSelectedAssetSymbol] = useState<string | null>(null);
  const [hoveredSlice, setHoveredSlice] = useState<TreasuryAllocationItem | null>(null);
  const [categoryFilter, setCategoryFilter] = useState<'ALL' | 'STABLES' | 'VOLATILE'>('ALL');

  // Allocation calculation
  const allocation = useMemo(() => calculateTreasuryAllocation(assets), [assets]);

  // Filtered allocation items for list display
  const displayAllocationItems = useMemo(() => {
    if (categoryFilter === 'STABLES') {
      return allocation.items.filter((item) => ['USDC', 'USDT', 'DAI'].includes(item.symbol));
    }
    if (categoryFilter === 'VOLATILE') {
      return allocation.items.filter((item) => !['USDC', 'USDT', 'DAI'].includes(item.symbol));
    }
    return allocation.items;
  }, [allocation.items, categoryFilter]);

  // Historical trend data generated deterministically and ending at current live values
  const historicalData = useMemo(() => {
    return generateHistoricalTreasuryTrends(timeframe, assets);
  }, [timeframe, assets]);

  // Trend metrics summary
  const metrics = useMemo(() => {
    return calculateTreasuryMetricsSummary(historicalData);
  }, [historicalData]);

  // Active asset for single-asset view
  const activeFocusSymbol = selectedAssetSymbol || allocation.dominantAsset?.symbol || 'NGTT';
  const activeFocusItem = allocation.items.find((item) => item.symbol === activeFocusSymbol) || allocation.items[0];

  // Tooltip formatter for USD currency
  const formatCurrency = (val: number) => {
    if (val >= 1_000_000) {
      return `$${(val / 1_000_000).toFixed(2)}M`;
    }
    if (val >= 1_000) {
      return `$${(val / 1_000).toFixed(1)}k`;
    }
    return `$${val.toLocaleString()}`;
  };

  return (
    <div className="space-y-6" data-testid="treasury-charts-container">
      {/* SECTION HEADER & QUICK METRICS */}
      <div className="flex flex-col lg:flex-row lg:items-center justify-between gap-4 border-b border-slate-800 pb-4">
        <div>
          <div className="flex items-center gap-2">
            <span className="p-1.5 rounded-lg bg-cyan-950 text-cyan-400 border border-cyan-800">
              <BarChart3 className="w-4 h-4" />
            </span>
            <h3 className="text-base font-bold text-slate-100">Treasury Portfolio & Historical Balance Analytics</h3>
          </div>
          <p className="text-xs text-slate-400 mt-1">
            Real-time asset allocation breakdown and historical balance trends powered by on-chain reserves and protocol fee sinks.
          </p>
        </div>

        {/* Highlight Badges */}
        <div className="flex flex-wrap items-center gap-2 text-xs">
          <div className="px-3 py-1.5 rounded-xl bg-slate-900 border border-slate-800 flex items-center gap-1.5">
            <span className="w-2 h-2 rounded-full bg-emerald-400 animate-pulse" />
            <span className="text-slate-400">Total Reserve:</span>
            <span className="font-bold text-slate-100 font-mono">${allocation.totalUsd.toLocaleString()}</span>
          </div>
          <div className="px-3 py-1.5 rounded-xl bg-slate-900 border border-slate-800 flex items-center gap-1.5">
            <span className="text-slate-400">Stablecoin Buffer:</span>
            <span className="font-bold text-emerald-400 font-mono">{allocation.stablecoinSharePct}%</span>
          </div>
          <div className="px-3 py-1.5 rounded-xl bg-slate-900 border border-slate-800 flex items-center gap-1.5">
            <span className="text-slate-400">Growth ({timeframe}):</span>
            <span className={`font-bold font-mono flex items-center ${metrics.percentageChange >= 0 ? 'text-emerald-400' : 'text-red-400'}`}>
              <ArrowUpRight className="w-3 h-3 mr-0.5" />
              {metrics.percentageChange >= 0 ? '+' : ''}{metrics.percentageChange}%
            </span>
          </div>
        </div>
      </div>

      {/* TOP ROW: ASSET ALLOCATION DONUT & BREAKDOWN LIST */}
      <div className="grid grid-cols-1 lg:grid-cols-12 gap-6">
        {/* Left: Recharts Donut Chart */}
        <div className="lg:col-span-5 rounded-2xl bg-slate-900/90 border border-slate-800 p-5 flex flex-col justify-between">
          <div className="flex items-center justify-between border-b border-slate-800/80 pb-3">
            <div className="flex items-center gap-2">
              <PieIcon className="w-4 h-4 text-cyan-400" />
              <h4 className="text-sm font-bold text-slate-200">Asset Allocation Breakdown</h4>
            </div>
            <span className="text-[11px] text-slate-400 font-mono">
              {allocation.items.length} Tracked Assets
            </span>
          </div>

          {/* Recharts PieChart */}
          <div className="relative w-full h-64 flex items-center justify-center my-2">
            <ResponsiveContainer width="100%" height="100%">
              <PieChart>
                <Pie
                  data={allocation.items}
                  dataKey="usdValueNum"
                  nameKey="symbol"
                  cx="50%"
                  cy="50%"
                  innerRadius={65}
                  outerRadius={95}
                  paddingAngle={3}
                  onMouseEnter={(_, index) => setHoveredSlice(allocation.items[index])}
                  onMouseLeave={() => setHoveredSlice(null)}
                  onClick={(_, index) => {
                    const item = allocation.items[index];
                    if (!item) return;
                    if (selectedAssetSymbol === item.symbol && viewMode === 'single') {
                      setSelectedAssetSymbol(null);
                      setViewMode('stacked');
                    } else {
                      setSelectedAssetSymbol(item.symbol);
                      setViewMode('single');
                    }
                  }}
                  cursor="pointer"
                >
                  {allocation.items.map((entry) => (
                    <Cell
                      key={`cell-${entry.symbol}`}
                      fill={entry.color}
                      stroke={selectedAssetSymbol === entry.symbol ? '#ffffff' : '#0f172a'}
                      strokeWidth={selectedAssetSymbol === entry.symbol ? 2 : 1}
                    />
                  ))}
                </Pie>
                <RechartsTooltip
                  content={({ active, payload }) => {
                    if (active && payload && payload.length) {
                      const data = payload[0].payload as TreasuryAllocationItem;
                      return (
                        <div className="rounded-xl bg-slate-950/95 border border-slate-700 p-3 shadow-xl text-xs space-y-1">
                          <div className="flex items-center gap-2 font-bold text-slate-200">
                            <span className="w-2.5 h-2.5 rounded-full" style={{ backgroundColor: data.color }} />
                            <span>{data.name} ({data.symbol})</span>
                          </div>
                          <div className="text-slate-400">Balance: <strong className="text-slate-200 font-mono">{data.balance}</strong></div>
                          <div className="text-slate-400">Valuation: <strong className="text-emerald-400 font-mono">{data.usdValueFormatted}</strong></div>
                          <div className="text-slate-400">Share: <strong className="text-cyan-400 font-mono">{data.percentage}%</strong></div>
                        </div>
                      );
                    }
                    return null;
                  }}
                />
              </PieChart>
            </ResponsiveContainer>

            {/* Donut Center Display */}
            <div className="absolute inset-0 flex flex-col items-center justify-center pointer-events-none">
              <span className="text-[10px] uppercase font-semibold text-slate-400 tracking-wider">
                {hoveredSlice ? hoveredSlice.symbol : 'Total Reserve'}
              </span>
              <span className="text-lg font-black text-slate-100 font-mono">
                {hoveredSlice
                  ? hoveredSlice.usdValueFormatted
                  : formatCurrency(allocation.totalUsd)}
              </span>
              <span className="text-[11px] font-mono text-cyan-400 font-semibold">
                {hoveredSlice
                  ? `${hoveredSlice.percentage}% of total`
                  : `${allocation.items.length} reserve assets`}
              </span>
            </div>
          </div>

          {/* Donut Footer Info */}
          <div className="pt-3 border-t border-slate-800/80 flex items-center justify-between text-xs text-slate-400">
            <span>Click any slice to focus trend</span>
            {selectedAssetSymbol && (
              <button
                onClick={() => {
                  setSelectedAssetSymbol(null);
                  setViewMode('stacked');
                }}
                className="text-cyan-400 hover:underline text-[11px]"
              >
                Reset Focus
              </button>
            )}
          </div>
        </div>

        {/* Right: Allocation Detailed Asset List */}
        <div className="lg:col-span-7 rounded-2xl bg-slate-900/90 border border-slate-800 p-5 flex flex-col justify-between">
          <div>
            <div className="flex flex-wrap items-center justify-between gap-2 border-b border-slate-800/80 pb-3">
              <div className="flex items-center gap-2">
                <Layers className="w-4 h-4 text-teal-400" />
                <h4 className="text-sm font-bold text-slate-200">Reserve Allocation Breakdown</h4>
              </div>

              {/* Category Filter Pills */}
              <div className="flex items-center gap-1 bg-slate-950 p-1 rounded-xl border border-slate-800 text-[11px]">
                <button
                  onClick={() => setCategoryFilter('ALL')}
                  className={`px-2.5 py-1 rounded-lg font-medium transition ${
                    categoryFilter === 'ALL'
                      ? 'bg-slate-800 text-cyan-400 font-bold'
                      : 'text-slate-400 hover:text-slate-200'
                  }`}
                  aria-label="Show all assets in breakdown"
                >
                  All ({allocation.items.length})
                </button>
                <button
                  onClick={() => setCategoryFilter('STABLES')}
                  className={`px-2.5 py-1 rounded-lg font-medium transition ${
                    categoryFilter === 'STABLES'
                      ? 'bg-slate-800 text-emerald-400 font-bold'
                      : 'text-slate-400 hover:text-slate-200'
                  }`}
                  aria-label="Filter stablecoins"
                >
                  Stablecoins
                </button>
                <button
                  onClick={() => setCategoryFilter('VOLATILE')}
                  className={`px-2.5 py-1 rounded-lg font-medium transition ${
                    categoryFilter === 'VOLATILE'
                      ? 'bg-slate-800 text-purple-400 font-bold'
                      : 'text-slate-400 hover:text-slate-200'
                  }`}
                  aria-label="Filter crypto & native assets"
                >
                  Native & Volatile
                </button>
              </div>
            </div>

            {/* List of Assets with Percentage Bars */}
            <div className="mt-3 space-y-2.5">
              {displayAllocationItems.map((item) => {
                const isSelected = selectedAssetSymbol === item.symbol;
                return (
                  <div
                    key={item.symbol}
                    onClick={() => {
                      if (isSelected && viewMode === 'single') {
                        setSelectedAssetSymbol(null);
                        setViewMode('stacked');
                      } else {
                        setSelectedAssetSymbol(item.symbol);
                        setViewMode('single');
                      }
                    }}
                    className={`p-3 rounded-xl border transition cursor-pointer flex flex-col sm:flex-row sm:items-center justify-between gap-2 ${
                      isSelected
                        ? 'bg-slate-800/90 border-cyan-500 shadow-md'
                        : 'bg-slate-950/60 border-slate-800/80 hover:border-slate-700'
                    }`}
                  >
                    <div className="flex items-center gap-3">
                      <span
                        className="w-3 h-3 rounded-full shrink-0 shadow-sm"
                        style={{ backgroundColor: item.color }}
                      />
                      <div>
                        <div className="flex items-center gap-2">
                          <span className="text-xs font-bold text-slate-100">{item.symbol}</span>
                          <span className="text-[11px] text-slate-400">{item.name}</span>
                          {item.symbol === 'NGTT' && (
                            <span className="px-1.5 py-0.2 rounded text-[9px] bg-cyan-950 text-cyan-300 border border-cyan-800">
                              Governance
                            </span>
                          )}
                          {item.symbol === 'ETH' && (
                            <span className="px-1.5 py-0.2 rounded text-[9px] bg-indigo-950 text-indigo-300 border border-indigo-800">
                              L1 Collateral
                            </span>
                          )}
                        </div>
                        <div className="text-[11px] text-slate-400 font-mono mt-0.5">
                          Balance: <strong className="text-slate-300">{item.balance}</strong>
                        </div>
                      </div>
                    </div>

                    <div className="text-right flex sm:flex-col items-center sm:items-end justify-between sm:justify-center">
                      <div className="text-xs font-bold text-emerald-400 font-mono">
                        {item.usdValueFormatted}
                      </div>
                      <div className="flex items-center gap-2 mt-0.5">
                        <div className="w-24 sm:w-28 bg-slate-800 h-1.5 rounded-full overflow-hidden">
                          <div
                            className="h-full rounded-full"
                            style={{
                              width: `${Math.min(100, item.percentage)}%`,
                              backgroundColor: item.color,
                            }}
                          />
                        </div>
                        <span className="text-[11px] font-mono text-slate-300 font-semibold w-10 text-right">
                          {item.percentage}%
                        </span>
                      </div>
                    </div>
                  </div>
                );
              })}
            </div>
          </div>

          <div className="mt-3 pt-3 border-t border-slate-800/80 text-[11px] text-slate-400 flex items-center justify-between">
            <span>Click asset row to inspect single-asset historical trajectory</span>
            <span className="font-mono text-cyan-400">Dual Timelock Protected</span>
          </div>
        </div>
      </div>

      {/* BOTTOM ROW: HISTORICAL BALANCE TRENDS (RECHARTS AREA & COMPOSED CHART) */}
      <div className="rounded-2xl bg-slate-900/90 border border-slate-800 p-5 space-y-4">
        {/* Controls Bar */}
        <div className="flex flex-col md:flex-row md:items-center justify-between gap-4 border-b border-slate-800 pb-4">
          <div>
            <div className="flex items-center gap-2">
              <TrendingUp className="w-4 h-4 text-emerald-400" />
              <h4 className="text-sm font-bold text-slate-200">Historical Reserve Balance Trends</h4>
            </div>
            <p className="text-xs text-slate-400 mt-0.5">
              Cumulative balance valuation and multi-asset composition tracking over selected historical epochs.
            </p>
          </div>

          <div className="flex flex-wrap items-center gap-2">
            {/* View Mode Switcher */}
            <div className="flex items-center bg-slate-950 p-1 rounded-xl border border-slate-800 text-xs">
              <button
                onClick={() => setViewMode('stacked')}
                className={`px-3 py-1.5 rounded-lg font-medium transition ${
                  viewMode === 'stacked'
                    ? 'bg-slate-800 text-cyan-400 font-bold'
                    : 'text-slate-400 hover:text-slate-200'
                }`}
                aria-label="View stacked multi-asset composition chart"
              >
                Stacked Composition
              </button>
              <button
                onClick={() => setViewMode('total')}
                className={`px-3 py-1.5 rounded-lg font-medium transition ${
                  viewMode === 'total'
                    ? 'bg-slate-800 text-emerald-400 font-bold'
                    : 'text-slate-400 hover:text-slate-200'
                }`}
                aria-label="View total valuation line chart"
              >
                Total Valuation
              </button>
              <button
                onClick={() => setViewMode('single')}
                className={`px-3 py-1.5 rounded-lg font-medium transition ${
                  viewMode === 'single'
                    ? 'bg-slate-800 text-purple-400 font-bold'
                    : 'text-slate-400 hover:text-slate-200'
                }`}
                aria-label="View single asset focus chart"
              >
                Single Asset ({activeFocusSymbol})
              </button>
            </div>

            {/* Timeframe Selector */}
            <div className="flex items-center bg-slate-950 p-1 rounded-xl border border-slate-800 text-xs font-mono">
              {(['7D', '30D', '90D', '1Y', 'ALL'] as TreasuryTimeframe[]).map((tf) => (
                <button
                  key={tf}
                  onClick={() => setTimeframe(tf)}
                  className={`px-2.5 py-1.5 rounded-lg font-semibold transition ${
                    timeframe === tf
                      ? 'bg-cyan-950 text-cyan-300 border border-cyan-800/80 shadow-sm'
                      : 'text-slate-400 hover:text-slate-200'
                  }`}
                  aria-label={`Select ${tf} historical timeframe`}
                >
                  {tf}
                </button>
              ))}
            </div>
          </div>
        </div>

        {/* Historical Trend KPI Strip */}
        <div className="grid grid-cols-2 sm:grid-cols-4 gap-3 py-1">
          <div className="p-3 rounded-xl bg-slate-950/80 border border-slate-800/80">
            <span className="text-[10px] uppercase font-bold text-slate-500">Starting Valuation</span>
            <div className="text-sm font-bold text-slate-200 font-mono mt-0.5">
              {formatCurrency(metrics.startUsd)}
            </div>
            <span className="text-[10px] text-slate-500 font-mono">Epoch baseline</span>
          </div>

          <div className="p-3 rounded-xl bg-slate-950/80 border border-slate-800/80">
            <span className="text-[10px] uppercase font-bold text-slate-500">Current Valuation</span>
            <div className="text-sm font-bold text-emerald-400 font-mono mt-0.5">
              {formatCurrency(metrics.currentUsd)}
            </div>
            <span className="text-[10px] text-emerald-500/80 font-mono">
              +{metrics.percentageChange}% change
            </span>
          </div>

          <div className="p-3 rounded-xl bg-slate-950/80 border border-slate-800/80">
            <span className="text-[10px] uppercase font-bold text-slate-500">Peak Reserve High</span>
            <div className="text-sm font-bold text-slate-200 font-mono mt-0.5">
              {formatCurrency(metrics.peakUsd)}
            </div>
            <span className="text-[10px] text-slate-500 font-mono">All-time period max</span>
          </div>

          <div className="p-3 rounded-xl bg-slate-950/80 border border-slate-800/80">
            <span className="text-[10px] uppercase font-bold text-slate-500">Net Growth Rate</span>
            <div className="text-sm font-bold text-cyan-400 font-mono mt-0.5">
              +{formatCurrency(metrics.averageGrowthPerStep)}
            </div>
            <span className="text-[10px] text-slate-500 font-mono">Avg net inflow / step</span>
          </div>
        </div>

        {/* Recharts Area Chart Container */}
        <div className="w-full h-80 pt-2">
          <ResponsiveContainer width="100%" height="100%">
            <AreaChart
              data={historicalData}
              margin={{ top: 10, right: 20, left: 10, bottom: 10 }}
            >
              <defs>
                {/* Linear Gradients for Area Fills */}
                <linearGradient id="colorTotal" x1="0" y1="0" x2="0" y2="1">
                  <stop offset="5%" stopColor="#10b981" stopOpacity={0.4} />
                  <stop offset="95%" stopColor="#10b981" stopOpacity={0.0} />
                </linearGradient>
                <linearGradient id="colorNGTT" x1="0" y1="0" x2="0" y2="1">
                  <stop offset="5%" stopColor="#06b6d4" stopOpacity={0.6} />
                  <stop offset="95%" stopColor="#06b6d4" stopOpacity={0.05} />
                </linearGradient>
                <linearGradient id="colorETH" x1="0" y1="0" x2="0" y2="1">
                  <stop offset="5%" stopColor="#6366f1" stopOpacity={0.6} />
                  <stop offset="95%" stopColor="#6366f1" stopOpacity={0.05} />
                </linearGradient>
                <linearGradient id="colorUSDC" x1="0" y1="0" x2="0" y2="1">
                  <stop offset="5%" stopColor="#10b981" stopOpacity={0.6} />
                  <stop offset="95%" stopColor="#10b981" stopOpacity={0.05} />
                </linearGradient>
                <linearGradient id="colorUSDT" x1="0" y1="0" x2="0" y2="1">
                  <stop offset="5%" stopColor="#14b8a6" stopOpacity={0.6} />
                  <stop offset="95%" stopColor="#14b8a6" stopOpacity={0.05} />
                </linearGradient>
                <linearGradient id="colorWETH" x1="0" y1="0" x2="0" y2="1">
                  <stop offset="5%" stopColor="#8b5cf6" stopOpacity={0.6} />
                  <stop offset="95%" stopColor="#8b5cf6" stopOpacity={0.05} />
                </linearGradient>
                <linearGradient id="colorDAI" x1="0" y1="0" x2="0" y2="1">
                  <stop offset="5%" stopColor="#f59e0b" stopOpacity={0.6} />
                  <stop offset="95%" stopColor="#f59e0b" stopOpacity={0.05} />
                </linearGradient>
              </defs>

              <CartesianGrid strokeDasharray="3 3" stroke="#1e293b" vertical={false} />

              <XAxis
                dataKey="label"
                stroke="#64748b"
                tick={{ fill: '#94a3b8', fontSize: 11 }}
                tickLine={{ stroke: '#334155' }}
              />

              <YAxis
                stroke="#64748b"
                tick={{ fill: '#94a3b8', fontSize: 11 }}
                tickLine={{ stroke: '#334155' }}
                tickFormatter={formatCurrency}
                width={65}
              />

              <RechartsTooltip
                content={({ active, payload, label }) => {
                  if (active && payload && payload.length) {
                    const point = payload[0].payload;
                    return (
                      <div className="rounded-xl bg-slate-950/95 border border-slate-700 p-3 shadow-2xl text-xs space-y-2 min-w-[200px]">
                        <div className="flex items-center justify-between border-b border-slate-800 pb-1.5 font-bold text-slate-200">
                          <span>{label}</span>
                          <span className="text-[10px] text-slate-400 font-mono">{point.date}</span>
                        </div>

                        <div className="space-y-1">
                          <div className="flex items-center justify-between text-slate-300">
                            <span className="font-semibold">Total Reserve:</span>
                            <span className="font-mono font-bold text-emerald-400">
                              ${point.totalUsd.toLocaleString()}
                            </span>
                          </div>

                          <div className="flex items-center justify-between text-slate-400 text-[11px]">
                            <span>Net Flow:</span>
                            <span className={`font-mono ${point.netInflowUsd >= 0 ? 'text-cyan-400' : 'text-amber-400'}`}>
                              {point.netInflowUsd >= 0 ? '+' : ''}${point.netInflowUsd.toLocaleString()}
                            </span>
                          </div>
                        </div>

                        {/* Breakdown in tooltip if stacked */}
                        {viewMode === 'stacked' && (
                          <div className="pt-1.5 border-t border-slate-800/80 space-y-1">
                            {allocation.items.map((item) => (
                              <div key={item.symbol} className="flex items-center justify-between text-[11px]">
                                <span className="flex items-center gap-1.5 text-slate-400">
                                  <span className="w-2 h-2 rounded-full" style={{ backgroundColor: item.color }} />
                                  <span>{item.symbol}</span>
                                </span>
                                <span className="font-mono text-slate-200">
                                  ${Number(point[item.symbol] || 0).toLocaleString()}
                                </span>
                              </div>
                            ))}
                          </div>
                        )}

                        {viewMode === 'single' && (
                          <div className="pt-1 border-t border-slate-800 text-[11px] flex justify-between">
                            <span className="text-slate-400">{activeFocusSymbol} Valuation:</span>
                            <span className="font-mono font-bold text-cyan-400">
                              ${Number(point[activeFocusSymbol] || 0).toLocaleString()}
                            </span>
                          </div>
                        )}
                      </div>
                    );
                  }
                  return null;
                }}
              />

              <Legend
                wrapperStyle={{ paddingTop: '10px', fontSize: '11px', color: '#94a3b8' }}
              />

              {/* View Mode 1: Stacked Multi-Asset Composition */}
              {viewMode === 'stacked' && (
                <>
                  <Area
                    type="monotone"
                    dataKey="NGTT"
                    stackId="1"
                    stroke="#06b6d4"
                    fill="url(#colorNGTT)"
                    name="NGTT (Governance)"
                  />
                  <Area
                    type="monotone"
                    dataKey="ETH"
                    stackId="1"
                    stroke="#6366f1"
                    fill="url(#colorETH)"
                    name="ETH (Native)"
                  />
                  <Area
                    type="monotone"
                    dataKey="USDC"
                    stackId="1"
                    stroke="#10b981"
                    fill="url(#colorUSDC)"
                    name="USDC (Circle)"
                  />
                  <Area
                    type="monotone"
                    dataKey="USDT"
                    stackId="1"
                    stroke="#14b8a6"
                    fill="url(#colorUSDT)"
                    name="USDT (Tether)"
                  />
                  <Area
                    type="monotone"
                    dataKey="WETH"
                    stackId="1"
                    stroke="#8b5cf6"
                    fill="url(#colorWETH)"
                    name="WETH (DeFi)"
                  />
                  <Area
                    type="monotone"
                    dataKey="DAI"
                    stackId="1"
                    stroke="#f59e0b"
                    fill="url(#colorDAI)"
                    name="DAI (Maker)"
                  />
                </>
              )}

              {/* View Mode 2: Total Valuation Curve */}
              {viewMode === 'total' && (
                <Area
                  type="monotone"
                  dataKey="totalUsd"
                  stroke="#10b981"
                  strokeWidth={2.5}
                  fill="url(#colorTotal)"
                  name="Total Treasury USD Valuation"
                />
              )}

              {/* View Mode 3: Single Asset Focus */}
              {viewMode === 'single' && (
                <Area
                  type="monotone"
                  dataKey={activeFocusSymbol}
                  stroke={activeFocusItem.color}
                  strokeWidth={2.5}
                  fill={`url(#color${activeFocusSymbol})`}
                  name={`${activeFocusSymbol} Reserve Valuation`}
                />
              )}
            </AreaChart>
          </ResponsiveContainer>
        </div>

        {/* Footer info & protocol notice */}
        <div className="pt-2 border-t border-slate-800/80 flex flex-col sm:flex-row sm:items-center justify-between gap-2 text-xs text-slate-500">
          <div className="flex items-center gap-2">
            <span className="w-1.5 h-1.5 rounded-full bg-cyan-400" />
            <span>NexusDAOTreasury: Continuous on-chain balance snapshots with Timelock synchronization</span>
          </div>
          <div className="font-mono text-[11px] text-slate-400">
            Latest Snapshot Block: <strong className="text-slate-300">#21,175,005</strong>
          </div>
        </div>
      </div>
    </div>
  );
};
