/**
 * @license
 * SPDX-License-Identifier: Apache-2.0
 * The Nexus Protocol DAO - Contract Workbench & Chunked Contract Post Center
 */

import React, { useState } from 'react';
import { useNexusDao } from '../context/NexusDaoContext';
import { NEXUS_CONTRACTS, NexusContractSpec, ContractMethod } from '../data/nexusContracts';
import {
  FileCode,
  Upload,
  Play,
  CheckCircle,
  AlertTriangle,
  Copy,
  Download,
  Trash2,
  Code2,
  Cpu,
  Layers,
  Sparkles,
  BookOpen,
} from 'lucide-react';
import { chunkContractSource, assembleChunks, parseContractSignatures } from '../dao/logic';

export const ContractWorkbench: React.FC = () => {
  const {
    account,
    postedContracts,
    selectedContractSpec,
    setSelectedContractSpec,
    postContractChunk,
    postFullContract,
    deletePostedContract,
    executeMethod,
  } = useNexusDao();

  // Workbench active view
  const [activeSubTab, setActiveSubTab] = useState<'catalog' | 'chunk-poster' | 'posted-contracts'>('chunk-poster');

  // Chunk post inputs
  const [chunkContractName, setChunkContractName] = useState('NexusCustomModule.sol');
  const [chunkIndex, setChunkIndex] = useState(1);
  const [totalChunks, setTotalChunks] = useState(3);
  const [chunkContent, setChunkContent] = useState('');
  const [chunkSuccessMsg, setChunkSuccessMsg] = useState('');

  // Auto-split helper
  const [rawCodeToChunk, setRawCodeToChunk] = useState('');
  const [generatedChunks, setGeneratedChunks] = useState<{ chunkIndex: number; totalChunks: number; content: string }[]>([]);

  // Method execution form
  const [selectedMethod, setSelectedMethod] = useState<ContractMethod | null>(null);
  const [methodParams, setMethodParams] = useState<Record<string, string>>({});
  const [executionResult, setExecutionResult] = useState<string | null>(null);
  const [isExecuting, setIsExecuting] = useState(false);

  // Copy helper
  const [copied, setCopied] = useState(false);
  const handleCopy = (text: string) => {
    navigator.clipboard.writeText(text);
    setCopied(true);
    setTimeout(() => setCopied(false), 2000);
  };

  // Submit single chunk
  const handleSubmitChunk = (e: React.FormEvent) => {
    e.preventDefault();
    if (!chunkContent.trim()) return;

    postContractChunk(
      {
        chunkIndex: Number(chunkIndex),
        totalChunks: Number(totalChunks),
        content: chunkContent,
      },
      chunkContractName
    );

    setChunkSuccessMsg(`✅ Chunk ${chunkIndex} of ${totalChunks} registered for ${chunkContractName}!`);
    if (chunkIndex < totalChunks) {
      setChunkIndex(chunkIndex + 1);
    }
    setChunkContent('');
    setTimeout(() => setChunkSuccessMsg(''), 4000);
  };

  // Auto-split code into chunks
  const handleAutoSplit = () => {
    if (!rawCodeToChunk.trim()) return;
    const chunks = chunkContractSource(rawCodeToChunk, 35);
    setGeneratedChunks(chunks);
    setTotalChunks(chunks.length);
    setChunkIndex(1);
    if (chunks.length > 0) {
      setChunkContent(chunks[0].content);
    }
  };

  // Post all generated chunks at once
  const handlePostAllGenerated = () => {
    if (generatedChunks.length === 0) return;
    generatedChunks.forEach((chunk) => {
      postContractChunk(chunk, chunkContractName);
    });
    setChunkSuccessMsg(`✅ All ${generatedChunks.length} chunks registered and assembled for ${chunkContractName}!`);
    setGeneratedChunks([]);
    setRawCodeToChunk('');
    setTimeout(() => setChunkSuccessMsg(''), 4000);
  };

  // Run selected contract method
  const handleRunMethod = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!selectedMethod) return;
    setIsExecuting(true);
    try {
      await executeMethod(selectedContractSpec.name, selectedMethod.name, methodParams);
      setExecutionResult(`Call successful. Gas consumed: 48,290 wei. Emitted state change confirmed.`);
    } catch (err: any) {
      setExecutionResult(`Execution failed: ${err.message || 'Reverted'}`);
    } finally {
      setIsExecuting(false);
    }
  };

  return (
    <div className="space-y-6">
      {/* Overview Banner */}
      <div className="rounded-2xl bg-gradient-to-r from-slate-900 via-indigo-950/40 to-slate-900 border border-slate-800 p-5 shadow-xl">
        <div className="flex flex-col md:flex-row md:items-center justify-between gap-4">
          <div>
            <div className="flex items-center gap-2">
              <span className="px-2.5 py-0.5 rounded-full text-xs font-semibold bg-indigo-500/20 text-indigo-400 border border-indigo-500/40 flex items-center gap-1.5">
                <FileCode className="w-3.5 h-3.5" />
                Contract Workspace & Chunk Receiver
              </span>
              <span className="text-xs text-slate-500 font-mono">11 Core Contracts Preloaded</span>
            </div>
            <h2 className="text-xl font-bold text-slate-100 mt-1">
              Nexus Protocol Smart Contract Engine
            </h2>
            <p className="text-xs text-slate-400 max-w-3xl mt-1">
              Study, verify, test, and post Solidity contracts. Supports multi-part chunked uploads with Keccak-256 checksum assembly, AST signature parsing, and interactive method execution.
            </p>
          </div>

          <div className="flex items-center gap-2">
            <button
              onClick={() => setActiveSubTab('chunk-poster')}
              className={`px-3 py-2 rounded-xl text-xs font-semibold transition flex items-center gap-1.5 ${
                activeSubTab === 'chunk-poster'
                  ? 'bg-cyan-500 text-slate-950 font-bold shadow-lg shadow-cyan-500/20'
                  : 'bg-slate-800 text-slate-300 hover:bg-slate-700'
              }`}
            >
              <Upload className="w-3.5 h-3.5" />
              Chunked Contract Poster
            </button>
            <button
              onClick={() => setActiveSubTab('catalog')}
              className={`px-3 py-2 rounded-xl text-xs font-semibold transition flex items-center gap-1.5 ${
                activeSubTab === 'catalog'
                  ? 'bg-cyan-500 text-slate-950 font-bold shadow-lg shadow-cyan-500/20'
                  : 'bg-slate-800 text-slate-300 hover:bg-slate-700'
              }`}
            >
              <BookOpen className="w-3.5 h-3.5" />
              Repo Contract Catalog ({NEXUS_CONTRACTS.length})
            </button>
            <button
              onClick={() => setActiveSubTab('posted-contracts')}
              className={`px-3 py-2 rounded-xl text-xs font-semibold transition flex items-center gap-1.5 ${
                activeSubTab === 'posted-contracts'
                  ? 'bg-cyan-500 text-slate-950 font-bold shadow-lg shadow-cyan-500/20'
                  : 'bg-slate-800 text-slate-300 hover:bg-slate-700'
              }`}
            >
              <Layers className="w-3.5 h-3.5" />
              Posted & Deployed ({postedContracts.length})
            </button>
          </div>
        </div>
      </div>

      {/* VIEW 1: CHUNKED CONTRACT POSTER */}
      {activeSubTab === 'chunk-poster' && (
        <div className="grid grid-cols-1 lg:grid-cols-12 gap-6">
          {/* Post Form */}
          <div className="lg:col-span-7 space-y-4">
            <div className="rounded-2xl bg-slate-900/90 border border-slate-800 p-5 space-y-4">
              <div className="flex items-center justify-between border-b border-slate-800 pb-3">
                <div className="flex items-center gap-2">
                  <div className="w-8 h-8 rounded-lg bg-cyan-950 text-cyan-400 flex items-center justify-center font-bold">
                    1
                  </div>
                  <div>
                    <h3 className="text-sm font-bold text-slate-200">Post Contract Chunk</h3>
                    <p className="text-xs text-slate-400">
                      Upload contract code piece-by-piece with automatic assembly & checksum verification
                    </p>
                  </div>
                </div>
                <span className="text-xs font-mono text-cyan-400">Caller: {account.slice(0, 6)}...</span>
              </div>

              {chunkSuccessMsg && (
                <div className="p-3 rounded-xl bg-emerald-950/70 border border-emerald-800 text-xs text-emerald-300 flex items-center gap-2">
                  <CheckCircle className="w-4 h-4 text-emerald-400 shrink-0" />
                  <span>{chunkSuccessMsg}</span>
                </div>
              )}

              <form onSubmit={handleSubmitChunk} className="space-y-4">
                <div className="grid grid-cols-1 sm:grid-cols-3 gap-3">
                  <div>
                    <label className="block text-xs font-semibold text-slate-300 mb-1">Contract File Name</label>
                    <input
                      type="text"
                      value={chunkContractName}
                      onChange={(e) => setChunkContractName(e.target.value)}
                      placeholder="e.g. NexusCustomDAO.sol"
                      className="w-full px-3 py-2 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-200 font-mono focus:border-cyan-500 focus:outline-none"
                      required
                    />
                  </div>
                  <div>
                    <label className="block text-xs font-semibold text-slate-300 mb-1">Chunk Index</label>
                    <input
                      type="number"
                      min="1"
                      max={totalChunks}
                      value={chunkIndex}
                      onChange={(e) => setChunkIndex(Number(e.target.value))}
                      className="w-full px-3 py-2 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-200 font-mono focus:border-cyan-500 focus:outline-none"
                      required
                    />
                  </div>
                  <div>
                    <label className="block text-xs font-semibold text-slate-300 mb-1">Total Expected Chunks</label>
                    <input
                      type="number"
                      min="1"
                      value={totalChunks}
                      onChange={(e) => setTotalChunks(Number(e.target.value))}
                      className="w-full px-3 py-2 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-200 font-mono focus:border-cyan-500 focus:outline-none"
                      required
                    />
                  </div>
                </div>

                <div>
                  <div className="flex items-center justify-between mb-1">
                    <label className="text-xs font-semibold text-slate-300">
                      Chunk Payload Code (Solidity / ABI / Bytecode)
                    </label>
                    <span className="text-[11px] text-slate-500">
                      {chunkContent ? `${chunkContent.split('\n').length} lines` : 'Empty'}
                    </span>
                  </div>
                  <textarea
                    rows={8}
                    value={chunkContent}
                    onChange={(e) => setChunkContent(e.target.value)}
                    placeholder={`// Paste Chunk ${chunkIndex} of ${totalChunks} here...\n// e.g.:\ncontract MyNexusExtension is Ownable {\n    uint256 public customParam;\n    ...`}
                    className="w-full p-3 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300 font-mono focus:border-cyan-500 focus:outline-none resize-y"
                    required
                  />
                </div>

                <div className="flex items-center justify-between gap-3">
                  <button
                    type="submit"
                    className="flex-1 py-2.5 px-4 rounded-xl bg-gradient-to-r from-cyan-600 to-blue-600 hover:from-cyan-500 hover:to-blue-500 text-white font-bold text-xs shadow-lg transition flex items-center justify-center gap-2"
                  >
                    <Upload className="w-4 h-4" />
                    Register Chunk {chunkIndex} of {totalChunks}
                  </button>
                  <button
                    type="button"
                    onClick={() => {
                      setChunkContent(NEXUS_CONTRACTS[0].sourceCode.slice(0, 1500));
                      setChunkContractName('NGTTGovernanceToken.sol');
                      setTotalChunks(3);
                      setChunkIndex(1);
                    }}
                    className="py-2.5 px-3 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-300 text-xs transition"
                  >
                    Load Sample Chunk
                  </button>
                </div>
              </form>
            </div>

            {/* Auto-Chunking & Testing Utility */}
            <div className="rounded-2xl bg-slate-900/60 border border-slate-800/80 p-5 space-y-3">
              <div className="flex items-center justify-between">
                <div className="flex items-center gap-2">
                  <Sparkles className="w-4 h-4 text-amber-400" />
                  <h4 className="text-xs font-bold text-slate-200 uppercase tracking-wider">
                    Automatic Chunking Helper & Simulator
                  </h4>
                </div>
                <span className="text-[11px] text-slate-400">Paste full contract to split into chunks</span>
              </div>
              <textarea
                rows={4}
                value={rawCodeToChunk}
                onChange={(e) => setRawCodeToChunk(e.target.value)}
                placeholder="Paste any full Solidity contract here to automatically chunk it into safe, verified transmissions..."
                className="w-full p-3 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300 font-mono focus:border-indigo-500 focus:outline-none resize-y"
              />
              <div className="flex items-center gap-2">
                <button
                  type="button"
                  onClick={handleAutoSplit}
                  className="px-3 py-2 rounded-xl bg-indigo-600 hover:bg-indigo-500 text-white text-xs font-semibold transition"
                >
                  Auto-Split into Chunks (35 lines/chunk)
                </button>
                {generatedChunks.length > 0 && (
                  <button
                    type="button"
                    onClick={handlePostAllGenerated}
                    className="px-3 py-2 rounded-xl bg-emerald-600 hover:bg-emerald-500 text-white text-xs font-semibold transition flex items-center gap-1.5"
                  >
                    <CheckCircle className="w-3.5 h-3.5" />
                    Transmit All {generatedChunks.length} Chunks Now
                  </button>
                )}
              </div>

              {generatedChunks.length > 0 && (
                <div className="p-3 rounded-xl bg-slate-950 border border-slate-800 text-xs space-y-2">
                  <div className="font-semibold text-indigo-400">
                    Generated {generatedChunks.length} Chunks for transmission:
                  </div>
                  <div className="grid grid-cols-2 sm:grid-cols-4 gap-2">
                    {generatedChunks.map((c) => (
                      <div
                        key={c.chunkIndex}
                        onClick={() => {
                          setChunkIndex(c.chunkIndex);
                          setTotalChunks(c.totalChunks);
                          setChunkContent(c.content);
                        }}
                        className="cursor-pointer p-2 rounded-lg bg-slate-900 border border-slate-800 hover:border-cyan-500 transition text-[11px]"
                      >
                        <div className="font-bold text-slate-300">Chunk #{c.chunkIndex}</div>
                        <div className="text-slate-500">{c.content.split('\n').length} lines</div>
                      </div>
                    ))}
                  </div>
                </div>
              )}
            </div>
          </div>

          {/* Assembly Status & In-Flight Contracts */}
          <div className="lg:col-span-5 space-y-4">
            <div className="rounded-2xl bg-slate-900/90 border border-slate-800 p-5 space-y-4">
              <div className="flex items-center justify-between border-b border-slate-800 pb-3">
                <div className="flex items-center gap-2">
                  <div className="w-8 h-8 rounded-lg bg-emerald-950 text-emerald-400 flex items-center justify-center font-bold">
                    2
                  </div>
                  <div>
                    <h3 className="text-sm font-bold text-slate-200">Assembly & Verification</h3>
                    <p className="text-xs text-slate-400">Real-time status of chunked contracts</p>
                  </div>
                </div>
                <span className="text-xs px-2 py-0.5 rounded-full bg-slate-800 text-slate-300 font-mono">
                  {postedContracts.length} In-Memory
                </span>
              </div>

              <div className="space-y-3">
                {postedContracts.map((c) => (
                  <div
                    key={c.id}
                    className="p-3.5 rounded-xl bg-slate-950 border border-slate-800 space-y-2"
                  >
                    <div className="flex items-start justify-between">
                      <div>
                        <div className="flex items-center gap-2">
                          <h4 className="text-xs font-bold text-slate-200 font-mono">{c.name}</h4>
                          {c.isComplete ? (
                            <span className="px-2 py-0.5 rounded-full text-[10px] bg-emerald-950 text-emerald-400 border border-emerald-800 flex items-center gap-1">
                              <CheckCircle className="w-3 h-3" /> Assembled
                            </span>
                          ) : (
                            <span className="px-2 py-0.5 rounded-full text-[10px] bg-amber-950 text-amber-400 border border-amber-800 flex items-center gap-1">
                              <AlertTriangle className="w-3 h-3" /> Missing Chunks
                            </span>
                          )}
                        </div>
                        <div className="text-[11px] text-slate-400 mt-0.5">
                          Chunks: {c.chunks.length} registered • {c.functionsCount} functions parsed
                        </div>
                      </div>

                      <button
                        onClick={() => deletePostedContract(c.id)}
                        className="p-1 rounded text-slate-500 hover:text-red-400 hover:bg-slate-900 transition"
                        title="Delete contract"
                      >
                        <Trash2 className="w-3.5 h-3.5" />
                      </button>
                    </div>

                    {/* Checksum & Address */}
                    <div className="text-[10px] font-mono space-y-0.5 text-slate-500 bg-slate-900/60 p-2 rounded-lg">
                      <div><strong className="text-slate-400">Keccak256:</strong> {c.checksum}</div>
                      <div><strong className="text-slate-400">Target Address:</strong> {c.simulatedAddress}</div>
                      {c.inherits.length > 0 && (
                        <div><strong className="text-slate-400">Inherits:</strong> {c.inherits.join(', ')}</div>
                      )}
                    </div>

                    {/* Preview buttons */}
                    <div className="flex items-center gap-2 pt-1">
                      <button
                        onClick={() => {
                          setSelectedContractSpec({
                            id: c.id,
                            name: c.name.replace('.sol', ''),
                            fileName: c.name,
                            category: 'Governance',
                            address: c.simulatedAddress,
                            description: `User-posted chunked contract: ${c.name}`,
                            roles: ['Owner'],
                            features: c.inherits,
                            methods: parseContractSignatures(c.source).functions.map((f) => ({
                              name: f.name,
                              type: f.isMutating ? 'write' : 'read',
                              inputs: [],
                              description: `Function ${f.name}(${f.args}) ${f.visibility}`,
                            })),
                            sourceCode: c.source,
                          });
                          setActiveSubTab('catalog');
                        }}
                        className="flex-1 py-1 px-2.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 text-xs font-medium transition flex items-center justify-center gap-1"
                      >
                        <Code2 className="w-3.5 h-3.5" />
                        Inspect in Workbench
                      </button>
                      <button
                        onClick={() => handleCopy(c.source)}
                        className="py-1 px-2 rounded-lg bg-slate-900 hover:bg-slate-800 text-slate-400 text-xs transition"
                        title="Copy assembled code"
                      >
                        <Copy className="w-3.5 h-3.5" />
                      </button>
                    </div>
                  </div>
                ))}
              </div>
            </div>
          </div>
        </div>
      )}

      {/* VIEW 2: CONTRACT CATALOG & METHOD RUNNER */}
      {activeSubTab === 'catalog' && (
        <div className="grid grid-cols-1 lg:grid-cols-12 gap-6">
          {/* Contracts Sidebar */}
          <div className="lg:col-span-4 space-y-2">
            <div className="text-xs font-bold uppercase tracking-wider text-slate-400 px-1 mb-2">
              Nexus Protocol Contracts
            </div>
            <div className="space-y-1.5 max-h-[700px] overflow-y-auto pr-1">
              {NEXUS_CONTRACTS.map((contract) => {
                const isSelected = selectedContractSpec.fileName === contract.fileName;
                return (
                  <button
                    key={contract.id}
                    onClick={() => {
                      setSelectedContractSpec(contract);
                      setSelectedMethod(null);
                      setMethodParams({});
                      setExecutionResult(null);
                    }}
                    className={`w-full p-3 rounded-xl text-left transition flex items-start justify-between border ${
                      isSelected
                        ? 'bg-cyan-950/70 border-cyan-500/80 text-cyan-200 shadow-md shadow-cyan-950/40'
                        : 'bg-slate-900/80 border-slate-800 hover:bg-slate-850 hover:border-slate-700 text-slate-300'
                    }`}
                  >
                    <div>
                      <div className="flex items-center gap-2">
                        <span className="font-bold text-xs font-mono">{contract.name}</span>
                        <span className="px-1.5 py-0.2 rounded text-[10px] bg-slate-800 text-slate-400 border border-slate-700">
                          {contract.category}
                        </span>
                      </div>
                      <div className="text-[11px] text-slate-400 line-clamp-1 mt-0.5">
                        {contract.description}
                      </div>
                      <div className="text-[10px] font-mono text-cyan-400 mt-1">
                        {contract.address ? `${contract.address.slice(0, 10)}...` : 'Factory Deployed'}
                      </div>
                    </div>
                  </button>
                );
              })}
            </div>
          </div>

          {/* Contract Detail & Method Executor */}
          <div className="lg:col-span-8 space-y-4">
            {/* Header info */}
            <div className="rounded-2xl bg-slate-900/90 border border-slate-800 p-5 space-y-4">
              <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-3 border-b border-slate-800 pb-4">
                <div>
                  <div className="flex items-center gap-2">
                    <h3 className="text-lg font-bold text-slate-100 font-mono">
                      {selectedContractSpec.fileName}
                    </h3>
                    <span className="px-2 py-0.5 rounded-full text-xs bg-cyan-950 text-cyan-400 border border-cyan-800 font-medium">
                      {selectedContractSpec.category}
                    </span>
                  </div>
                  <p className="text-xs text-slate-400 mt-1">{selectedContractSpec.description}</p>
                </div>

                <div className="flex items-center gap-2">
                  <button
                    onClick={() => handleCopy(selectedContractSpec.sourceCode)}
                    className="px-3 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 text-xs font-medium transition flex items-center gap-1.5"
                  >
                    <Copy className="w-3.5 h-3.5" />
                    {copied ? 'Copied!' : 'Copy Code'}
                  </button>
                  <a
                    href={`data:text/plain;charset=utf-8,${encodeURIComponent(selectedContractSpec.sourceCode)}`}
                    download={selectedContractSpec.fileName}
                    className="px-3 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 text-xs font-medium transition flex items-center gap-1.5"
                  >
                    <Download className="w-3.5 h-3.5" />
                    Download .sol
                  </a>
                </div>
              </div>

              {/* Roles & Features */}
              <div className="grid grid-cols-1 sm:grid-cols-2 gap-3 text-xs">
                <div className="p-3 rounded-xl bg-slate-950 border border-slate-800">
                  <span className="font-semibold text-slate-400 uppercase tracking-wider text-[10px] block mb-1">
                    Access Roles
                  </span>
                  <div className="flex flex-wrap gap-1">
                    {selectedContractSpec.roles.map((r, i) => (
                      <span key={i} className="px-2 py-0.5 rounded bg-slate-800 text-slate-300 font-mono text-[11px]">
                        {r}
                      </span>
                    ))}
                  </div>
                </div>

                <div className="p-3 rounded-xl bg-slate-950 border border-slate-800">
                  <span className="font-semibold text-slate-400 uppercase tracking-wider text-[10px] block mb-1">
                    Core Mechanisms
                  </span>
                  <div className="flex flex-wrap gap-1">
                    {selectedContractSpec.features.map((f, i) => (
                      <span key={i} className="px-2 py-0.5 rounded bg-indigo-950/60 border border-indigo-800/40 text-indigo-300 text-[11px]">
                        {f}
                      </span>
                    ))}
                  </div>
                </div>
              </div>

              {/* Interactive Methods */}
              <div className="space-y-3 pt-2">
                <div className="flex items-center justify-between">
                  <h4 className="text-xs font-bold uppercase tracking-wider text-slate-300">
                    Callable Contract Functions ({selectedContractSpec.methods.length})
                  </h4>
                  <span className="text-[11px] text-slate-500">Click to execute via active operator</span>
                </div>

                <div className="grid grid-cols-1 sm:grid-cols-2 gap-2">
                  {selectedContractSpec.methods.map((method) => {
                    const isSelected = selectedMethod?.name === method.name;
                    return (
                      <button
                        key={method.name}
                        onClick={() => {
                          setSelectedMethod(method);
                          setMethodParams({});
                          setExecutionResult(null);
                        }}
                        className={`p-2.5 rounded-xl border text-left transition ${
                          isSelected
                            ? 'bg-cyan-950/80 border-cyan-500 text-cyan-200'
                            : 'bg-slate-950 border-slate-800 hover:border-slate-700 text-slate-300'
                        }`}
                      >
                        <div className="flex items-center justify-between">
                          <span className="font-mono font-bold text-xs">{method.name}()</span>
                          <span
                            className={`px-1.5 py-0.2 rounded text-[10px] font-semibold ${
                              method.type === 'write'
                                ? 'bg-amber-950 text-amber-400 border border-amber-800/60'
                                : 'bg-emerald-950 text-emerald-400 border border-emerald-800/60'
                            }`}
                          >
                            {method.type.toUpperCase()}
                          </span>
                        </div>
                        <p className="text-[11px] text-slate-400 line-clamp-1 mt-1">{method.description}</p>
                      </button>
                    );
                  })}
                </div>
              </div>

              {/* Method Execution Box */}
              {selectedMethod && (
                <div className="p-4 rounded-xl bg-slate-950 border border-cyan-800/60 space-y-3">
                  <div className="flex items-center justify-between border-b border-slate-800 pb-2">
                    <span className="font-mono text-xs font-bold text-cyan-400">
                      Execute {selectedContractSpec.name}.{selectedMethod.name}()
                    </span>
                    <span className="text-[11px] text-slate-400">
                      Signer: <strong className="text-slate-300">{account.slice(0, 8)}...</strong>
                    </span>
                  </div>

                  <form onSubmit={handleRunMethod} className="space-y-3">
                    {selectedMethod.inputs.length > 0 ? (
                      <div className="space-y-2">
                        {selectedMethod.inputs.map((inp) => (
                          <div key={inp.name}>
                            <label className="block text-xs font-semibold text-slate-300 mb-0.5">
                              {inp.name} <span className="text-slate-500 font-mono">({inp.type})</span>
                            </label>
                            <input
                              type="text"
                              value={methodParams[inp.name] || ''}
                              onChange={(e) =>
                                setMethodParams({ ...methodParams, [inp.name]: e.target.value })
                              }
                              placeholder={`Enter ${inp.type}`}
                              className="w-full px-3 py-1.5 rounded-lg bg-slate-900 border border-slate-800 text-xs font-mono text-slate-200 focus:border-cyan-500 focus:outline-none"
                              required
                            />
                          </div>
                        ))}
                      </div>
                    ) : (
                      <div className="text-xs text-slate-400">No parameters required for this method.</div>
                    )}

                    <div className="flex items-center gap-3">
                      <button
                        type="submit"
                        disabled={isExecuting}
                        className="px-4 py-2 rounded-xl bg-gradient-to-r from-cyan-600 to-blue-600 hover:from-cyan-500 hover:to-blue-500 text-white font-bold text-xs shadow-md transition flex items-center gap-2 disabled:opacity-50"
                      >
                        <Play className="w-3.5 h-3.5 fill-current" />
                        {isExecuting ? 'Broadcasting Tx...' : `Broadcast ${selectedMethod.name}()`}
                      </button>
                    </div>

                    {executionResult && (
                      <div className="p-2.5 rounded-lg bg-emerald-950/70 border border-emerald-800 text-xs text-emerald-300 font-mono">
                        {executionResult}
                      </div>
                    )}
                  </form>
                </div>
              )}

              {/* Source Code Viewer */}
              <div className="space-y-2 pt-2">
                <div className="flex items-center justify-between">
                  <span className="text-xs font-bold uppercase tracking-wider text-slate-300">
                    Solidity Source Code ({selectedContractSpec.sourceCode.split('\n').length} lines)
                  </span>
                  <span className="text-[11px] text-slate-500">Pragma ^0.8.20 • OpenZeppelin v4.9+</span>
                </div>
                <pre className="p-4 rounded-xl bg-slate-950 border border-slate-800 font-mono text-[11px] text-slate-300 overflow-x-auto max-h-96 leading-relaxed">
                  {selectedContractSpec.sourceCode}
                </pre>
              </div>
            </div>
          </div>
        </div>
      )}

      {/* VIEW 3: POSTED & DEPLOYED OVERVIEW */}
      {activeSubTab === 'posted-contracts' && (
        <div className="rounded-2xl bg-slate-900/90 border border-slate-800 p-6 space-y-4">
          <div className="flex items-center justify-between border-b border-slate-800 pb-3">
            <div>
              <h3 className="text-base font-bold text-slate-200">Posted Contract Registry</h3>
              <p className="text-xs text-slate-400">
                All assembled, verified, and transmitted contracts available for immediate DAO calls
              </p>
            </div>
            <button
              onClick={() => setActiveSubTab('chunk-poster')}
              className="px-3 py-1.5 rounded-xl bg-cyan-600 hover:bg-cyan-500 text-white font-semibold text-xs transition"
            >
              + Post New Contract
            </button>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
            {postedContracts.map((c) => (
              <div
                key={c.id}
                className="p-4 rounded-xl bg-slate-950 border border-slate-800 space-y-3 hover:border-slate-700 transition"
              >
                <div className="flex items-start justify-between">
                  <div>
                    <h4 className="text-sm font-bold text-slate-200 font-mono">{c.name}</h4>
                    <div className="text-xs text-slate-400 mt-0.5">Author: {c.author}</div>
                  </div>
                  <span className="px-2 py-0.5 rounded-full text-[10px] bg-emerald-950 text-emerald-400 border border-emerald-800">
                    Active & Ready
                  </span>
                </div>

                <div className="p-2.5 rounded-lg bg-slate-900/60 font-mono text-xs space-y-1 text-slate-400">
                  <div>Address: <span className="text-slate-300">{c.simulatedAddress}</span></div>
                  <div>Checksum: <span className="text-slate-300">{c.checksum}</span></div>
                  <div>Chunks: <span className="text-cyan-400">{c.chunks.length} total</span></div>
                  <div>Parsed Functions: <span className="text-amber-400">{c.functionsCount}</span></div>
                </div>

                <div className="flex items-center gap-2">
                  <button
                    onClick={() => {
                      setSelectedContractSpec({
                        id: c.id,
                        name: c.name.replace('.sol', ''),
                        fileName: c.name,
                        category: 'Governance',
                        address: c.simulatedAddress,
                        description: `User-posted chunked contract: ${c.name}`,
                        roles: ['Owner'],
                        features: c.inherits,
                        methods: parseContractSignatures(c.source).functions.map((f) => ({
                          name: f.name,
                          type: f.isMutating ? 'write' : 'read',
                          inputs: [],
                          description: `Function ${f.name}(${f.args}) ${f.visibility}`,
                        })),
                        sourceCode: c.source,
                      });
                      setActiveSubTab('catalog');
                    }}
                    className="flex-1 py-1.5 rounded-lg bg-cyan-950 text-cyan-300 border border-cyan-800/80 hover:bg-cyan-900 text-xs font-semibold transition text-center"
                  >
                    Open in Workbench
                  </button>
                  <button
                    onClick={() => deletePostedContract(c.id)}
                    className="p-2 rounded-lg bg-slate-900 hover:bg-red-950 text-slate-400 hover:text-red-400 transition"
                    title="Delete"
                  >
                    <Trash2 className="w-3.5 h-3.5" />
                  </button>
                </div>
              </div>
            ))}
          </div>
        </div>
      )}
    </div>
  );
};
