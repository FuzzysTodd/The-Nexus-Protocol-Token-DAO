/**
 * @license
 * SPDX-License-Identifier: Apache-2.0
 * The Nexus Protocol DAO - Forex Automation & Fiat Trader Command Center
 */

import React, { useState } from 'react';
import { useNexusDao } from '../context/NexusDaoContext';
import { ForexPair } from '../dao/logic';
import {
  DollarSign,
  TrendingUp,
  ArrowRightLeft,
  Bot,
  Zap,
  Globe,
  CheckCircle2,
  AlertCircle,
  PlayCircle,
  PauseCircle,
  ShieldCheck,
  RefreshCw,
  ExternalLink,
} from 'lucide-react';

export const ForexFiatTrader: React.FC = () => {
  const {
    forexPairs,
    forexBots,
    forexTrades,
    executeForexTrade,
    toggleForexBot,
    runForexBotCycle,
    operatorRole,
  } = useNexusDao();

  const [selectedPairSymbol, setSelectedPairSymbol] = useState<string>('EURC/USDC');
  const [tradeSide, setTradeSide] = useState<'BUY' | 'SELL'>('BUY');
  const [tradeAmount, setTradeAmount] = useState<string>('10000');
  const [lastExecutedTradeId, setLastExecutedTradeId] = useState<string | null>(null);

  const selectedPair = forexPairs.find((p) => p.symbol === selectedPairSymbol) || forexPairs[0];

  const parsedAmount = parseFloat(tradeAmount) || 0;
  const activeRate = tradeSide === 'BUY' ? selectedPair.ask : selectedPair.bid;
  const estimatedTotalUsd = parsedAmount * activeRate;
  const estimatedFeeUsd = estimatedTotalUsd * (selectedPair.spreadBps / 10000);

  const handleExecuteTrade = (e: React.FormEvent) => {
    e.preventDefault();
    if (parsedAmount <= 0) return;
    const trade = executeForexTrade(selectedPair.symbol, tradeSide, parsedAmount);
    setLastExecutedTradeId(trade.id);
  };

  const totalBotProfit = forexBots.reduce((sum, b) => sum + b.profitUsd, 0);
  const totalBotTrades = forexBots.reduce((sum, b) => sum + b.totalTrades, 0);

  return (
    <div className="space-y-6" data-testid="forex-fiat-trader-view">
      {/* Hero Banner */}
      <div className="rounded-2xl bg-gradient-to-r from-slate-900 via-emerald-950/30 to-slate-900 border border-slate-800 p-6 shadow-xl">
        <div className="flex flex-col lg:flex-row lg:items-center justify-between gap-4">
          <div>
            <div className="flex items-center gap-2">
              <span className="px-2.5 py-0.5 rounded-full text-xs font-semibold bg-emerald-500/20 text-emerald-400 border border-emerald-500/40 flex items-center gap-1.5">
                <Globe className="w-3.5 h-3.5" />
                Autonomous FX & Fiat Engine
              </span>
              <span className="text-xs text-slate-500 font-mono">Circle Mint FX Rails & Uniswap v3 EURC</span>
            </div>
            <h2 className="text-xl font-bold text-slate-100 mt-1">
              Forex Automation & Fiat Trader Terminal
            </h2>
            <p className="text-xs text-slate-400 max-w-2xl mt-1">
              Institutional-grade automated foreign exchange, cross-currency triangular arbitrage, and synthetic fiat settlement powered by Circle Mint, Synthetix sFX, and Chainlink oracle feeds.
            </p>
          </div>

          <div className="flex flex-wrap items-center gap-3">
            <div className="px-3.5 py-2 rounded-xl bg-slate-950/80 border border-slate-800 text-left">
              <div className="text-[10px] uppercase font-bold text-slate-500">24h FX Volume</div>
              <div className="text-sm font-bold text-slate-100 font-mono mt-0.5">
                $88,700,000 USD
              </div>
            </div>
            <div className="px-3.5 py-2 rounded-xl bg-slate-950/80 border border-slate-800 text-left">
              <div className="text-[10px] uppercase font-bold text-slate-500">Bot Fleet Net Profit</div>
              <div className="text-sm font-bold text-emerald-400 font-mono mt-0.5">
                +${totalBotProfit.toLocaleString()} USD
              </div>
            </div>
          </div>
        </div>

        {/* Live Currency Ticker */}
        <div className="grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-6 gap-2.5 mt-5 pt-4 border-t border-slate-800/80">
          {forexPairs.map((p) => {
            const isSelected = p.symbol === selectedPairSymbol;
            return (
              <div
                key={p.symbol}
                onClick={() => setSelectedPairSymbol(p.symbol)}
                className={`p-3 rounded-xl border transition cursor-pointer ${
                  isSelected
                    ? 'bg-slate-800/90 border-cyan-400 shadow-md'
                    : 'bg-slate-950/60 border-slate-800/80 hover:border-slate-700'
                }`}
              >
                <div className="flex items-center justify-between">
                  <span className="text-xs font-bold text-slate-200">{p.symbol}</span>
                  <span
                    className={`text-[10px] font-mono font-bold ${
                      p.change24h >= 0 ? 'text-emerald-400' : 'text-red-400'
                    }`}
                  >
                    {p.change24h >= 0 ? '+' : ''}{p.change24h}%
                  </span>
                </div>
                <div className="text-sm font-mono font-bold text-slate-100 mt-1">
                  {p.bid.toFixed(p.symbol.includes('JPY') ? 2 : 4)}
                </div>
                <div className="text-[10px] text-slate-400 font-mono flex items-center justify-between mt-0.5">
                  <span>Spread: {p.spreadBps} bps</span>
                  <span className="text-cyan-400">{p.base}</span>
                </div>
              </div>
            );
          })}
        </div>
      </div>

      {/* Main Grid: FX Trade Terminal & Bots Fleet */}
      <div className="grid grid-cols-1 lg:grid-cols-12 gap-6">
        {/* Left: Interactive Trade Terminal */}
        <div className="lg:col-span-5 rounded-2xl bg-slate-900/90 border border-slate-800 p-5 space-y-4">
          <div className="flex items-center justify-between border-b border-slate-800 pb-3">
            <div className="flex items-center gap-2">
              <ArrowRightLeft className="w-4 h-4 text-cyan-400" />
              <h3 className="text-sm font-bold text-slate-200">Fiat Currency Swap Terminal</h3>
            </div>
            <span className="text-xs font-mono text-emerald-400 font-semibold flex items-center gap-1">
              <span className="w-1.5 h-1.5 rounded-full bg-emerald-400 animate-pulse" />
              {selectedPair.onchainRail}
            </span>
          </div>

          <form onSubmit={handleExecuteTrade} className="space-y-4">
            {/* Pair Selector */}
            <div>
              <label className="block text-xs font-semibold text-slate-300 mb-1">Trading Pair</label>
              <select
                value={selectedPairSymbol}
                onChange={(e) => setSelectedPairSymbol(e.target.value)}
                className="w-full px-3 py-2 rounded-xl bg-slate-950 border border-slate-800 text-xs font-mono text-slate-200 focus:border-cyan-500 focus:outline-none"
              >
                {forexPairs.map((p) => (
                  <option key={p.symbol} value={p.symbol}>
                    {p.symbol} (Bid: {p.bid} / Ask: {p.ask}) - {p.syntheticPool}
                  </option>
                ))}
              </select>
            </div>

            {/* Side Tabs */}
            <div className="grid grid-cols-2 gap-2 p-1 rounded-xl bg-slate-950 border border-slate-800 text-xs font-bold">
              <button
                type="button"
                onClick={() => setTradeSide('BUY')}
                className={`py-2 rounded-lg transition ${
                  tradeSide === 'BUY'
                    ? 'bg-emerald-600 text-white shadow-md'
                    : 'text-slate-400 hover:text-slate-200'
                }`}
              >
                BUY {selectedPair.base}
              </button>
              <button
                type="button"
                onClick={() => setTradeSide('SELL')}
                className={`py-2 rounded-lg transition ${
                  tradeSide === 'SELL'
                    ? 'bg-red-600 text-white shadow-md'
                    : 'text-slate-400 hover:text-slate-200'
                }`}
              >
                SELL {selectedPair.base}
              </button>
            </div>

            {/* Amount Input */}
            <div>
              <div className="flex items-center justify-between text-xs mb-1">
                <label className="font-semibold text-slate-300">Amount ({selectedPair.base})</label>
                <span className="text-slate-500 font-mono">Min: 100 {selectedPair.base}</span>
              </div>
              <div className="relative">
                <input
                  type="number"
                  step="any"
                  value={tradeAmount}
                  onChange={(e) => setTradeAmount(e.target.value)}
                  placeholder="e.g. 10000"
                  className="w-full px-3 py-2 rounded-xl bg-slate-950 border border-slate-800 text-xs font-mono text-slate-100 focus:border-cyan-500 focus:outline-none pr-16"
                  required
                />
                <button
                  type="button"
                  onClick={() => setTradeAmount('50000')}
                  className="absolute right-2 top-1.5 px-2 py-0.5 rounded text-[10px] font-bold bg-slate-800 text-cyan-400 hover:bg-slate-700"
                >
                  50k
                </button>
              </div>
            </div>

            {/* Order Execution Details */}
            <div className="p-3 rounded-xl bg-slate-950/80 border border-slate-800/80 space-y-1.5 text-xs font-mono">
              <div className="flex items-center justify-between text-slate-400">
                <span>Execution Rate:</span>
                <span className="text-slate-200 font-bold">{activeRate.toFixed(4)} USD</span>
              </div>
              <div className="flex items-center justify-between text-slate-400">
                <span>Est. Total Settlement:</span>
                <span className="text-emerald-400 font-bold">${estimatedTotalUsd.toLocaleString(undefined, { minimumFractionDigits: 2 })} USD</span>
              </div>
              <div className="flex items-center justify-between text-slate-400">
                <span>Protocol Spread Fee:</span>
                <span className="text-slate-300">${estimatedFeeUsd.toFixed(2)} ({selectedPair.spreadBps} bps)</span>
              </div>
              <div className="flex items-center justify-between text-slate-400">
                <span>Settlement Rail:</span>
                <span className="text-cyan-400">{selectedPair.onchainRail}</span>
              </div>
            </div>

            <button
              type="submit"
              className={`w-full py-2.5 rounded-xl font-bold text-xs shadow-lg transition flex items-center justify-center gap-2 ${
                tradeSide === 'BUY'
                  ? 'bg-gradient-to-r from-emerald-600 to-teal-600 hover:from-emerald-500 hover:to-teal-500 text-white'
                  : 'bg-gradient-to-r from-red-600 to-rose-600 hover:from-red-500 hover:to-rose-500 text-white'
              }`}
            >
              <Zap className="w-4 h-4 fill-current" />
              Execute {tradeSide} {parsedAmount.toLocaleString()} {selectedPair.base}
            </button>
          </form>

          {lastExecutedTradeId && (
            <div className="p-2.5 rounded-xl bg-emerald-950/60 border border-emerald-800/80 text-xs text-emerald-300 flex items-center justify-between">
              <span className="flex items-center gap-1.5">
                <CheckCircle2 className="w-4 h-4 text-emerald-400" />
                Trade #{lastExecutedTradeId} Settled On-Chain!
              </span>
              <span className="font-mono text-[10px] text-emerald-400">Block #21,175,005</span>
            </div>
          )}
        </div>

        {/* Right: Automated Forex Bots & Triangular Arbitrage Fleet */}
        <div className="lg:col-span-7 rounded-2xl bg-slate-900/90 border border-slate-800 p-5 space-y-4">
          <div className="flex flex-wrap items-center justify-between gap-2 border-b border-slate-800 pb-3">
            <div className="flex items-center gap-2">
              <Bot className="w-4 h-4 text-amber-400" />
              <h3 className="text-sm font-bold text-slate-200">
                Autonomous Forex & Arbitrage Bot Fleet ({forexBots.length})
              </h3>
            </div>
            <div className="flex items-center gap-2 text-xs font-mono text-slate-400">
              <span>Total Bot Trades: <strong className="text-cyan-300">{totalBotTrades}</strong></span>
              <span>•</span>
              <span>Cumulative Profit: <strong className="text-emerald-400">+${totalBotProfit.toLocaleString()}</strong></span>
            </div>
          </div>

          <div className="space-y-3">
            {forexBots.map((bot) => (
              <div
                key={bot.id}
                className="p-4 rounded-xl bg-slate-950 border border-slate-800 space-y-2.5 hover:border-slate-700 transition"
              >
                <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-2">
                  <div className="flex items-center gap-2.5">
                    <span
                      className={`w-2 h-2 rounded-full ${
                        bot.status === 'ACTIVE' ? 'bg-emerald-400 animate-pulse' : 'bg-amber-400'
                      }`}
                    />
                    <h4 className="text-xs font-bold text-slate-100">{bot.name}</h4>
                    <span className="px-2 py-0.5 rounded text-[10px] font-bold font-mono bg-slate-800 text-cyan-400">
                      {bot.pair}
                    </span>
                    <span className="px-2 py-0.5 rounded text-[10px] font-mono bg-purple-950/80 text-purple-300 border border-purple-800/60">
                      {bot.strategy.replace(/_/g, ' ')}
                    </span>
                  </div>

                  <div className="flex items-center gap-2">
                    <button
                      onClick={() => runForexBotCycle(bot.id)}
                      className="px-2.5 py-1 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 text-xs font-semibold flex items-center gap-1 transition"
                      title="Run manual arbitrage cycle"
                    >
                      <RefreshCw className="w-3 h-3" />
                      Run Cycle
                    </button>
                    <button
                      onClick={() => toggleForexBot(bot.id)}
                      className={`px-3 py-1 rounded-lg text-xs font-bold flex items-center gap-1 transition ${
                        bot.status === 'ACTIVE'
                          ? 'bg-amber-950/80 hover:bg-amber-900 border border-amber-800 text-amber-300'
                          : 'bg-emerald-600 hover:bg-emerald-500 text-white'
                      }`}
                    >
                      {bot.status === 'ACTIVE' ? (
                        <>
                          <PauseCircle className="w-3 h-3" /> Pause
                        </>
                      ) : (
                        <>
                          <PlayCircle className="w-3 h-3" /> Activate
                        </>
                      )}
                    </button>
                  </div>
                </div>

                <div className="grid grid-cols-2 sm:grid-cols-4 gap-2 pt-2 border-t border-slate-900 text-xs font-mono">
                  <div>
                    <span className="text-[10px] text-slate-500 uppercase">Trades Executed</span>
                    <div className="text-slate-200 font-bold">{bot.totalTrades}</div>
                  </div>
                  <div>
                    <span className="text-[10px] text-slate-500 uppercase">Net Yield Generated</span>
                    <div className="text-emerald-400 font-bold">+${bot.profitUsd.toLocaleString()}</div>
                  </div>
                  <div>
                    <span className="text-[10px] text-slate-500 uppercase">Latency</span>
                    <div className="text-cyan-400 font-bold">{bot.executionLatencyMs}ms</div>
                  </div>
                  <div>
                    <span className="text-[10px] text-slate-500 uppercase">Last Execution</span>
                    <div className="text-slate-400 text-[11px] truncate">{bot.lastRun}</div>
                  </div>
                </div>
              </div>
            ))}
          </div>
        </div>
      </div>

      {/* Recent On-Chain FX Executions Log */}
      <div className="rounded-2xl bg-slate-900/90 border border-slate-800 p-5 space-y-3">
        <div className="flex items-center justify-between border-b border-slate-800 pb-3">
          <div className="flex items-center gap-2">
            <ShieldCheck className="w-4 h-4 text-emerald-400" />
            <h3 className="text-sm font-bold text-slate-200">
              Recent On-Chain Forex Executions ({forexTrades.length})
            </h3>
          </div>
          <span className="text-xs text-slate-400 font-mono">
            Zero-slippage Circle Mint & Uniswap v3 FX Settlement
          </span>
        </div>

        <div className="overflow-x-auto">
          <table className="w-full text-xs text-left">
            <thead>
              <tr className="border-b border-slate-800 text-[11px] text-slate-500 uppercase font-mono">
                <th className="py-2.5 px-3">Trade ID / Time</th>
                <th className="py-2.5 px-3">Pair & Side</th>
                <th className="py-2.5 px-3">Base Amount</th>
                <th className="py-2.5 px-3">Execution Rate</th>
                <th className="py-2.5 px-3">Total Settlement</th>
                <th className="py-2.5 px-3">Settlement Rail</th>
                <th className="py-2.5 px-3">Tx Hash</th>
                <th className="py-2.5 px-3 text-right">Status</th>
              </tr>
            </thead>
            <tbody className="divide-y divide-slate-850 font-mono">
              {forexTrades.map((t) => (
                <tr key={t.id} className="hover:bg-slate-950/60 transition">
                  <td className="py-2.5 px-3">
                    <div className="font-bold text-slate-200">{t.id}</div>
                    <div className="text-[10px] text-slate-500">{t.timestamp}</div>
                  </td>
                  <td className="py-2.5 px-3">
                    <span
                      className={`px-2 py-0.5 rounded text-[10px] font-bold ${
                        t.side === 'BUY'
                          ? 'bg-emerald-950 text-emerald-400 border border-emerald-800/60'
                          : 'bg-red-950 text-red-400 border border-red-800/60'
                      }`}
                    >
                      {t.side} {t.pair}
                    </span>
                  </td>
                  <td className="py-2.5 px-3 text-slate-200">{t.amountBase.toLocaleString()}</td>
                  <td className="py-2.5 px-3 text-slate-300">{t.rate}</td>
                  <td className="py-2.5 px-3 text-emerald-400 font-bold">${t.totalUsd.toLocaleString()}</td>
                  <td className="py-2.5 px-3 text-cyan-400">{t.settlementRail}</td>
                  <td className="py-2.5 px-3 text-slate-400 font-mono">{t.txHash}</td>
                  <td className="py-2.5 px-3 text-right">
                    <span className="px-2 py-0.5 rounded text-[10px] font-bold bg-emerald-950 text-emerald-300 border border-emerald-800">
                      {t.status}
                    </span>
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </div>
    </div>
  );
};
