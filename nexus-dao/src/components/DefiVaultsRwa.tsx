/**
 * @license
 * SPDX-License-Identifier: Apache-2.0
 * The Nexus Protocol DAO - DeFi Vaults & Real World Assets (RWA)
 */

import React, { useState } from 'react';
import { useNexusDao } from '../context/NexusDaoContext';
import {
  Layers,
  Building2,
  TrendingUp,
  Percent,
  Coins,
  ShieldCheck,
  CheckCircle,
  ExternalLink,
  Lock,
  Unlock,
} from 'lucide-react';

export const DefiVaultsRwa: React.FC = () => {
  const { account, executeMethod } = useNexusDao();

  // LP Staking State
  const [stakedLp, setStakedLp] = useState(12.5);
  const [earnedNgtt, setEarnedNgtt] = useState(4820);
  const [lpDepositAmount, setLpDepositAmount] = useState('');

  // Fractal Vault State
  const [fractalShares, setFractalShares] = useState(8500);
  const [fractalDepositAmount, setFractalDepositAmount] = useState('');

  // Options Vault State
  const [optionsShares, setOptionsShares] = useState(14000);
  const [optionsDepositAmount, setOptionsDepositAmount] = useState('');

  // RWA Deeds Catalog
  const [rwaDeeds, setRwaDeeds] = useState([
    {
      tokenId: 1,
      title: 'Cheyenne Wyoming Commercial Tech Center (LLC Deed #01)',
      ipfsCid: 'ipfs://QmYwAPJzv5CZsnA625s3Xf2nemtYgPpHdWEz79ojWnPbdG',
      valuationCents: 45000000, // $450,000.00
      rentalYieldBps: 850, // 8.50%
      fractionalized: true,
      fractionalSymbol: 'NX-CHEY',
      custodian: 'Wyoming DAO LLC Registered Agent',
    },
    {
      tokenId: 2,
      title: 'Denver Metro Solar Edge Facility (LLC Deed #02)',
      ipfsCid: 'ipfs://QmZ84bN21mZ9J8Q11F8k1pP78Zmn82N1P9QzZnm841b',
      valuationCents: 82000000, // $820,000.00
      rentalYieldBps: 1120, // 11.20%
      fractionalized: false,
      fractionalSymbol: null,
      custodian: 'Wyoming DAO LLC Registered Agent',
    },
  ]);

  const handleLpDeposit = async (e: React.FormEvent) => {
    e.preventDefault();
    const amt = parseFloat(lpDepositAmount) || 0;
    if (amt <= 0) return;
    await executeMethod('NexusLPStaking', 'deposit', { amount: amt });
    setStakedLp((prev) => prev + amt);
    setLpDepositAmount('');
  };

  const handleClaimLpRewards = async () => {
    if (earnedNgtt <= 0) return;
    await executeMethod('NexusLPStaking', 'claimRewards', {});
    setEarnedNgtt(0);
  };

  const handleExitAllLp = async () => {
    await executeMethod('NexusLPStaking', 'exitAll', {});
    setStakedLp(0);
    setEarnedNgtt(0);
  };

  const handleFractalDeposit = async (e: React.FormEvent) => {
    e.preventDefault();
    const amt = parseFloat(fractalDepositAmount) || 0;
    if (amt <= 0) return;
    await executeMethod('NexusFractalVault', 'deposit', { assets: amt });
    setFractalShares((prev) => prev + amt * 0.98); // conversion factor
    setFractalDepositAmount('');
  };

  const handleOptionsDeposit = async (e: React.FormEvent) => {
    e.preventDefault();
    const amt = parseFloat(optionsDepositAmount) || 0;
    if (amt <= 0) return;
    await executeMethod('NexusOptionsVault', 'deposit', { assets: amt });
    setOptionsShares((prev) => prev + amt);
    setOptionsDepositAmount('');
  };

  const handleFractionalizeDeed = async (tokenId: number) => {
    await executeMethod('NexusFractionalize', 'fractionalize', { tokenId });
    setRwaDeeds((prev) =>
      prev.map((d) =>
        d.tokenId === tokenId
          ? { ...d, fractionalized: true, fractionalSymbol: `NX-RWA${tokenId}` }
          : d
      )
    );
  };

  return (
    <div className="space-y-6">
      {/* Hero Banner */}
      <div className="rounded-2xl bg-gradient-to-r from-slate-900 via-emerald-950/30 to-slate-900 border border-slate-800 p-6 shadow-xl">
        <div className="flex flex-col md:flex-row md:items-center justify-between gap-4">
          <div>
            <div className="flex items-center gap-2">
              <span className="px-2.5 py-0.5 rounded-full text-xs font-semibold bg-emerald-500/20 text-emerald-400 border border-emerald-500/40 flex items-center gap-1.5">
                <Layers className="w-3.5 h-3.5" />
                DeFi Vaults & Real World Assets
              </span>
              <span className="text-xs text-slate-500 font-mono">
                NexusLPStaking • FractalVault • OptionsVault • NexusRWA
              </span>
            </div>
            <h2 className="text-xl font-bold text-slate-100 mt-1">
              Automated Yield & Wyoming DAO LLC Deeds
            </h2>
            <p className="text-xs text-slate-400 max-w-2xl mt-1">
              Stake LP tokens for continuous NGTT yields, compound returns via ERC-4626 Fractal Vaults, underwrite covered options premiums, and trade fractionalized real-world property deeds.
            </p>
          </div>
        </div>
      </div>

      {/* DeFi Vaults Grid */}
      <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
        {/* Card 1: LP Staking */}
        <div className="rounded-2xl bg-slate-900/90 border border-slate-800 p-5 space-y-4">
          <div className="flex items-center justify-between border-b border-slate-800 pb-3">
            <div>
              <h3 className="text-sm font-bold text-slate-100">Nexus LP Staking</h3>
              <p className="text-[11px] text-slate-400">Uniswap V3 NGTT/ETH LP</p>
            </div>
            <span className="px-2 py-0.5 rounded text-[10px] bg-emerald-950 text-emerald-400 border border-emerald-800 font-mono font-bold">
              64.5% APY
            </span>
          </div>

          <div className="p-3 rounded-xl bg-slate-950 border border-slate-800 space-y-2 text-xs font-mono">
            <div className="flex justify-between">
              <span className="text-slate-400">Your Staked LP:</span>
              <span className="text-slate-200 font-bold">{stakedLp.toFixed(2)} LP</span>
            </div>
            <div className="flex justify-between">
              <span className="text-slate-400">Unclaimed NGTT:</span>
              <span className="text-amber-300 font-bold">{earnedNgtt.toLocaleString()} NGTT</span>
            </div>
          </div>

          <form onSubmit={handleLpDeposit} className="space-y-2">
            <input
              type="number"
              step="any"
              value={lpDepositAmount}
              onChange={(e) => setLpDepositAmount(e.target.value)}
              placeholder="Amount LP to stake"
              className="w-full px-3 py-2 rounded-xl bg-slate-950 border border-slate-800 text-xs font-mono text-slate-200 focus:border-emerald-500 focus:outline-none"
            />
            <button
              type="submit"
              className="w-full py-2 rounded-xl bg-emerald-600 hover:bg-emerald-500 text-white font-bold text-xs transition"
            >
              Deposit & Stake LP
            </button>
          </form>

          <div className="flex gap-2">
            <button
              onClick={handleClaimLpRewards}
              disabled={earnedNgtt <= 0}
              className="flex-1 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-amber-300 text-xs font-semibold transition disabled:opacity-40"
            >
              Claim Rewards
            </button>
            <button
              onClick={handleExitAllLp}
              disabled={stakedLp <= 0}
              className="flex-1 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-red-400 text-xs font-semibold transition disabled:opacity-40"
            >
              Exit All
            </button>
          </div>
        </div>

        {/* Card 2: Fractal Vault (ERC-4626) */}
        <div className="rounded-2xl bg-slate-900/90 border border-slate-800 p-5 space-y-4">
          <div className="flex items-center justify-between border-b border-slate-800 pb-3">
            <div>
              <h3 className="text-sm font-bold text-slate-100">Fractal Vault</h3>
              <p className="text-[11px] text-slate-400">ERC-4626 Auto-Compounding</p>
            </div>
            <span className="px-2 py-0.5 rounded text-[10px] bg-cyan-950 text-cyan-400 border border-cyan-800 font-mono font-bold">
              28.0% APY
            </span>
          </div>

          <div className="p-3 rounded-xl bg-slate-950 border border-slate-800 space-y-2 text-xs font-mono">
            <div className="flex justify-between">
              <span className="text-slate-400">Your Vault Shares:</span>
              <span className="text-slate-200 font-bold">{fractalShares.toLocaleString()} fxShares</span>
            </div>
            <div className="flex justify-between">
              <span className="text-slate-400">Reinvest Rate:</span>
              <span className="text-cyan-300 font-bold">950 BPS (95%)</span>
            </div>
          </div>

          <form onSubmit={handleFractalDeposit} className="space-y-2">
            <input
              type="number"
              step="any"
              value={fractalDepositAmount}
              onChange={(e) => setFractalDepositAmount(e.target.value)}
              placeholder="Amount NGTT to deposit"
              className="w-full px-3 py-2 rounded-xl bg-slate-950 border border-slate-800 text-xs font-mono text-slate-200 focus:border-cyan-500 focus:outline-none"
            />
            <button
              type="submit"
              className="w-full py-2 rounded-xl bg-cyan-600 hover:bg-cyan-500 text-white font-bold text-xs transition"
            >
              Deposit & Compound
            </button>
          </form>

          <button
            onClick={() => {
              if (fractalShares > 0) {
                setFractalShares(0);
                executeMethod('NexusFractalVault', 'redeem', { shares: fractalShares });
              }
            }}
            disabled={fractalShares <= 0}
            className="w-full py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 text-xs font-semibold transition disabled:opacity-40"
          >
            Redeem All Shares
          </button>
        </div>

        {/* Card 3: Options Premium Vault */}
        <div className="rounded-2xl bg-slate-900/90 border border-slate-800 p-5 space-y-4">
          <div className="flex items-center justify-between border-b border-slate-800 pb-3">
            <div>
              <h3 className="text-sm font-bold text-slate-100">Options Vault</h3>
              <p className="text-[11px] text-slate-400">Covered Call Yield Underwriting</p>
            </div>
            <span className="px-2 py-0.5 rounded text-[10px] bg-indigo-950 text-indigo-400 border border-indigo-800 font-mono font-bold">
              42.5% APY
            </span>
          </div>

          <div className="p-3 rounded-xl bg-slate-950 border border-slate-800 space-y-2 text-xs font-mono">
            <div className="flex justify-between">
              <span className="text-slate-400">Your Options Shares:</span>
              <span className="text-slate-200 font-bold">{optionsShares.toLocaleString()} optShares</span>
            </div>
            <div className="flex justify-between">
              <span className="text-slate-400">Premium Pool:</span>
              <span className="text-indigo-300 font-bold">34,500 NGTT</span>
            </div>
          </div>

          <form onSubmit={handleOptionsDeposit} className="space-y-2">
            <input
              type="number"
              step="any"
              value={optionsDepositAmount}
              onChange={(e) => setOptionsDepositAmount(e.target.value)}
              placeholder="Amount NGTT to deposit"
              className="w-full px-3 py-2 rounded-xl bg-slate-950 border border-slate-800 text-xs font-mono text-slate-200 focus:border-indigo-500 focus:outline-none"
            />
            <button
              type="submit"
              className="w-full py-2 rounded-xl bg-indigo-600 hover:bg-indigo-500 text-white font-bold text-xs transition"
            >
              Deposit for Option Premiums
            </button>
          </form>

          <button
            onClick={() => {
              if (optionsShares > 0) {
                setOptionsShares(0);
                executeMethod('NexusOptionsVault', 'redeem', { shares: optionsShares });
              }
            }}
            disabled={optionsShares <= 0}
            className="w-full py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 text-xs font-semibold transition disabled:opacity-40"
          >
            Redeem All Shares
          </button>
        </div>
      </div>

      {/* Real World Assets (RWA) & Fractionalization */}
      <div className="rounded-2xl bg-slate-900/90 border border-slate-800 p-6 space-y-4">
        <div className="flex items-center justify-between border-b border-slate-800 pb-3">
          <div className="flex items-center gap-2">
            <Building2 className="w-5 h-5 text-emerald-400" />
            <div>
              <h3 className="text-base font-bold text-slate-100">
                Nexus RWA: Tokenized Property Deeds (Wyoming DAO LLC)
              </h3>
              <p className="text-xs text-slate-400">
                Contracts: NexusRWA.sol (ERC-721) & NexusFractionalize.sol (ERC-20)
              </p>
            </div>
          </div>
          <span className="text-xs font-mono text-emerald-400 px-2.5 py-0.5 rounded-full bg-emerald-950 border border-emerald-800">
            Legal LLC Compliant
          </span>
        </div>

        <div className="space-y-3">
          {rwaDeeds.map((deed) => (
            <div
              key={deed.tokenId}
              className="p-4 rounded-xl bg-slate-950 border border-slate-800 flex flex-col md:flex-row md:items-center justify-between gap-4"
            >
              <div className="space-y-1">
                <div className="flex items-center gap-2">
                  <span className="text-xs font-bold font-mono text-emerald-400">
                    NFT #{deed.tokenId}
                  </span>
                  <h4 className="text-sm font-bold text-slate-200">{deed.title}</h4>
                </div>
                <div className="text-xs text-slate-400 font-mono flex flex-wrap gap-x-4 gap-y-1">
                  <span>Valuation: <strong className="text-slate-200">${(deed.valuationCents / 100).toLocaleString()} USD</strong></span>
                  <span>Rental Yield: <strong className="text-emerald-400">{(deed.rentalYieldBps / 100).toFixed(2)}% APY</strong></span>
                  <span>Custodian: <strong className="text-slate-300">{deed.custodian}</strong></span>
                </div>
                <div className="text-[11px] text-slate-500 font-mono truncate">
                  Deed Legal Hash: {deed.ipfsCid}
                </div>
              </div>

              <div className="flex items-center gap-2">
                {deed.fractionalized ? (
                  <span className="px-3 py-1.5 rounded-xl bg-emerald-950 text-emerald-300 border border-emerald-800 text-xs font-bold font-mono flex items-center gap-1.5">
                    <CheckCircle className="w-3.5 h-3.5" />
                    Fractionalized ({deed.fractionalSymbol})
                  </span>
                ) : (
                  <button
                    onClick={() => handleFractionalizeDeed(deed.tokenId)}
                    className="px-4 py-2 rounded-xl bg-emerald-600 hover:bg-emerald-500 text-white font-bold text-xs shadow-md transition flex items-center gap-1.5"
                  >
                    <Unlock className="w-3.5 h-3.5" />
                    Fractionalize into ERC-20
                  </button>
                )}
              </div>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
};
