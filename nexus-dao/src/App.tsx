/**
 * @license
 * SPDX-License-Identifier: Apache-2.0
 * The Nexus Protocol DAO - Main Application Shell
 */

import React, { useState } from 'react';
import { NexusDaoProvider } from './context/NexusDaoContext';
import { HeaderNav } from './components/HeaderNav';
import { GovernanceCenter } from './components/GovernanceCenter';
import { TreasuryManager } from './components/TreasuryManager';
import { ContractWorkbench } from './components/ContractWorkbench';
import { GameTheoryMcp } from './components/GameTheoryMcp';
import { BuilderFundRevenue } from './components/BuilderFundRevenue';
import { DefiVaultsRwa } from './components/DefiVaultsRwa';
import { FinancialSignalsBus } from './components/FinancialSignalsBus';
import { Gp22AndPythonAnalytics } from './components/Gp22AndPythonAnalytics';
import { PayableContractStudio } from './components/PayableContractStudio';
import { CircleBillPayOrchestrator } from './components/CircleBillPayOrchestrator';
import { CopilotWorkflowEngine } from './components/CopilotWorkflowEngine';
import { ForexFiatTrader } from './components/ForexFiatTrader';
import { WithdrawalCenter } from './components/WithdrawalCenter';
import { FinancialOpsApprovals } from './components/FinancialOpsApprovals';
import { TransactionConsole } from './components/TransactionConsole';
import { NEXUS_METADATA } from './data/nexusContracts';
import { ShieldCheck, ExternalLink, Globe, Cpu } from 'lucide-react';

function DaoAppContent() {
  const [activeTab, setActiveTabState] = useState<string>(() => {
    if (typeof window !== 'undefined') {
      const param = new URLSearchParams(window.location.search).get('tab');
      if (param) return param;
    }
    return 'treasury';
  });

  const setActiveTab = (tab: string) => {
    setActiveTabState(tab);
    if (typeof window !== 'undefined') {
      const url = new URL(window.location.href);
      url.searchParams.set('tab', tab);
      window.history.replaceState({}, '', url.toString());
    }
  };

  return (
    <div className="min-h-screen bg-slate-950 text-slate-100 flex flex-col font-sans selection:bg-cyan-500 selection:text-slate-950">
      {/* Top Header & Navigation */}
      <HeaderNav activeTab={activeTab} setActiveTab={setActiveTab} />

      {/* Main Workspace Body */}
      <main className="flex-1 max-w-7xl w-full mx-auto px-4 py-6 space-y-6">
        {activeTab === 'governance' && <GovernanceCenter />}
        {activeTab === 'treasury' && <TreasuryManager />}
        {activeTab === 'forex-trader' && <ForexFiatTrader />}
        {activeTab === 'withdrawals' && <WithdrawalCenter />}
        {activeTab === 'financial-ops' && <FinancialOpsApprovals />}
        {activeTab === 'workbench' && <ContractWorkbench />}
        {activeTab === 'payable-studio' && <PayableContractStudio />}
        {activeTab === 'circle-bill-pay' && <CircleBillPayOrchestrator />}
        {activeTab === 'copilot-workflows' && <CopilotWorkflowEngine />}
        {activeTab === 'mcp-swarm' && <GameTheoryMcp />}
        {activeTab === 'signals-bus' && <FinancialSignalsBus />}
        {activeTab === 'gp22-analytics' && <Gp22AndPythonAnalytics />}
        {activeTab === 'builder-fund' && <BuilderFundRevenue />}
        {activeTab === 'vaults-rwa' && <DefiVaultsRwa />}

        {/* Global On-Chain Real-Time Event Console */}
        <div className="pt-4">
          <TransactionConsole />
        </div>
      </main>

      {/* Protocol Footer */}
      <footer className="border-t border-slate-900 bg-slate-950 px-4 py-8 text-xs text-slate-500">
        <div className="max-w-7xl mx-auto flex flex-col md:flex-row items-center justify-between gap-4">
          <div className="space-y-1 text-center md:text-left">
            <div className="flex items-center justify-center md:justify-start gap-2 text-slate-300 font-semibold">
              <ShieldCheck className="w-4 h-4 text-cyan-400" />
              <span>The Nexus Protocol Token DAO</span>
              <span className="text-slate-600">•</span>
              <span className="text-amber-400 font-mono">NGTT Governance</span>
            </div>
            <p className="text-[11px] text-slate-500">
              Nexus Encryption Standard (NES) v1.0 • Canonical Authority: @{NEXUS_METADATA.ownerAuthority} (
              {NEXUS_METADATA.ownerAddress.slice(0, 10)}...{NEXUS_METADATA.ownerAddress.slice(-6)})
            </p>
          </div>

          <div className="flex flex-wrap items-center justify-center gap-4 text-slate-400">
            <a
              href={NEXUS_METADATA.repositoryUrl}
              target="_blank"
              rel="noreferrer"
              className="hover:text-cyan-400 transition flex items-center gap-1"
            >
              GitHub Repository <ExternalLink className="w-3 h-3" />
            </a>
            <span className="text-slate-800">•</span>
            <span className="font-mono text-cyan-400">tenkrypt.cb.id</span>
            <span className="text-slate-800">•</span>
            <span>1 Billion Total Supply</span>
          </div>
        </div>
      </footer>
    </div>
  );
}

export default function App() {
  return (
    <NexusDaoProvider>
      <DaoAppContent />
    </NexusDaoProvider>
  );
}
