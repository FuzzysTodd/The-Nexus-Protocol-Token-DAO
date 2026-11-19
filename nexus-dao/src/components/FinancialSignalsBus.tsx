/**
 * @license
 * SPDX-License-Identifier: Apache-2.0
 * The Nexus Protocol DAO - Financial Signals Bus & Automated Bot Fleet
 */

import React, { useState, useMemo } from 'react';
import { useNexusDao } from '../context/NexusDaoContext';
import {
  solveSignalDegradation,
  RepairedSignalResult,
  SignalDegradationType,
  SIGNAL_CHANNEL_PRESETS,
  validateSignalBroadcast,
  computeExpectedTransmittal,
  generateSignalProofFuzz,
  ProofFuzzVector,
} from '../dao/logic';
import {
  Activity,
  Radio,
  Zap,
  Cpu,
  RefreshCw,
  CheckCircle2,
  AlertTriangle,
  Play,
  RotateCcw,
  Sparkles,
  Server,
  ArrowRight,
  TrendingUp,
  Sliders,
  Send,
  Terminal,
  ShieldCheck,
  Check,
  Copy,
  ChevronDown,
  ChevronUp,
  Fingerprint,
  Gauge,
  SlidersHorizontal,
} from 'lucide-react';

export const FinancialSignalsBus: React.FC = () => {
  const {
    financialSignals,
    broadcastFinancialSignal,
    botFleet,
    toggleBotStatus,
    triggerBotRun,
  } = useNexusDao();

  // Signal repair solver state
  const [selectedPreset, setSelectedPreset] = useState<string>('spiked');
  const [customSignalInput, setCustomSignalInput] = useState<string>('102.5, 340.0, 99.8, 410.2, 98.4');
  const [expectedMidpoint, setExpectedMidpoint] = useState<number>(100);
  const [solverResult, setSolverResult] = useState<RepairedSignalResult | null>(() => {
    return solveSignalDegradation([102.5, 340.0, 99.8, 410.2, 98.4], [100, 100, 100, 100, 100], 1000);
  });

  // Signal broadcaster form & preset selection
  const [newChannel, setNewChannel] = useState<string>('oracle.price.eth_usd');
  const [newValue, setNewValue] = useState<string>('3150.25');
  const [newUnit, setNewUnit] = useState<string>('USD');
  const [newMetadata, setNewMetadata] = useState<string>('Chainlink v0.8 Aggregator Sync • Mainnet');
  const [broadcastSuccess, setBroadcastSuccess] = useState<boolean>(false);
  const [nonceCounter, setNonceCounter] = useState<number>(1);
  const [showJsonTransmittal, setShowJsonTransmittal] = useState<boolean>(false);
  const [copiedHash, setCopiedHash] = useState<boolean>(false);

  // Proof Fuzzing state
  const [fuzzReport, setFuzzReport] = useState<ReturnType<typeof generateSignalProofFuzz>>(() => {
    return generateSignalProofFuzz('oracle.price.eth_usd', 3150.25);
  });
  const [isFuzzingRunning, setIsFuzzingRunning] = useState<boolean>(false);
  const [showFuzzDetails, setShowFuzzDetails] = useState<boolean>(true);

  // Active Channel Preset
  const activePreset = useMemo(() => {
    return (
      SIGNAL_CHANNEL_PRESETS[newChannel] || {
        channel: newChannel,
        label: newChannel,
        defaultValue: 100,
        unit: 'USD',
        metadata: 'Generic Signal',
        min: 0,
        max: 1000000,
        category: 'oracle' as const,
        description: 'Custom signal channel',
      }
    );
  }, [newChannel]);

  // Handle channel dropdown selection with automatic price preset calibration
  const handleChannelChange = (channelKey: string) => {
    setNewChannel(channelKey);
    const preset = SIGNAL_CHANNEL_PRESETS[channelKey];
    if (preset) {
      setNewValue(preset.defaultValue.toString());
      setNewUnit(preset.unit);
      setNewMetadata(preset.metadata);
      // Run fuzz test against new preset default
      setFuzzReport(generateSignalProofFuzz(channelKey, preset.defaultValue));
    }
  };

  // Quick preset price adjustments
  const applyQuickPriceAdjustment = (type: 'DEFAULT' | 'PLUS_5' | 'MINUS_5' | 'MIN_ENVELOPE' | 'MAX_ENVELOPE') => {
    const base = activePreset.defaultValue;
    let target = base;
    if (type === 'DEFAULT') target = base;
    else if (type === 'PLUS_5') target = Math.round(base * 1.05 * 10000) / 10000;
    else if (type === 'MINUS_5') target = Math.round(base * 0.95 * 10000) / 10000;
    else if (type === 'MIN_ENVELOPE') target = activePreset.min;
    else if (type === 'MAX_ENVELOPE') target = activePreset.max;

    setNewValue(target.toString());
    setFuzzReport(generateSignalProofFuzz(newChannel, target));
  };

  // Run proof fuzz engine on demand
  const handleRunProofFuzz = () => {
    setIsFuzzingRunning(true);
    setTimeout(() => {
      const numVal = parseFloat(newValue);
      const valToFuzz = !isNaN(numVal) && numVal > 0 ? numVal : activePreset.defaultValue;
      const report = generateSignalProofFuzz(newChannel, valToFuzz);
      setFuzzReport(report);
      setIsFuzzingRunning(false);
      setShowFuzzDetails(true);
    }, 300);
  };

  // Inject a specific fuzzed vector directly into the broadcast form
  const handleApplyFuzzVector = (vector: ProofFuzzVector) => {
    setNewValue(vector.fuzzedValue.toString());
  };

  // Real-time validation computation
  const parsedValue = parseFloat(newValue);
  const validation = useMemo(() => {
    return validateSignalBroadcast(newChannel, isNaN(parsedValue) ? NaN : parsedValue);
  }, [newChannel, parsedValue]);

  // Expected transmittal packet preview
  const expectedTransmittal = useMemo(() => {
    return computeExpectedTransmittal(
      newChannel,
      isNaN(parsedValue) ? 0 : parsedValue,
      newUnit,
      newMetadata,
      nonceCounter
    );
  }, [newChannel, parsedValue, newUnit, newMetadata, nonceCounter]);

  const copyTransmittalHash = () => {
    if (navigator.clipboard) {
      navigator.clipboard.writeText(expectedTransmittal.proofHash);
      setCopiedHash(true);
      setTimeout(() => setCopiedHash(false), 2000);
    }
  };

  // Preset handler for 1000-particle solver
  const handlePresetSelect = (preset: string) => {
    setSelectedPreset(preset);
    let values: number[] = [];
    if (preset === 'clean') {
      values = [100.1, 99.8, 100.4, 99.9, 100.2];
    } else if (preset === 'noisy') {
      values = [108.4, 93.2, 111.0, 92.5, 107.1];
    } else if (preset === 'drifted') {
      values = [135.2, 142.0, 138.4, 144.5, 139.8];
    } else if (preset === 'spiked') {
      values = [102.5, 340.0, 99.8, 410.2, 98.4];
    } else if (preset === 'dropped') {
      values = [0.0, 0.0, 99.4, 101.2, 0.0];
    } else if (preset === 'critical') {
      values = [320.0, 12.0, 480.0, 0.0, 290.0];
    }
    setCustomSignalInput(values.join(', '));
    const result = solveSignalDegradation(values, new Array(values.length).fill(expectedMidpoint), 1000);
    setSolverResult(result);
  };

  const runSolver = () => {
    try {
      const parsed = customSignalInput
        .split(',')
        .map((s) => parseFloat(s.trim()))
        .filter((n) => !isNaN(n));
      if (parsed.length === 0) return;
      const expected = new Array(parsed.length).fill(expectedMidpoint);
      const res = solveSignalDegradation(parsed, expected, 1000);
      setSolverResult(res);
    } catch {
      // ignore
    }
  };

  const handleBroadcastRepaired = () => {
    if (!solverResult || solverResult.repairedSignal.length === 0) return;
    const avgRepaired =
      solverResult.repairedSignal.reduce((a, b) => a + b, 0) / solverResult.repairedSignal.length;
    broadcastFinancialSignal(
      'repaired.consensus.1000particle',
      Math.round(avgRepaired * 100) / 100,
      'pts',
      `Classification: ${solverResult.classification} | Confidence: ${Math.round(solverResult.consensusConfidence * 100)}%`
    );
  };

  const handleManualBroadcast = (e: React.FormEvent) => {
    e.preventDefault();
    const val = parseFloat(newValue);
    if (isNaN(val)) return;
    broadcastFinancialSignal(newChannel, val, newUnit, newMetadata);
    setNonceCounter((prev) => prev + 1);
    setBroadcastSuccess(true);
    setTimeout(() => setBroadcastSuccess(false), 3000);
  };

  const getDegradationBadgeColor = (type: SignalDegradationType) => {
    switch (type) {
      case 'CLEAN':
        return 'bg-emerald-950/80 text-emerald-400 border-emerald-500/30';
      case 'NOISY':
        return 'bg-amber-950/80 text-amber-400 border-amber-500/30';
      case 'DRIFTED':
        return 'bg-orange-950/80 text-orange-400 border-orange-500/30';
      case 'SPIKED':
        return 'bg-rose-950/80 text-rose-400 border-rose-500/30';
      case 'DROPPED':
        return 'bg-red-950/80 text-red-400 border-red-500/30';
      case 'CRITICALLY_ILL':
        return 'bg-purple-950/80 text-purple-400 border-purple-500/30';
      default:
        return 'bg-slate-800 text-slate-300 border-slate-700';
    }
  };

  return (
    <div className="space-y-6">
      {/* Top Banner */}
      <div className="bg-gradient-to-r from-slate-900 via-indigo-950/40 to-slate-900 border border-indigo-900/40 rounded-xl p-6">
        <div className="flex flex-col md:flex-row md:items-center justify-between gap-4">
          <div className="space-y-1">
            <div className="inline-flex items-center gap-2 px-2.5 py-1 rounded-full bg-indigo-950 border border-indigo-700/50 text-indigo-400 text-xs font-mono font-medium">
              <Radio className="w-3.5 h-3.5 animate-pulse text-indigo-400" />
              nexus-signal-bus.js :8790
            </div>
            <h1 className="text-2xl font-bold text-white tracking-tight">
              Financial Signals Bus & Bot Fleet
            </h1>
            <p className="text-slate-400 text-sm max-w-2xl">
              Real-time multiplexed event router for Oracle prices, treasury flows, and arbitrage spreads,
              paired with our 1,000-particle consensus signal degradation solver and automated financial agents.
            </p>
          </div>

          <div className="flex items-center gap-3">
            <div className="px-3.5 py-2 rounded-lg bg-slate-900/90 border border-slate-800 text-center">
              <div className="text-[11px] text-slate-400 uppercase font-mono">Signals Active</div>
              <div className="text-lg font-bold text-cyan-400 font-mono">{financialSignals.length}</div>
            </div>
            <div className="px-3.5 py-2 rounded-lg bg-slate-900/90 border border-slate-800 text-center">
              <div className="text-[11px] text-slate-400 uppercase font-mono">Fleet Online</div>
              <div className="text-lg font-bold text-emerald-400 font-mono">
                {botFleet.filter((b) => b.status === 'ONLINE').length}/{botFleet.length}
              </div>
            </div>
          </div>
        </div>
      </div>

      {/* Grid: Live Signal Stream + Enhanced Broadcaster & Transmittal Console */}
      <div className="grid grid-cols-1 xl:grid-cols-12 gap-6">
        {/* Live Signal Stream (5 cols) */}
        <div className="xl:col-span-5 bg-slate-900/80 border border-slate-800 rounded-xl p-5 space-y-4 flex flex-col">
          <div className="flex items-center justify-between">
            <div className="flex items-center gap-2">
              <Activity className="w-5 h-5 text-cyan-400" />
              <h2 className="text-base font-semibold text-slate-100">Live Crypto Signals Stream</h2>
            </div>
            <span className="text-xs font-mono text-emerald-400 flex items-center gap-1.5 bg-emerald-950/60 px-2 py-0.5 rounded border border-emerald-500/20">
              <span className="w-1.5 h-1.5 rounded-full bg-emerald-400 animate-ping" />
              Streaming (Port 8790)
            </span>
          </div>

          <div className="divide-y divide-slate-800/80 flex-1 max-h-[560px] overflow-y-auto pr-1">
            {financialSignals.map((sig) => (
              <div
                key={sig.id}
                className="py-3 flex flex-col sm:flex-row sm:items-center justify-between gap-2 hover:bg-slate-850/50 px-2 rounded-lg transition"
              >
                <div className="space-y-0.5">
                  <div className="flex items-center gap-2">
                    <span className="font-mono text-xs font-semibold text-indigo-300">
                      {sig.channel}
                    </span>
                    <span
                      className={`text-[10px] uppercase font-mono px-1.5 py-0.5 rounded border ${
                        sig.status === 'nominal'
                          ? 'bg-emerald-950/60 text-emerald-400 border-emerald-500/20'
                          : sig.status === 'alert'
                          ? 'bg-rose-950/60 text-rose-400 border-rose-500/20'
                          : 'bg-cyan-950/60 text-cyan-400 border-cyan-500/20'
                      }`}
                    >
                      {sig.status}
                    </span>
                  </div>
                  {sig.metadata && (
                    <div className="text-xs text-slate-400 font-mono">{sig.metadata}</div>
                  )}
                </div>

                <div className="text-right sm:text-right flex items-center sm:flex-col justify-between sm:justify-center gap-2">
                  <div className="text-base font-bold font-mono text-white">
                    {sig.value.toLocaleString()} <span className="text-xs text-slate-400">{sig.unit}</span>
                  </div>
                  <div className="text-[10px] text-slate-500 font-mono">{sig.timestamp}</div>
                </div>
              </div>
            ))}
          </div>
        </div>

        {/* Signal Emitter / Broadcaster & Transmittal / Proof Fuzz Console (7 cols) */}
        <div className="xl:col-span-7 space-y-6">
          {/* Main Broadcast Form Card */}
          <div className="bg-slate-900/80 border border-slate-800 rounded-xl p-5 space-y-4">
            <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-2">
              <div className="flex items-center gap-2">
                <Send className="w-5 h-5 text-indigo-400" />
                <h2 className="text-base font-semibold text-slate-100">Broadcast Signal Engine</h2>
              </div>
              <span className="text-xs font-mono text-indigo-300 bg-indigo-950/70 border border-indigo-700/40 px-2 py-0.5 rounded">
                Calibrated Price Presets & Bounds Checking
              </span>
            </div>

            <p className="text-xs text-slate-400">
              Selecting a channel from the menu automatically configures calibrated baseline prices, expected bounds, and transmittal metadata.
            </p>

            <form onSubmit={handleManualBroadcast} className="space-y-4">
              {/* Channel Dropdown with Calibrated Price Labels */}
              <div>
                <label className="text-[11px] font-mono text-slate-400 uppercase flex items-center justify-between">
                  <span>Channel Protocol Select (Auto-Sets Calibrated Price)</span>
                  <span className="text-cyan-400 text-[10px] font-mono">Category: {activePreset.category.toUpperCase()}</span>
                </label>
                <select
                  value={newChannel}
                  onChange={(e) => handleChannelChange(e.target.value)}
                  className="w-full mt-1.5 bg-slate-950 border border-slate-700 rounded-lg px-3 py-2.5 text-sm text-slate-100 focus:outline-none focus:border-indigo-500 font-mono shadow-inner cursor-pointer"
                >
                  <option value="oracle.price.eth_usd">
                    oracle.price.eth_usd — ETH / USD Spot Oracle ($3,150.25 USD)
                  </option>
                  <option value="oracle.price.btc_usd">
                    oracle.price.btc_usd — BTC / USD Satoshi Index ($88,450.00 USD)
                  </option>
                  <option value="forex.eur_usd.spot">
                    forex.eur_usd.spot — EUR / USD Forex Spot (1.0845 USD)
                  </option>
                  <option value="forex.usd_jpy.spot">
                    forex.usd_jpy.spot — USD / JPY Forex Spot (153.42 JPY)
                  </option>
                  <option value="treasury.flow.inflow">
                    treasury.flow.inflow — Treasury Inflow Velocity ($18,250.00 USD)
                  </option>
                  <option value="treasury.flow.outflow">
                    treasury.flow.outflow — Treasury Outflow Clearing ($25,000.00 USD)
                  </option>
                  <option value="arbitrage.dex_spread">
                    arbitrage.dex_spread — Triangular DEX Spread (14.80 bps)
                  </option>
                  <option value="builder.microfee.logged">
                    builder.microfee.logged — Builder Micro-Fee Royalty (0.0042 ETH)
                  </option>
                  <option value="liquidity.amm.depth">
                    liquidity.amm.depth — AMM Liquidity Depth ($4,250,000.00 USD)
                  </option>
                </select>
                <div className="mt-1 text-[11px] text-slate-500 font-sans">
                  {activePreset.description}
                </div>
              </div>

              {/* Value & Unit with Quick Presets */}
              <div className="space-y-2">
                <div className="grid grid-cols-1 sm:grid-cols-3 gap-3">
                  <div className="sm:col-span-2">
                    <label className="text-[11px] font-mono text-slate-400 uppercase flex items-center justify-between">
                      <span>Broadcast Price / Value</span>
                      <span className="text-[10px] text-slate-500">
                        Calibrated: {activePreset.defaultValue.toLocaleString()} {activePreset.unit}
                      </span>
                    </label>
                    <input
                      type="number"
                      step="any"
                      value={newValue}
                      onChange={(e) => {
                        setNewValue(e.target.value);
                        const n = parseFloat(e.target.value);
                        if (!isNaN(n) && n > 0) {
                          setFuzzReport(generateSignalProofFuzz(newChannel, n));
                        }
                      }}
                      className="w-full mt-1 bg-slate-950 border border-slate-700 rounded-lg px-3 py-2 text-sm text-slate-200 focus:outline-none focus:border-indigo-500 font-mono"
                      required
                    />
                  </div>
                  <div>
                    <label className="text-[11px] font-mono text-slate-400 uppercase">Unit</label>
                    <input
                      type="text"
                      value={newUnit}
                      onChange={(e) => setNewUnit(e.target.value)}
                      className="w-full mt-1 bg-slate-950 border border-slate-700 rounded-lg px-3 py-2 text-sm text-slate-200 focus:outline-none focus:border-indigo-500 font-mono"
                      required
                    />
                  </div>
                </div>

                {/* Quick Calibrated Adjustment Pills */}
                <div className="flex flex-wrap items-center gap-1.5 pt-1">
                  <span className="text-[10px] uppercase font-mono text-slate-500 mr-1">Calibrated Quick Sets:</span>
                  <button
                    type="button"
                    onClick={() => applyQuickPriceAdjustment('DEFAULT')}
                    className="text-[11px] font-mono px-2 py-0.5 rounded bg-indigo-950/70 border border-indigo-700/50 text-indigo-300 hover:bg-indigo-900/60 transition"
                  >
                    Default ({activePreset.defaultValue.toLocaleString()})
                  </button>
                  <button
                    type="button"
                    onClick={() => applyQuickPriceAdjustment('PLUS_5')}
                    className="text-[11px] font-mono px-2 py-0.5 rounded bg-slate-800 hover:bg-slate-700 text-slate-300 transition"
                  >
                    +5% Volatility
                  </button>
                  <button
                    type="button"
                    onClick={() => applyQuickPriceAdjustment('MINUS_5')}
                    className="text-[11px] font-mono px-2 py-0.5 rounded bg-slate-800 hover:bg-slate-700 text-slate-300 transition"
                  >
                    -5% Dip
                  </button>
                  <button
                    type="button"
                    onClick={() => applyQuickPriceAdjustment('MIN_ENVELOPE')}
                    className="text-[11px] font-mono px-2 py-0.5 rounded bg-slate-800 hover:bg-slate-700 text-slate-300 transition"
                  >
                    Min ({activePreset.min.toLocaleString()})
                  </button>
                  <button
                    type="button"
                    onClick={() => applyQuickPriceAdjustment('MAX_ENVELOPE')}
                    className="text-[11px] font-mono px-2 py-0.5 rounded bg-slate-800 hover:bg-slate-700 text-slate-300 transition"
                  >
                    Max ({activePreset.max.toLocaleString()})
                  </button>
                </div>
              </div>

              {/* Real-time Protocol Validation Feedback */}
              <div
                className={`p-3 rounded-lg border text-xs flex items-start gap-2.5 transition ${
                  !validation.isValid
                    ? 'bg-rose-950/70 border-rose-500/40 text-rose-300'
                    : validation.status === 'EXTREME_DEVIATION'
                    ? 'bg-amber-950/70 border-amber-500/40 text-amber-300'
                    : 'bg-emerald-950/70 border-emerald-500/40 text-emerald-300'
                }`}
              >
                {!validation.isValid ? (
                  <AlertTriangle className="w-4 h-4 text-rose-400 mt-0.5 flex-shrink-0" />
                ) : validation.status === 'EXTREME_DEVIATION' ? (
                  <AlertTriangle className="w-4 h-4 text-amber-400 mt-0.5 flex-shrink-0" />
                ) : (
                  <CheckCircle2 className="w-4 h-4 text-emerald-400 mt-0.5 flex-shrink-0" />
                )}
                <div className="space-y-1 flex-1">
                  <div className="flex items-center justify-between font-mono font-semibold">
                    <span>
                      {validation.isValid
                        ? validation.status === 'EXTREME_DEVIATION'
                          ? 'Validation Alert: Outlier Deviation'
                          : 'Validation Passed: Within Protocol Envelope'
                        : 'Validation Failed: Outside Protocol Envelope'}
                    </span>
                    <span className="text-[10px] px-1.5 py-0.5 rounded bg-slate-900/80 border border-slate-700">
                      Deviation: {validation.deviationPercent > 0 ? '+' : ''}
                      {validation.deviationPercent}%
                    </span>
                  </div>
                  <div className="text-[11px] opacity-90">{validation.message}</div>
                  <div className="text-[10px] font-mono text-slate-400 pt-0.5">
                    Calibrated Bound: [{activePreset.min.toLocaleString()} — {activePreset.max.toLocaleString()} {activePreset.unit}]
                  </div>
                </div>
              </div>

              {/* Metadata / Source */}
              <div>
                <label className="text-[11px] font-mono text-slate-400 uppercase">Metadata / Source Verification</label>
                <input
                  type="text"
                  value={newMetadata}
                  onChange={(e) => setNewMetadata(e.target.value)}
                  className="w-full mt-1 bg-slate-950 border border-slate-700 rounded-lg px-3 py-2 text-sm text-slate-200 focus:outline-none focus:border-indigo-500 text-xs font-mono"
                  placeholder="e.g. Chainlink v0.8 Aggregator Sync • Mainnet"
                />
              </div>

              {/* Action Buttons */}
              <div className="flex flex-col sm:flex-row gap-2 pt-1">
                <button
                  type="submit"
                  disabled={!validation.isValid}
                  className={`flex-1 py-2.5 px-4 rounded-lg text-sm font-semibold transition flex items-center justify-center gap-2 shadow-lg ${
                    validation.isValid
                      ? 'bg-indigo-600 hover:bg-indigo-500 text-white shadow-indigo-600/20 cursor-pointer'
                      : 'bg-slate-800 text-slate-500 cursor-not-allowed border border-slate-700'
                  }`}
                >
                  <Zap className="w-4 h-4" />
                  Emit into Signal Bus
                </button>

                <button
                  type="button"
                  onClick={handleRunProofFuzz}
                  disabled={isFuzzingRunning}
                  className="py-2.5 px-4 rounded-lg text-sm font-semibold transition bg-slate-800 hover:bg-slate-700 text-cyan-300 border border-cyan-800/40 flex items-center justify-center gap-2 cursor-pointer"
                >
                  <Sparkles className={`w-4 h-4 text-cyan-400 ${isFuzzingRunning ? 'animate-spin' : ''}`} />
                  {isFuzzingRunning ? 'Fuzzing Bus...' : 'Run Proof Fuzz (7 Vectors)'}
                </button>
              </div>

              {broadcastSuccess && (
                <div className="p-2.5 rounded-lg bg-emerald-950/80 border border-emerald-500/40 text-emerald-400 text-xs flex items-center gap-2 animate-fadeIn">
                  <CheckCircle2 className="w-4 h-4 flex-shrink-0" />
                  <span>Signal successfully broadcasted to decentralized event bus with proof hash {expectedTransmittal.proofHash.slice(0, 16)}...</span>
                </div>
              )}
            </form>
          </div>

          {/* Expected Transmittal Packet Preview */}
          <div className="bg-slate-900/80 border border-slate-800 rounded-xl p-5 space-y-4">
            <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-2">
              <div className="flex items-center gap-2">
                <Fingerprint className="w-5 h-5 text-emerald-400" />
                <h3 className="text-base font-semibold text-slate-100">Expected Transmittal Packet</h3>
              </div>
              <div className="flex items-center gap-2">
                <span
                  className={`text-[10px] font-mono px-2 py-0.5 rounded border uppercase font-bold ${
                    expectedTransmittal.validationStatus === 'PASSED'
                      ? 'bg-emerald-950/70 text-emerald-400 border-emerald-500/30'
                      : expectedTransmittal.validationStatus === 'WARNING'
                      ? 'bg-amber-950/70 text-amber-400 border-amber-500/30'
                      : 'bg-rose-950/70 text-rose-400 border-rose-500/30'
                  }`}
                >
                  Transmittal: {expectedTransmittal.validationStatus} • {expectedTransmittal.fuzzResilienceTier}
                </span>
                <button
                  type="button"
                  onClick={() => setShowJsonTransmittal(!showJsonTransmittal)}
                  className="text-xs text-slate-400 hover:text-slate-200 transition font-mono bg-slate-950 px-2 py-0.5 rounded border border-slate-800"
                >
                  {showJsonTransmittal ? 'Card View' : 'Raw JSON'}
                </button>
              </div>
            </div>

            {showJsonTransmittal ? (
              <div className="bg-slate-950 rounded-lg p-3 border border-slate-800 font-mono text-[11px] text-cyan-300 overflow-x-auto">
                <pre>{JSON.stringify(expectedTransmittal, null, 2)}</pre>
              </div>
            ) : (
              <div className="space-y-3">
                <div className="grid grid-cols-2 sm:grid-cols-4 gap-2.5">
                  <div className="p-2.5 rounded-lg bg-slate-950/70 border border-slate-800/80">
                    <div className="text-[10px] font-mono uppercase text-slate-400">Packet Nonce</div>
                    <div className="text-sm font-bold font-mono text-cyan-300">{expectedTransmittal.packetNonce}</div>
                  </div>
                  <div className="p-2.5 rounded-lg bg-slate-950/70 border border-slate-800/80">
                    <div className="text-[10px] font-mono uppercase text-slate-400">Payload Value</div>
                    <div className="text-sm font-bold font-mono text-white">
                      {expectedTransmittal.formattedValue} <span className="text-xs text-slate-400">{expectedTransmittal.unit}</span>
                    </div>
                  </div>
                  <div className="p-2.5 rounded-lg bg-slate-950/70 border border-slate-800/80">
                    <div className="text-[10px] font-mono uppercase text-slate-400">Est. Latency</div>
                    <div className="text-sm font-bold font-mono text-emerald-400">~{expectedTransmittal.expectedLatencyMs} ms</div>
                  </div>
                  <div className="p-2.5 rounded-lg bg-slate-950/70 border border-slate-800/80">
                    <div className="text-[10px] font-mono uppercase text-slate-400">Network Rail</div>
                    <div className="text-xs font-bold font-mono text-indigo-300 truncate">:8790 Bus</div>
                  </div>
                </div>

                <div className="space-y-1.5 p-3 rounded-lg bg-slate-950/90 border border-slate-800 font-mono text-xs">
                  <div className="flex items-center justify-between text-slate-400 text-[11px]">
                    <span className="flex items-center gap-1.5">
                      <ShieldCheck className="w-3.5 h-3.5 text-cyan-400" />
                      Cryptographic Proof Hash (Keccak256 Simulation)
                    </span>
                    <button
                      type="button"
                      onClick={copyTransmittalHash}
                      className="text-cyan-400 hover:text-cyan-300 flex items-center gap-1 text-[10px] cursor-pointer"
                    >
                      {copiedHash ? <Check className="w-3 h-3 text-emerald-400" /> : <Copy className="w-3 h-3" />}
                      {copiedHash ? 'Copied' : 'Copy Hash'}
                    </button>
                  </div>
                  <div className="text-cyan-300 break-all select-all text-[11px] bg-slate-900/60 p-1.5 rounded border border-slate-800/60">
                    {expectedTransmittal.proofHash}
                  </div>

                  <div className="pt-1.5 flex flex-col sm:flex-row sm:items-center justify-between text-[11px] text-slate-400 gap-1 border-t border-slate-800/60 mt-2">
                    <span className="truncate">
                      Signature Tag: <span className="text-amber-400 font-mono">{expectedTransmittal.signatureProof}</span>
                    </span>
                    <span className="text-slate-500 text-[10px]">
                      Merkle Leaf: {expectedTransmittal.merkleLeaf.slice(0, 14)}...
                    </span>
                  </div>
                </div>
              </div>
            )}
          </div>

          {/* Proof Fuzzing & Stress Engine Card */}
          <div className="bg-slate-900/80 border border-slate-800 rounded-xl p-5 space-y-4">
            <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-2">
              <div className="flex items-center gap-2">
                <Gauge className="w-5 h-5 text-cyan-400" />
                <h3 className="text-base font-semibold text-slate-100">Proof Fuzzing & Boundary Stress Engine</h3>
              </div>
              <div className="flex items-center gap-2">
                <span
                  className={`text-xs font-mono font-bold px-2.5 py-0.5 rounded border ${
                    fuzzReport.resilienceScore >= 85
                      ? 'bg-emerald-950/80 text-emerald-400 border-emerald-500/30'
                      : 'bg-amber-950/80 text-amber-400 border-amber-500/30'
                  }`}
                >
                  {fuzzReport.resilienceScore}% Fuzz Resilience ({fuzzReport.vectors.filter((v) => v.isValid).length}/{fuzzReport.vectors.length} Passed)
                </span>
                <button
                  type="button"
                  onClick={() => setShowFuzzDetails(!showFuzzDetails)}
                  className="p-1 rounded text-slate-400 hover:text-white"
                >
                  {showFuzzDetails ? <ChevronUp className="w-4 h-4" /> : <ChevronDown className="w-4 h-4" />}
                </button>
              </div>
            </div>

            <p className="text-xs text-slate-400">
              {fuzzReport.summary}
            </p>

            {showFuzzDetails && (
              <div className="overflow-x-auto">
                <table className="w-full text-left text-xs font-mono">
                  <thead>
                    <tr className="border-b border-slate-800 text-[10px] text-slate-400 uppercase">
                      <th className="pb-2">Fuzz Vector</th>
                      <th className="pb-2">Delta Multiplier</th>
                      <th className="pb-2">Fuzzed Value</th>
                      <th className="pb-2">Proof Hash (0x...)</th>
                      <th className="pb-2">Status</th>
                      <th className="pb-2 text-right">Action</th>
                    </tr>
                  </thead>
                  <tbody className="divide-y divide-slate-800/60">
                    {fuzzReport.vectors.map((vec) => (
                      <tr key={vec.id} className="hover:bg-slate-850/40 transition">
                        <td className="py-2.5 font-medium text-slate-300">{vec.label}</td>
                        <td className="py-2.5 text-slate-400">
                          {vec.inputMultiplier.toFixed(3)}x ({vec.toleranceDeltaPercent > 0 ? '+' : ''}{vec.toleranceDeltaPercent}%)
                        </td>
                        <td className="py-2.5 text-white font-bold">
                          {vec.fuzzedValue.toLocaleString()} {activePreset.unit}
                        </td>
                        <td className="py-2.5 text-cyan-400 text-[10px]">{vec.proofHash.slice(0, 10)}...</td>
                        <td className="py-2.5">
                          <span
                            className={`text-[9px] uppercase px-1.5 py-0.5 rounded font-bold border ${
                              vec.fuzzStatus === 'VERIFIED'
                                ? 'bg-emerald-950/70 text-emerald-400 border-emerald-500/20'
                                : vec.fuzzStatus === 'CRITICAL_SPIKE'
                                ? 'bg-amber-950/70 text-amber-400 border-amber-500/20'
                                : 'bg-rose-950/70 text-rose-400 border-rose-500/20'
                            }`}
                          >
                            {vec.fuzzStatus}
                          </span>
                        </td>
                        <td className="py-2.5 text-right">
                          <button
                            type="button"
                            onClick={() => handleApplyFuzzVector(vec)}
                            className="text-[10px] px-2 py-0.5 rounded bg-slate-800 hover:bg-slate-700 text-indigo-300 transition cursor-pointer"
                          >
                            Apply
                          </button>
                        </td>
                      </tr>
                    ))}
                  </tbody>
                </table>
              </div>
            )}
          </div>
        </div>
      </div>

      {/* 1,000-Particle Consensus Signal Degradation Solver */}
      <div className="bg-slate-900/80 border border-slate-800 rounded-xl p-6 space-y-6">
        <div className="flex flex-col md:flex-row md:items-center justify-between gap-4">
          <div className="space-y-1">
            <div className="flex items-center gap-2">
              <Sparkles className="w-5 h-5 text-amber-400" />
              <h2 className="text-lg font-bold text-white">
                1,000-Particle Consensus Signal Degradation Solver
              </h2>
            </div>
            <p className="text-slate-400 text-sm">
              Ported directly from <code className="text-amber-400">nexus/signal_repair.py</code>. Simulates 1,000 parallel
              particles taking median consensus to detect anomalies (clean, noisy, drifted, spiked, clipped, dropped)
              and restore fidelity before contract execution.
            </p>
          </div>

          {solverResult && (
            <div className="flex items-center gap-3">
              <div
                className={`px-3 py-1.5 rounded-lg border font-mono text-xs font-bold uppercase ${getDegradationBadgeColor(
                  solverResult.classification
                )}`}
              >
                State: {solverResult.classification}
              </div>
              <div className="px-3 py-1.5 rounded-lg bg-slate-950 border border-slate-800 font-mono text-xs text-slate-300">
                Confidence: <strong className="text-cyan-400">{Math.round(solverResult.consensusConfidence * 100)}%</strong>
              </div>
            </div>
          )}
        </div>

        {/* Preset Selector */}
        <div className="space-y-2">
          <label className="text-xs font-mono text-slate-400 uppercase">Test Degradation Scenarios</label>
          <div className="flex flex-wrap gap-2">
            {[
              { id: 'clean', label: 'Nominal Clean Feed' },
              { id: 'noisy', label: 'Moderate High-Frequency Noise' },
              { id: 'drifted', label: 'Systemic Upward Drift' },
              { id: 'spiked', label: 'Flash Spikes / Extreme Outliers' },
              { id: 'dropped', label: 'Sensor / Feed Dropouts (0.0)' },
              { id: 'critical', label: 'Critically Ill / High Variance' },
            ].map((p) => (
              <button
                key={p.id}
                onClick={() => handlePresetSelect(p.id)}
                className={`px-3 py-1.5 rounded-lg text-xs font-medium transition ${
                  selectedPreset === p.id
                    ? 'bg-amber-500/20 text-amber-300 border border-amber-500/40'
                    : 'bg-slate-950 text-slate-400 border border-slate-800 hover:text-slate-200'
                }`}
              >
                {p.label}
              </button>
            ))}
          </div>
        </div>

        {/* Input & Controls */}
        <div className="grid grid-cols-1 md:grid-cols-4 gap-4">
          <div className="md:col-span-3 space-y-1">
            <label className="text-[11px] font-mono text-slate-400 uppercase">
              Raw Signal Array (Comma Separated)
            </label>
            <input
              type="text"
              value={customSignalInput}
              onChange={(e) => setCustomSignalInput(e.target.value)}
              className="w-full bg-slate-950 border border-slate-700 rounded-lg px-3 py-2 text-sm text-slate-200 font-mono focus:outline-none focus:border-amber-500"
            />
          </div>

          <div className="space-y-1">
            <label className="text-[11px] font-mono text-slate-400 uppercase">Expected Midpoint</label>
            <input
              type="number"
              value={expectedMidpoint}
              onChange={(e) => setExpectedMidpoint(parseFloat(e.target.value) || 100)}
              className="w-full bg-slate-950 border border-slate-700 rounded-lg px-3 py-2 text-sm text-slate-200 font-mono focus:outline-none focus:border-amber-500"
            />
          </div>
        </div>

        <div className="flex flex-wrap items-center gap-3">
          <button
            onClick={runSolver}
            className="py-2 px-5 bg-amber-600 hover:bg-amber-500 text-slate-950 font-semibold rounded-lg text-sm transition flex items-center gap-2 shadow-lg shadow-amber-600/20"
          >
            <RefreshCw className="w-4 h-4" />
            Run 1,000-Particle Consensus Repair
          </button>

          {solverResult && (
            <button
              onClick={handleBroadcastRepaired}
              className="py-2 px-4 bg-slate-800 hover:bg-slate-700 text-cyan-300 rounded-lg text-sm font-medium transition flex items-center gap-2 border border-slate-700"
            >
              <Radio className="w-4 h-4 text-cyan-400" />
              Broadcast Repaired Consensus to Bus
            </button>
          )}
        </div>

        {/* Solver Output Comparison */}
        {solverResult && (
          <div className="bg-slate-950 border border-slate-800/80 rounded-xl p-5 space-y-4">
            <h3 className="text-xs font-mono uppercase text-slate-400 font-semibold tracking-wider">
              Ensemble Convergence Results
            </h3>

            <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
              <div className="p-4 rounded-lg bg-slate-900 border border-slate-800">
                <div className="text-[11px] font-mono text-slate-400 uppercase">Input Classification</div>
                <div className="text-xl font-bold font-mono text-white mt-1">
                  {solverResult.classification}
                </div>
                <div className="text-xs text-slate-500 mt-1">
                  Detected via variance & deviation thresholds
                </div>
              </div>

              <div className="p-4 rounded-lg bg-slate-900 border border-slate-800">
                <div className="text-[11px] font-mono text-slate-400 uppercase">Corrections Applied</div>
                <div className="text-xl font-bold font-mono text-amber-400 mt-1">
                  {solverResult.correctionsApplied} / {solverResult.rawSignal.length} samples
                </div>
                <div className="text-xs text-slate-500 mt-1">
                  Re-weighted toward 1000-particle median
                </div>
              </div>

              <div className="p-4 rounded-lg bg-slate-900 border border-slate-800">
                <div className="text-[11px] font-mono text-slate-400 uppercase">Consensus Confidence</div>
                <div className="text-xl font-bold font-mono text-emerald-400 mt-1">
                  {(solverResult.consensusConfidence * 100).toFixed(1)}%
                </div>
                <div className="text-xs text-slate-500 mt-1">
                  Particle cluster distribution tightness
                </div>
              </div>
            </div>

            {/* Side-by-side array inspect */}
            <div className="grid grid-cols-1 md:grid-cols-2 gap-4 pt-2">
              <div className="p-3 rounded-lg bg-slate-900/60 border border-slate-800/80">
                <div className="text-[11px] font-mono text-rose-400 uppercase font-semibold mb-1">
                  Raw Degraded Input:
                </div>
                <div className="font-mono text-xs text-slate-300 break-words">
                  [{solverResult.rawSignal.map((n) => n.toFixed(1)).join(', ')}]
                </div>
              </div>

              <div className="p-3 rounded-lg bg-slate-900/60 border border-slate-800/80">
                <div className="text-[11px] font-mono text-emerald-400 uppercase font-semibold mb-1">
                  Repaired 1000-Particle Consensus:
                </div>
                <div className="font-mono text-xs text-slate-300 break-words">
                  [{solverResult.repairedSignal.map((n) => n.toFixed(1)).join(', ')}]
                </div>
              </div>
            </div>
          </div>
        )}
      </div>

      {/* Automated Bot Fleet Grid */}
      <div className="bg-slate-900/80 border border-slate-800 rounded-xl p-6 space-y-5">
        <div className="flex flex-col md:flex-row md:items-center justify-between gap-4">
          <div className="space-y-1">
            <div className="flex items-center gap-2">
              <Cpu className="w-5 h-5 text-indigo-400" />
              <h2 className="text-lg font-bold text-white">Automated Bot Fleet & Financial Rails</h2>
            </div>
            <p className="text-slate-400 text-sm">
              Executes autonomous monitoring scripts and MCP agents (<code className="text-indigo-400">mcp-fin-011</code> through{' '}
              <code className="text-indigo-400">mcp-fin-015</code>, plus Node.js bots) for accounting, health, intel, and registry sync.
            </p>
          </div>
          <div className="text-xs font-mono text-slate-400">
            Total Bots Registered: <strong className="text-white font-bold">{botFleet.length}</strong>
          </div>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
          {botFleet.map((bot) => (
            <div
              key={bot.id}
              className="bg-slate-950 border border-slate-800 rounded-xl p-4 flex flex-col justify-between gap-4 hover:border-slate-700 transition"
            >
              <div className="space-y-2">
                <div className="flex items-center justify-between">
                  <div className="flex items-center gap-2">
                    <span className="w-2 h-2 rounded-full bg-emerald-400 animate-pulse" />
                    <span className="font-mono text-xs font-bold text-slate-200">{bot.name}</span>
                  </div>
                  <span
                    className={`text-[10px] font-mono uppercase px-2 py-0.5 rounded border ${
                      bot.status === 'ONLINE'
                        ? 'bg-emerald-950/80 text-emerald-400 border-emerald-500/30'
                        : bot.status === 'EXECUTING'
                        ? 'bg-indigo-950/80 text-indigo-400 border-indigo-500/30 animate-pulse'
                        : 'bg-slate-900 text-slate-400 border-slate-800'
                    }`}
                  >
                    {bot.status}
                  </span>
                </div>

                <div className="text-[11px] font-mono text-slate-400">
                  Script: <span className="text-amber-400">{bot.script}</span>
                </div>

                <p className="text-xs text-slate-300 leading-relaxed">{bot.role}</p>

                <div className="pt-1 flex items-center justify-between text-[11px] font-mono text-slate-400 border-t border-slate-900">
                  <span>Tasks: <strong className="text-white">{bot.tasksCompleted}</strong></span>
                  <span>Latency: <strong className="text-cyan-400">{bot.latencyMs}ms</strong></span>
                </div>

                <div className="text-[10px] font-mono text-slate-500 truncate">
                  Last: {bot.lastAction}
                </div>
              </div>

              <div className="flex items-center gap-2 pt-2 border-t border-slate-900">
                <button
                  onClick={() => triggerBotRun(bot.id)}
                  disabled={bot.status === 'EXECUTING'}
                  className="flex-1 py-1.5 px-3 bg-indigo-600/30 hover:bg-indigo-600/50 text-indigo-300 border border-indigo-500/30 rounded-lg text-xs font-semibold transition flex items-center justify-center gap-1.5 disabled:opacity-50"
                >
                  <Play className="w-3.5 h-3.5" />
                  Trigger Run
                </button>
                <button
                  onClick={() => toggleBotStatus(bot.id)}
                  className="py-1.5 px-3 bg-slate-900 hover:bg-slate-850 text-slate-400 border border-slate-800 rounded-lg text-xs font-mono transition"
                >
                  {bot.status === 'ONLINE' ? 'Standby' : 'Online'}
                </button>
              </div>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
};
