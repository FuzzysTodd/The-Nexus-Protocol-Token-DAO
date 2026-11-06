/**
 * @license
 * SPDX-License-Identifier: Apache-2.0
 * The Nexus Protocol DAO - Multi-Asset Treasury & Multisig Vault
 */

import React, { useState } from 'react';
import { useNexusDao } from '../context/NexusDaoContext';
import { NEXUS_METADATA } from '../data/nexusContracts';
import { TreasuryCharts } from './TreasuryCharts';
import {
  Wallet,
  ArrowUpRight,
  ShieldCheck,
  AlertTriangle,
  Lock,
  PauseCircle,
  PlayCircle,
  Coins,
  CheckCircle,
  Clock,
  Send,
} from 'lucide-react';

export const TreasuryManager: React.FC = () => {
  const {
    account,
    treasuryAssets,
    isTreasuryPaused,
    toggleTreasuryPause,
    largeTransfers,
    requestTransfer,
    confirmLargeTransfer,
    executeLargeTransfer,
    operatorRole,
  } = useNexusDao();

  const [selectedAsset, setSelectedAsset] = useState('ETH');
  const [transferAmount, setTransferAmount] = useState('');
  const [transferRecipient, setTransferRecipient] = useState('');
  const [showTransferModal, setShowTransferModal] = useState(false);

  const totalTreasuryUsd = treasuryAssets.reduce((sum, a) => {
    const num = parseFloat(a.usdValue.replace(/[^0-9.-]+/g, '')) || 0;
    return sum + num;
  }, 0);

  const isGuardianOrOwner =
    operatorRole === 'Owner (FuzzysTodd)' || operatorRole === 'Super Delegate';

  const handleTransferSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    if (!transferAmount || !transferRecipient.trim()) return;
    requestTransfer(selectedAsset, transferAmount, transferRecipient.trim());
    setTransferAmount('');
    setTransferRecipient('');
    setShowTransferModal(false);
  };

  return (
    <div className="space-y-6">
      {/* Treasury Hero Banner */}
      <div className="rounded-2xl bg-gradient-to-r from-slate-900 via-teal-950/30 to-slate-900 border border-slate-800 p-6 shadow-xl">
        <div className="flex flex-col md:flex-row md:items-center justify-between gap-4">
          <div>
            <div className="flex items-center gap-2">
              <span className="px-2.5 py-0.5 rounded-full text-xs font-semibold bg-teal-500/20 text-teal-400 border border-teal-500/40 flex items-center gap-1.5">
                <Wallet className="w-3.5 h-3.5" />
                NexusDAOTreasury Vault
              </span>
              <span className="text-xs text-slate-500 font-mono">Contract: NexusDAOTreasury.sol</span>
            </div>
            <h2 className="text-xl font-bold text-slate-100 mt-1">
              Multi-Asset Protocol Treasury
            </h2>
            <p className="text-xs text-slate-400 max-w-2xl mt-1">
              Holds protocol reserves with Timelock-gated execution. Transfers exceeding 50 ETH or 100,000 ERC-20 tokens require dual GUARDIAN_ROLE co-signatures.
            </p>
          </div>

          <div className="flex items-center gap-2">
            {isGuardianOrOwner && (
              <button
                onClick={toggleTreasuryPause}
                className={`px-3.5 py-2 rounded-xl text-xs font-bold transition flex items-center gap-1.5 ${
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
              onClick={() => setShowTransferModal(true)}
              className="px-4 py-2 rounded-xl bg-gradient-to-r from-teal-600 to-cyan-600 hover:from-teal-500 hover:to-cyan-500 text-white font-bold text-xs shadow-lg transition flex items-center gap-1.5"
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
          <div className="flex items-center gap-4 text-xs font-mono text-slate-400">
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
                      className="px-3.5 py-1.5 rounded-xl bg-amber-600 hover:bg-amber-500 text-white font-bold text-xs transition disabled:opacity-40"
                    >
                      Co-Sign as Guardian
                    </button>
                  )}

                  {req.status === 'Confirmed' && (
                    <button
                      onClick={() => executeLargeTransfer(req.nonce)}
                      className="px-3.5 py-1.5 rounded-xl bg-emerald-600 hover:bg-emerald-500 text-white font-bold text-xs transition"
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
