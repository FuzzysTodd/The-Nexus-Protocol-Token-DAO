/**
 * @license
 * SPDX-License-Identifier: Apache-2.0
 * The Nexus Protocol DAO - Microsoft Copilot Workflow & Trigger Engine
 * Modular workflow folders and trigger mechanics designed to
 * "rub the mass of the agent and MCP swarm" with 432Hz harmonic alignment.
 */

import React, { useState } from 'react';
import { useNexusDao } from '../context/NexusDaoContext';
import {
  CopilotWorkflowFolder,
  TriggerType,
  evaluateTriggerCondition,
  MassAgentRubResult,
} from '../dao/logic';
import { NEXUS_METADATA } from '../data/nexusContracts';
import {
  Cpu,
  Zap,
  FolderKanban,
  Radio,
  Activity,
  Sliders,
  Play,
  CheckCircle2,
  AlertTriangle,
  RefreshCw,
  FolderPlus,
  Coins,
  ShieldAlert,
  ArrowRight,
  Flame,
  Binary,
  Layers,
  Sparkles,
  Server,
  Clock,
  Send,
  Eye,
} from 'lucide-react';

export const CopilotWorkflowEngine: React.FC = () => {
  const {
    account,
    copilotFolders,
    toggleCopilotFolderActive,
    createCopilotFolder,
    rubAgentMass,
    lastMassRubResult,
    botFleet,
    toggleBotStatus,
    triggerBotRun,
    financialSignals,
  } = useNexusDao();

  const [isRubbingMass, setIsRubbingMass] = useState(false);
  const [pulseWave, setPulseWave] = useState(false);
  const [selectedFolder, setSelectedFolder] = useState<CopilotWorkflowFolder | null>(
    () => copilotFolders[0] || null
  );

  // New folder creation state
  const [showCreateModal, setShowCreateModal] = useState(false);
  const [newFolderName, setNewFolderName] = useState('');
  const [newFolderPath, setNewFolderPath] = useState('📁 /workflows/custom-agent-trigger/');
  const [newCategory, setNewCategory] = useState<CopilotWorkflowFolder['category']>('MCP_SWARM');
  const [newTriggerType, setNewTriggerType] = useState<TriggerType>('SATOSHI_BUFFER_CAP');
  const [newTriggerCondition, setNewTriggerCondition] = useState('Buffer >= 50,000 sats');
  const [newSelectedAgents, setNewSelectedAgents] = useState<string[]>([
    'mcp-fin-011',
    'mcp-fin-014',
  ]);
  const [newDescription, setNewDescription] = useState('');

  // Live trigger testing state
  const [testResult, setTestResult] = useState<{
    folderId: string;
    fired: boolean;
    reason: string;
  } | null>(null);

  // "Rub the Mass of the Agent and MCP" handler
  const handleRubAgentMass = () => {
    setIsRubbingMass(true);
    setPulseWave(true);

    setTimeout(() => {
      const result = rubAgentMass();
      setIsRubbingMass(false);
      setTimeout(() => setPulseWave(false), 1500);
    }, 450);
  };

  const handleTestTrigger = (folder: CopilotWorkflowFolder) => {
    const fired = evaluateTriggerCondition(folder, {
      manualTriggerFired: folder.triggerType === 'MANUAL_MASS_TRIGGER',
      satoshiBuffer: 125_000n,
      oracleDeviationPct: 0.65,
      poolBalanceWei: 80_000_000_000_000_000n,
      onChainEvent: 'ContractChunkPosted',
    });

    setTestResult({
      folderId: folder.id,
      fired,
      reason: fired
        ? `Trigger condition satisfied: ${folder.triggerCondition}`
        : `Trigger condition not met for current environment state`,
    });
  };

  const handleCreateFolder = (e: React.FormEvent) => {
    e.preventDefault();
    if (!newFolderName.trim()) return;

    createCopilotFolder({
      folderPath: newFolderPath.trim(),
      name: newFolderName.trim(),
      category: newCategory,
      description: newDescription.trim() || 'Custom Copilot workflow folder replacing static scripts',
      triggerType: newTriggerType,
      triggerCondition: newTriggerCondition.trim(),
      targetAgents: newSelectedAgents,
      isActive: true,
      triggerMechanicsSummary: `Automated ${newTriggerType} execution node for ${newSelectedAgents.join(', ')}.`,
    });

    setShowCreateModal(false);
    setNewFolderName('');
    setNewDescription('');
  };

  const activeFoldersCount = copilotFolders.filter((f) => f.isActive).length;
  const onlineBotsCount = botFleet.filter((b) => b.status === 'ONLINE').length;

  return (
    <div className="space-y-6">
      {/* Top Banner: Swarm Mass Command Bar */}
      <div className="relative overflow-hidden rounded-xl border border-cyan-500/30 bg-gradient-to-r from-slate-950 via-slate-900 to-cyan-950/40 p-6 shadow-2xl">
        {/* Harmonic Wave pulse effect */}
        {pulseWave && (
          <div className="absolute inset-0 bg-cyan-500/10 pointer-events-none animate-pulse" />
        )}

        <div className="relative z-10 flex flex-col lg:flex-row lg:items-center justify-between gap-6">
          <div className="space-y-2">
            <div className="flex items-center gap-2 text-xs font-mono text-cyan-400">
              <FolderKanban className="w-4 h-4 text-cyan-400" />
              <span>Microsoft Copilot Workflow & Trigger Engine</span>
              <span className="text-slate-600">•</span>
              <span className="text-amber-400 font-semibold">{NEXUS_METADATA.standard}</span>
              <span className="text-slate-600">•</span>
              <span className="text-emerald-400">Harmonic Swarm 432.08 Hz</span>
            </div>

            <h1 className="text-2xl md:text-3xl font-bold text-slate-100 flex items-center gap-3">
              <span>Workflow Folders & Trigger Mechanics</span>
              <span className="text-xs font-mono px-2.5 py-1 rounded-full bg-cyan-950 border border-cyan-800 text-cyan-300">
                Swarm Mass Resonance
              </span>
            </h1>

            <p className="text-xs text-slate-400 max-w-3xl">
              Modular Copilot folders replacing legacy workflows with automated trigger mechanics to{' '}
              <strong className="text-cyan-300 font-mono">rub the mass of the agent and MCP swarm</strong>.
              Coordinates on-chain events, oracle thresholds, Satoshi sweeps, and simultaneous multi-bot execution.
            </p>

            {/* Quick Metrics */}
            <div className="flex flex-wrap items-center gap-4 pt-1 text-xs font-mono text-slate-300">
              <div className="flex items-center gap-1.5 bg-slate-900/80 px-2.5 py-1 rounded border border-slate-800">
                <Server className="w-3.5 h-3.5 text-cyan-400" />
                <span>MCP Bots: <strong className="text-emerald-400">{onlineBotsCount} / {botFleet.length} Online</strong></span>
              </div>
              <div className="flex items-center gap-1.5 bg-slate-900/80 px-2.5 py-1 rounded border border-slate-800">
                <FolderKanban className="w-3.5 h-3.5 text-blue-400" />
                <span>Folders: <strong className="text-blue-300">{activeFoldersCount} Active</strong></span>
              </div>
              <div className="flex items-center gap-1.5 bg-slate-900/80 px-2.5 py-1 rounded border border-slate-800">
                <Radio className="w-3.5 h-3.5 text-amber-400" />
                <span>Consensus: <strong className="text-amber-300">99.7% Alignment</strong></span>
              </div>
            </div>
          </div>

          {/* THE MASTER BUTTON: Rub the Mass of the Agent and MCP */}
          <div className="flex flex-col items-stretch lg:items-end gap-2.5 min-w-[280px]">
            <button
              onClick={handleRubAgentMass}
              disabled={isRubbingMass}
              className="relative group px-6 py-4 rounded-xl font-bold text-sm text-slate-950 shadow-2xl transition-all duration-300 transform active:scale-95 disabled:opacity-75 bg-gradient-to-r from-cyan-400 via-teal-300 to-emerald-400 hover:from-cyan-300 hover:to-emerald-300"
            >
              <div className="flex items-center justify-center gap-2.5">
                <Zap className={`w-5 h-5 ${isRubbingMass ? 'animate-spin' : 'group-hover:scale-110 transition-transform'}`} />
                <span className="tracking-wide uppercase font-mono text-xs md:text-sm">
                  {isRubbingMass ? 'Harmonizing Swarm Mass...' : 'Rub the Mass of Agent & MCP'}
                </span>
              </div>
              <div className="text-[10px] font-mono text-slate-900/80 text-center mt-1">
                Blast All 6 Bots & Trigger Folders Simultaneously
              </div>
            </button>

            <div className="flex items-center justify-between w-full text-[11px] font-mono text-slate-400 px-1">
              <span>Harmonic: 432.08 Hz</span>
              <button
                onClick={() => setShowCreateModal(true)}
                className="text-cyan-400 hover:text-cyan-300 flex items-center gap-1 font-semibold"
              >
                <FolderPlus className="w-3.5 h-3.5" />
                + New Copilot Folder
              </button>
            </div>
          </div>
        </div>
      </div>

      {/* Visual Pipeline Flow Diagram */}
      <div className="bg-slate-900/60 border border-slate-800 rounded-xl p-4 text-xs font-mono">
        <div className="text-slate-400 font-semibold mb-3 flex items-center gap-2">
          <Activity className="w-4 h-4 text-cyan-400" />
          <span>Copilot Trigger Architecture: Event Disparity → Mass Agent Rub → On-Chain Execution</span>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-4 gap-3 text-center">
          <div className="bg-slate-950/70 border border-slate-800 rounded-lg p-3 space-y-1">
            <div className="text-[10px] text-slate-500 uppercase tracking-wider">Phase 1: Ingestion</div>
            <div className="text-xs font-semibold text-cyan-300">Trigger Mechanics</div>
            <div className="text-[11px] text-slate-400">Oracle / Sats / Bytecode / Cron</div>
          </div>

          <div className="bg-slate-950/70 border border-slate-800 rounded-lg p-3 space-y-1">
            <div className="text-[10px] text-slate-500 uppercase tracking-wider">Phase 2: Modular Folders</div>
            <div className="text-xs font-semibold text-blue-300">📁 /workflows/ Pipeline</div>
            <div className="text-[11px] text-slate-400">6 Copilot Replaced Subroutines</div>
          </div>

          <div className="bg-slate-950/70 border border-slate-800 rounded-lg p-3 space-y-1">
            <div className="text-[10px] text-slate-500 uppercase tracking-wider">Phase 3: Resonant Rub</div>
            <div className="text-xs font-semibold text-emerald-300">MCP Fleet Mass Rub</div>
            <div className="text-[11px] text-slate-400">mcp-fin-011 to 015 & Accounting</div>
          </div>

          <div className="bg-slate-950/70 border border-slate-800 rounded-lg p-3 space-y-1">
            <div className="text-[10px] text-slate-500 uppercase tracking-wider">Phase 4: Settlement</div>
            <div className="text-xs font-semibold text-amber-300">Payable Value Transfer</div>
            <div className="text-[11px] text-slate-400">Split to 10 Builder Streams & Vaults</div>
          </div>
        </div>
      </div>

      {/* Main Grid: Copilot Workflow Folders on Left, Live Telemetry & Inspector on Right */}
      <div className="grid grid-cols-1 lg:grid-cols-12 gap-6">
        {/* Left Column: Copilot Workflow Folders List */}
        <div className="lg:col-span-7 space-y-4">
          <div className="flex items-center justify-between">
            <div className="flex items-center gap-2 text-sm font-semibold text-slate-200">
              <FolderKanban className="w-4 h-4 text-cyan-400" />
              <span>Copilot Modular Workflow Folders ({copilotFolders.length})</span>
            </div>
            <span className="text-[11px] text-slate-400 font-mono">
              Replaces legacy hardcoded workflows
            </span>
          </div>

          <div className="space-y-3">
            {copilotFolders.map((folder) => {
              const isSelected = selectedFolder?.id === folder.id;
              return (
                <div
                  key={folder.id}
                  onClick={() => setSelectedFolder(folder)}
                  className={`cursor-pointer rounded-xl border p-4 transition-all duration-200 ${
                    isSelected
                      ? 'border-cyan-500 bg-slate-900/90 ring-1 ring-cyan-500 shadow-lg shadow-cyan-950/30'
                      : 'border-slate-800 bg-slate-900/50 hover:border-slate-700 hover:bg-slate-900/70'
                  }`}
                >
                  <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-2 border-b border-slate-800 pb-2.5">
                    <div className="space-y-0.5">
                      <div className="flex items-center gap-2">
                        <span className="font-mono text-xs font-bold text-cyan-300">
                          {folder.folderPath}
                        </span>
                        <span
                          className={`text-[9px] font-mono px-1.5 py-0.5 rounded uppercase font-semibold ${
                            folder.status === 'SUCCESS'
                              ? 'bg-emerald-950 text-emerald-400 border border-emerald-800/60'
                              : folder.status === 'LISTENING'
                              ? 'bg-blue-950 text-blue-400 border border-blue-800/60'
                              : 'bg-slate-800 text-slate-400'
                          }`}
                        >
                          {folder.status}
                        </span>
                      </div>
                      <div className="text-xs font-semibold text-slate-200">{folder.name}</div>
                    </div>

                    <div className="flex items-center gap-2 self-start sm:self-auto">
                      <button
                        type="button"
                        onClick={(e) => {
                          e.stopPropagation();
                          handleTestTrigger(folder);
                        }}
                        className="px-2.5 py-1 bg-slate-800 hover:bg-slate-700 text-[10px] font-mono text-cyan-300 rounded border border-slate-700 flex items-center gap-1 transition"
                      >
                        <Play className="w-2.5 h-2.5 text-cyan-400" />
                        Test Trigger
                      </button>

                      <button
                        type="button"
                        onClick={(e) => {
                          e.stopPropagation();
                          toggleCopilotFolderActive(folder.id);
                        }}
                        className={`px-2 py-1 text-[10px] font-mono font-semibold rounded transition ${
                          folder.isActive
                            ? 'bg-emerald-950/60 text-emerald-400 border border-emerald-800/60'
                            : 'bg-slate-800 text-slate-400'
                        }`}
                      >
                        {folder.isActive ? 'ENABLED' : 'PAUSED'}
                      </button>
                    </div>
                  </div>

                  <div className="py-2.5 text-xs text-slate-400 leading-relaxed">
                    {folder.description}
                  </div>

                  <div className="grid grid-cols-1 sm:grid-cols-2 gap-2 text-[11px] font-mono pt-1 text-slate-400">
                    <div className="bg-slate-950/60 p-2 rounded border border-slate-800/80 space-y-0.5">
                      <div className="text-[10px] text-slate-500 uppercase">Trigger Mechanics</div>
                      <div className="text-cyan-300 truncate font-semibold">{folder.triggerType}</div>
                      <div className="text-[10px] text-slate-400 truncate">{folder.triggerCondition}</div>
                    </div>

                    <div className="bg-slate-950/60 p-2 rounded border border-slate-800/80 space-y-0.5">
                      <div className="text-[10px] text-slate-500 uppercase">Target MCP Swarm</div>
                      <div className="text-emerald-300 truncate font-semibold">
                        {folder.targetAgents.slice(0, 3).join(', ')}
                        {folder.targetAgents.length > 3 && ` +${folder.targetAgents.length - 3}`}
                      </div>
                      <div className="text-[10px] text-slate-400">
                        Executions: {folder.totalExecutions}
                      </div>
                    </div>
                  </div>
                </div>
              );
            })}
          </div>

          {/* Test Trigger Results notification */}
          {testResult && (
            <div
              className={`p-3 rounded-lg border text-xs font-mono flex items-center justify-between ${
                testResult.fired
                  ? 'bg-emerald-950/40 border-emerald-600 text-emerald-200'
                  : 'bg-amber-950/40 border-amber-600 text-amber-200'
              }`}
            >
              <div className="flex items-center gap-2">
                {testResult.fired ? (
                  <CheckCircle2 className="w-4 h-4 text-emerald-400" />
                ) : (
                  <AlertTriangle className="w-4 h-4 text-amber-400" />
                )}
                <span>{testResult.reason}</span>
              </div>
              <button
                onClick={() => setTestResult(null)}
                className="text-[10px] text-slate-400 hover:text-slate-200"
              >
                Dismiss
              </button>
            </div>
          )}
        </div>

        {/* Right Column: Swarm Telemetry & Selected Folder Deep-Dive */}
        <div className="lg:col-span-5 space-y-4">
          {/* Swarm Mass Rub Telemetry Card */}
          <div className="bg-slate-900/80 border border-slate-800 rounded-xl p-5 space-y-4">
            <div className="flex items-center justify-between border-b border-slate-800 pb-3">
              <div className="flex items-center gap-2 font-semibold text-sm text-slate-200">
                <Activity className="w-4 h-4 text-emerald-400" />
                <span>Swarm Mass Rub Telemetry</span>
              </div>
              <span className="text-[11px] font-mono text-emerald-400 bg-emerald-950/60 px-2 py-0.5 rounded border border-emerald-800/60">
                Resonant 432.08 Hz
              </span>
            </div>

            {lastMassRubResult ? (
              <div className="space-y-3">
                <div className="grid grid-cols-2 gap-2 text-xs font-mono">
                  <div className="bg-slate-950 p-2 rounded border border-slate-800">
                    <div className="text-[10px] text-slate-500">Activated Bots</div>
                    <div className="text-emerald-400 font-bold text-sm">
                      {lastMassRubResult.totalAgentsActivated} / 6
                    </div>
                  </div>
                  <div className="bg-slate-950 p-2 rounded border border-slate-800">
                    <div className="text-[10px] text-slate-500">Consensus Score</div>
                    <div className="text-cyan-400 font-bold text-sm">
                      {lastMassRubResult.consensusScore}%
                    </div>
                  </div>
                  <div className="bg-slate-950 p-2 rounded border border-slate-800">
                    <div className="text-[10px] text-slate-500">Gas Consumed</div>
                    <div className="text-amber-400 font-mono text-sm">
                      {lastMassRubResult.totalGasUsed.toLocaleString()}
                    </div>
                  </div>
                  <div className="bg-slate-950 p-2 rounded border border-slate-800">
                    <div className="text-[10px] text-slate-500">Routed Payable</div>
                    <div className="text-blue-400 font-mono text-sm">
                      {(Number(lastMassRubResult.routedPayableWei) / 1e18).toFixed(4)} ETH
                    </div>
                  </div>
                </div>

                <div className="space-y-1.5 text-xs">
                  <div className="text-[11px] font-semibold text-slate-300">Agent Dispatch Verifications:</div>
                  <div className="space-y-1 max-h-56 overflow-y-auto pr-1">
                    {lastMassRubResult.agentDispatches.map((d, i) => (
                      <div
                        key={i}
                        className="bg-slate-950/80 p-2 rounded border border-slate-800/80 text-[11px] font-mono space-y-0.5"
                      >
                        <div className="flex items-center justify-between text-cyan-300 font-semibold">
                          <span>{d.agentId} ({d.role})</span>
                          <span className="text-[9px] text-emerald-400">{d.latencyMs}ms</span>
                        </div>
                        <div className="text-[10px] text-slate-400 leading-tight">
                          {d.actionPerformed}
                        </div>
                      </div>
                    ))}
                  </div>
                </div>

                <div className="text-[10px] font-mono text-slate-500 truncate pt-1">
                  Audit Hash: {lastMassRubResult.auditHash}
                </div>
              </div>
            ) : (
              <div className="text-center py-8 text-slate-500 text-xs font-mono space-y-2">
                <Cpu className="w-8 h-8 text-slate-600 mx-auto animate-pulse" />
                <p>Click "Rub the Mass of Agent & MCP" above to trigger simultaneous multi-agent resonance and view telemetry.</p>
              </div>
            )}
          </div>

          {/* Connected Autonomous Bot Fleet Status */}
          <div className="bg-slate-900/80 border border-slate-800 rounded-xl p-5 space-y-3">
            <div className="flex items-center justify-between border-b border-slate-800 pb-2.5">
              <div className="flex items-center gap-2 font-semibold text-xs text-slate-200">
                <Server className="w-4 h-4 text-cyan-400" />
                <span>Connected MCP Bot Fleet ({botFleet.length})</span>
              </div>
              <span className="text-[10px] font-mono text-slate-400">
                financial-ops-bots.json
              </span>
            </div>

            <div className="space-y-1.5 max-h-60 overflow-y-auto pr-1">
              {botFleet.map((bot) => (
                <div
                  key={bot.id}
                  className="bg-slate-950/60 p-2 rounded border border-slate-800 flex items-center justify-between text-xs"
                >
                  <div className="space-y-0.5 truncate mr-2">
                    <div className="flex items-center gap-1.5 font-mono text-[11px] text-slate-200 font-semibold">
                      <span className="w-1.5 h-1.5 rounded-full bg-emerald-400 animate-pulse" />
                      <span>{bot.name}</span>
                      <span className="text-[9px] text-slate-500 font-normal">({bot.id})</span>
                    </div>
                    <div className="text-[10px] text-slate-400 truncate">{bot.role}</div>
                  </div>

                  <div className="flex items-center gap-1.5">
                    <button
                      type="button"
                      onClick={() => triggerBotRun(bot.id)}
                      className="px-2 py-0.5 bg-cyan-950 hover:bg-cyan-900 text-cyan-300 text-[10px] font-mono rounded border border-cyan-800/60 transition"
                    >
                      Run
                    </button>
                    <button
                      type="button"
                      onClick={() => toggleBotStatus(bot.id)}
                      className={`px-1.5 py-0.5 text-[9px] font-mono rounded transition ${
                        bot.status === 'ONLINE'
                          ? 'bg-emerald-950 text-emerald-400'
                          : 'bg-slate-800 text-slate-400'
                      }`}
                    >
                      {bot.status}
                    </button>
                  </div>
                </div>
              ))}
            </div>
          </div>
        </div>
      </div>

      {/* Modal: Create Custom Copilot Folder */}
      {showCreateModal && (
        <div className="fixed inset-0 z-50 bg-black/80 backdrop-blur-sm flex items-center justify-center p-4">
          <div className="bg-slate-900 border border-slate-700 rounded-xl max-w-lg w-full p-6 space-y-4 shadow-2xl">
            <div className="flex items-center justify-between border-b border-slate-800 pb-3">
              <div className="flex items-center gap-2 font-bold text-sm text-slate-100">
                <FolderPlus className="w-4 h-4 text-cyan-400" />
                <span>Create New Copilot Workflow Folder</span>
              </div>
              <button
                onClick={() => setShowCreateModal(false)}
                className="text-slate-400 hover:text-slate-200 text-sm font-mono"
              >
                ✕
              </button>
            </div>

            <form onSubmit={handleCreateFolder} className="space-y-3 text-xs">
              <div className="space-y-1">
                <label className="text-slate-300 font-medium">Folder Path</label>
                <input
                  type="text"
                  value={newFolderPath}
                  onChange={(e) => setNewFolderPath(e.target.value)}
                  className="w-full bg-slate-950 border border-slate-700 rounded-lg px-3 py-1.5 font-mono text-cyan-300 focus:outline-none focus:border-cyan-500"
                  placeholder="📁 /workflows/my-custom-trigger/"
                  required
                />
              </div>

              <div className="space-y-1">
                <label className="text-slate-300 font-medium">Workflow Name</label>
                <input
                  type="text"
                  value={newFolderName}
                  onChange={(e) => setNewFolderName(e.target.value)}
                  className="w-full bg-slate-950 border border-slate-700 rounded-lg px-3 py-1.5 text-slate-200 focus:outline-none focus:border-cyan-500"
                  placeholder="e.g. Volatility Arbitrage Trigger"
                  required
                />
              </div>

              <div className="grid grid-cols-2 gap-3">
                <div className="space-y-1">
                  <label className="text-slate-300 font-medium">Trigger Type</label>
                  <select
                    value={newTriggerType}
                    onChange={(e) => setNewTriggerType(e.target.value as TriggerType)}
                    className="w-full bg-slate-950 border border-slate-700 rounded-lg px-2.5 py-1.5 text-slate-200 focus:outline-none focus:border-cyan-500"
                  >
                    <option value="SATOSHI_BUFFER_CAP">SATOSHI_BUFFER_CAP</option>
                    <option value="ORACLE_THRESHOLD">ORACLE_THRESHOLD</option>
                    <option value="ON_CHAIN_EVENT">ON_CHAIN_EVENT</option>
                    <option value="CRON_SCHEDULE">CRON_SCHEDULE</option>
                    <option value="MANUAL_MASS_TRIGGER">MANUAL_MASS_TRIGGER</option>
                    <option value="MCP_CROSS_CASCADE">MCP_CROSS_CASCADE</option>
                  </select>
                </div>

                <div className="space-y-1">
                  <label className="text-slate-300 font-medium">Category</label>
                  <select
                    value={newCategory}
                    onChange={(e) => setNewCategory(e.target.value as any)}
                    className="w-full bg-slate-950 border border-slate-700 rounded-lg px-2.5 py-1.5 text-slate-200 focus:outline-none focus:border-cyan-500"
                  >
                    <option value="MCP_SWARM">MCP_SWARM</option>
                    <option value="PAYABLE_LIQUIDITY">PAYABLE_LIQUIDITY</option>
                    <option value="ORACLE_HEDGE">ORACLE_HEDGE</option>
                    <option value="SECURITY_GUARD">SECURITY_GUARD</option>
                    <option value="GAME_THEORY">GAME_THEORY</option>
                    <option value="GATEWAY_NANOPAYMENTS">GATEWAY_NANOPAYMENTS</option>
                  </select>
                </div>
              </div>

              <div className="space-y-1">
                <label className="text-slate-300 font-medium">Trigger Condition Formula</label>
                <input
                  type="text"
                  value={newTriggerCondition}
                  onChange={(e) => setNewTriggerCondition(e.target.value)}
                  className="w-full bg-slate-950 border border-slate-700 rounded-lg px-3 py-1.5 font-mono text-emerald-300 focus:outline-none focus:border-cyan-500"
                  placeholder="e.g. Sats >= 100,000 OR Price Spread > 0.50%"
                  required
                />
              </div>

              <div className="space-y-1">
                <label className="text-slate-300 font-medium">Description</label>
                <textarea
                  value={newDescription}
                  onChange={(e) => setNewDescription(e.target.value)}
                  className="w-full bg-slate-950 border border-slate-700 rounded-lg px-3 py-1.5 text-slate-200 focus:outline-none focus:border-cyan-500 h-16"
                  placeholder="Explain what this Copilot workflow folder coordinates and triggers"
                />
              </div>

              <div className="flex items-center justify-end gap-2 pt-2 border-t border-slate-800">
                <button
                  type="button"
                  onClick={() => setShowCreateModal(false)}
                  className="px-3 py-1.5 bg-slate-800 hover:bg-slate-700 text-slate-300 rounded text-xs"
                >
                  Cancel
                </button>
                <button
                  type="submit"
                  className="px-4 py-1.5 bg-cyan-600 hover:bg-cyan-500 text-white font-semibold rounded text-xs shadow-md shadow-cyan-900/40"
                >
                  Create Folder
                </button>
              </div>
            </form>
          </div>
        </div>
      )}
    </div>
  );
};
