/**
 * @license
 * SPDX-License-Identifier: Apache-2.0
 * The Nexus Protocol DAO - Top Navigation and Operator Bar
 */

import React, { useState } from 'react';
import { useNexusDao } from '../context/NexusDaoContext';
import { NEXUS_METADATA, NEXUS_NETWORKS } from '../data/nexusContracts';
import {
  Shield,
  Wallet,
  Globe,
  ChevronDown,
  CheckCircle2,
  ExternalLink,
  Cpu,
  Layers,
  Coins,
  FileCode,
  Flame,
  Award,
  Radio,
  GitPullRequest,
  FolderKanban,
  Zap,
  CreditCard,
  DollarSign,
  ArrowDownToLine,
  FileCheck2,
} from 'lucide-react';

interface HeaderNavProps {
  activeTab: string;
  setActiveTab: (tab: string) => void;
}

export const HeaderNav: React.FC<HeaderNavProps> = ({ activeTab, setActiveTab }) => {
  const {
    account,
    ensOrHandle,
    network,
    isMetaMaskConnected,
    operatorRole,
    connectMetaMask,
    switchAccount,
    switchNetwork,
    ngttBalance,
    votingPower,
    isTreasuryPaused,
  } = useNexusDao();

  const [showAccountMenu, setShowAccountMenu] = useState(false);
  const [showNetworkMenu, setShowNetworkMenu] = useState(false);

  const formattedNgtt = (Number(ngttBalance / 10n ** 18n)).toLocaleString();
  const formattedVotes = (Number(votingPower / 10n ** 18n)).toLocaleString();

  const operatorPresets = [
    {
      name: 'Owner (FuzzysTodd)',
      address: NEXUS_METADATA.ownerAddress,
      handle: NEXUS_METADATA.coinbaseHandle,
      role: 'Owner (FuzzysTodd)',
      badge: 'Owner / Canonical Authority',
    },
    {
      name: 'Super Delegate Alpha',
      address: '0x71C83647209B16fa4876b20C1d88A2c1B1c9e831',
      handle: 'super-alpha.eth',
      role: 'Super Delegate',
      badge: 'Guardian & Canceller',
    },
    {
      name: 'MPC Node Operator',
      address: '0x90F79bf6EB2c4f870365E785982E1f101E93b906',
      handle: 'mpc-operator.eth',
      role: 'Token Holder',
      badge: 'Active Builder / Player',
    },
  ];

  const navItems = [
    { id: 'governance', label: 'Governance & Timelock', icon: Shield },
    { id: 'treasury', label: 'Treasury & Multisig', icon: Wallet },
    { id: 'forex-trader', label: 'Forex & Fiat Trader', icon: DollarSign },
    { id: 'withdrawals', label: 'Withdrawal Center', icon: ArrowDownToLine },
    { id: 'financial-ops', label: 'Financial Ops & Approvals', icon: FileCheck2 },
    { id: 'builder-fund', label: 'Builder Fund & 10 Streams', icon: Coins },
    { id: 'payable-studio', label: 'Payable Contract Studio', icon: Coins },
    { id: 'circle-bill-pay', label: 'Circle Bill Pay & Orchestrator', icon: CreditCard },
    { id: 'copilot-workflows', label: 'Copilot Workflows & Swarm', icon: FolderKanban },
    { id: 'workbench', label: 'Contract Workbench & Poster', icon: FileCode },
    { id: 'mcp-swarm', label: 'Game Theory & MCP Swarm', icon: Cpu },
    { id: 'signals-bus', label: 'Financial Signals & Bus', icon: Radio },
    { id: 'gp22-analytics', label: 'GP-22 & Python Suite', icon: GitPullRequest },
    { id: 'vaults-rwa', label: 'DeFi Vaults & RWA', icon: Layers },
  ];

  return (
    <header className="border-b border-slate-800 bg-slate-950/90 backdrop-blur-md sticky top-0 z-50">
      {/* Top Protocol Status Bar */}
      <div className="border-b border-slate-800/80 bg-slate-900/60 px-4 py-1.5 text-xs">
        <div className="max-w-7xl mx-auto flex flex-wrap items-center justify-between gap-2 text-slate-400">
          <div className="flex items-center gap-3">
            <span className="inline-flex items-center gap-1.5 font-medium text-emerald-400">
              <span className="w-2 h-2 rounded-full bg-emerald-500 animate-pulse" />
              Nexus Protocol DAO: Operational
            </span>
            <span className="text-slate-600">|</span>
            <span>Standard: <strong className="text-slate-300">{NEXUS_METADATA.standard}</strong></span>
            <span className="text-slate-600">|</span>
            <span>Canonical Authority: <strong className="text-amber-400">@{NEXUS_METADATA.ownerAuthority}</strong></span>
          </div>

          <div className="flex items-center gap-3 text-slate-400">
            {isTreasuryPaused && (
              <span className="px-2 py-0.5 rounded bg-red-950/80 border border-red-800/80 text-red-400 font-semibold flex items-center gap-1">
                <Flame className="w-3 h-3" /> TREASURY PAUSED
              </span>
            )}
            <a
              href={NEXUS_METADATA.repositoryUrl}
              target="_blank"
              rel="noreferrer"
              className="inline-flex items-center gap-1 hover:text-cyan-400 transition"
            >
              GitHub Repo <ExternalLink className="w-3 h-3" />
            </a>
            <span className="text-slate-600">|</span>
            <span>Coinbase Handle: <strong className="text-cyan-300">{NEXUS_METADATA.coinbaseHandle}</strong></span>
          </div>
        </div>
      </div>

      {/* Main Header */}
      <div className="max-w-7xl mx-auto px-4 py-3 flex items-center justify-between gap-4">
        {/* Brand */}
        <div className="flex items-center gap-3">
          <div className="w-10 h-10 rounded-xl bg-gradient-to-br from-cyan-500 via-blue-600 to-indigo-600 flex items-center justify-center shadow-lg shadow-cyan-500/20 text-white font-black text-xl tracking-wider">
            NX
          </div>
          <div>
            <div className="flex items-center gap-2">
              <h1 className="text-lg font-bold text-slate-100 tracking-tight">The Nexus Protocol</h1>
              <span className="px-1.5 py-0.5 text-[10px] font-semibold uppercase tracking-wider rounded bg-cyan-950 text-cyan-400 border border-cyan-800/60">
                DAO Operating Center
              </span>
            </div>
            <p className="text-xs text-slate-400 font-mono">
              NGTT Token: {NEXUS_METADATA.mainnetAddress.slice(0, 8)}...{NEXUS_METADATA.mainnetAddress.slice(-6)}
            </p>
          </div>
        </div>

        {/* Account / Network Controls */}
        <div className="flex items-center gap-2 sm:gap-3">
          {/* Network Switcher */}
          <div className="relative">
            <button
              onClick={() => setShowNetworkMenu(!showNetworkMenu)}
              className="flex items-center gap-1.5 px-3 py-1.5 rounded-lg bg-slate-900 border border-slate-800 hover:border-slate-700 text-xs text-slate-300 font-medium transition"
              aria-label="Select Network"
            >
              <Globe className="w-3.5 h-3.5 text-cyan-400" />
              <span>{network.name}</span>
              <ChevronDown className="w-3 h-3 text-slate-400" />
            </button>

            {showNetworkMenu && (
              <div className="absolute right-0 mt-2 w-56 rounded-xl bg-slate-900 border border-slate-800 shadow-2xl p-1 z-50">
                <div className="px-3 py-1.5 text-[11px] font-semibold text-slate-400 uppercase tracking-wider">
                  Supported Networks
                </div>
                {NEXUS_NETWORKS.map((net) => (
                  <button
                    key={net.chainId}
                    onClick={() => {
                      switchNetwork(net.chainId);
                      setShowNetworkMenu(false);
                    }}
                    className={`w-full flex items-center justify-between px-3 py-2 rounded-lg text-xs transition text-left ${
                      network.chainId === net.chainId
                        ? 'bg-cyan-950/70 text-cyan-300 border border-cyan-800/50'
                        : 'text-slate-300 hover:bg-slate-800'
                    }`}
                  >
                    <div>
                      <div className="font-semibold">{net.name}</div>
                      <div className="text-[10px] text-slate-400">Chain ID: {net.chainId}</div>
                    </div>
                    {network.chainId === net.chainId && <CheckCircle2 className="w-3.5 h-3.5 text-cyan-400" />}
                  </button>
                ))}
              </div>
            )}
          </div>

          {/* Voting Power / Holdings Pill */}
          <div className="hidden md:flex items-center gap-2 px-3 py-1.5 rounded-lg bg-slate-900/90 border border-slate-800 text-xs">
            <Award className="w-3.5 h-3.5 text-amber-400" />
            <div className="text-left font-mono">
              <span className="text-slate-400">Votes: </span>
              <span className="font-semibold text-amber-300">{formattedVotes}</span>
              <span className="text-slate-500 text-[10px] ml-1">NGTT</span>
            </div>
          </div>

          {/* Operator / Wallet Selector */}
          <div className="relative">
            <button
              onClick={() => setShowAccountMenu(!showAccountMenu)}
              className="flex items-center gap-2 px-3 py-1.5 rounded-lg bg-slate-900 border border-slate-800 hover:border-slate-700 text-xs text-slate-200 transition"
              aria-label="Select Operator or Connect Wallet"
            >
              <div className="w-2 h-2 rounded-full bg-cyan-400" />
              <div className="text-left">
                <div className="font-semibold text-slate-200 flex items-center gap-1">
                  {ensOrHandle || `${account.slice(0, 6)}...${account.slice(-4)}`}
                </div>
                <div className="text-[10px] text-cyan-400">{operatorRole}</div>
              </div>
              <ChevronDown className="w-3.5 h-3.5 text-slate-400 ml-1" />
            </button>

            {showAccountMenu && (
              <div className="absolute right-0 mt-2 w-80 rounded-xl bg-slate-900 border border-slate-800 shadow-2xl p-2 z-50">
                <div className="px-3 py-2 border-b border-slate-800 mb-1">
                  <div className="text-[11px] font-semibold text-slate-400 uppercase tracking-wider">
                    Operator Identity & Role
                  </div>
                  <div className="font-mono text-xs text-slate-300 break-all mt-0.5">{account}</div>
                  <div className="text-xs text-amber-400 mt-1">NGTT Balance: {formattedNgtt}</div>
                </div>

                <div className="p-1 space-y-1">
                  <div className="text-[10px] uppercase font-bold text-slate-500 px-2 py-1">Quick Switch Operator</div>
                  {operatorPresets.map((preset) => (
                    <button
                      key={preset.address}
                      onClick={() => {
                        switchAccount(preset.address, preset.role);
                        setShowAccountMenu(false);
                      }}
                      className={`w-full flex items-center justify-between p-2 rounded-lg text-left text-xs transition ${
                        account.toLowerCase() === preset.address.toLowerCase()
                          ? 'bg-cyan-950/70 border border-cyan-800/60 text-cyan-300'
                          : 'text-slate-300 hover:bg-slate-800'
                      }`}
                    >
                      <div>
                        <div className="font-semibold text-slate-200">{preset.name}</div>
                        <div className="text-[10px] text-slate-400 font-mono">
                          {preset.address.slice(0, 8)}...{preset.address.slice(-6)}
                        </div>
                        <div className="text-[10px] text-cyan-400">{preset.badge}</div>
                      </div>
                      {account.toLowerCase() === preset.address.toLowerCase() && (
                        <CheckCircle2 className="w-4 h-4 text-cyan-400" />
                      )}
                    </button>
                  ))}

                  <div className="pt-2 border-t border-slate-800">
                    <button
                      onClick={() => {
                        connectMetaMask();
                        setShowAccountMenu(false);
                      }}
                      className="w-full flex items-center justify-center gap-2 px-3 py-2 rounded-lg bg-gradient-to-r from-cyan-600 to-blue-600 hover:from-cyan-500 hover:to-blue-500 text-white font-medium text-xs shadow-md transition"
                    >
                      <Wallet className="w-3.5 h-3.5" />
                      {isMetaMaskConnected ? 'MetaMask Connected' : 'Connect Injected MetaMask'}
                    </button>
                  </div>
                </div>
              </div>
            )}
          </div>
        </div>
      </div>

      {/* Primary Navigation Tabs */}
      <nav className="max-w-7xl mx-auto px-4 flex items-center space-x-1 overflow-x-auto no-scrollbar border-t border-slate-800/60">
        {navItems.map((item) => {
          const Icon = item.icon;
          const isActive = activeTab === item.id;
          return (
            <button
              key={item.id}
              onClick={() => setActiveTab(item.id)}
              className={`flex items-center gap-2 px-4 py-2.5 text-xs font-semibold whitespace-nowrap border-b-2 transition ${
                isActive
                  ? 'border-cyan-400 text-cyan-400 bg-cyan-950/30'
                  : 'border-transparent text-slate-400 hover:text-slate-200 hover:border-slate-700'
              }`}
            >
              <Icon className={`w-4 h-4 ${isActive ? 'text-cyan-400' : 'text-slate-500'}`} />
              {item.label}
              {item.id === 'forex-trader' && (
                <span className="px-1.5 py-0.2 rounded-full text-[10px] bg-cyan-950 text-cyan-300 border border-cyan-700">
                  Auto-FX Rails
                </span>
              )}
              {item.id === 'withdrawals' && (
                <span className="px-1.5 py-0.2 rounded-full text-[10px] bg-rose-950 text-rose-300 border border-rose-700">
                  Multi-Rail Payout
                </span>
              )}
              {item.id === 'financial-ops' && (
                <span className="px-1.5 py-0.2 rounded-full text-[10px] bg-amber-950 text-amber-300 border border-amber-700 font-semibold">
                  Dual-Sign Queue
                </span>
              )}
              {item.id === 'builder-fund' && (
                <span className="px-1.5 py-0.2 rounded-full text-[10px] bg-emerald-950 text-emerald-300 border border-emerald-700 animate-pulse font-semibold">
                  10/10 Activated
                </span>
              )}
              {item.id === 'payable-studio' && (
                <span className="px-1.5 py-0.2 rounded-full text-[10px] bg-emerald-950 text-emerald-300 border border-emerald-700">
                  Payables & Value
                </span>
              )}
              {item.id === 'circle-bill-pay' && (
                <span className="px-1.5 py-0.2 rounded-full text-[10px] bg-emerald-950 text-emerald-300 border border-emerald-700 animate-pulse font-semibold">
                  Auto-Orchestrator
                </span>
              )}
              {item.id === 'copilot-workflows' && (
                <span className="px-1.5 py-0.2 rounded-full text-[10px] bg-cyan-950 text-cyan-300 border border-cyan-700">
                  Rub Mass
                </span>
              )}
              {item.id === 'workbench' && (
                <span className="px-1.5 py-0.2 rounded-full text-[10px] bg-indigo-950 text-indigo-300 border border-indigo-700">
                  Chunk Engine
                </span>
              )}
              {item.id === 'signals-bus' && (
                <span className="px-1.5 py-0.2 rounded-full text-[10px] bg-amber-950 text-amber-300 border border-amber-700">
                  1000-Particle
                </span>
              )}
              {item.id === 'gp22-analytics' && (
                <span className="px-1.5 py-0.2 rounded-full text-[10px] bg-purple-950 text-purple-300 border border-purple-700">
                  GP-22 & ML
                </span>
              )}
            </button>
          );
        })}
      </nav>
    </header>
  );
};
