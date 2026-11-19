/**
 * @license
 * SPDX-License-Identifier: Apache-2.0
 * The Nexus Protocol DAO - Real-Time Transaction & Event Console
 */

import React, { useState } from 'react';
import { useNexusDao } from '../context/NexusDaoContext';
import { Terminal, CheckCircle2, ChevronRight, Search, Trash2 } from 'lucide-react';

export const TransactionConsole: React.FC = () => {
  const { executionLogs } = useNexusDao();
  const [filterQuery, setFilterQuery] = useState('');
  const [isExpanded, setIsExpanded] = useState(false);

  const filteredLogs = executionLogs.filter(
    (log) =>
      log.method.toLowerCase().includes(filterQuery.toLowerCase()) ||
      log.target.toLowerCase().includes(filterQuery.toLowerCase()) ||
      log.details.toLowerCase().includes(filterQuery.toLowerCase())
  );

  return (
    <div className="rounded-2xl bg-slate-950 border border-slate-800 overflow-hidden shadow-2xl">
      {/* Console Header Bar */}
      <div className="bg-slate-900/90 px-4 py-2.5 flex items-center justify-between border-b border-slate-800">
        <div className="flex items-center gap-2">
          <Terminal className="w-4 h-4 text-cyan-400" />
          <span className="text-xs font-bold text-slate-200 uppercase tracking-wider">
            DAO On-Chain Execution Bus ({executionLogs.length} Events)
          </span>
          <span className="w-2 h-2 rounded-full bg-emerald-500 animate-ping" />
        </div>

        <div className="flex items-center gap-3">
          <div className="relative">
            <Search className="w-3 h-3 text-slate-500 absolute left-2.5 top-2" />
            <input
              type="text"
              value={filterQuery}
              onChange={(e) => setFilterQuery(e.target.value)}
              placeholder="Filter events..."
              className="pl-7 pr-2.5 py-1 rounded-lg bg-slate-950 border border-slate-800 text-[11px] text-slate-300 font-mono focus:outline-none focus:border-cyan-500"
            />
          </div>

          <button
            onClick={() => setIsExpanded(!isExpanded)}
            className="text-xs text-slate-400 hover:text-slate-200 font-mono transition"
          >
            {isExpanded ? 'Collapse' : 'Expand'}
          </button>
        </div>
      </div>

      {/* Console Body */}
      <div
        className={`p-3 font-mono text-xs space-y-2 overflow-y-auto ${
          isExpanded ? 'max-h-96' : 'max-h-48'
        }`}
      >
        {filteredLogs.length === 0 ? (
          <div className="text-slate-600 text-center py-4">No events matching filter.</div>
        ) : (
          filteredLogs.map((log) => (
            <div
              key={log.id}
              className="p-2.5 rounded-lg bg-slate-900/60 border border-slate-800/80 hover:border-slate-700 transition space-y-1"
            >
              <div className="flex items-center justify-between text-[11px]">
                <div className="flex items-center gap-2 text-cyan-400">
                  <span className="text-slate-500">{log.timestamp}</span>
                  <span className="font-bold">[{log.target}]</span>
                  <span className="text-slate-200">{log.method}</span>
                </div>
                <div className="flex items-center gap-2">
                  <span className="text-emerald-400 font-bold flex items-center gap-1">
                    <CheckCircle2 className="w-3 h-3" /> {log.status}
                  </span>
                  <span className="text-slate-500 font-mono">{log.txHash}</span>
                </div>
              </div>
              <div className="text-[11px] text-slate-400 pl-4 border-l border-slate-800">
                {log.details}
              </div>
            </div>
          ))
        )}
      </div>
    </div>
  );
};
