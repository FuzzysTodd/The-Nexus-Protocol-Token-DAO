/**
 * @license
 * SPDX-License-Identifier: Apache-2.0
 * The Nexus Protocol DAO - Financial Operations & Dual-Sign Approvals Center
 */

import React, { useState } from 'react';
import { useNexusDao } from '../context/NexusDaoContext';
import { FinancialApprovalItem } from '../dao/logic';
import {
  FileCheck2,
  ShieldCheck,
  AlertTriangle,
  Clock,
  CheckCircle,
  XCircle,
  Bot,
  Layers,
  Activity,
  ArrowUpRight,
  ExternalLink,
  Shield,
  Zap,
} from 'lucide-react';

export const FinancialOpsApprovals: React.FC = () => {
  const {
    account,
    operatorRole,
    financialApprovals,
    signFinancialApproval,
    executeFinancialApproval,
    vetoFinancialApproval,
    botFleet,
  } = useNexusDao();

  const [selectedTypeFilter, setSelectedTypeFilter] = useState<string>('ALL');

  const isGuardianOrOwner =
    operatorRole === 'Owner (FuzzysTodd)' || operatorRole === 'Super Delegate';

  const filteredApprovals = financialApprovals.filter((item) => {
    if (selectedTypeFilter === 'ALL') return true;
    return item.type === selectedTypeFilter;
  });

  const pendingCount = financialApprovals.filter(
    (a) => a.status === 'PENDING_GUARDIAN'
  ).length;
  const readyCount = financialApprovals.filter(
    (a) => a.status === 'READY_FOR_EXECUTION'
  ).length;

  const totalValuePending = financialApprovals
    .filter((a) => a.status === 'PENDING_GUARDIAN' || a.status === 'READY_FOR_EXECUTION')
    .reduce((sum, a) => sum + a.amountUsd, 0);

  return (
    <div className="space-y-6" data-testid="financial-ops-approvals-view">
      {/* Hero Banner */}
      <div className="rounded-2xl bg-gradient-to-r from-slate-900 via-cyan-950/30 to-slate-900 border border-slate-800 p-6 shadow-xl">
        <div className="flex flex-col lg:flex-row lg:items-center justify-between gap-4">
          <div>
            <div className="flex items-center gap-2">
              <span className="px-2.5 py-0.5 rounded-full text-xs font-semibold bg-cyan-500/20 text-cyan-400 border border-cyan-500/40 flex items-center gap-1.5">
                <FileCheck2 className="w-3.5 h-3.5" />
                Financial Operations & Approvals
              </span>
              <span className="text-xs text-slate-500 font-mono">Dual-Guardian Protocol Governance</span>
            </div>
            <h2 className="text-xl font-bold text-slate-100 mt-1">
              Treasury Approvals, Policy Governance & Financial Ops
            </h2>
            <p className="text-xs text-slate-400 max-w-2xl mt-1">
              Multi-signature operational workflow governing fiat withdrawals, high-value treasury transfers, autonomous Forex bot risk limits, and financial bot fleet health.
            </p>
          </div>

          <div className="flex flex-wrap items-center gap-3">
            <div className="px-3.5 py-2 rounded-xl bg-slate-950/80 border border-slate-800 text-left">
              <div className="text-[10px] uppercase font-bold text-slate-500">Pending Signatures</div>
              <div className="text-sm font-bold text-amber-400 font-mono mt-0.5">
                {pendingCount} Required
              </div>
            </div>
            <div className="px-3.5 py-2 rounded-xl bg-slate-950/80 border border-slate-800 text-left">
              <div className="text-[10px] uppercase font-bold text-slate-500">Ready for Execution</div>
              <div className="text-sm font-bold text-emerald-400 font-mono mt-0.5">
                {readyCount} Authorized
              </div>
            </div>
            <div className="px-3.5 py-2 rounded-xl bg-slate-950/80 border border-slate-800 text-left">
              <div className="text-[10px] uppercase font-bold text-slate-500">Under Review Value</div>
              <div className="text-sm font-bold text-cyan-400 font-mono mt-0.5">
                ${totalValuePending.toLocaleString()} USD
              </div>
            </div>
          </div>
        </div>

        {/* Daily Velocity & Guardian Meter Strip */}
        <div className="grid grid-cols-1 md:grid-cols-3 gap-3 mt-5 pt-4 border-t border-slate-800/80 text-xs">
          <div className="p-3 rounded-xl bg-slate-950/60 border border-slate-800/80 space-y-1">
            <div className="flex items-center justify-between text-slate-400">
              <span>Daily Capital Velocity Used:</span>
              <span className="font-mono text-slate-200 font-bold">$142,500 / $500,000 (28.5%)</span>
            </div>
            <div className="w-full bg-slate-800 h-1.5 rounded-full overflow-hidden">
              <div className="h-full bg-cyan-400 rounded-full" style={{ width: '28.5%' }} />
            </div>
          </div>

          <div className="p-3 rounded-xl bg-slate-950/60 border border-slate-800/80 flex items-center justify-between">
            <div>
              <span className="text-[10px] uppercase font-bold text-slate-500">Active Guardians</span>
              <div className="text-slate-200 font-mono font-bold mt-0.5">2 / 2 Online</div>
            </div>
            <span className="px-2 py-0.5 rounded text-[10px] font-bold bg-emerald-950 text-emerald-400 border border-emerald-800">
              QUORUM READY
            </span>
          </div>

          <div className="p-3 rounded-xl bg-slate-950/60 border border-slate-800/80 flex items-center justify-between">
            <div>
              <span className="text-[10px] uppercase font-bold text-slate-500">Pre-Flight AML Check</span>
              <div className="text-slate-200 font-mono font-bold mt-0.5">0 Sanction Hits</div>
            </div>
            <span className="px-2 py-0.5 rounded text-[10px] font-bold bg-cyan-950 text-cyan-300 border border-cyan-800">
              TRM LABS PASS
            </span>
          </div>
        </div>
      </div>

      {/* Main Approvals Queue */}
      <div className="rounded-2xl bg-slate-900/90 border border-slate-800 p-5 space-y-4">
        <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-3 border-b border-slate-800 pb-3">
          <div className="flex items-center gap-2">
            <ShieldCheck className="w-4 h-4 text-cyan-400" />
            <h3 className="text-sm font-bold text-slate-200">
              Financial Approvals & Dual-Signature Queue ({filteredApprovals.length})
            </h3>
          </div>

          {/* Filter Pills */}
          <div className="flex items-center gap-1 bg-slate-950 p-1 rounded-xl border border-slate-800 text-[11px]">
            {['ALL', 'WITHDRAWAL', 'LARGE_TRANSFER', 'FOREX_POLICY', 'BOT_AUTHORIZATION'].map((type) => (
              <button
                key={type}
                onClick={() => setSelectedTypeFilter(type)}
                className={`px-2.5 py-1 rounded-lg font-medium transition ${
                  selectedTypeFilter === type
                    ? 'bg-slate-800 text-cyan-400 font-bold'
                    : 'text-slate-400 hover:text-slate-200'
                }`}
              >
                {type.replace(/_/g, ' ')}
              </button>
            ))}
          </div>
        </div>

        <div className="space-y-3">
          {filteredApprovals.map((item) => {
            const hasSigned = item.signatures.includes(account);
            const isReady = item.status === 'READY_FOR_EXECUTION';
            const isExecuted = item.status === 'EXECUTED';
            const isVetoed = item.status === 'VETOED';

            return (
              <div
                key={item.id}
                className="p-4 rounded-xl bg-slate-950 border border-slate-800 flex flex-col md:flex-row md:items-center justify-between gap-4 hover:border-slate-700 transition"
              >
                <div className="space-y-1.5 flex-1">
                  <div className="flex items-center gap-2 flex-wrap">
                    <span className="text-xs font-bold text-slate-100 font-mono">{item.id}</span>
                    <span
                      className={`px-2 py-0.5 rounded text-[10px] font-bold font-mono uppercase ${
                        item.priority === 'CRITICAL'
                          ? 'bg-red-950 text-red-400 border border-red-800'
                          : item.priority === 'HIGH'
                          ? 'bg-amber-950 text-amber-400 border border-amber-800'
                          : 'bg-slate-800 text-slate-300'
                      }`}
                    >
                      {item.priority}
                    </span>
                    <span className="px-2 py-0.5 rounded text-[10px] font-bold font-mono bg-cyan-950 text-cyan-300 border border-cyan-800">
                      {item.type.replace(/_/g, ' ')}
                    </span>
                    <span className="text-xs font-bold text-emerald-400 font-mono">
                      ${item.amountUsd.toLocaleString()} USD
                    </span>
                    <span
                      className={`px-2 py-0.5 rounded text-[10px] font-bold font-mono uppercase ${
                        isExecuted
                          ? 'bg-emerald-950 text-emerald-400 border border-emerald-800'
                          : isVetoed
                          ? 'bg-red-950 text-red-400 border border-red-800'
                          : isReady
                          ? 'bg-cyan-950 text-cyan-400 border border-cyan-800'
                          : 'bg-amber-950 text-amber-400 border border-amber-800'
                      }`}
                    >
                      {item.status.replace(/_/g, ' ')}
                    </span>
                  </div>

                  <h4 className="text-sm font-bold text-slate-100">{item.title}</h4>
                  <p className="text-xs text-slate-400 leading-relaxed">{item.description}</p>

                  <div className="flex flex-wrap items-center gap-4 text-[11px] text-slate-500 font-mono pt-1">
                    <span>
                      Signatures:{' '}
                      <strong className="text-slate-200">
                        {item.signatures.length} / {item.requiredSignatures}
                      </strong>
                    </span>
                    <span>•</span>
                    <span>Target: <strong className="text-cyan-400">{item.targetContractOrRail}</strong></span>
                    <span>•</span>
                    <span>Risk Score: <strong className="text-emerald-400">{item.complianceRiskScore}/100 (Clean)</strong></span>
                    <span>•</span>
                    <span>Created: {item.createdAt}</span>
                  </div>
                </div>

                {/* Action Buttons */}
                <div className="flex items-center gap-2 shrink-0">
                  {!isExecuted && !isVetoed && (
                    <>
                      {!hasSigned && item.status === 'PENDING_GUARDIAN' && (
                        <button
                          onClick={() => signFinancialApproval(item.id)}
                          disabled={!isGuardianOrOwner}
                          className="px-3.5 py-1.5 rounded-xl bg-amber-600 hover:bg-amber-500 text-white font-bold text-xs transition disabled:opacity-40"
                        >
                          Sign as Guardian
                        </button>
                      )}

                      {hasSigned && item.status === 'PENDING_GUARDIAN' && (
                        <span className="text-xs font-semibold text-cyan-400 flex items-center gap-1 font-mono">
                          <CheckCircle className="w-3.5 h-3.5" /> Signed by You
                        </span>
                      )}

                      {isReady && (
                        <button
                          onClick={() => executeFinancialApproval(item.id)}
                          className="px-4 py-1.5 rounded-xl bg-emerald-600 hover:bg-emerald-500 text-white font-bold text-xs shadow-lg transition"
                        >
                          Execute On-Chain
                        </button>
                      )}

                      <button
                        onClick={() => vetoFinancialApproval(item.id)}
                        disabled={!isGuardianOrOwner}
                        className="px-2.5 py-1.5 rounded-xl bg-slate-800 hover:bg-red-950 hover:text-red-300 text-slate-400 text-xs transition disabled:opacity-40"
                        title="Emergency veto item"
                      >
                        Veto
                      </button>
                    </>
                  )}

                  {isExecuted && (
                    <span className="text-xs text-emerald-400 font-medium flex items-center gap-1">
                      <CheckCircle className="w-3.5 h-3.5" /> Executed
                    </span>
                  )}

                  {isVetoed && (
                    <span className="text-xs text-red-400 font-medium flex items-center gap-1">
                      <XCircle className="w-3.5 h-3.5" /> Vetoed
                    </span>
                  )}
                </div>
              </div>
            );
          })}
        </div>
      </div>

      {/* Financial Operations Autonomous Bots Status */}
      <div className="rounded-2xl bg-slate-900/90 border border-slate-800 p-5 space-y-4">
        <div className="flex items-center justify-between border-b border-slate-800 pb-3">
          <div className="flex items-center gap-2">
            <Bot className="w-4 h-4 text-purple-400" />
            <h3 className="text-sm font-bold text-slate-200">
              Financial Ops Bots Fleet & Ledger Sync
            </h3>
          </div>
          <span className="text-xs text-emerald-400 font-mono font-semibold">
            All 6 Bots Operational (0 Incidents)
          </span>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-3">
          {botFleet.map((bot) => (
            <div
              key={bot.id}
              className="p-3.5 rounded-xl bg-slate-950 border border-slate-800 space-y-2 hover:border-slate-700 transition"
            >
              <div className="flex items-center justify-between">
                <div className="flex items-center gap-2">
                  <span className="w-2 h-2 rounded-full bg-emerald-400 animate-pulse" />
                  <h4 className="text-xs font-bold text-slate-100">{bot.name}</h4>
                </div>
                <span className="text-[10px] font-mono text-cyan-400 font-semibold">
                  {bot.latencyMs}ms
                </span>
              </div>
              <p className="text-[11px] text-slate-400 font-mono truncate">{bot.script}</p>
              <p className="text-xs text-slate-400">{bot.role}</p>
              <div className="pt-2 border-t border-slate-900 text-[11px] text-slate-500 font-mono flex items-center justify-between">
                <span>Tasks: <strong className="text-slate-300">{bot.tasksCompleted}</strong></span>
                <span className="text-emerald-400 font-semibold">Synced</span>
              </div>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
};
