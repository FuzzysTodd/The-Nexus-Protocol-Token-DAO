/**
 * @license
 * SPDX-License-Identifier: Apache-2.0
 * The Nexus Protocol DAO - On-Chain Governance & Timelock Engine
 */

import React, { useState } from 'react';
import { useNexusDao } from '../context/NexusDaoContext';
import { NEXUS_METADATA, NEXUS_CONTRACTS } from '../data/nexusContracts';
import { checkQuorum, getTimelockStatus } from '../dao/logic';
import {
  Vote,
  Clock,
  ShieldAlert,
  CheckCircle2,
  XCircle,
  PlusCircle,
  Users,
  Timer,
  ChevronRight,
  ExternalLink,
  Lock,
  Unlock,
  AlertOctagon,
} from 'lucide-react';

export const GovernanceCenter: React.FC = () => {
  const {
    account,
    votingPower,
    ngttBalance,
    delegatedTo,
    delegateVotes,
    proposals,
    createProposal,
    castVote,
    queueProposal,
    executeProposal,
    cancelProposal,
    operatorRole,
  } = useNexusDao();

  // Create Proposal Modal
  const [showCreateModal, setShowCreateModal] = useState(false);
  const [propTitle, setPropTitle] = useState('');
  const [propDesc, setPropDesc] = useState('');
  const [propTarget, setPropTarget] = useState(NEXUS_CONTRACTS[3].name);
  const [propAddress, setPropAddress] = useState(NEXUS_CONTRACTS[3].address || '');
  const [propCalldata, setPropCalldata] = useState('executeTransfer(address, uint256)');

  // Delegation Modal
  const [showDelegateModal, setShowDelegateModal] = useState(false);
  const [customDelegate, setCustomDelegate] = useState('');

  const [filterStatus, setFilterStatus] = useState<string>('all');

  const nowSeconds = Math.floor(Date.now() / 1000);
  const totalSupply = 1_000_000_000n * 10n ** 18n;

  const filteredProposals = proposals.filter((p) => {
    if (filterStatus === 'all') return true;
    return p.status.toLowerCase() === filterStatus.toLowerCase();
  });

  const handleCreateProposalSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    if (!propTitle.trim() || !propDesc.trim()) return;

    createProposal({
      title: propTitle,
      description: propDesc,
      targetContract: propTarget,
      targetAddress: propAddress,
      callValueEth: '0',
      calldataPreview: propCalldata,
    });

    setPropTitle('');
    setPropDesc('');
    setShowCreateModal(false);
  };

  const handleDelegateSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    if (!customDelegate.trim()) return;
    delegateVotes(customDelegate.trim());
    setShowDelegateModal(false);
  };

  const isGuardianOrOwner =
    operatorRole === 'Owner (FuzzysTodd)' || operatorRole === 'Super Delegate';

  return (
    <div className="space-y-6">
      {/* Governance Hero Header */}
      <div className="rounded-2xl bg-gradient-to-r from-slate-900 via-blue-950/40 to-slate-900 border border-slate-800 p-6 shadow-xl">
        <div className="flex flex-col md:flex-row md:items-center justify-between gap-4">
          <div>
            <div className="flex items-center gap-2">
              <span className="px-2.5 py-0.5 rounded-full text-xs font-semibold bg-blue-500/20 text-blue-400 border border-blue-500/40 flex items-center gap-1.5">
                <Vote className="w-3.5 h-3.5" />
                NexusDAOGovernor & Timelock
              </span>
              <span className="text-xs text-slate-500 font-mono">Contract: NexusDAOGovernor.sol</span>
            </div>
            <h2 className="text-xl font-bold text-slate-100 mt-1">
              Decentralized On-Chain Governance
            </h2>
            <p className="text-xs text-slate-400 max-w-2xl mt-1">
              Token-weighted democracy with OpenZeppelin checkpoint snapshots, a strict 4% quorum requirement, and a 2-day TimelockController delay on all state modifications.
            </p>
          </div>

          <div className="flex items-center gap-2">
            <button
              onClick={() => setShowDelegateModal(true)}
              className="px-3.5 py-2 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-200 text-xs font-semibold transition flex items-center gap-1.5"
            >
              <Users className="w-3.5 h-3.5 text-cyan-400" />
              Manage Delegation
            </button>
            <button
              onClick={() => setShowCreateModal(true)}
              className="px-4 py-2 rounded-xl bg-gradient-to-r from-cyan-600 to-blue-600 hover:from-cyan-500 hover:to-blue-500 text-white text-xs font-bold shadow-lg transition flex items-center gap-1.5"
            >
              <PlusCircle className="w-3.5 h-3.5" />
              New Proposal
            </button>
          </div>
        </div>

        {/* Governance Stats Bar */}
        <div className="grid grid-cols-2 sm:grid-cols-4 gap-3 mt-5 pt-5 border-t border-slate-800/80">
          <div className="p-3 rounded-xl bg-slate-950/60 border border-slate-800/80">
            <div className="text-[10px] uppercase font-bold text-slate-400">Voting Delay</div>
            <div className="text-sm font-bold text-slate-200 font-mono mt-0.5">7,200 blocks</div>
            <div className="text-[11px] text-slate-500">~1 day on Ethereum</div>
          </div>
          <div className="p-3 rounded-xl bg-slate-950/60 border border-slate-800/80">
            <div className="text-[10px] uppercase font-bold text-slate-400">Voting Period</div>
            <div className="text-sm font-bold text-slate-200 font-mono mt-0.5">50,400 blocks</div>
            <div className="text-[11px] text-slate-500">~7 days duration</div>
          </div>
          <div className="p-3 rounded-xl bg-slate-950/60 border border-slate-800/80">
            <div className="text-[10px] uppercase font-bold text-slate-400">Quorum Target</div>
            <div className="text-sm font-bold text-amber-300 font-mono mt-0.5">4.00% (40M NGTT)</div>
            <div className="text-[11px] text-slate-500">Snapshot-weighted</div>
          </div>
          <div className="p-3 rounded-xl bg-slate-950/60 border border-slate-800/80">
            <div className="text-[10px] uppercase font-bold text-slate-400">Timelock Delay</div>
            <div className="text-sm font-bold text-cyan-400 font-mono mt-0.5">2 Days (172,800s)</div>
            <div className="text-[11px] text-slate-500">Mandatory queue window</div>
          </div>
        </div>
      </div>

      {/* Filter Tabs */}
      <div className="flex items-center justify-between flex-wrap gap-3">
        <div className="flex items-center gap-1.5 p-1 rounded-xl bg-slate-900 border border-slate-800 text-xs">
          {['all', 'active', 'queued', 'executed', 'succeeded'].map((status) => (
            <button
              key={status}
              onClick={() => setFilterStatus(status)}
              className={`px-3 py-1.5 rounded-lg font-semibold uppercase text-[10px] tracking-wider transition ${
                filterStatus === status
                  ? 'bg-cyan-950 text-cyan-300 border border-cyan-800'
                  : 'text-slate-400 hover:text-slate-200'
              }`}
            >
              {status}
            </button>
          ))}
        </div>

        <div className="text-xs text-slate-400">
          Your Voting Weight:{' '}
          <strong className="text-amber-300 font-mono">
            {Number(votingPower / 10n ** 18n).toLocaleString()} NGTT
          </strong>
        </div>
      </div>

      {/* Proposal Cards List */}
      <div className="space-y-4">
        {filteredProposals.map((proposal) => {
          const totalVotes = proposal.forVotes + proposal.againstVotes + proposal.abstainVotes;
          const quorum = checkQuorum(totalVotes, totalSupply);
          const timelock = proposal.queuedTimestamp
            ? getTimelockStatus(proposal.queuedTimestamp, NEXUS_METADATA.timelockDelaySeconds, nowSeconds)
            : null;

          const forPct = totalVotes > 0n ? Number((proposal.forVotes * 100n) / totalVotes) : 0;
          const againstPct = totalVotes > 0n ? Number((proposal.againstVotes * 100n) / totalVotes) : 0;

          return (
            <div
              key={proposal.id}
              className="rounded-2xl bg-slate-900/90 border border-slate-800 p-5 space-y-4 hover:border-slate-700 transition shadow-lg"
            >
              {/* Proposal Header */}
              <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-2 border-b border-slate-800 pb-3">
                <div className="flex items-center gap-2.5">
                  <span className="w-7 h-7 rounded-lg bg-slate-800 flex items-center justify-center font-bold text-xs font-mono text-cyan-400">
                    #{proposal.id}
                  </span>
                  <h3 className="text-sm sm:text-base font-bold text-slate-100">{proposal.title}</h3>
                </div>

                <div className="flex items-center gap-2">
                  <span
                    className={`px-2.5 py-0.5 rounded-full text-xs font-bold font-mono uppercase ${
                      proposal.status === 'Active'
                        ? 'bg-blue-950 text-blue-400 border border-blue-800 animate-pulse'
                        : proposal.status === 'Queued'
                        ? 'bg-amber-950 text-amber-400 border border-amber-800'
                        : proposal.status === 'Executed'
                        ? 'bg-emerald-950 text-emerald-400 border border-emerald-800'
                        : proposal.status === 'Succeeded'
                        ? 'bg-cyan-950 text-cyan-400 border border-cyan-800'
                        : 'bg-red-950 text-red-400 border border-red-800'
                    }`}
                  >
                    {proposal.status}
                  </span>

                  {proposal.userVoted && (
                    <span className="px-2 py-0.5 rounded-full text-[10px] bg-slate-800 text-slate-300 font-mono">
                      Voted {proposal.userVoted.toUpperCase()}
                    </span>
                  )}
                </div>
              </div>

              {/* Description & Target */}
              <p className="text-xs text-slate-300 leading-relaxed">{proposal.description}</p>

              <div className="p-3 rounded-xl bg-slate-950 border border-slate-800 font-mono text-xs space-y-1 text-slate-400">
                <div className="flex items-center justify-between">
                  <span>
                    <strong className="text-slate-300">Target Contract:</strong> {proposal.targetContract}
                  </span>
                  <span className="text-[11px] text-slate-500">{proposal.targetAddress}</span>
                </div>
                <div>
                  <strong className="text-slate-300">Calldata Preview:</strong>{' '}
                  <span className="text-cyan-400 break-all">{proposal.calldataPreview}</span>
                </div>
              </div>

              {/* Voting Progress & Quorum Bar */}
              <div className="space-y-2">
                <div className="flex items-center justify-between text-xs">
                  <div className="flex items-center gap-3">
                    <span className="text-emerald-400 font-semibold">
                      For: {Number(proposal.forVotes / 10n ** 18n).toLocaleString()} NGTT ({forPct}%)
                    </span>
                    <span className="text-red-400 font-semibold">
                      Against: {Number(proposal.againstVotes / 10n ** 18n).toLocaleString()} NGTT ({againstPct}%)
                    </span>
                  </div>
                  <div className="text-slate-400">
                    Quorum:{' '}
                    <strong className={quorum.hasQuorum ? 'text-emerald-400' : 'text-amber-400'}>
                      {quorum.percentageReached.toFixed(2)}% / 4.00%
                    </strong>
                  </div>
                </div>

                <div className="w-full h-2.5 rounded-full bg-slate-950 border border-slate-800 overflow-hidden flex">
                  <div
                    className="h-full bg-gradient-to-r from-emerald-500 to-teal-400 transition-all duration-500"
                    style={{ width: `${Math.min(100, forPct)}%` }}
                  />
                  <div
                    className="h-full bg-gradient-to-r from-red-500 to-rose-400 transition-all duration-500"
                    style={{ width: `${Math.min(100, againstPct)}%` }}
                  />
                </div>
              </div>

              {/* Timelock Countdown (if Queued) */}
              {proposal.status === 'Queued' && timelock && (
                <div className="p-3.5 rounded-xl bg-amber-950/40 border border-amber-800/60 space-y-2">
                  <div className="flex items-center justify-between text-xs">
                    <span className="text-amber-300 font-semibold flex items-center gap-1.5">
                      <Clock className="w-3.5 h-3.5 animate-spin" />
                      Timelock Delay Countdown (48 Hours)
                    </span>
                    <span className="font-mono text-amber-200">
                      {timelock.isReady
                        ? '✅ Ready to Execute'
                        : `${Math.floor(timelock.remainingSeconds / 3600)}h ${Math.floor(
                            (timelock.remainingSeconds % 3600) / 60
                          )}m remaining`}
                    </span>
                  </div>
                  <div className="w-full h-2 rounded-full bg-slate-900 overflow-hidden">
                    <div
                      className="h-full bg-amber-500 transition-all duration-500"
                      style={{ width: `${timelock.percentElapsed}%` }}
                    />
                  </div>
                </div>
              )}

              {/* Action Buttons */}
              <div className="flex items-center justify-between pt-2 border-t border-slate-800/80">
                {/* Active Voting Buttons */}
                {proposal.status === 'Active' && (
                  <div className="flex items-center gap-2">
                    <button
                      onClick={() => castVote(proposal.id, 'for')}
                      disabled={!!proposal.userVoted}
                      className="px-3.5 py-1.5 rounded-xl bg-emerald-600 hover:bg-emerald-500 text-white font-bold text-xs transition disabled:opacity-50"
                    >
                      Vote FOR
                    </button>
                    <button
                      onClick={() => castVote(proposal.id, 'against')}
                      disabled={!!proposal.userVoted}
                      className="px-3.5 py-1.5 rounded-xl bg-red-600 hover:bg-red-500 text-white font-bold text-xs transition disabled:opacity-50"
                    >
                      Vote AGAINST
                    </button>
                    <button
                      onClick={() => castVote(proposal.id, 'abstain')}
                      disabled={!!proposal.userVoted}
                      className="px-3.5 py-1.5 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-300 font-bold text-xs transition disabled:opacity-50"
                    >
                      ABSTAIN
                    </button>
                  </div>
                )}

                {/* Queue into Timelock */}
                {proposal.status === 'Succeeded' && (
                  <button
                    onClick={() => queueProposal(proposal.id)}
                    className="px-4 py-2 rounded-xl bg-amber-600 hover:bg-amber-500 text-white font-bold text-xs transition flex items-center gap-1.5"
                  >
                    <Lock className="w-3.5 h-3.5" />
                    Queue in NexusDAOTimelock (2-Day Delay)
                  </button>
                )}

                {/* Execute from Timelock */}
                {proposal.status === 'Queued' && (
                  <div className="flex items-center gap-2">
                    <button
                      onClick={() => executeProposal(proposal.id)}
                      className="px-4 py-2 rounded-xl bg-emerald-600 hover:bg-emerald-500 text-white font-bold text-xs transition flex items-center gap-1.5"
                    >
                      <Unlock className="w-3.5 h-3.5" />
                      Execute On-Chain Transaction
                    </button>

                    {/* Guardian Emergency Cancel */}
                    {isGuardianOrOwner && (
                      <button
                        onClick={() => cancelProposal(proposal.id)}
                        className="px-3 py-2 rounded-xl bg-red-950/80 border border-red-800 text-red-300 hover:bg-red-900 text-xs font-semibold transition flex items-center gap-1.5"
                        title="Emergency Veto by CANCELLER_ROLE"
                      >
                        <AlertOctagon className="w-3.5 h-3.5 text-red-400" />
                        Guardian Veto (Cancel)
                      </button>
                    )}
                  </div>
                )}

                {/* Executed Badge */}
                {proposal.status === 'Executed' && (
                  <div className="text-xs text-emerald-400 font-medium flex items-center gap-1.5">
                    <CheckCircle2 className="w-4 h-4" />
                    Transaction executed and active in protocol state.
                  </div>
                )}

                <span className="text-[11px] font-mono text-slate-500">
                  Proposer: {proposal.proposer.slice(0, 8)}...
                </span>
              </div>
            </div>
          );
        })}
      </div>

      {/* CREATE PROPOSAL MODAL */}
      {showCreateModal && (
        <div className="fixed inset-0 z-50 bg-black/80 backdrop-blur-sm flex items-center justify-center p-4">
          <div className="w-full max-w-xl rounded-2xl bg-slate-900 border border-slate-800 p-6 shadow-2xl space-y-4">
            <div className="flex items-center justify-between border-b border-slate-800 pb-3">
              <div>
                <h3 className="text-base font-bold text-slate-100">Create DAO Proposal</h3>
                <p className="text-xs text-slate-400">
                  Proposal threshold required: 10,000 NGTT (You hold:{' '}
                  {Number(votingPower / 10n ** 18n).toLocaleString()})
                </p>
              </div>
              <button
                onClick={() => setShowCreateModal(false)}
                className="text-slate-400 hover:text-slate-200"
              >
                ✕
              </button>
            </div>

            <form onSubmit={handleCreateProposalSubmit} className="space-y-4">
              <div>
                <label className="block text-xs font-semibold text-slate-300 mb-1">Proposal Title</label>
                <input
                  type="text"
                  value={propTitle}
                  onChange={(e) => setPropTitle(e.target.value)}
                  placeholder="e.g. NIP-04: Allocate 50,000 NGTT to LP Staking Pool"
                  className="w-full px-3 py-2 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-200 focus:border-cyan-500 focus:outline-none"
                  required
                />
              </div>

              <div>
                <label className="block text-xs font-semibold text-slate-300 mb-1">
                  Description & Justification
                </label>
                <textarea
                  rows={3}
                  value={propDesc}
                  onChange={(e) => setPropDesc(e.target.value)}
                  placeholder="Detail the rationale, parameters, and risk assessment..."
                  className="w-full p-3 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-200 focus:border-cyan-500 focus:outline-none"
                  required
                />
              </div>

              <div className="grid grid-cols-2 gap-3">
                <div>
                  <label className="block text-xs font-semibold text-slate-300 mb-1">Target Contract</label>
                  <select
                    value={propTarget}
                    onChange={(e) => {
                      setPropTarget(e.target.value);
                      const found = NEXUS_CONTRACTS.find((c) => c.name === e.target.value);
                      if (found?.address) setPropAddress(found.address);
                    }}
                    className="w-full px-3 py-2 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-200 focus:border-cyan-500 focus:outline-none"
                  >
                    {NEXUS_CONTRACTS.map((c) => (
                      <option key={c.id} value={c.name}>
                        {c.name}
                      </option>
                    ))}
                  </select>
                </div>
                <div>
                  <label className="block text-xs font-semibold text-slate-300 mb-1">Target Address</label>
                  <input
                    type="text"
                    value={propAddress}
                    onChange={(e) => setPropAddress(e.target.value)}
                    className="w-full px-3 py-2 rounded-xl bg-slate-950 border border-slate-800 text-xs font-mono text-slate-200 focus:border-cyan-500 focus:outline-none"
                    required
                  />
                </div>
              </div>

              <div>
                <label className="block text-xs font-semibold text-slate-300 mb-1">Calldata Specification</label>
                <input
                  type="text"
                  value={propCalldata}
                  onChange={(e) => setPropCalldata(e.target.value)}
                  placeholder="e.g. refillRewardPool(50000000000000000000000)"
                  className="w-full px-3 py-2 rounded-xl bg-slate-950 border border-slate-800 text-xs font-mono text-slate-200 focus:border-cyan-500 focus:outline-none"
                  required
                />
              </div>

              <div className="flex items-center justify-end gap-3 pt-2">
                <button
                  type="button"
                  onClick={() => setShowCreateModal(false)}
                  className="px-4 py-2 rounded-xl bg-slate-800 text-slate-300 text-xs font-semibold hover:bg-slate-700 transition"
                >
                  Cancel
                </button>
                <button
                  type="submit"
                  className="px-5 py-2 rounded-xl bg-gradient-to-r from-cyan-600 to-blue-600 hover:from-cyan-500 hover:to-blue-500 text-white font-bold text-xs shadow-lg transition"
                >
                  Publish On-Chain Proposal
                </button>
              </div>
            </form>
          </div>
        </div>
      )}

      {/* DELEGATE MODAL */}
      {showDelegateModal && (
        <div className="fixed inset-0 z-50 bg-black/80 backdrop-blur-sm flex items-center justify-center p-4">
          <div className="w-full max-w-md rounded-2xl bg-slate-900 border border-slate-800 p-6 shadow-2xl space-y-4">
            <div className="flex items-center justify-between border-b border-slate-800 pb-3">
              <div>
                <h3 className="text-base font-bold text-slate-100">Delegate Voting Weight</h3>
                <p className="text-xs text-slate-400">
                  Activates your ERC20Votes checkpoints for proposal voting
                </p>
              </div>
              <button
                onClick={() => setShowDelegateModal(false)}
                className="text-slate-400 hover:text-slate-200"
              >
                ✕
              </button>
            </div>

            <div className="space-y-3">
              <div className="p-3 rounded-xl bg-slate-950 border border-slate-800 text-xs space-y-1">
                <div>Currently Delegated To:</div>
                <div className="font-mono text-cyan-400 break-all">{delegatedTo}</div>
              </div>

              <div className="space-y-2">
                <button
                  type="button"
                  onClick={() => {
                    delegateVotes(account);
                    setShowDelegateModal(false);
                  }}
                  className="w-full p-2.5 rounded-xl bg-slate-800 hover:bg-slate-700 text-left text-xs transition"
                >
                  <div className="font-semibold text-slate-200">Self-Delegate</div>
                  <div className="text-[11px] text-slate-400">Keep full voting authority on your own wallet</div>
                </button>

                <button
                  type="button"
                  onClick={() => {
                    delegateVotes(NEXUS_METADATA.ownerAddress);
                    setShowDelegateModal(false);
                  }}
                  className="w-full p-2.5 rounded-xl bg-slate-800 hover:bg-slate-700 text-left text-xs transition"
                >
                  <div className="font-semibold text-amber-300">Delegate to @FuzzysTodd (Founder)</div>
                  <div className="text-[11px] text-slate-400 font-mono">{NEXUS_METADATA.ownerAddress}</div>
                </button>
              </div>

              <form onSubmit={handleDelegateSubmit} className="pt-2 border-t border-slate-800 space-y-3">
                <div>
                  <label className="block text-xs font-semibold text-slate-300 mb-1">
                    Or Delegate to Custom Address
                  </label>
                  <input
                    type="text"
                    value={customDelegate}
                    onChange={(e) => setCustomDelegate(e.target.value)}
                    placeholder="0x..."
                    className="w-full px-3 py-2 rounded-xl bg-slate-950 border border-slate-800 text-xs font-mono text-slate-200 focus:border-cyan-500 focus:outline-none"
                    required
                  />
                </div>
                <button
                  type="submit"
                  className="w-full py-2.5 rounded-xl bg-cyan-600 hover:bg-cyan-500 text-white font-bold text-xs shadow-md transition"
                >
                  Confirm Delegation
                </button>
              </form>
            </div>
          </div>
        </div>
      )}
    </div>
  );
};
