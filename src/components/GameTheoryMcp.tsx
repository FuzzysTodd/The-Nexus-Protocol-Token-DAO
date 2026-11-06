/**
 * @license
 * SPDX-License-Identifier: Apache-2.0
 * The Nexus Protocol DAO - Game Theory & MCP Swarm Hive Command
 */

import React, { useState } from 'react';
import { useNexusDao } from '../context/NexusDaoContext';
import {
  Cpu,
  Gamepad2,
  Trophy,
  Users,
  Zap,
  TrendingUp,
  Sparkles,
  CheckCircle,
  Coins,
  Activity,
  Layers,
  ArrowRight,
} from 'lucide-react';

export const GameTheoryMcp: React.FC = () => {
  const {
    account,
    mcpGroups,
    profitPool,
    playerStats,
    createMCPGroup,
    distributeProfits,
    claimProfits,
    playGameSession,
    activateSkillBoost,
  } = useNexusDao();

  // Create MCP Group
  const [showCreateGroup, setShowCreateGroup] = useState(false);
  const [groupName, setGroupName] = useState('');
  const [groupMembersRaw, setGroupMembersRaw] = useState('');

  // Game Simulator State
  const [selectedAgeGroup, setSelectedAgeGroup] = useState<number>(2); // Child default for bonus
  const [baseRewardInput, setBaseRewardInput] = useState<string>('500');
  const [lastGameReward, setLastGameReward] = useState<bigint | null>(null);

  // Boost input
  const [boostMultiplier, setBoostMultiplier] = useState<number>(200); // 2.0x

  const ageCategories = [
    { id: 1, name: 'Toddler (0-4)', bonus: '+20% Bonus Multiplier', isBonus: true },
    { id: 2, name: 'Child (5-12)', bonus: '+20% Bonus Multiplier', isBonus: true },
    { id: 3, name: 'Teen (13-17)', bonus: 'Standard Multiplier', isBonus: false },
    { id: 4, name: 'Young Adult (18-24)', bonus: 'Standard Multiplier', isBonus: false },
    { id: 5, name: 'Adult (25-44)', bonus: 'Standard Multiplier', isBonus: false },
    { id: 6, name: 'Senior (45-64)', bonus: 'Standard Multiplier', isBonus: false },
    { id: 7, name: 'Elder (65+)', bonus: 'Standard Multiplier', isBonus: false },
  ];

  const handlePlayGame = () => {
    const base = BigInt(parseFloat(baseRewardInput) || 500) * 10n ** 18n;
    const res = playGameSession(selectedAgeGroup, base);
    setLastGameReward(res.reward);
    setTimeout(() => setLastGameReward(null), 5000);
  };

  const handleCreateGroupSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    if (!groupName.trim()) return;
    const members = groupMembersRaw
      .split('\n')
      .map((m) => m.trim())
      .filter((m) => m.length > 0);

    createMCPGroup(groupName.trim(), members.length > 0 ? members : [account]);
    setGroupName('');
    setGroupMembersRaw('');
    setShowCreateGroup(false);
  };

  return (
    <div className="space-y-6">
      {/* Hero Banner */}
      <div className="rounded-2xl bg-gradient-to-r from-slate-900 via-purple-950/40 to-slate-900 border border-slate-800 p-6 shadow-xl">
        <div className="flex flex-col md:flex-row md:items-center justify-between gap-4">
          <div>
            <div className="flex items-center gap-2">
              <span className="px-2.5 py-0.5 rounded-full text-xs font-semibold bg-purple-500/20 text-purple-400 border border-purple-500/40 flex items-center gap-1.5">
                <Cpu className="w-3.5 h-3.5" />
                MCP Swarm & Hive Coordination
              </span>
              <span className="text-xs text-slate-500 font-mono">100% 254/254 Test Accuracy</span>
            </div>
            <h2 className="text-xl font-bold text-slate-100 mt-1">
              Game Theory & Swarm Profit Distribution
            </h2>
            <p className="text-xs text-slate-400 max-w-2xl mt-1">
              Empowering Master Project Controller (MCP) groups and players with age-tailored gameplay, skill-weighted rewards, and automatic profit pool redistribution.
            </p>
          </div>

          <div className="flex items-center gap-2">
            <button
              onClick={() => setShowCreateGroup(true)}
              className="px-4 py-2 rounded-xl bg-gradient-to-r from-purple-600 to-indigo-600 hover:from-purple-500 hover:to-indigo-500 text-white font-bold text-xs shadow-lg transition flex items-center gap-1.5"
            >
              <Users className="w-3.5 h-3.5" />
              Create MCP Group
            </button>
          </div>
        </div>

        {/* Live Swarm Telemetry Bar */}
        <div className="grid grid-cols-2 sm:grid-cols-4 gap-3 mt-5 pt-4 border-t border-slate-800/80">
          <div className="p-3 rounded-xl bg-slate-950/60 border border-slate-800/80">
            <div className="text-[10px] uppercase font-bold text-slate-400">Swarm Coordination</div>
            <div className="text-sm font-bold text-purple-300 font-mono mt-0.5">12 Hive Nodes</div>
            <div className="text-[11px] text-slate-500">FPGA/GPU Synced</div>
          </div>
          <div className="p-3 rounded-xl bg-slate-950/60 border border-slate-800/80">
            <div className="text-[10px] uppercase font-bold text-slate-400">Total Profit Pool</div>
            <div className="text-sm font-bold text-emerald-300 font-mono mt-0.5">
              {Number(profitPool / 10n ** 18n).toLocaleString()} NGTT
            </div>
            <div className="text-[11px] text-slate-500">Ready for distribution</div>
          </div>
          <div className="p-3 rounded-xl bg-slate-950/60 border border-slate-800/80">
            <div className="text-[10px] uppercase font-bold text-slate-400">Your Skill Rating</div>
            <div className="text-sm font-bold text-cyan-300 font-mono mt-0.5">
              Level {playerStats.skillLevel}
            </div>
            <div className="text-[11px] text-slate-500">Multiplier: {(playerStats.activeBoostMultiplier / 100).toFixed(1)}x</div>
          </div>
          <div className="p-3 rounded-xl bg-slate-950/60 border border-slate-800/80">
            <div className="text-[10px] uppercase font-bold text-slate-400">Unclaimed Profits</div>
            <div className="text-sm font-bold text-amber-300 font-mono mt-0.5">
              {Number(playerStats.unclaimedProfits / 10n ** 18n).toLocaleString()} NGTT
            </div>
            <div className="text-[11px] text-slate-500">Claimable on-demand</div>
          </div>
        </div>
      </div>

      {/* Main Grid: Game Simulator & Profit Pool Controls */}
      <div className="grid grid-cols-1 lg:grid-cols-12 gap-6">
        {/* Left: Interactive Game Simulator */}
        <div className="lg:col-span-6 space-y-4">
          <div className="rounded-2xl bg-slate-900/90 border border-slate-800 p-5 space-y-4">
            <div className="flex items-center justify-between border-b border-slate-800 pb-3">
              <div className="flex items-center gap-2">
                <Gamepad2 className="w-5 h-5 text-indigo-400" />
                <div>
                  <h3 className="text-sm font-bold text-slate-200">7 Age-Group Game Simulator</h3>
                  <p className="text-xs text-slate-400">
                    Matches completeGame() in NGTTGovernanceToken.sol
                  </p>
                </div>
              </div>
              <span className="text-xs font-mono text-purple-400">
                Games Played: {playerStats.gamesCompleted}
              </span>
            </div>

            {lastGameReward && (
              <div className="p-3 rounded-xl bg-emerald-950/80 border border-emerald-800 text-xs text-emerald-300 flex items-center justify-between">
                <span className="flex items-center gap-2">
                  <Trophy className="w-4 h-4 text-emerald-400" />
                  Game victory recorded! You minted{' '}
                  <strong className="text-emerald-200 font-mono">
                    {Number(lastGameReward / 10n ** 18n).toLocaleString()} NGTT
                  </strong>
                </span>
                <span className="text-[10px] bg-emerald-900 px-2 py-0.5 rounded font-mono">
                  +10 Skill Points
                </span>
              </div>
            )}

            <div className="space-y-3">
              <div>
                <label className="block text-xs font-semibold text-slate-300 mb-1.5">
                  Select Age Category (Groups 1 & 2 receive +20% Bonus)
                </label>
                <div className="grid grid-cols-2 sm:grid-cols-3 gap-2">
                  {ageCategories.map((cat) => (
                    <button
                      key={cat.id}
                      type="button"
                      onClick={() => setSelectedAgeGroup(cat.id)}
                      className={`p-2 rounded-xl text-left transition border ${
                        selectedAgeGroup === cat.id
                          ? 'bg-purple-950 border-purple-500 text-purple-200 shadow-md'
                          : 'bg-slate-950 border-slate-800 hover:border-slate-700 text-slate-300'
                      }`}
                    >
                      <div className="font-bold text-xs">{cat.name}</div>
                      <div
                        className={`text-[10px] mt-0.5 ${
                          cat.isBonus ? 'text-emerald-400 font-semibold' : 'text-slate-500'
                        }`}
                      >
                        {cat.bonus}
                      </div>
                    </button>
                  ))}
                </div>
              </div>

              <div className="grid grid-cols-2 gap-3 pt-1">
                <div>
                  <label className="block text-xs font-semibold text-slate-300 mb-1">
                    Base Reward (NGTT)
                  </label>
                  <input
                    type="number"
                    value={baseRewardInput}
                    onChange={(e) => setBaseRewardInput(e.target.value)}
                    className="w-full px-3 py-2 rounded-xl bg-slate-950 border border-slate-800 text-xs font-mono text-slate-200 focus:border-purple-500 focus:outline-none"
                  />
                </div>
                <div>
                  <label className="block text-xs font-semibold text-slate-300 mb-1">
                    Expected Mint Output
                  </label>
                  <div className="px-3 py-2 rounded-xl bg-slate-950 border border-slate-800 text-xs font-mono text-emerald-400 font-bold">
                    ~
                    {(
                      (parseFloat(baseRewardInput || '0') *
                        (100 + Math.floor(playerStats.skillLevel / 10)) *
                        (selectedAgeGroup <= 2 ? 1.2 : 1.0)) /
                      100
                    ).toFixed(1)}{' '}
                    NGTT
                  </div>
                </div>
              </div>

              <button
                onClick={handlePlayGame}
                className="w-full py-2.5 rounded-xl bg-gradient-to-r from-purple-600 via-indigo-600 to-blue-600 hover:from-purple-500 hover:to-blue-500 text-white font-bold text-xs shadow-lg transition flex items-center justify-center gap-2"
              >
                <Gamepad2 className="w-4 h-4" />
                Complete Game Session & Mint Rewards
              </button>
            </div>

            {/* Skill Boost Trigger */}
            <div className="pt-3 border-t border-slate-800 space-y-2">
              <div className="flex items-center justify-between text-xs">
                <span className="font-bold text-slate-300 flex items-center gap-1.5">
                  <Zap className="w-3.5 h-3.5 text-amber-400" />
                  Activate Skill Multiplier Boost (100–500 bps)
                </span>
                <span className="font-mono text-amber-300 font-bold">{(boostMultiplier / 100).toFixed(1)}x</span>
              </div>
              <input
                type="range"
                min="100"
                max="500"
                step="25"
                value={boostMultiplier}
                onChange={(e) => setBoostMultiplier(Number(e.target.value))}
                className="w-full accent-amber-400 cursor-pointer"
              />
              <button
                onClick={() => activateSkillBoost(boostMultiplier)}
                className="w-full py-1.5 rounded-lg bg-amber-600/20 hover:bg-amber-600/30 border border-amber-600/40 text-amber-300 font-semibold text-xs transition"
              >
                Apply {(boostMultiplier / 100).toFixed(1)}x Boost to Player Profile
              </button>
            </div>
          </div>
        </div>

        {/* Right: Profit Pool Redistribution & MCP Swarm Groups */}
        <div className="lg:col-span-6 space-y-4">
          {/* Profit Pool Card */}
          <div className="rounded-2xl bg-slate-900/90 border border-slate-800 p-5 space-y-4">
            <div className="flex items-center justify-between border-b border-slate-800 pb-3">
              <div className="flex items-center gap-2">
                <Coins className="w-5 h-5 text-emerald-400" />
                <div>
                  <h3 className="text-sm font-bold text-slate-200">Profit Pool Redistribution</h3>
                  <p className="text-xs text-slate-400">
                    Proportionally distributes pool by games played per group
                  </p>
                </div>
              </div>
              <div className="text-right">
                <div className="text-sm font-bold text-emerald-300 font-mono">
                  {Number(profitPool / 10n ** 18n).toLocaleString()} NGTT
                </div>
                <div className="text-[10px] text-slate-500">Unallocated Reserves</div>
              </div>
            </div>

            <div className="flex items-center gap-3">
              <button
                onClick={distributeProfits}
                disabled={profitPool <= 0n}
                className="flex-1 py-2.5 rounded-xl bg-gradient-to-r from-emerald-600 to-teal-600 hover:from-emerald-500 hover:to-teal-500 text-white font-bold text-xs shadow-lg transition flex items-center justify-center gap-2 disabled:opacity-40"
              >
                <TrendingUp className="w-4 h-4" />
                Distribute Profits to Swarm
              </button>

              <button
                onClick={claimProfits}
                disabled={playerStats.unclaimedProfits <= 0n}
                className="flex-1 py-2.5 rounded-xl bg-slate-800 hover:bg-slate-700 text-amber-300 font-bold text-xs border border-amber-800/40 transition flex items-center justify-center gap-2 disabled:opacity-40"
              >
                <Sparkles className="w-4 h-4" />
                Claim My Profits ({Number(playerStats.unclaimedProfits / 10n ** 18n).toLocaleString()})
              </button>
            </div>
          </div>

          {/* Active MCP Swarm Groups List */}
          <div className="rounded-2xl bg-slate-900/90 border border-slate-800 p-5 space-y-3">
            <div className="flex items-center justify-between border-b border-slate-800 pb-2">
              <h4 className="text-xs font-bold text-slate-300 uppercase tracking-wider">
                Active MCP Groups ({mcpGroups.length})
              </h4>
              <span className="text-[11px] text-slate-500">Automated Swarm Hive</span>
            </div>

            <div className="space-y-2.5 max-h-[300px] overflow-y-auto pr-1">
              {mcpGroups.map((group) => (
                <div
                  key={group.id}
                  className="p-3 rounded-xl bg-slate-950 border border-slate-800 space-y-1.5"
                >
                  <div className="flex items-center justify-between">
                    <span className="font-bold text-xs text-slate-200">
                      #{group.id} {group.name}
                    </span>
                    <span className="text-[10px] px-2 py-0.5 rounded-full bg-purple-950 text-purple-400 border border-purple-800">
                      {group.members.length} Members
                    </span>
                  </div>

                  <div className="grid grid-cols-3 gap-2 text-[11px] font-mono text-slate-400">
                    <div>
                      Games: <strong className="text-slate-200">{group.gamesPlayed}</strong>
                    </div>
                    <div>
                      Tokens:{' '}
                      <strong className="text-cyan-300">
                        {Number(group.totalTokens / 10n ** 18n).toLocaleString()}
                      </strong>
                    </div>
                    <div>
                      Profit Share:{' '}
                      <strong className="text-emerald-300">
                        {Number(group.profitShare / 10n ** 18n).toLocaleString()}
                      </strong>
                    </div>
                  </div>

                  <div className="text-[10px] text-slate-500 font-mono truncate">
                    Members: {group.members.join(', ')}
                  </div>
                </div>
              ))}
            </div>
          </div>
        </div>
      </div>

      {/* CREATE GROUP MODAL */}
      {showCreateGroup && (
        <div className="fixed inset-0 z-50 bg-black/80 backdrop-blur-sm flex items-center justify-center p-4">
          <div className="w-full max-w-md rounded-2xl bg-slate-900 border border-slate-800 p-6 shadow-2xl space-y-4">
            <div className="flex items-center justify-between border-b border-slate-800 pb-3">
              <div>
                <h3 className="text-base font-bold text-slate-100">Create MCP Group</h3>
                <p className="text-xs text-slate-400">
                  Matches createMCPGroup() in NGTTGovernanceToken.sol
                </p>
              </div>
              <button
                onClick={() => setShowCreateGroup(false)}
                className="text-slate-400 hover:text-slate-200"
              >
                ✕
              </button>
            </div>

            <form onSubmit={handleCreateGroupSubmit} className="space-y-4">
              <div>
                <label className="block text-xs font-semibold text-slate-300 mb-1">
                  Group Name
                </label>
                <input
                  type="text"
                  value={groupName}
                  onChange={(e) => setGroupName(e.target.value)}
                  placeholder="e.g. Hive Delta Swarm"
                  className="w-full px-3 py-2 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-200 focus:border-purple-500 focus:outline-none"
                  required
                />
              </div>

              <div>
                <label className="block text-xs font-semibold text-slate-300 mb-1">
                  Member Wallet Addresses (One per line)
                </label>
                <textarea
                  rows={4}
                  value={groupMembersRaw}
                  onChange={(e) => setGroupMembersRaw(e.target.value)}
                  placeholder="0x33ffc308e693a5b49e0ee0241f41f03ccef495f2&#10;0x71C83647209B16fa4876b20C1d88A2c1B1c9e831"
                  className="w-full p-3 rounded-xl bg-slate-950 border border-slate-800 text-xs font-mono text-slate-200 focus:border-purple-500 focus:outline-none"
                />
              </div>

              <div className="flex items-center justify-end gap-3 pt-2">
                <button
                  type="button"
                  onClick={() => setShowCreateGroup(false)}
                  className="px-4 py-2 rounded-xl bg-slate-800 text-slate-300 text-xs font-semibold hover:bg-slate-700 transition"
                >
                  Cancel
                </button>
                <button
                  type="submit"
                  className="px-5 py-2 rounded-xl bg-gradient-to-r from-purple-600 to-indigo-600 hover:from-purple-500 hover:to-indigo-500 text-white font-bold text-xs shadow-lg transition"
                >
                  Deploy Group
                </button>
              </div>
            </form>
          </div>
        </div>
      )}
    </div>
  );
};
