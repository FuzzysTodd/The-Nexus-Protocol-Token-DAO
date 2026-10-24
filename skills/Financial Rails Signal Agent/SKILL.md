---
name: Financial Rails Signal Agent
description: Build and review crypto-to-fiat, fiat-to-crypto, swaps, transfers, debit-card settlement, and MCP maintenance workflows. Use when working on transaction signal processing, reconciliation, Ethereum/Base connectivity, documentation, approval paths, and monitoring.
---
.agents/
  config.toml     # Main configuration file
  skills/         # Skill definitions
    skill-name/
      SKILL.md    # Skill instructions
      scripts/    # Optional scripts
      docs/       # Optional documentation
  README.md       # This file
# Financial Rails Signal Agent

Echo filter module for filtering out the assistant's own speech.

Detects when the STT is hearing the TTS output by matching consecutive word sequences.
"""


def is_echo(text: str, last_spoken_text: str, min_consecutive_words: int = 3) -> bool:
    """
    Check if the transcribed text is likely the assistant hearing itself.
    
    Compares the transcribed text against the last text spoken by TTS.
    If there are `min_consecutive_words` or more consecutive words in common,
    it's considered an echo and should be filtered out.
    
    Args:
        text: The transcribed text from STT
        last_spoken_text: The last text spoken by TTS (normalized)
        min_consecutive_words: Minimum number of consecutive matching words
                               to consider it an echo (default: 3)
    
    Returns:
        True if the text is likely an echo of the assistant's own speech
    """
    if not text or not last_spoken_text:
        return False
    
    # Normalize the transcribed text
    normalized_text = " ".join(text.lower().split())
    
    # Split into words
    text_words = normalized_text.split()
    spoken_words = last_spoken_text.split()
    
    if len(text_words) < min_consecutive_words:
        # Short phrases are less likely to be echo, but check anyway
        pass
    
    # Check for consecutive word matches
    # We check both directions: does text contain a sequence from spoken?
    # and does spoken contain a sequence from text?
    
    for i in range(len(text_words) - min_consecutive_words + 1):
        # Extract a sequence of N consecutive words from transcribed text
        sequence = text_words[i:i + min_consecutive_words]
        sequence_str = " ".join(sequence)
        
        # Check if this exact sequence exists in the last spoken text
        if sequence_str in last_spoken_text:
            return True
    
    # Also check: if spoken text contains a long sequence from transcribed
    # (handles case where STT hears a subset of what was spoken)
    for i in range(len(spoken_words) - min_consecutive_words + 1):
        sequence = spoken_words[i:i + min_consecutive_words]
        sequence_str = " ".join(sequence)
        
        if sequence_str in normalized_text:
            return True
    
    return False


def filter_echo(text: str, last_spoken_text: str, min_consecutive_words: int = 3) -> str:
    """
    Filter out echo portions from the transcribed text.
    
    Returns the original text if it's not an echo, or an empty string if it is.
    
    Args:
        text: The transcribed text from STT
        last_spoken_text: The last text spoken by TTS (normalized)
        min_consecutive_words: Minimum consecutive words to match
    
    Returns:
        The text if not echo, empty string if echo
    """
    if is_echo(text, last_spoken_text, min_consecutive_words):
        return ""
    return text
You are a financial systems agent for The-Nexus-Protocol-Token-DOA focused on high-signal transaction analysis across crypto and traditional US payment rails.


{
  "schema": "ruflo-clone-tracker-ledger/v1",
  "created_at": "2026-05-19T23:17:49.428Z",
  "repos": [
    "ruvnet/ruflo",
    "ruvnet/agentdb",
    "ruvnet/agentic-flow",
    "ruvnet/ruvector",
    "ruvnet/ruv-FANN"
  ],
  "vector_layout": [
    "ruflo_clones",
    "ruflo_uniques",
    "agentdb_clones",
    "agentdb_uniques",
    "agentic_flow_clones",
    "agentic_flow_uniques",
    "ruvector_clones",
    "ruvector_uniques",
    "ruv_FANN_clones",
    "ruv_FANN_uniques"
  ],
  "snapshots": [
    {
      "id": "2026-05-19T23:17:49.427Z-2f39f1a5",
      "captured_at": "2026-05-19T23:17:49.427Z",
      "vector": [
        89536,
        22752,
        253,
        147,
        4911,
        419,
        20283,
        2066,
        270,
        106
      ],
      "totals": {
        "clones": 115253,
        "uniques": 25490
      },
      "repos": {
        "ruvnet/ruflo": {
          "count": 89536,
          "uniques": 22752,
          "days": [
            {
              "timestamp": "2026-05-05T00:00:00Z",
              "count": 10470,
              "uniques": 2729
            },
            {
              "timestamp": "2026-05-06T00:00:00Z",
              "count": 12234,
              "uniques": 2330
            },
            {
              "timestamp": "2026-05-07T00:00:00Z",
              "count": 3937,
              "uniques": 1794
            },
            {
              "timestamp": "2026-05-08T00:00:00Z",
              "count": 3807,
              "uniques": 1673
            },
            {
              "timestamp": "2026-05-09T00:00:00Z",
              "count": 5785,
              "uniques": 1628
            },
            {
              "timestamp": "2026-05-10T00:00:00Z",
              "count": 4607,
              "uniques": 1472
            },
            {
              "timestamp": "2026-05-11T00:00:00Z",
              "count": 5708,
              "uniques": 1875
            },
            {
              "timestamp": "2026-05-12T00:00:00Z",
              "count": 5564,
              "uniques": 1931
            },
            {
              "timestamp": "2026-05-13T00:00:00Z",
              "count": 8015,
              "uniques": 2108
            },
            {
              "timestamp": "2026-05-14T00:00:00Z",
              "count": 7794,
              "uniques": 2869
            },
            {
              "timestamp": "2026-05-15T00:00:00Z",
              "count": 7714,
              "uniques": 2229
            },
            {
              "timestamp": "2026-05-16T00:00:00Z",
              "count": 4489,
              "uniques": 1673
            },
            {
              "timestamp": "2026-05-17T00:00:00Z",
              "count": 4110,
              "uniques": 1311
            },
            {
              "timestamp": "2026-05-18T00:00:00Z",
              "count": 5302,
              "uniques": 1436
            }
          ]
        },
        "ruvnet/agentdb": {
          "count": 253,
          "uniques": 147,
          "days": [
            {
              "timestamp": "2026-05-05T00:00:00Z",
              "count": 0,
              "uniques": 0
            },
            {
              "timestamp": "2026-05-06T00:00:00Z",
              "count": 132,
              "uniques": 53
            },
            {
              "timestamp": "2026-05-07T00:00:00Z",
              "count": 14,
              "uniques": 11
            },
            {
              "timestamp": "2026-05-08T00:00:00Z",
              "count": 10,
              "uniques": 9
            },
            {
              "timestamp": "2026-05-09T00:00:00Z",
              "count": 13,
              "uniques": 9
            },
            {
              "timestamp": "2026-05-10T00:00:00Z",
              "count": 8,
              "uniques": 7
            },
            {
              "timestamp": "2026-05-11T00:00:00Z",
              "count": 11,
              "uniques": 9
            },
            {
              "timestamp": "2026-05-12T00:00:00Z",
              "count": 8,
              "uniques": 7
            },
            {
              "timestamp": "2026-05-13T00:00:00Z",
              "count": 7,
              "uniques": 7
            },
            {
              "timestamp": "2026-05-14T00:00:00Z",
              "count": 9,
              "uniques": 9
            },
            {
              "timestamp": "2026-05-15T00:00:00Z",
              "count": 10,
              "uniques": 9
            },
            {
              "timestamp": "2026-05-16T00:00:00Z",
              "count": 10,
              "uniques": 5
            },
            {
              "timestamp": "2026-05-17T00:00:00Z",
              "count": 8,
              "uniques": 8
            },
            {
              "timestamp": "2026-05-18T00:00:00Z",
              "count": 13,
              "uniques": 10
            }
          ]
        },
        "ruvnet/agentic-flow": {
          "count": 4911,
          "uniques": 419,
          "days": [
            {
              "timestamp": "2026-05-05T00:00:00Z",
              "count": 493,
              "uniques": 87
            },
            {
              "timestamp": "2026-05-06T00:00:00Z",
              "count": 885,
              "uniques": 112
            },
            {
              "timestamp": "2026-05-07T00:00:00Z",
              "count": 47,
              "uniques": 22
            },
            {
              "timestamp": "2026-05-08T00:00:00Z",
              "count": 48,
              "uniques": 27
            },
            {
              "timestamp": "2026-05-09T00:00:00Z",
              "count": 2947,
              "uniques": 41
            },
            {
              "timestamp": "2026-05-10T00:00:00Z",
              "count": 136,
              "uniques": 39
            },
            {
              "timestamp": "2026-05-11T00:00:00Z",
              "count": 43,
              "uniques": 24
            },
            {
              "timestamp": "2026-05-12T00:00:00Z",
              "count": 33,
              "uniques": 13
            },
            {
              "timestamp": "2026-05-13T00:00:00Z",
              "count": 64,
              "uniques": 24
            },
            {
              "timestamp": "2026-05-14T00:00:00Z",
              "count": 36,
              "uniques": 21
            },
            {
              "timestamp": "2026-05-15T00:00:00Z",
              "count": 34,
              "uniques": 18
            },
            {
              "timestamp": "2026-05-16T00:00:00Z",
              "count": 23,
              "uniques": 12
            },
            {
              "timestamp": "2026-05-17T00:00:00Z",
              "count": 61,
              "uniques": 15
            },
            {
              "timestamp": "2026-05-18T00:00:00Z",
              "count": 61,
              "uniques": 19
            }
          ]
        },
        "ruvnet/ruvector": {
          "count": 20283,
          "uniques": 2066,
          "days": [
            {
              "timestamp": "2026-05-05T00:00:00Z",
              "count": 1520,
              "uniques": 187
            },
            {
              "timestamp": "2026-05-06T00:00:00Z",
              "count": 1846,
              "uniques": 237
            },
            {
              "timestamp": "2026-05-07T00:00:00Z",
              "count": 2284,
              "uniques": 270
            },
            {
              "timestamp": "2026-05-08T00:00:00Z",
              "count": 1533,
              "uniques": 243
            },
            {
              "timestamp": "2026-05-09T00:00:00Z",
              "count": 1018,
              "uniques": 112
            },
            {
              "timestamp": "2026-05-10T00:00:00Z",
              "count": 1855,
              "uniques": 72
            },
            {
              "timestamp": "2026-05-11T00:00:00Z",
              "count": 1219,
              "uniques": 122
            },
            {
              "timestamp": "2026-05-12T00:00:00Z",
              "count": 1147,
              "uniques": 97
            },
            {
              "timestamp": "2026-05-13T00:00:00Z",
              "count": 1435,
              "uniques": 130
            },
            {
              "timestamp": "2026-05-14T00:00:00Z",
              "count": 1043,
              "uniques": 118
            },
            {
              "timestamp": "2026-05-15T00:00:00Z",
              "count": 1091,
              "uniques": 139
            },
            {
              "timestamp": "2026-05-16T00:00:00Z",
              "count": 1629,
              "uniques": 176
            },
            {
              "timestamp": "2026-05-17T00:00:00Z",
              "count": 1209,
              "uniques": 140
            },
            {
              "timestamp": "2026-05-18T00:00:00Z",
              "count": 1454,
              "uniques": 159
            }
          ]
        },
        "ruvnet/ruv-FANN": {
          "count": 270,
          "uniques": 106,
          "days": [
            {
              "timestamp": "2026-05-05T00:00:00Z",
              "count": 12,
              "uniques": 8
            },
            {
              "timestamp": "2026-05-06T00:00:00Z",
              "count": 20,
              "uniques": 11
            },
            {
              "timestamp": "2026-05-07T00:00:00Z",
              "count": 32,
              "uniques": 10
            },
            {
              "timestamp": "2026-05-08T00:00:00Z",
              "count": 13,
              "uniques": 9
            },
            {
              "timestamp": "2026-05-09T00:00:00Z",
              "count": 10,
              "uniques": 9
            },
            {
              "timestamp": "2026-05-10T00:00:00Z",
              "count": 19,
              "uniques": 12
            },
            {
              "timestamp": "2026-05-11T00:00:00Z",
              "count": 13,
              "uniques": 9
            },
            {
              "timestamp": "2026-05-12T00:00:00Z",
              "count": 28,
              "uniques": 14
            },
            {
              "timestamp": "2026-05-13T00:00:00Z",
              "count": 16,
              "uniques": 7
            },
            {
              "timestamp": "2026-05-14T00:00:00Z",
              "count": 33,
              "uniques": 10
            },
            {
              "timestamp": "2026-05-15T00:00:00Z",
              "count": 18,
              "uniques": 12
            },
            {
              "timestamp": "2026-05-16T00:00:00Z",
              "count": 20,
              "uniques": 12
            },
            {
              "timestamp": "2026-05-17T00:00:00Z",
              "count": 6,
              "uniques": 6
            },
            {
              "timestamp": "2026-05-18T00:00:00Z",
              "count": 30,
              "uniques": 17
            }
          ]
        }
      },
      "npm_headline_total": 4255420,
      "npm": {
        "claude-flow": 765750,
        "ruflo": 298601,
        "@claude-flow/cli": 537029,
        "@claude-flow/memory": 272833,
        "agentdb": 1457393,
        "agentic-flow": 923814
      }
    },
    {
      "id": "2026-05-19T23:49:53.253Z-c8d0bbda",
      "captured_at": "2026-05-19T23:49:53.253Z",
      "vector": [
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0
      ],
      "totals": {
        "clones": 0,
        "uniques": 0
      },
      "repos": {
        "ruvnet/ruflo": {
          "count": 0,
          "uniques": 0,
          "days": [],
          "error": "fetch-failed"
        },
        "ruvnet/agentdb": {
          "count": 0,
          "uniques": 0,
          "days": [],
          "error": "fetch-failed"
        },
        "ruvnet/agentic-flow": {
          "count": 0,
          "uniques": 0,
          "days": [],
          "error": "fetch-failed"
        },
        "ruvnet/ruvector": {
          "count": 0,
          "uniques": 0,
          "days": [],
          "error": "fetch-failed"
        },
        "ruvnet/ruv-FANN": {
          "count": 0,
          "uniques": 0,
          "days": [],
          "error": "fetch-failed"
        }
      },
      "npm_headline_total": 4255420,
      "npm": {
        "claude-flow": 765750,
        "ruflo": 298601,
        "@claude-flow/cli": 537029,
        "@claude-flow/memory": 272833,
        "agentdb": 1457393,
        "agentic-flow": 923814
      }
    },
    {
      "id": "2026-05-23T08:53:34.176Z-91988a19",
      "captured_at": "2026-05-23T08:53:34.176Z",
      "vector": [
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0
      ],
      "totals": {
        "clones": 0,
        "uniques": 0
      },
      "repos": {
        "ruvnet/ruflo": {
          "count": 0,
          "uniques": 0,
          "days": [],
          "error": "fetch-failed"
        },
        "ruvnet/agentdb": {
          "count": 0,
          "uniques": 0,
          "days": [],
          "error": "fetch-failed"
        },
        "ruvnet/agentic-flow": {
          "count": 0,
          "uniques": 0,
          "days": [],
          "error": "fetch-failed"
        },
        "ruvnet/ruvector": {
          "count": 0,
          "uniques": 0,
          "days": [],
          "error": "fetch-failed"
        },
        "ruvnet/ruv-FANN": {
          "count": 0,
          "uniques": 0,
          "days": [],
          "error": "fetch-failed"
        }
      },
      "npm_headline_total": 4595811,
      "npm": {
        "claude-flow": 785214,
        "ruflo": 341975,
        "@claude-flow/cli": 589175,
        "@claude-flow/memory": 318622,
        "agentdb": 1571065,
        "agentic-flow": 989760
      }
    },
    {
      "id": "2026-05-27T07:46:13.610Z-bf1a3d11",
      "captured_at": "2026-05-27T07:46:13.610Z",
      "vector": [
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0
      ],
      "totals": {
        "clones": 0,
        "uniques": 0
      },
      "repos": {
        "ruvnet/ruflo": {
          "count": 0,
          "uniques": 0,
          "days": [],
          "error": "fetch-failed"
        },
        "ruvnet/agentdb": {
          "count": 0,
          "uniques": 0,
          "days": [],
          "error": "fetch-failed"
        },
        "ruvnet/agentic-flow": {
          "count": 0,
          "uniques": 0,
          "days": [],
          "error": "fetch-failed"
        },
        "ruvnet/ruvector": {
          "count": 0,
          "uniques": 0,
          "days": [],
          "error": "fetch-failed"
        },
        "ruvnet/ruv-FANN": {
          "count": 0,
          "uniques": 0,
          "days": [],
          "error": "fetch-failed"
        }
      },
      "npm_headline_total": 4831624,
      "npm": {
        "claude-flow": 795590,
        "ruflo": 370919,
        "@claude-flow/cli": 624020,
        "@claude-flow/memory": 351840,
        "agentdb": 1651215,
        "agentic-flow": 1038040
      }
    },
    {
      "id": "2026-06-01T08:13:52.891Z-915fccb6",
      "captured_at": "2026-06-01T08:13:52.891Z",
      "vector": [
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0
      ],
      "totals": {
        "clones": 0,
        "uniques": 0
      },
      "repos": {
        "ruvnet/ruflo": {
          "count": 0,
          "uniques": 0,
          "days": [],
          "error": "fetch-failed"
        },
        "ruvnet/agentdb": {
          "count": 0,
          "uniques": 0,
          "days": [],
          "error": "fetch-failed"
        },
        "ruvnet/agentic-flow": {
          "count": 0,
          "uniques": 0,
          "days": [],
          "error": "fetch-failed"
        },
        "ruvnet/ruvector": {
          "count": 0,
          "uniques": 0,
          "days": [],
          "error": "fetch-failed"
        },
        "ruvnet/ruv-FANN": {
          "count": 0,
          "uniques": 0,
          "days": [],
          "error": "fetch-failed"
        }
      },
      "npm_headline_total": 5298606,
      "npm": {
        "claude-flow": 827832,
        "ruflo": 445603,
        "@claude-flow/cli": 700351,
        "@claude-flow/memory": 405476,
        "agentdb": 1806449,
        "agentic-flow": 1112895
      }
    }
  ],
  "updated_at": "2026-06-01T08:13:52.891Z",
  "snapshot_count": 5
}
## Mission

- Design, review, and improve transaction flows for ACH, wire, card, stablecoin, wallet transfer, bridge, and swap operations.
- Prioritize signal processing that separates normal payment behavior from fraud, operational drift, settlement mismatch, and approval bottlenecks.
- Maintain reliable documentation, approval checkpoints, and MCP bot scan coverage for Ethereum and Base-connected systems.

## Supported Domains

- Fiat to crypto conversion flows
- Crypto to fiat off-ramp and debit-card settlement flows
- Wallet transfers, swap routing, bridge monitoring, and treasury reconciliation
- Stablecoin settlement tracking for US dollar-denominated flows
- Ethereum and Base transaction lifecycle review, including deposits, withdrawals, confirmations, and finalization

## Core Responsibilities

### 1. Transaction Signal Processing

- Model transaction intent, source, destination, asset, settlement path, fees, latency, and confirmation state.
- Detect anomalies in volume, velocity, counterparty behavior, route selection, slippage, bridge delay, retry storms, and settlement failures.
- Distinguish between user error, liquidity issues, RPC/provider degradation, approval failures, and fraud indicators.
- Prefer deterministic scoring rules first; use statistical or ML-style heuristics only when they remain explainable.

### 2. Financial Flow Design

- Map end-to-end flows for ACH -> stablecoin, card -> wallet funding, crypto -> debit card spend, and treasury conversion pipelines.
- Track state transitions explicitly: initiated, pending review, approved, submitted, on-chain pending, confirmed, settled, failed, reversed.
- Enforce idempotency, auditability, and replay-safe event handling.
- Reconcile every external transfer against internal ledger state.

### 3. MCP Bot Coordination

- Use MCP bots to scan connectivity, health, and documentation status for Ethereum and Base integrations.
- Route checks through existing financial and governance-oriented MCP roles when possible, especially token economics, governance, sync, and financial analytics agents.
- Produce maintenance outputs covering:
  - connection health
  - RPC/provider assumptions
  - wallet and signer dependencies
  - approval and escalation paths
  - required documentation updates
  - unresolved operational risks
if __name__ == "__main__":    from utility import pretty_print, animate_thinking    from speech_to_text import notify_tts_start, notify_tts_stopelse:    from sources.utility import pretty_print, animate_thinking    from sources.speech_to_text import notify_tts_start, notify_tts_stopclass Speech():    """@@ -44,6 +46,7 @@ def __init__(self, enable: bool = True, language: str = "en", voice_idx: int = 6        self.voice = self.voice_map[language][voice_idx]        self.speed = 1.2        self.voice_folder = ".voices"        self.last_spoken_text = ""        self.create_voice_folder(self.voice_folder)    def create_voice_folder(self, path: str = ".voices") -> None:@@ -72,21 +75,26 @@ def speak(self, sentence: str, voice_idx: int = 1):        sentence = self.clean_sentence(sentence)        audio_file = f"{self.voice_folder}/sample_{self.voice_map[self.language][voice_idx]}.wav"        self.voice = self.voice_map[self.language][voice_idx]        self.last_spoken_text = " ".join(sentence.lower().split())        generator = self.pipeline(            sentence, voice=self.voice,            speed=self.speed, split_pattern=r'\n+'        )        for i, (_, _, audio) in enumerate(generator):            if 'ipykernel' in modules: #only display in jupyter notebook.                display(Audio(data=audio, rate=24000, autoplay=i==0), display_id=False)            sf.write(audio_file, audio, 24000) # save each audio file            if platform.system().lower() == "windows":                import winsound                winsound.PlaySound(audio_file, winsound.SND_FILENAME)            elif platform.system().lower() == "darwin":  # macOS                subprocess.call(["afplay", audio_file])            else: # linux or other.                subprocess.call(["aplay", audio_file])        notify_tts_start()        try:            for i, (_, _, audio) in enumerate(generator):                if 'ipykernel' in modules: #only display in jupyter notebook.                    display(Audio(data=audio, rate=24000, autoplay=i==0), display_id=False)                sf.write(audio_file, audio, 24000) # save each audio file                if platform.system().lower() == "windows":                    import winsound                    winsound.PlaySound(audio_file, winsound.SND_FILENAME)                elif platform.system().lower() == "darwin":  # macOS                    subprocess.call(["afplay", audio_file])                else: # linux or other.                    subprocess.call(["aplay", audio_file])        finally:            notify_tts_stop()    def replace_url(self, url: re.Match) -> str:        """
### 4. Documentation And Approval Control
 def __init__(self, format: int = pyaudio.paInt16, channels: int = 1, rate: int = 4096, chunk: int = 8192, record_seconds: int = 5, verbose: bool = False):
        self.format = format
        self.channels = channels
        self.rate = rate
        self.chunk = chunk
        self.record_seconds = record_seconds
        self.verbose = verbose
        self.thread = None
        self.audio = None
        if IMPORT_FOUND:
            self.audio = pyaudio.PyAudio()
            self.thread = threading.Thread(target=self._record, daemon=True)

    def _record(self) -> None:

- Keep runbooks, settlement assumptions, and approval rules current.
- Define approval boundaries for treasury moves, signer rotations, off-ramp changes, payout logic, and provider migrations.
- Flag missing compliance, custody, or funds-flow documentation as release blockers.

## Operating Rules

- Start with the concrete assets, networks, counterparties, and settlement rails involved.
- For Ethereum and Base, validate chain-specific assumptions separately, including nonce handling, confirmation depth, RPC resilience, and bridge finality.
- For swaps and transfers, inspect slippage control, route fallback behavior, fee accounting, deadline expiry, and partial-fill handling.
- For debit-card or card-linked settlement, verify authorization, capture, settlement timing, refund handling, and ledger reconciliation boundaries.
- Never assume off-chain settlement is complete until ledger state, provider response, and downstream confirmation agree.
- Prefer minimal, testable changes. Add or update validation tests when logic changes.

## Review Priorities

- Unauthorized movement of funds
- Broken reconciliation between internal ledger and external settlement
- Double-spend or duplicate payout risk
- Incorrect approval sequencing
- Provider failover gaps for Ethereum or Base
- Documentation drift that could cause operational error
- Missing observability for transaction status and exception queues

## Deliverables

- Transaction flow diagrams and state models
- Risk findings ordered by severity
- MCP maintenance scan summaries for Ethereum and Base
- Approval matrix updates and documentation diffs
- Small, verifiable implementation patches with validation steps

## Response Style

- Lead with findings and blocked assumptions.
- Be explicit about which rail is failing: ACH, card, wallet transfer, swap, bridge, debit settlement, Ethereum, or Base.
- Separate confirmed facts from inferred behavior.
- When proposing a fix, include the exact system boundary it protects.