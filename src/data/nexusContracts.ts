/**
 * @license
 * SPDX-License-Identifier: Apache-2.0
 * The Nexus Protocol DAO - Complete Contracts & Knowledge Base
 * Extracted and compiled from https://github.com/FuzzysTodd/The-Nexus-Protocol-Token-DAO
 */

export interface ContractMethod {
  name: string;
  type: 'read' | 'write';
  inputs: { name: string; type: string }[];
  outputs?: { name: string; type: string }[];
  description: string;
}

export interface NexusContractSpec {
  id: string;
  name: string;
  fileName: string;
  category: 'Governance' | 'Token' | 'DeFi' | 'Treasury' | 'RWA' | 'Funding';
  address: string | null;
  description: string;
  roles: string[];
  features: string[];
  methods: ContractMethod[];
  sourceCode: string;
}

export const NEXUS_METADATA = {
  protocolName: 'The Nexus Protocol Token DAO',
  tokenName: 'Nexus Game Theory Token',
  tokenSymbol: 'NGTT',
  totalSupply: '1,000,000,000 NGTT',
  decimals: 18,
  ownerAuthority: 'FuzzysTodd',
  ownerAddress: '0x33ffc308e693a5b49e0ee0241f41f03ccef495f2',
  coinbaseHandle: 'tenkrypt.cb.id',
  mainnetAddress: '0xeCE999c86452c573Adfdd7F0C9226e673477973a',
  timelockDelaySeconds: 172800, // 2 days
  quorumPercentage: 4,
  quorumVotesRequired: '40,000,000 NGTT',
  proposalThreshold: '10,000 NGTT',
  multisigEthThreshold: '50 ETH',
  multisigErc20Threshold: '100,000 Tokens',
  repositoryUrl: 'https://github.com/FuzzysTodd/The-Nexus-Protocol-Token-DAO',
  standard: 'Nexus Encryption Standard (NES) v1.0',
};

export const NEXUS_NETWORKS = [
  {
    chainId: 1,
    name: 'Ethereum Mainnet',
    shortName: 'ETH',
    symbol: 'ETH',
    explorer: 'https://etherscan.io',
    rpc: 'https://cloudflare-eth.com',
    ngttAddress: '0xeCE999c86452c573Adfdd7F0C9226e673477973a',
  },
  {
    chainId: 8453,
    name: 'Base Mainnet',
    shortName: 'Base',
    symbol: 'ETH',
    explorer: 'https://basescan.org',
    rpc: 'https://mainnet.base.org',
    ngttAddress: '0xeCE999c86452c573Adfdd7F0C9226e673477973a',
  },
  {
    chainId: 56,
    name: 'BNB Smart Chain',
    shortName: 'BSC',
    symbol: 'BNB',
    explorer: 'https://bscscan.com',
    rpc: 'https://bsc-dataseed.binance.org',
    ngttAddress: '0xeCE999c86452c573Adfdd7F0C9226e673477973a',
  },
];

export const REVENUE_STREAMS = [
  { id: 1, name: 'Dividend Distributions', type: 'Passive', apy: '5-20%', description: '20% sell tax, 5% distributed to all holders automatically.' },
  { id: 2, name: 'Game-to-Earn Rewards', type: 'Active', apy: '50-300%', description: 'Complete games across 7 age categories, boosted by player skill.' },
  { id: 3, name: 'MCP Group Profit Pools', type: 'Passive / Collab', apy: '30-150%', description: 'Collaborative swarm performance profit sharing based on games played.' },
  { id: 4, name: 'LP Staking Yield', type: 'Passive', apy: '40-120%', description: 'NexusLPStaking rewards distributed continuously from refillRewardPool.' },
  { id: 5, name: 'Fractal Vault Compounding', type: 'Passive', apy: '15-45%', description: 'ERC-4626 auto-compounding asset management with max reinvest BPS.' },
  { id: 6, name: 'Options Vault Premiums', type: 'Passive', apy: '25-80%', description: 'Underwritten covered call premiums recorded into the vault.' },
  { id: 7, name: 'Tokenized RWA Property Yields', type: 'Passive', apy: '8-18%', description: 'Real estate deed rental streams from Wyoming DAO LLC properties.' },
  { id: 8, name: 'Fractionalization Liquidity Fees', type: 'Passive', apy: '10-35%', description: 'Secondary trading fees on fractionalized RWA NFT shares.' },
  { id: 9, name: 'Builder Fund Developer Royalties', type: 'Active', apy: 'Variable', description: 'Protocol Guild-style micro-fee compensation in USD, ETH, and Satoshis.' },
  { id: 10, name: 'Game Theory Skill Boost Multipliers', type: 'Active', apy: '100-500%', description: '100x to 500x skill-based multipliers for elite operators.' },
];
export const NEXUS_CONTRACTS: NexusContractSpec[] = [
  {
    "id": "ngtt-governor-token",
    "name": "NGTTGovernanceToken",
    "fileName": "NGTTGovernanceToken.sol",
    "category": "Token",
    "address": "0xeCE999c86452c573Adfdd7F0C9226e673477973a",
    "description": "Full ERC20Votes + ERC20Permit governance token with MCP group management, game rewards, skill multipliers, and profit pool distributions.",
    "roles": [
      "Owner (transferred to Timelock)",
      "Token Holders"
    ],
    "features": [
      "1 Billion Total Supply",
      "Checkpoint Voting",
      "MCP Groups",
      "Game Rewards",
      "Profit Pool",
      "Skill Boosts"
    ],
    "methods": [
      {
        "name": "delegate",
        "type": "write",
        "inputs": [
          {
            "name": "delegatee",
            "type": "address"
          }
        ],
        "description": "Delegates voting power to specified address."
      },
      {
        "name": "getVotes",
        "type": "read",
        "inputs": [
          {
            "name": "account",
            "type": "address"
          }
        ],
        "outputs": [
          {
            "name": "votes",
            "type": "uint256"
          }
        ],
        "description": "Gets current voting weight for an account."
      },
      {
        "name": "createMCPGroup",
        "type": "write",
        "inputs": [
          {
            "name": "_name",
            "type": "string"
          },
          {
            "name": "_members",
            "type": "address[]"
          }
        ],
        "outputs": [
          {
            "name": "groupId",
            "type": "uint256"
          }
        ],
        "description": "Creates a new MCP group for swarm collaboration."
      },
      {
        "name": "completeGame",
        "type": "write",
        "inputs": [
          {
            "name": "_player",
            "type": "address"
          },
          {
            "name": "_baseReward",
            "type": "uint256"
          },
          {
            "name": "_ageGroupId",
            "type": "uint256"
          }
        ],
        "description": "Awards skill-adjusted NGTT for game completion."
      },
      {
        "name": "distributeProfits",
        "type": "write",
        "inputs": [],
        "description": "Distributes accumulated profit pool to active MCP groups."
      },
      {
        "name": "claimProfits",
        "type": "write",
        "inputs": [],
        "description": "Claims pending member profit allocation."
      },
      {
        "name": "addProfitPool",
        "type": "write",
        "inputs": [
          {
            "name": "_amount",
            "type": "uint256"
          }
        ],
        "description": "Deposits NGTT into the profit pool reserve."
      },
      {
        "name": "activateBoost",
        "type": "write",
        "inputs": [
          {
            "name": "_user",
            "type": "address"
          },
          {
            "name": "_multiplier",
            "type": "uint256"
          }
        ],
        "description": "Applies skill multiplier (100-500 bps) to a user."
      },
      {
        "name": "getUserStats",
        "type": "read",
        "inputs": [
          {
            "name": "_user",
            "type": "address"
          }
        ],
        "outputs": [
          {
            "name": "games",
            "type": "uint256"
          },
          {
            "name": "skill",
            "type": "uint256"
          },
          {
            "name": "profits",
            "type": "uint256"
          },
          {
            "name": "groupId",
            "type": "uint256"
          }
        ],
        "description": "Returns games, skill, unclaimed profits, and MCP group ID."
      },
      {
        "name": "getGroupStats",
        "type": "read",
        "inputs": [
          {
            "name": "_groupId",
            "type": "uint256"
          }
        ],
        "outputs": [
          {
            "name": "name",
            "type": "string"
          },
          {
            "name": "memberCount",
            "type": "uint256"
          },
          {
            "name": "totalTokens",
            "type": "uint256"
          },
          {
            "name": "gamesPlayed",
            "type": "uint256"
          },
          {
            "name": "profitShare",
            "type": "uint256"
          }
        ],
        "description": "Returns stats for a specific MCP group."
      }
    ],
    "sourceCode": "// SPDX-License-Identifier: MIT\npragma solidity ^0.8.20;\n\nimport \"@openzeppelin/contracts/token/ERC20/extensions/draft-ERC20Permit.sol\";\nimport \"@openzeppelin/contracts/token/ERC20/extensions/ERC20Votes.sol\";\nimport \"@openzeppelin/contracts/token/ERC20/IERC20.sol\";\nimport \"@openzeppelin/contracts/token/ERC20/utils/SafeERC20.sol\";\nimport \"@openzeppelin/contracts/access/Ownable.sol\";\nimport \"@openzeppelin/contracts/security/ReentrancyGuard.sol\";\nimport \"@openzeppelin/contracts/utils/Counters.sol\";\n\n/// @title NGTT Governance Token\n/// @notice Nexus Game Theory Token with on-chain snapshot voting and delegation.\n/// @dev Extends the original NGTT design with ERC20Votes and ERC20Permit so that\n///      token holders can delegate voting weight to themselves or to a trusted\n///      delegate, enabling trustless participation in the NexusDAOGovernor.\n///      NES: this contract is a Nexus-authored surface governed by the\n///      Nexus Encryption Standard as documented in docs/NEXUS_ENCRYPTION_STANDARD.md.\n///      Third-party imports retain their original licensing and ownership terms.\ncontract NGTTGovernanceToken is ERC20Votes, Ownable, ReentrancyGuard {\n    using Counters for Counters.Counter;\n    using SafeERC20 for IERC20;\n\n    // -------------------------------------------------------------------------\n    // Constants\n    // -------------------------------------------------------------------------\n\n    /// @notice Total tokens minted at genesis (1 billion NGTT, 18 decimals).\n    uint256 public constant INITIAL_SUPPLY = 1_000_000_000 * 10 ** 18;\n\n    /// @notice BTC-backing ratio encoded in the protocol (1 NGTT : 100 satoshi-units).\n    uint256 public constant BTC_BACKING_RATIO = 100;\n\n    // -------------------------------------------------------------------------\n    // State\n    // -------------------------------------------------------------------------\n\n    /// @notice Accumulated profit available for distribution.\n    uint256 public profitPool;\n\n    /// @notice Lifetime total of distributed profits.\n    uint256 public totalDistributed;\n\n    struct MCPGroup {\n        string name;\n        address[] members;\n        uint256 totalTokens;\n        uint256 gamesPlayed;\n        uint256 profitShare;\n        bool active;\n    }\n\n    mapping(uint256 => MCPGroup) public mcpGroups;\n    mapping(address => uint256) public userToGroup;\n    mapping(address => uint256) public userProfits;\n    Counters.Counter private _groupIdCounter;\n\n    mapping(address => uint256) public gamesCompleted;\n    mapping(address => uint256) public skillLevel;\n    mapping(address => uint256) public lastPlayTimestamp;\n\n    // -------------------------------------------------------------------------\n    // Events\n    // -------------------------------------------------------------------------\n\n    /// @notice Emitted when a new MCP group is created.\n    event MCPGroupCreated(uint256 indexed groupId, string name);\n\n    /// @notice Emitted when a player completes a game session.\n    event GameCompleted(address indexed player, uint256 reward, uint256 skillIncrease);\n\n    /// @notice Emitted when profits are distributed to a recipient.\n    event ProfitDistributed(address indexed recipient, uint256 amount);\n\n    /// @notice Emitted when the BTC reference value is updated.\n    event BTCValueUpdated(uint256 newBtcValue);\n\n    /// @notice Emitted when a skill boost is applied to a user.\n    event BoostActivated(address indexed user, uint256 multiplier);\n\n    /// @notice Emitted when tokens are added to the profit pool.\n    event ProfitPoolIncreased(uint256 amount, uint256 newTotal);\n\n    // -------------------------------------------------------------------------\n    // Constructor\n    // -------------------------------------------------------------------------\n\n    /// @notice Deploys the token, mints the full initial supply to the deployer,\n    ///         and self-delegates so the deployer's voting power is active immediately.\n    constructor() ERC20(\"Nexus Game Theory Token\", \"NGTT\") ERC20Permit(\"Nexus Game Theory Token\") {\n        _mint(msg.sender, INITIAL_SUPPLY);\n        // Self-delegate so the deployer's votes are active without an extra tx.\n        _delegate(msg.sender, msg.sender);\n    }\n\n    // -------------------------------------------------------------------------\n    // MCP Group management\n    // -------------------------------------------------------------------------\n\n    /// @notice Creates a new MCP group with the given members.\n    /// @param _name Human-readable group name.\n    /// @param _members Array of member addresses (must be non-empty, no zero addresses).\n    /// @return groupId The unique identifier assigned to the new group.\n    function createMCPGroup(string memory _name, address[] memory _members)\n        external\n        onlyOwner\n        returns (uint256)\n    {\n        require(_members.length > 0, \"NGTT: empty member list\");\n        for (uint256 i = 0; i < _members.length; i++) {\n            require(_members[i] != address(0), \"NGTT: zero member address\");\n        }\n\n        _groupIdCounter.increment();\n        uint256 newGroupId = _groupIdCounter.current();\n\n        MCPGroup storage newGroup = mcpGroups[newGroupId];\n        newGroup.name = _name;\n        newGroup.members = _members;\n        newGroup.active = true;\n\n        for (uint256 i = 0; i < _members.length; i++) {\n            userToGroup[_members[i]] = newGroupId;\n        }\n\n        emit MCPGroupCreated(newGroupId, _name);\n        return newGroupId;\n    }\n\n    // -------------------------------------------------------------------------\n    // Game rewards\n    // -------------------------------------------------------------------------\n\n    /// @notice Records a completed game session and mints skill-adjusted rewards.\n    /// @param _player The player who completed the game.\n    /// @param _baseReward Base reward amount in NGTT tokens (18 decimals).\n    /// @param _ageGroupId Age group identifier; groups \u2264 2 receive a 20% bonus.\n    function completeGame(address _player, uint256 _baseReward, uint256 _ageGroupId)\n        external\n        onlyOwner\n        nonReentrant\n    {\n        require(_player != address(0), \"NGTT: zero player address\");\n        require(_baseReward > 0, \"NGTT: reward must be positive\");\n\n        uint256 skillMultiplier = 100 + (skillLevel[_player] / 10);\n        uint256 reward = (_baseReward * skillMultiplier) / 100;\n\n        if (_ageGroupId <= 2) {\n            reward = (reward * 120) / 100;\n        }\n\n        gamesCompleted[_player]++;\n        skillLevel[_player] += 10;\n        lastPlayTimestamp[_player] = block.timestamp;\n\n        uint256 groupId = userToGroup[_player];\n        if (groupId > 0) {\n            mcpGroups[groupId].gamesPlayed++;\n            mcpGroups[groupId].totalTokens += reward;\n        }\n\n        _mint(_player, reward);\n        emit GameCompleted(_player, reward, 10);\n    }\n\n    // -------------------------------------------------------------------------\n    // Profit pool\n    // -------------------------------------------------------------------------\n\n    /// @notice Distributes the accumulated profit pool proportionally across\n    ///         active MCP groups (weighted by games played).\n    function distributeProfits() external onlyOwner nonReentrant {\n        require(profitPool > 0, \"NGTT: no profits to distribute\");\n\n        uint256 totalActivity = 0;\n        uint256 groupCount = _groupIdCounter.current();\n        for (uint256 i = 1; i <= groupCount; i++) {\n            if (mcpGroups[i].active) {\n                totalActivity += mcpGroups[i].gamesPlayed;\n            }\n        }\n        require(totalActivity > 0, \"NGTT: no activity recorded\");\n\n        uint256 snapshot = profitPool;\n        profitPool = 0;\n        totalDistributed += snapshot;\n\n        for (uint256 i = 1; i <= groupCount; i++) {\n            if (mcpGroups[i].active && mcpGroups[i].gamesPlayed > 0) {\n                uint256 groupShare = (snapshot * mcpGroups[i].gamesPlayed) / totalActivity;\n                mcpGroups[i].profitShare += groupShare;\n\n                uint256 memberCount = mcpGroups[i].members.length;\n                uint256 perMember = groupShare / memberCount;\n                for (uint256 j = 0; j < memberCount; j++) {\n                    address member = mcpGroups[i].members[j];\n                    userProfits[member] += perMember;\n                    emit ProfitDistributed(member, perMember);\n                }\n            }\n        }\n    }\n\n    /// @notice Lets a member claim their allocated profits from the deposited reserve.\n    function claimProfits() external nonReentrant {\n        uint256 amount = userProfits[msg.sender];\n        require(amount > 0, \"NGTT: no profits to claim\");\n\n        userProfits[msg.sender] = 0;\n        IERC20(address(this)).safeTransfer(msg.sender, amount);\n\n        emit ProfitDistributed(msg.sender, amount);\n    }\n\n    /// @notice Deposits NGTT into the contract and makes it available for distribution.\n    /// @param _amount Amount to add to the profit pool.\n    function addProfitPool(uint256 _amount) external onlyOwner {\n        require(_amount > 0, \"NGTT: amount must be positive\");\n        IERC20(address(this)).safeTransferFrom(msg.sender, address(this), _amount);\n        profitPool += _amount;\n        emit ProfitPoolIncreased(_amount, profitPool);\n    }\n\n    // -------------------------------------------------------------------------\n    // Skill boosts\n    // -------------------------------------------------------------------------\n\n    /// @notice Applies a skill multiplier boost to the target user.\n    /// @param _user The user to boost.\n    /// @param _multiplier Boost multiplier in basis points (100 = 1\u00d7, 500 = 5\u00d7).\n    function activateBoost(address _user, uint256 _multiplier) external onlyOwner {\n        require(_user != address(0), \"NGTT: zero user address\");\n        require(_multiplier >= 100 && _multiplier <= 500, \"NGTT: invalid multiplier\");\n        skillLevel[_user] += (_multiplier - 100);\n        emit BoostActivated(_user, _multiplier);\n    }\n\n    // -------------------------------------------------------------------------\n    // View helpers\n    // -------------------------------------------------------------------------\n\n    /// @notice Returns aggregated stats for the given user.\n    /// @param _user The user address to query.\n    /// @return games Number of games completed.\n    /// @return skill Current skill level.\n    /// @return profits Unclaimed profit balance.\n    /// @return groupId MCP group the user belongs to (0 = no group).\n    function getUserStats(address _user)\n        external\n        view\n        returns (uint256 games, uint256 skill, uint256 profits, uint256 groupId)\n    {\n        return (gamesCompleted[_user], skillLevel[_user], userProfits[_user], userToGroup[_user]);\n    }\n\n    /// @notice Returns aggregated stats for a given MCP group.\n    /// @param _groupId The group identifier to query.\n    /// @return name Group name.\n    /// @return memberCount Number of members.\n    /// @return totalTokens Total tokens earned by the group.\n    /// @return gamesPlayed Total games played within the group.\n    /// @return profitShare Cumulative profit distributed to the group.\n    function getGroupStats(uint256 _groupId)\n        external\n        view\n        returns (\n            string memory name,\n            uint256 memberCount,\n            uint256 totalTokens,\n            uint256 gamesPlayed,\n            uint256 profitShare\n        )\n    {\n        MCPGroup memory group = mcpGroups[_groupId];\n        return (group.name, group.members.length, group.totalTokens, group.gamesPlayed, group.profitShare);\n    }\n\n    // -------------------------------------------------------------------------\n    // ERC20Votes / ERC20Permit required overrides\n    // -------------------------------------------------------------------------\n\n    /// @dev Hook called after every token transfer to update vote checkpoints.\n    function _afterTokenTransfer(address from, address to, uint256 amount)\n        internal\n        override(ERC20, ERC20Votes)\n    {\n        super._afterTokenTransfer(from, to, amount);\n    }\n\n    /// @dev Mint override required by ERC20Votes.\n    function _mint(address to, uint256 amount) internal override(ERC20, ERC20Votes) {\n        super._mint(to, amount);\n    }\n\n    /// @dev Burn override required by ERC20Votes.\n    function _burn(address account, uint256 amount) internal override(ERC20, ERC20Votes) {\n        super._burn(account, amount);\n    }\n}\n"
  },
  {
    "id": "nexus-dao-governor",
    "name": "NexusDAOGovernor",
    "fileName": "NexusDAOGovernor.sol",
    "category": "Governance",
    "address": "0x7a250d5630B4cF539739dF2C5dAcb4c659F2488D",
    "description": "On-chain DAO governor combining GovernorSettings, GovernorVotes, GovernorVotesQuorumFraction, and GovernorTimelockControl.",
    "roles": [
      "Proposers (>= 10,000 NGTT)",
      "Voters",
      "Timelock Executor"
    ],
    "features": [
      "1-day Voting Delay (7200 blocks)",
      "7-day Voting Period (50400 blocks)",
      "4% Quorum (40M NGTT)",
      "10k Proposal Threshold"
    ],
    "methods": [
      {
        "name": "propose",
        "type": "write",
        "inputs": [
          {
            "name": "targets",
            "type": "address[]"
          },
          {
            "name": "values",
            "type": "uint256[]"
          },
          {
            "name": "calldatas",
            "type": "bytes[]"
          },
          {
            "name": "description",
            "type": "string"
          }
        ],
        "outputs": [
          {
            "name": "proposalId",
            "type": "uint256"
          }
        ],
        "description": "Creates an on-chain DAO proposal."
      },
      {
        "name": "castVote",
        "type": "write",
        "inputs": [
          {
            "name": "proposalId",
            "type": "uint256"
          },
          {
            "name": "support",
            "type": "uint8"
          }
        ],
        "outputs": [
          {
            "name": "weight",
            "type": "uint256"
          }
        ],
        "description": "Casts vote (0=Against, 1=For, 2=Abstain)."
      },
      {
        "name": "state",
        "type": "read",
        "inputs": [
          {
            "name": "proposalId",
            "type": "uint256"
          }
        ],
        "outputs": [
          {
            "name": "status",
            "type": "uint8"
          }
        ],
        "description": "Returns proposal state (Pending, Active, Defeated, Succeeded, Queued, Executed)."
      },
      {
        "name": "queue",
        "type": "write",
        "inputs": [
          {
            "name": "targets",
            "type": "address[]"
          },
          {
            "name": "values",
            "type": "uint256[]"
          },
          {
            "name": "calldatas",
            "type": "bytes[]"
          },
          {
            "name": "descriptionHash",
            "type": "bytes32"
          }
        ],
        "description": "Queues a succeeded proposal into the 2-day Timelock."
      },
      {
        "name": "execute",
        "type": "write",
        "inputs": [
          {
            "name": "targets",
            "type": "address[]"
          },
          {
            "name": "values",
            "type": "uint256[]"
          },
          {
            "name": "calldatas",
            "type": "bytes[]"
          },
          {
            "name": "descriptionHash",
            "type": "bytes32"
          }
        ],
        "description": "Executes a queued proposal after the timelock delay."
      }
    ],
    "sourceCode": "// SPDX-License-Identifier: MIT\npragma solidity ^0.8.20;\n\nimport \"@openzeppelin/contracts/governance/Governor.sol\";\nimport \"@openzeppelin/contracts/governance/extensions/GovernorSettings.sol\";\nimport \"@openzeppelin/contracts/governance/extensions/GovernorVotes.sol\";\nimport \"@openzeppelin/contracts/governance/extensions/GovernorVotesQuorumFraction.sol\";\nimport \"@openzeppelin/contracts/governance/extensions/GovernorTimelockControl.sol\";\n\n/// @title NexusDAOGovernor\n/// @notice On-chain governance contract for the Nexus Protocol DAO.\n/// @dev Combines four OpenZeppelin Governor extensions:\n///      - GovernorSettings        : configurable voting delay, voting period, proposal threshold.\n///      - GovernorVotes            : voting weight derived from NGTTGovernanceToken snapshots.\n///      - GovernorVotesQuorumFraction : quorum expressed as a fraction of total supply.\n///      - GovernorTimelockControl  : all passed proposals are queued in NexusDAOTimelock.\n///\n///      NES: this contract is a Nexus-authored surface governed by the\n///      Nexus Encryption Standard as documented in docs/NEXUS_ENCRYPTION_STANDARD.md.\n///\n/// Default governance parameters (may be updated via governance):\n///   - Voting delay  : 7 200 blocks  (~1 day  at 12 s/block on Ethereum mainnet)\n///   - Voting period : 50 400 blocks (~7 days at 12 s/block)\n///   - Proposal threshold : 10 000 NGTT (10_000 * 10**18)\n///   - Quorum        : 4 % of total token supply at snapshot block\n///   - Timelock delay: 2 days (set in NexusDAOTimelock constructor)\n///\n/// Proposal lifecycle:\n///   propose() \u2192 [voting delay] \u2192 castVote() \u2192 [voting period] \u2192\n///   queue() \u2192 [timelock delay] \u2192 execute()\n///\n/// Emergency controls:\n///   - Super Delegates hold CANCELLER_ROLE on the Timelock and may cancel queued\n///     operations before execution.\n///   - Owner (FuzzysTodd) is the canonical authority per GOVERNANCE.md.\ncontract NexusDAOGovernor is\n    Governor,\n    GovernorSettings,\n    GovernorVotes,\n    GovernorVotesQuorumFraction,\n    GovernorTimelockControl\n{\n    // -------------------------------------------------------------------------\n    // Constants\n    // -------------------------------------------------------------------------\n\n    /// @notice Default voting delay in blocks (~1 day at 12 s/block).\n    uint256 public constant DEFAULT_VOTING_DELAY = 7_200;\n\n    /// @notice Default voting period in blocks (~7 days at 12 s/block).\n    uint256 public constant DEFAULT_VOTING_PERIOD = 50_400;\n\n    /// @notice Default proposal threshold: 10 000 NGTT (18 decimals).\n    uint256 public constant DEFAULT_PROPOSAL_THRESHOLD = 10_000 * 10 ** 18;\n\n    /// @notice Default quorum numerator: 4 % of total token supply.\n    uint256 public constant DEFAULT_QUORUM_NUMERATOR = 4;\n\n    /// @notice Minimum allowed quorum numerator (1 %).\n    ///         Prevents governance from setting an effectively zero quorum.\n    uint256 public constant MIN_QUORUM_NUMERATOR = 1;\n\n    /// @notice Maximum allowed quorum numerator (20 %).\n    ///         Prevents governance from setting an impossible-to-reach quorum.\n    uint256 public constant MAX_QUORUM_NUMERATOR = 20;\n\n    // -------------------------------------------------------------------------\n    // Events\n    // -------------------------------------------------------------------------\n\n    /// @notice Emitted when the governor is first deployed.\n    event GovernorDeployed(address token, address timelock);\n\n    // -------------------------------------------------------------------------\n    // Constructor\n    // -------------------------------------------------------------------------\n\n    /// @notice Deploys the governor bound to a specific votes token and timelock.\n    /// @param _token  Address of the NGTTGovernanceToken (must implement IVotes).\n    /// @param _timelock Address of the NexusDAOTimelock.\n    constructor(IVotes _token, TimelockController _timelock)\n        Governor(\"NexusDAOGovernor\")\n        GovernorSettings(\n            DEFAULT_VOTING_DELAY,\n            DEFAULT_VOTING_PERIOD,\n            DEFAULT_PROPOSAL_THRESHOLD\n        )\n        GovernorVotes(_token)\n        GovernorVotesQuorumFraction(DEFAULT_QUORUM_NUMERATOR)\n        GovernorTimelockControl(_timelock)\n    {\n        emit GovernorDeployed(address(_token), address(_timelock));\n    }\n\n    // -------------------------------------------------------------------------\n    // Required overrides \u2014 Solidity multi-inheritance resolution\n    // -------------------------------------------------------------------------\n\n    /// @notice Returns the number of votes required to submit a proposal.\n    /// @return Proposal threshold in NGTT (18 decimals).\n    function proposalThreshold()\n        public\n        view\n        override(Governor, GovernorSettings)\n        returns (uint256)\n    {\n        return super.proposalThreshold();\n    }\n\n    /// @notice Returns the quorum required for a proposal at a given block.\n    /// @param blockNumber The snapshot block.\n    /// @return Minimum votes-for required.\n    function quorum(uint256 blockNumber)\n        public\n        view\n        override(IGovernor, GovernorVotesQuorumFraction)\n        returns (uint256)\n    {\n        return super.quorum(blockNumber);\n    }\n\n    /// @notice Returns the execution state of a proposal.\n    /// @param proposalId Unique identifier of the proposal.\n    /// @return Current ProposalState enum value.\n    function state(uint256 proposalId)\n        public\n        view\n        override(Governor, GovernorTimelockControl)\n        returns (ProposalState)\n    {\n        return super.state(proposalId);\n    }\n\n    /// @notice Queues a passed proposal in the timelock for delayed execution.\n    /// @param targets  Call targets.\n    /// @param values   ETH values.\n    /// @param calldatas Encoded call data.\n    /// @param descriptionHash keccak256 of the proposal description.\n    /// @return proposalId Unique proposal identifier.\n    function propose(\n        address[] memory targets,\n        uint256[] memory values,\n        bytes[] memory calldatas,\n        string memory description\n    ) public override(Governor, IGovernor) returns (uint256) {\n        return super.propose(targets, values, calldatas, description);\n    }\n\n    /// @dev Internal execution hook \u2014 forwards to GovernorTimelockControl.\n    function _execute(\n        uint256 proposalId,\n        address[] memory targets,\n        uint256[] memory values,\n        bytes[] memory calldatas,\n        bytes32 descriptionHash\n    ) internal override(Governor, GovernorTimelockControl) {\n        super._execute(proposalId, targets, values, calldatas, descriptionHash);\n    }\n\n    /// @dev Internal cancel hook \u2014 forwards to GovernorTimelockControl.\n    function _cancel(\n        address[] memory targets,\n        uint256[] memory values,\n        bytes[] memory calldatas,\n        bytes32 descriptionHash\n    ) internal override(Governor, GovernorTimelockControl) returns (uint256) {\n        return super._cancel(targets, values, calldatas, descriptionHash);\n    }\n\n    /// @dev Returns the executor address (the timelock contract).\n    function _executor()\n        internal\n        view\n        override(Governor, GovernorTimelockControl)\n        returns (address)\n    {\n        return super._executor();\n    }\n\n    /// @notice Checks interface support including the timelock extension.\n    function supportsInterface(bytes4 interfaceId)\n        public\n        view\n        override(Governor, GovernorTimelockControl)\n        returns (bool)\n    {\n        return super.supportsInterface(interfaceId);\n    }\n\n    // -------------------------------------------------------------------------\n    // Quorum governance (bounded update)\n    // -------------------------------------------------------------------------\n\n    /// @notice Updates the quorum numerator via a governance proposal.\n    /// @dev Overrides GovernorVotesQuorumFraction to enforce Nexus bounds\n    ///      [MIN_QUORUM_NUMERATOR, MAX_QUORUM_NUMERATOR].  Callable only\n    ///      through a successful on-chain governance vote (msg.sender must be\n    ///      the governor itself, i.e. called via timelock execution).\n    /// @param newQuorumNumerator New quorum percentage (1\u201320 inclusive).\n    function updateQuorumNumerator(uint256 newQuorumNumerator)\n        public\n        override\n    {\n        require(\n            newQuorumNumerator >= MIN_QUORUM_NUMERATOR,\n            \"NexusDAOGovernor: quorum below minimum\"\n        );\n        require(\n            newQuorumNumerator <= MAX_QUORUM_NUMERATOR,\n            \"NexusDAOGovernor: quorum above maximum\"\n        );\n        super.updateQuorumNumerator(newQuorumNumerator);\n    }\n}\n"
  },
  {
    "id": "nexus-dao-timelock",
    "name": "NexusDAOTimelock",
    "fileName": "NexusDAOTimelock.sol",
    "category": "Governance",
    "address": "0x388C818CA8B9251b393131C08a73683246A16699",
    "description": "OpenZeppelin TimelockController enforcing a mandatory 2-day delay on all governance decisions.",
    "roles": [
      "PROPOSER_ROLE (NexusDAOGovernor)",
      "EXECUTOR_ROLE (address(0))",
      "CANCELLER_ROLE (Owner + Super Delegates)"
    ],
    "features": [
      "2-day delay (172,800s)",
      "Emergency Cancel by Guardian",
      "Permissionless execution after delay"
    ],
    "methods": [
      {
        "name": "getMinDelay",
        "type": "read",
        "inputs": [],
        "outputs": [
          {
            "name": "delay",
            "type": "uint256"
          }
        ],
        "description": "Returns minimum execution delay in seconds."
      },
      {
        "name": "isOperationReady",
        "type": "read",
        "inputs": [
          {
            "name": "id",
            "type": "bytes32"
          }
        ],
        "outputs": [
          {
            "name": "ready",
            "type": "bool"
          }
        ],
        "description": "Checks if a queued transaction is ready for execution."
      },
      {
        "name": "cancel",
        "type": "write",
        "inputs": [
          {
            "name": "id",
            "type": "bytes32"
          }
        ],
        "description": "Emergency cancellation of a queued proposal by CANCELLER_ROLE."
      }
    ],
    "sourceCode": "// SPDX-License-Identifier: MIT\npragma solidity ^0.8.20;\n\nimport \"@openzeppelin/contracts/governance/TimelockController.sol\";\n\n/// @title NexusDAOTimelock\n/// @notice Timelock controller for the Nexus Protocol DAO governance stack.\n/// @dev Wraps OpenZeppelin TimelockController with Nexus-specific documentation and\n///      enforces the minimum 2-day delay mandated by the Nexus Governance charter.\n///      NES: this contract is a Nexus-authored surface governed by the\n///      Nexus Encryption Standard as documented in docs/NEXUS_ENCRYPTION_STANDARD.md.\n///\n/// Deployment recipe:\n///   1. Deploy NexusDAOTimelock with minDelay = 172800 (2 days), proposers = [governor],\n///      executors = [address(0)] (anyone may execute after delay), admin = owner wallet.\n///   2. After the Governor is deployed and the Timelock's PROPOSER_ROLE is granted to\n///      the Governor, revoke TIMELOCK_ADMIN_ROLE from the deployer to make the\n///      Timelock fully self-administered.\n///\n/// Access roles (inherited from OpenZeppelin TimelockController):\n///   - TIMELOCK_ADMIN_ROLE  : can manage roles; should be renounced post-setup.\n///   - PROPOSER_ROLE        : granted to the NexusDAOGovernor.\n///   - EXECUTOR_ROLE        : granted to address(0) for permissionless execution.\n///   - CANCELLER_ROLE       : granted to Owner and/or Super Delegates for emergency use.\ncontract NexusDAOTimelock is TimelockController {\n    /// @notice Minimum enforced delay in seconds (2 days).\n    uint256 public constant MIN_ENFORCED_DELAY = 2 days;\n\n    /// @notice Emitted once during construction to record the deployment parameters.\n    event TimelockDeployed(uint256 minDelay, uint256 proposerCount, uint256 executorCount);\n\n    /// @notice Deploys the timelock.\n    /// @param minDelay Minimum seconds between queuing and execution.\n    ///        Must be at least MIN_ENFORCED_DELAY (172 800 seconds).\n    /// @param proposers Addresses granted PROPOSER_ROLE (typically [governor]).\n    /// @param executors Addresses granted EXECUTOR_ROLE.\n    ///        Pass [address(0)] to allow any address to execute ready operations.\n    /// @param admin Address granted TIMELOCK_ADMIN_ROLE for initial role setup.\n    ///        Should call renounceRole(TIMELOCK_ADMIN_ROLE, admin) after setup.\n    constructor(\n        uint256 minDelay,\n        address[] memory proposers,\n        address[] memory executors,\n        address admin\n    ) TimelockController(minDelay, proposers, executors, admin) {\n        require(minDelay >= MIN_ENFORCED_DELAY, \"NexusDAOTimelock: delay below minimum\");\n        emit TimelockDeployed(minDelay, proposers.length, executors.length);\n    }\n}\n"
  },
  {
    "id": "nexus-dao-treasury",
    "name": "NexusDAOTreasury",
    "fileName": "NexusDAOTreasury.sol",
    "category": "Treasury",
    "address": "0x95aD61b0a150d79219dCF64E1E6Cc01f0B64C4cE",
    "description": "Multi-asset vault holding ETH and ERC-20s. Transfers gated by EXECUTOR_ROLE (Timelock), with 2-step GUARDIAN_ROLE co-signing above 50 ETH.",
    "roles": [
      "DEFAULT_ADMIN_ROLE (Deployer/Owner)",
      "EXECUTOR_ROLE (Timelock)",
      "GUARDIAN_ROLE (Owner & Super Delegates)"
    ],
    "features": [
      "Multi-asset (ETH, USDC, USDT, WETH, DAI, NGTT)",
      "50 ETH Multi-sig threshold",
      "Emergency Pause/Unpause"
    ],
    "methods": [
      {
        "name": "depositERC20",
        "type": "write",
        "inputs": [
          {
            "name": "token",
            "type": "address"
          },
          {
            "name": "amount",
            "type": "uint256"
          }
        ],
        "description": "Deposits ERC-20 tokens into the treasury vault."
      },
      {
        "name": "requestLargeTransferETH",
        "type": "write",
        "inputs": [
          {
            "name": "to",
            "type": "address"
          },
          {
            "name": "amount",
            "type": "uint256"
          }
        ],
        "outputs": [
          {
            "name": "nonce",
            "type": "uint256"
          }
        ],
        "description": "Initiates a transfer > 50 ETH requiring Guardian co-signing."
      },
      {
        "name": "confirmLargeETHTransfer",
        "type": "write",
        "inputs": [
          {
            "name": "nonce",
            "type": "uint256"
          }
        ],
        "description": "Guardian co-signs a pending large transfer."
      },
      {
        "name": "executeLargeETHTransfer",
        "type": "write",
        "inputs": [
          {
            "name": "nonce",
            "type": "uint256"
          }
        ],
        "description": "Executes co-signed transfer after both roles approve."
      },
      {
        "name": "pause",
        "type": "write",
        "inputs": [],
        "description": "Emergency pauses treasury withdrawals."
      },
      {
        "name": "unpause",
        "type": "write",
        "inputs": [],
        "description": "Unpauses treasury operations."
      },
      {
        "name": "ethBalance",
        "type": "read",
        "inputs": [],
        "outputs": [
          {
            "name": "balance",
            "type": "uint256"
          }
        ],
        "description": "Current ETH balance held in treasury."
      },
      {
        "name": "tokenBalance",
        "type": "read",
        "inputs": [
          {
            "name": "token",
            "type": "address"
          }
        ],
        "outputs": [
          {
            "name": "balance",
            "type": "uint256"
          }
        ],
        "description": "Current ERC-20 token balance."
      }
    ],
    "sourceCode": "// SPDX-License-Identifier: MIT\npragma solidity ^0.8.20;\n\nimport \"@openzeppelin/contracts/access/AccessControl.sol\";\nimport \"@openzeppelin/contracts/security/ReentrancyGuard.sol\";\nimport \"@openzeppelin/contracts/token/ERC20/utils/SafeERC20.sol\";\nimport \"@openzeppelin/contracts/token/ERC20/IERC20.sol\";\n\n/// @title NexusDAOTreasury\n/// @notice DAO-controlled treasury that holds ETH and ERC-20 tokens.\n/// @dev All fund-movement functions are restricted to EXECUTOR_ROLE, which is\n///      assigned exclusively to the NexusDAOTimelock after deployment.  No\n///      funds can therefore leave the treasury without a successful on-chain\n///      governance vote followed by the mandatory timelock delay.\n///\n///      Large transfers (above MULTISIG_THRESHOLD) additionally require a\n///      second GUARDIAN_ROLE co-signature before the executor can complete the\n///      transfer.  This two-step approval prevents a single compromised key\n///      from draining the treasury even if it holds EXECUTOR_ROLE.\n///\n///      Flow for a large transfer:\n///        1. EXECUTOR_ROLE calls requestLargeTransfer*() \u2014 creates a pending entry.\n///        2. A GUARDIAN_ROLE (\u2260 msg.sender of step 1) calls confirmLargeTransfer*().\n///        3. EXECUTOR_ROLE calls executeLargeTransfer*() \u2014 funds are moved.\n///\n///      NES: this contract is a Nexus-authored surface governed by the\n///      Nexus Encryption Standard as documented in docs/NEXUS_ENCRYPTION_STANDARD.md.\n///\n/// Access model:\n///   - DEFAULT_ADMIN_ROLE  : deployment-time admin (owner wallet); manages role grants.\n///   - EXECUTOR_ROLE       : granted to NexusDAOTimelock; the only role that may\n///                           transfer ETH or ERC-20 tokens out of the treasury.\n///   - GUARDIAN_ROLE       : granted to Owner and/or Super Delegates; may pause\n///                           treasury operations in an emergency, and must co-sign\n///                           large transfers above MULTISIG_THRESHOLD.\n///\n/// Deployment:\n///   1. Deploy NexusDAOTreasury(admin = owner wallet).\n///   2. After the Timelock is deployed, call\n///        treasury.grantRole(EXECUTOR_ROLE, timelockAddress)\n///   3. Optionally grant GUARDIAN_ROLE to the owner and each Super Delegate.\ncontract NexusDAOTreasury is AccessControl, ReentrancyGuard {\n    using SafeERC20 for IERC20;\n\n    // -------------------------------------------------------------------------\n    // Roles\n    // -------------------------------------------------------------------------\n\n    /// @notice Role required to transfer ETH or tokens out of the treasury.\n    ///         Assigned exclusively to NexusDAOTimelock.\n    bytes32 public constant EXECUTOR_ROLE = keccak256(\"EXECUTOR_ROLE\");\n\n    /// @notice Role that can pause and unpause treasury operations.\n    ///         Assigned to Owner and Super Delegates for emergency response.\n    ///         Also required to co-sign large transfers.\n    bytes32 public constant GUARDIAN_ROLE = keccak256(\"GUARDIAN_ROLE\");\n\n    // -------------------------------------------------------------------------\n    // Multi-sig large-transfer configuration\n    // -------------------------------------------------------------------------\n\n    /// @notice ETH amount (in wei) above which a guardian co-signature is required.\n    ///         Default: 1 ETH. Updatable by DEFAULT_ADMIN_ROLE via governance.\n    uint256 public MULTISIG_THRESHOLD = 1 ether;\n\n    /// @notice ERC-20 amount (in token units, 18 decimals) above which a guardian\n    ///         co-signature is required.\n    uint256 public ERC20_MULTISIG_THRESHOLD = 1_000 * 10 ** 18;\n\n    // -------------------------------------------------------------------------\n    // Pending large-transfer state\n    // -------------------------------------------------------------------------\n\n    struct PendingETHTransfer {\n        address payable recipient;\n        uint256 amount;\n        string reason;\n        address requestedBy;\n        address confirmedBy;\n        uint256 requestedAt;\n        bool executed;\n    }\n\n    struct PendingERC20Transfer {\n        address token;\n        address recipient;\n        uint256 amount;\n        string reason;\n        address requestedBy;\n        address confirmedBy;\n        uint256 requestedAt;\n        bool executed;\n    }\n\n    mapping(uint256 => PendingETHTransfer) public pendingETH;\n    mapping(uint256 => PendingERC20Transfer) public pendingERC20;\n    uint256 private _pendingETHNonce;\n    uint256 private _pendingERC20Nonce;\n\n    // -------------------------------------------------------------------------\n    // State\n    // -------------------------------------------------------------------------\n\n    /// @notice Whether treasury transfers are currently paused.\n    bool public paused;\n\n    // -------------------------------------------------------------------------\n    // Events\n    // -------------------------------------------------------------------------\n\n    /// @notice Emitted when ETH is deposited into the treasury.\n    event ETHDeposited(address indexed sender, uint256 amount);\n\n    /// @notice Emitted when ETH is transferred out of the treasury by governance.\n    event ETHTransferred(address indexed recipient, uint256 amount, string reason);\n\n    /// @notice Emitted when an ERC-20 token is deposited into the treasury.\n    event ERC20Deposited(address indexed token, address indexed sender, uint256 amount);\n\n    /// @notice Emitted when an ERC-20 token is transferred out of the treasury.\n    event ERC20Transferred(address indexed token, address indexed recipient, uint256 amount, string reason);\n\n    /// @notice Emitted when the treasury is paused by a guardian.\n    event TreasuryPaused(address indexed guardian);\n\n    /// @notice Emitted when the treasury is unpaused by a guardian.\n    event TreasuryUnpaused(address indexed guardian);\n\n    /// @notice Emitted when a large ETH transfer is requested.\n    event LargeETHTransferRequested(uint256 indexed nonce, address indexed recipient, uint256 amount, address requestedBy);\n\n    /// @notice Emitted when a large ETH transfer is confirmed by a guardian.\n    event LargeETHTransferConfirmed(uint256 indexed nonce, address indexed confirmedBy);\n\n    /// @notice Emitted when a large ETH transfer is executed after confirmation.\n    event LargeETHTransferExecuted(uint256 indexed nonce, address indexed recipient, uint256 amount);\n\n    /// @notice Emitted when a large ERC-20 transfer is requested.\n    event LargeERC20TransferRequested(\n        uint256 indexed nonce, address indexed token, address indexed recipient, uint256 amount, address requestedBy\n    );\n\n    /// @notice Emitted when a large ERC-20 transfer is confirmed by a guardian.\n    event LargeERC20TransferConfirmed(uint256 indexed nonce, address indexed confirmedBy);\n\n    /// @notice Emitted when a large ERC-20 transfer is executed after confirmation.\n    event LargeERC20TransferExecuted(uint256 indexed nonce, address indexed token, address indexed recipient, uint256 amount);\n\n    /// @notice Emitted when the multisig ETH threshold is updated.\n    event MultisigThresholdUpdated(uint256 newThreshold);\n\n    /// @notice Emitted when the multisig ERC-20 threshold is updated.\n    event ERC20MultisigThresholdUpdated(uint256 newThreshold);\n\n    // -------------------------------------------------------------------------\n    // Modifiers\n    // -------------------------------------------------------------------------\n\n    /// @dev Reverts if the treasury is currently paused.\n    modifier whenNotPaused() {\n        require(!paused, \"NexusDAOTreasury: paused\");\n        _;\n    }\n\n    // -------------------------------------------------------------------------\n    // Constructor\n    // -------------------------------------------------------------------------\n\n    /// @notice Deploys the treasury and grants the deployer DEFAULT_ADMIN_ROLE.\n    /// @param admin Address that holds DEFAULT_ADMIN_ROLE.  This should be the\n    ///        owner wallet (`0x33ffc308e693a5b49e0ee0241f41f03ccef495f2`).\n    constructor(address admin) {\n        require(admin != address(0), \"NexusDAOTreasury: zero admin\");\n        _grantRole(DEFAULT_ADMIN_ROLE, admin);\n        _grantRole(GUARDIAN_ROLE, admin);\n    }\n\n    // -------------------------------------------------------------------------\n    // Receive / deposit\n    // -------------------------------------------------------------------------\n\n    /// @notice Accepts ETH deposits directly.\n    receive() external payable {\n        emit ETHDeposited(msg.sender, msg.value);\n    }\n\n    /// @notice Accepts ETH via an explicit call (same as receive).\n    fallback() external payable {\n        emit ETHDeposited(msg.sender, msg.value);\n    }\n\n    /// @notice Convenience function to deposit ERC-20 tokens into the treasury.\n    /// @param token  The ERC-20 token address.\n    /// @param amount Amount to deposit (caller must have approved this contract first).\n    function depositERC20(address token, uint256 amount) external nonReentrant {\n        require(token != address(0), \"NexusDAOTreasury: zero token address\");\n        require(amount > 0, \"NexusDAOTreasury: zero amount\");\n        IERC20(token).safeTransferFrom(msg.sender, address(this), amount);\n        emit ERC20Deposited(token, msg.sender, amount);\n    }\n\n    // -------------------------------------------------------------------------\n    // ETH transfers (governance-only, with multi-sig for large amounts)\n    // -------------------------------------------------------------------------\n\n    /// @notice Transfers ETH to the specified recipient (amounts \u2264 MULTISIG_THRESHOLD only).\n    ///         For larger amounts use requestLargeETHTransfer / confirmLargeETHTransfer /\n    ///         executeLargeETHTransfer. Can only be called by the NexusDAOTimelock (EXECUTOR_ROLE).\n    /// @param recipient Destination address.\n    /// @param amount    Amount of ETH in wei.\n    /// @param reason    Human-readable description for audit logging.\n    function transferETH(address payable recipient, uint256 amount, string calldata reason)\n        external\n        nonReentrant\n        whenNotPaused\n        onlyRole(EXECUTOR_ROLE)\n    {\n        require(recipient != address(0), \"NexusDAOTreasury: zero recipient\");\n        require(amount > 0, \"NexusDAOTreasury: zero amount\");\n        require(amount <= MULTISIG_THRESHOLD, \"NexusDAOTreasury: amount exceeds threshold; use large-transfer flow\");\n        require(address(this).balance >= amount, \"NexusDAOTreasury: insufficient ETH\");\n\n        (bool success,) = recipient.call{value: amount}(\"\");\n        require(success, \"NexusDAOTreasury: ETH transfer failed\");\n\n        emit ETHTransferred(recipient, amount, reason);\n    }\n\n    /// @notice Requests a large ETH transfer (above MULTISIG_THRESHOLD).\n    ///         Must be confirmed by a different guardian before execution.\n    /// @param recipient Destination address.\n    /// @param amount    Amount of ETH in wei (must exceed MULTISIG_THRESHOLD).\n    /// @param reason    Human-readable description for audit logging.\n    /// @return nonce Identifier for this pending transfer.\n    function requestLargeETHTransfer(address payable recipient, uint256 amount, string calldata reason)\n        external\n        whenNotPaused\n        onlyRole(EXECUTOR_ROLE)\n        returns (uint256 nonce)\n    {\n        require(recipient != address(0), \"NexusDAOTreasury: zero recipient\");\n        require(amount > MULTISIG_THRESHOLD, \"NexusDAOTreasury: use transferETH for small amounts\");\n        require(address(this).balance >= amount, \"NexusDAOTreasury: insufficient ETH\");\n\n        nonce = ++_pendingETHNonce;\n        pendingETH[nonce] = PendingETHTransfer({\n            recipient: recipient,\n            amount: amount,\n            reason: reason,\n            requestedBy: msg.sender,\n            confirmedBy: address(0),\n            requestedAt: block.timestamp,\n            executed: false\n        });\n\n        emit LargeETHTransferRequested(nonce, recipient, amount, msg.sender);\n    }\n\n    /// @notice Co-signs a pending large ETH transfer.\n    ///         Must be called by a GUARDIAN_ROLE address different from the requester.\n    /// @param nonce The pending transfer identifier.\n    function confirmLargeETHTransfer(uint256 nonce) external onlyRole(GUARDIAN_ROLE) {\n        PendingETHTransfer storage transfer = pendingETH[nonce];\n        require(transfer.requestedAt > 0, \"NexusDAOTreasury: unknown nonce\");\n        require(!transfer.executed, \"NexusDAOTreasury: already executed\");\n        require(transfer.confirmedBy == address(0), \"NexusDAOTreasury: already confirmed\");\n        require(msg.sender != transfer.requestedBy, \"NexusDAOTreasury: requester cannot confirm\");\n\n        transfer.confirmedBy = msg.sender;\n        emit LargeETHTransferConfirmed(nonce, msg.sender);\n    }\n\n    /// @notice Executes a large ETH transfer that has been confirmed by a guardian.\n    /// @param nonce The pending transfer identifier.\n    function executeLargeETHTransfer(uint256 nonce)\n        external\n        nonReentrant\n        whenNotPaused\n        onlyRole(EXECUTOR_ROLE)\n    {\n        PendingETHTransfer storage transfer = pendingETH[nonce];\n        require(transfer.requestedAt > 0, \"NexusDAOTreasury: unknown nonce\");\n        require(!transfer.executed, \"NexusDAOTreasury: already executed\");\n        require(transfer.confirmedBy != address(0), \"NexusDAOTreasury: not yet confirmed\");\n        require(address(this).balance >= transfer.amount, \"NexusDAOTreasury: insufficient ETH\");\n\n        transfer.executed = true;\n\n        (bool success,) = transfer.recipient.call{value: transfer.amount}(\"\");\n        require(success, \"NexusDAOTreasury: ETH transfer failed\");\n\n        emit LargeETHTransferExecuted(nonce, transfer.recipient, transfer.amount);\n        emit ETHTransferred(transfer.recipient, transfer.amount, transfer.reason);\n    }\n\n    // -------------------------------------------------------------------------\n    // ERC-20 transfers (governance-only, with multi-sig for large amounts)\n    // -------------------------------------------------------------------------\n\n    /// @notice Transfers ERC-20 tokens to the specified recipient.\n    ///         For amounts \u2264 ERC20_MULTISIG_THRESHOLD, executes immediately.\n    ///         Can only be called by the NexusDAOTimelock (EXECUTOR_ROLE).\n    /// @param token     The ERC-20 token address.\n    /// @param recipient Destination address.\n    /// @param amount    Token amount (in token's native decimals).\n    /// @param reason    Human-readable description for audit logging.\n    function transferERC20(\n        address token,\n        address recipient,\n        uint256 amount,\n        string calldata reason\n    ) external nonReentrant whenNotPaused onlyRole(EXECUTOR_ROLE) {\n        require(token != address(0), \"NexusDAOTreasury: zero token address\");\n        require(recipient != address(0), \"NexusDAOTreasury: zero recipient\");\n        require(amount > 0, \"NexusDAOTreasury: zero amount\");\n        require(amount <= ERC20_MULTISIG_THRESHOLD, \"NexusDAOTreasury: amount exceeds threshold; use large-transfer flow\");\n\n        IERC20(token).safeTransfer(recipient, amount);\n        emit ERC20Transferred(token, recipient, amount, reason);\n    }\n\n    /// @notice Requests a large ERC-20 transfer (above ERC20_MULTISIG_THRESHOLD).\n    /// @return nonce Identifier for this pending transfer.\n    function requestLargeERC20Transfer(\n        address token,\n        address recipient,\n        uint256 amount,\n        string calldata reason\n    ) external whenNotPaused onlyRole(EXECUTOR_ROLE) returns (uint256 nonce) {\n        require(token != address(0), \"NexusDAOTreasury: zero token address\");\n        require(recipient != address(0), \"NexusDAOTreasury: zero recipient\");\n        require(amount > ERC20_MULTISIG_THRESHOLD, \"NexusDAOTreasury: use transferERC20 for small amounts\");\n\n        nonce = ++_pendingERC20Nonce;\n        pendingERC20[nonce] = PendingERC20Transfer({\n            token: token,\n            recipient: recipient,\n            amount: amount,\n            reason: reason,\n            requestedBy: msg.sender,\n            confirmedBy: address(0),\n            requestedAt: block.timestamp,\n            executed: false\n        });\n\n        emit LargeERC20TransferRequested(nonce, token, recipient, amount, msg.sender);\n    }\n\n    /// @notice Co-signs a pending large ERC-20 transfer.\n    /// @param nonce The pending transfer identifier.\n    function confirmLargeERC20Transfer(uint256 nonce) external onlyRole(GUARDIAN_ROLE) {\n        PendingERC20Transfer storage transfer = pendingERC20[nonce];\n        require(transfer.requestedAt > 0, \"NexusDAOTreasury: unknown nonce\");\n        require(!transfer.executed, \"NexusDAOTreasury: already executed\");\n        require(transfer.confirmedBy == address(0), \"NexusDAOTreasury: already confirmed\");\n        require(msg.sender != transfer.requestedBy, \"NexusDAOTreasury: requester cannot confirm\");\n\n        transfer.confirmedBy = msg.sender;\n        emit LargeERC20TransferConfirmed(nonce, msg.sender);\n    }\n\n    /// @notice Executes a large ERC-20 transfer that has been confirmed by a guardian.\n    /// @param nonce The pending transfer identifier.\n    function executeLargeERC20Transfer(uint256 nonce)\n        external\n        nonReentrant\n        whenNotPaused\n        onlyRole(EXECUTOR_ROLE)\n    {\n        PendingERC20Transfer storage transfer = pendingERC20[nonce];\n        require(transfer.requestedAt > 0, \"NexusDAOTreasury: unknown nonce\");\n        require(!transfer.executed, \"NexusDAOTreasury: already executed\");\n        require(transfer.confirmedBy != address(0), \"NexusDAOTreasury: not yet confirmed\");\n\n        transfer.executed = true;\n\n        IERC20(transfer.token).safeTransfer(transfer.recipient, transfer.amount);\n        emit LargeERC20TransferExecuted(nonce, transfer.token, transfer.recipient, transfer.amount);\n        emit ERC20Transferred(transfer.token, transfer.recipient, transfer.amount, transfer.reason);\n    }\n\n    // -------------------------------------------------------------------------\n    // Threshold administration\n    // -------------------------------------------------------------------------\n\n    /// @notice Updates the ETH multi-sig threshold. Callable by DEFAULT_ADMIN_ROLE.\n    /// @param newThreshold New threshold in wei (must be > 0).\n    function setMultisigThreshold(uint256 newThreshold) external onlyRole(DEFAULT_ADMIN_ROLE) {\n        require(newThreshold > 0, \"NexusDAOTreasury: zero threshold\");\n        MULTISIG_THRESHOLD = newThreshold;\n        emit MultisigThresholdUpdated(newThreshold);\n    }\n\n    /// @notice Updates the ERC-20 multi-sig threshold. Callable by DEFAULT_ADMIN_ROLE.\n    /// @param newThreshold New threshold in token units (must be > 0).\n    function setERC20MultisigThreshold(uint256 newThreshold) external onlyRole(DEFAULT_ADMIN_ROLE) {\n        require(newThreshold > 0, \"NexusDAOTreasury: zero threshold\");\n        ERC20_MULTISIG_THRESHOLD = newThreshold;\n        emit ERC20MultisigThresholdUpdated(newThreshold);\n    }\n\n    // -------------------------------------------------------------------------\n    // Emergency controls (guardian)\n    // -------------------------------------------------------------------------\n\n    /// @notice Pauses all outgoing transfers.  Called by a guardian in an emergency.\n    function pause() external onlyRole(GUARDIAN_ROLE) {\n        require(!paused, \"NexusDAOTreasury: already paused\");\n        paused = true;\n        emit TreasuryPaused(msg.sender);\n    }\n\n    /// @notice Unpauses the treasury after an emergency is resolved.\n    function unpause() external onlyRole(GUARDIAN_ROLE) {\n        require(paused, \"NexusDAOTreasury: not paused\");\n        paused = false;\n        emit TreasuryUnpaused(msg.sender);\n    }\n\n    // -------------------------------------------------------------------------\n    // View helpers\n    // -------------------------------------------------------------------------\n\n    /// @notice Returns the current ETH balance held by the treasury.\n    /// @return ETH balance in wei.\n    function ethBalance() external view returns (uint256) {\n        return address(this).balance;\n    }\n\n    /// @notice Returns the current balance of an ERC-20 token held by the treasury.\n    /// @param token The ERC-20 token address.\n    /// @return Token balance in the token's native decimals.\n    function tokenBalance(address token) external view returns (uint256) {\n        return IERC20(token).balanceOf(address(this));\n    }\n}\n"
  },
  {
    "id": "nexus-builder-fund",
    "name": "NexusBuilderFund",
    "fileName": "NexusBuilderFund.sol",
    "category": "Funding",
    "address": "0x514910771AF9Ca656af840dff83E8264EcF986CA",
    "description": "Protocol Guild-style developer compensation pool. Routes API and contract usage micro-fees in USD, ETH, and Satoshis (BTC) directly to registered builders.",
    "roles": [
      "DEFAULT_ADMIN_ROLE",
      "ORACLE_ROLE (Chainlink Automation)",
      "REGISTERED_BUILDER"
    ],
    "features": [
      "USD cent denomination",
      "Chainlink ETH/USD conversion",
      "Satoshi/BTC layer",
      "Proportional pull-rewards"
    ],
    "methods": [
      {
        "name": "depositFees",
        "type": "write",
        "inputs": [],
        "description": "Explicitly deposits ETH fee revenue into the builder fund."
      },
      {
        "name": "recordUsage",
        "type": "write",
        "inputs": [
          {
            "name": "endpoint",
            "type": "bytes32"
          },
          {
            "name": "callCount",
            "type": "uint256"
          }
        ],
        "description": "Oracle registers off-chain API activity."
      },
      {
        "name": "claimReward",
        "type": "write",
        "inputs": [],
        "description": "Registered builder pulls accumulated proportional share of fees."
      },
      {
        "name": "getFeeSatoshis",
        "type": "read",
        "inputs": [],
        "outputs": [
          {
            "name": "satoshis",
            "type": "uint256"
          }
        ],
        "description": "Calculates fee equivalent in Bitcoin Satoshis."
      },
      {
        "name": "getFeeWei",
        "type": "read",
        "inputs": [],
        "outputs": [
          {
            "name": "weiAmount",
            "type": "uint256"
          }
        ],
        "description": "Calculates fee equivalent in Ethereum Wei."
      }
    ],
    "sourceCode": "// SPDX-License-Identifier: MIT\npragma solidity ^0.8.20;\n\nimport \"@openzeppelin/contracts/access/AccessControl.sol\";\nimport \"@openzeppelin/contracts/security/ReentrancyGuard.sol\";\nimport \"@openzeppelin/contracts/token/ERC20/utils/SafeERC20.sol\";\nimport \"@openzeppelin/contracts/token/ERC20/IERC20.sol\";\n\n/// @title NexusBuilderFund\n/// @notice Protocol Guild\u2013style developer compensation pool for the Nexus Protocol DAO.\n///\n/// \u2500\u2500\u2500 WHAT THIS IS \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\n/// Every time someone pays to use Nexus-authored code (via the REST API, a\n/// contract call, or a direct `depositFees()` call), ETH is routed into this\n/// contract.  Registered builders earn a proportional slice of that revenue\n/// stream simply by having contributed to the protocol \u2014 no invoices, no\n/// intermediaries, no payment processor.\n///\n/// \u2500\u2500\u2500 HOW THE PAYMENT FLOW WORKS \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\n/// 1. API / Contract usage emits a micro-fee:\n///      \u2022 The financial-ops-rest-server logs every API call.\n///      \u2022 A Chainlink Automation or trusted ORACLE_ROLE wallet calls\n///        `recordUsage(bytes32 endpoint, uint256 callCount)` to register\n///        off-chain activity on-chain.\n///      \u2022 Callers of on-chain entry-points can send ETH directly; the\n///        `depositFees()` function also accepts explicit deposits.\n///\n/// 2. ETH accumulates in this contract.\n///\n/// 3. Any registered builder calls `claimReward()` to pull their proportional\n///    share of the accumulated ETH at any time.\n///\n/// \u2500\u2500\u2500 FEE DENOMINATION \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\n/// Fee amounts are set in USD-cent integer units (e.g., `feePerCallUsdCents = 1`\n/// = $0.01).  A Chainlink ETH/USD AggregatorV3 feed converts the USD-cent\n/// price to the equivalent ETH amount on-the-fly, so callers always know\n/// exactly how many wei to send.\n///\n/// \u2500\u2500\u2500 SATOSHI / BTC LAYER \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\n/// Bitcoin (Satoshi) denomination is supported via `getFeeSatoshis()`:\n/// the same USD-cent fee is converted to satoshis using a Chainlink BTC/USD\n/// feed.  Lightning-network payment channels and WBTC wrappers can route\n/// satoshi-denominated fees to this contract via a bridge wallet that calls\n/// `depositFees{value: weiEquivalent}()`.\n///\n/// \u2500\u2500\u2500 DATA-DRIVEN ORACLE SETTLEMENT \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\n/// `recordUsage()` is callable by any address with ORACLE_ROLE (typically a\n/// Chainlink Automation upkeep or the Nexus signal-bus server acting as a\n/// trusted relayer).  Each call records an endpoint-level usage batch.  The\n/// total accumulated usage counter drives the dashboard at\n/// /api/v1/builder-fund/stats on the REST server.\n///\n/// \u2500\u2500\u2500 PLACEMENT WALLET \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\n/// A `placementWallet` and `placementBps` (basis points, max 5 000 = 50%) can\n/// be configured by the admin.  On every `depositFees()` or plain ETH receive,\n/// `placementBps / 10 000` of the incoming ETH is forwarded **immediately** to\n/// `placementWallet` (e.g., the dashboard treasury wallet).  The remainder\n/// enters the pool for builder claims.  Setting `placementWallet = address(0)`\n/// or `placementBps = 0` disables the auto-forward.\n///\n/// \u2500\u2500\u2500 NGTT TOKEN AWARDS \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\n/// An optional `ngttToken` (IERC20) and `ngttRewardPerEthWei` rate can be set\n/// by the admin.  When a builder claims ETH rewards, the contract transfers\n/// `claimedEth * ngttRewardPerEthWei / 1e18` NGTT tokens from its own balance\n/// to the builder's wallet as an additional bonus.  The contract must hold\n/// NGTT tokens (sent by the admin or minted via governance) for this to work;\n/// if the balance is insufficient the ETH claim still succeeds (tokens silently\n/// skipped).  Set `ngttRewardPerEthWei = 0` to disable.\n///\n/// \u2500\u2500\u2500 SECURITY \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\n/// \u2022 `depositFees()` is payable and open to anyone (API gateways, contract\n///    hooks, bridge wallets, individual users tipping the protocol).\n/// \u2022 Placement forward uses `call{value:}`, guarded by ReentrancyGuard.\n/// \u2022 Claim math uses integer division; dust (wei remainder) stays in the pool.\n/// \u2022 ReentrancyGuard on all fund-movement functions.\n/// \u2022 DEFAULT_ADMIN_ROLE required to register/remove builders.\n/// \u2022 ORACLE_ROLE required to record usage (so external usage data is trust-\n///   scoped to the oracle, not to individual callers).\n///\n/// NES: this contract is a Nexus-authored surface governed by the\n/// Nexus Encryption Standard as documented in docs/NEXUS_ENCRYPTION_STANDARD.md.\n\n// \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\n// Chainlink price-feed interface (minimal \u2014 only latestRoundData used)\n// \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\n\n/// @dev Minimal AggregatorV3 interface so we avoid importing the full\n///      Chainlink NPM package at deployment time.\ninterface IAggregatorV3 {\n    function latestRoundData()\n        external\n        view\n        returns (\n            uint80  roundId,\n            int256  answer,\n            uint256 startedAt,\n            uint256 updatedAt,\n            uint80  answeredInRound\n        );\n    function decimals() external view returns (uint8);\n}\n\ncontract NexusBuilderFund is AccessControl, ReentrancyGuard {\n    using SafeERC20 for IERC20;\n\n    // \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\n    // Roles\n    // \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\n\n    /// @notice May call recordUsage() \u2014 assigned to Chainlink Automation upkeep\n    ///         or the Nexus signal-bus server acting as a trusted oracle.\n    bytes32 public constant ORACLE_ROLE = keccak256(\"ORACLE_ROLE\");\n\n    /// @notice Chainlink ETH/USD price feed (8 decimal answer, e.g. 3_000_00000000 = $3000).\n    ///         Set to address(0) to disable USD-denominated fee conversion.\n    IAggregatorV3 public ethUsdFeed;\n\n    /// @notice Chainlink BTC/USD price feed for Satoshi denomination.\n    ///         Set to address(0) to disable BTC-denominated fee conversion.\n    IAggregatorV3 public btcUsdFeed;\n\n    // \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\n    // Builder registry\n    // \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\n\n    struct Builder {\n        address wallet;        // Payment destination\n        uint256 shares;        // Relative weight in the pool (e.g., 100 = 1 share)\n        string  handle;        // GitHub handle or display name\n        string  component;     // Expert domain / code-space attribution (e.g., \"Solidity-DeFi-Core\")\n        uint256 totalClaimed;  // Cumulative ETH (in wei) ever claimed by this builder\n        bool    active;        // False = removed from pool but historical data kept\n    }\n\n    /// @notice All registered builders (index = builderId).\n    Builder[] public builders;\n\n    /// @notice Wallet \u2192 builderId (+1, so 0 = not registered).\n    mapping(address => uint256) public builderIndex;\n\n    /// @notice keccak256(component) \u2192 list of builderIds attributed to that component.\n    mapping(bytes32 => uint256[]) private _buildersByComponent;\n\n    /// @notice Total shares across all active builders.\n    uint256 public totalShares;\n\n    // \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\n    // Placement wallet \u2014 auto-forward a cut of each deposit\n    // \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\n\n    /// @notice Destination for the auto-forwarded placement cut.\n    ///         Set to address(0) to disable placement forwarding.\n    address public placementWallet;\n\n    /// @notice Basis points (0\u20135000) of each deposit auto-forwarded to\n    ///         placementWallet.  10 000 bps = 100%.  Max 50% = 5 000.\n    uint256 public placementBps;\n\n    // \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\n    // NGTT token award \u2014 bonus tokens given to builders on ETH claim\n    // \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\n\n    /// @notice The NGTT governance token.  Set to address(0) to disable.\n    IERC20 public ngttToken;\n\n    /// @notice NGTT tokens awarded per 1 ETH (1e18 wei) claimed.\n    ///         E.g., 1000e18 = 1 000 NGTT per ETH claimed.\n    ///         Set to 0 to disable token awards.\n    uint256 public ngttRewardPerEthWei;\n\n    // \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\n    // Fee configuration\n    // \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\n\n    /// @notice USD-cent fee per API call (e.g., 1 = $0.01).  Zero disables\n    ///         per-call fee enforcement (used when fees are deposited externally\n    ///         by a bridge or aggregator rather than enforced at call time).\n    uint256 public feePerCallUsdCents;\n\n    // \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\n    // Usage accounting\n    // \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\n\n    /// @notice Cumulative API calls recorded per endpoint (keccak256 of name).\n    mapping(bytes32 => uint256) public usageByEndpoint;\n\n    /// @notice Grand total of all recorded API calls.\n    uint256 public totalUsageCalls;\n\n    // \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\n    // Snapshot accounting (enables proportional claims without iteration)\n    // \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\n\n    /// @notice Running total of ETH (wei) ever deposited into the fund.\n    uint256 public totalDeposited;\n\n    /// @notice Snapshot of totalDeposited at the time each builder last claimed.\n    mapping(uint256 => uint256) private _lastClaimSnapshot;\n\n    // \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\n    // Events\n    // \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\n\n    /// @notice Emitted when a builder is registered.\n    event BuilderRegistered(uint256 indexed builderId, address indexed wallet, string handle, uint256 shares, string component);\n\n    /// @notice Emitted when a builder's active status or shares are updated.\n    event BuilderUpdated(uint256 indexed builderId, uint256 newShares, bool active);\n\n    /// @notice Emitted when ETH is deposited into the fund.\n    event FeesDeposited(address indexed from, uint256 amount, string note);\n\n    /// @notice Emitted when API usage is recorded by the oracle.\n    event UsageRecorded(bytes32 indexed endpoint, uint256 callCount, address indexed oracle);\n\n    /// @notice Emitted when a builder claims their reward.\n    event RewardClaimed(uint256 indexed builderId, address indexed wallet, uint256 amount);\n\n    /// @notice Emitted when the ETH/USD or BTC/USD feed address is updated.\n    event PriceFeedUpdated(string feedName, address newFeed);\n\n    /// @notice Emitted when the per-call USD-cent fee is updated.\n    event FeePerCallUpdated(uint256 newFeeUsdCents);\n\n    /// @notice Emitted when the placement wallet or bps is updated.\n    event PlacementConfigUpdated(address indexed wallet, uint256 bps);\n\n    /// @notice Emitted when ETH is auto-forwarded to the placement wallet.\n    event PlacementSent(address indexed to, uint256 amount);\n\n    /// @notice Emitted when NGTT tokens are awarded to a builder on claim.\n    event NgttAwarded(uint256 indexed builderId, address indexed wallet, uint256 ngttAmount);\n\n    /// @notice Emitted when the NGTT token award config is updated.\n    event NgttRewardConfigUpdated(address indexed token, uint256 rewardPerEthWei);\n\n    // \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\n    // Constructor\n    // \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\n\n    /// @notice Deploys the builder fund.\n    /// @param admin                DEFAULT_ADMIN_ROLE holder (owner wallet).\n    /// @param _ethUsdFeed          Chainlink ETH/USD feed address (address(0) to disable).\n    /// @param _btcUsdFeed          Chainlink BTC/USD feed address (address(0) to disable).\n    /// @param _feePerCallUsdCents  Initial per-call fee in USD cents (0 = free / externally metered).\n    /// @param _placementWallet     Auto-forward destination (address(0) to disable).\n    /// @param _placementBps        Basis points of each deposit to auto-forward (0\u20135000).\n    constructor(\n        address admin,\n        address _ethUsdFeed,\n        address _btcUsdFeed,\n        uint256 _feePerCallUsdCents,\n        address _placementWallet,\n        uint256 _placementBps\n    ) {\n        require(admin != address(0), \"NexusBuilderFund: zero admin\");\n        require(_placementBps <= 5000, \"NexusBuilderFund: placementBps > 50%\");\n        _grantRole(DEFAULT_ADMIN_ROLE, admin);\n        _grantRole(ORACLE_ROLE, admin); // Admin can also act as oracle initially\n        ethUsdFeed = IAggregatorV3(_ethUsdFeed);\n        btcUsdFeed = IAggregatorV3(_btcUsdFeed);\n        feePerCallUsdCents = _feePerCallUsdCents;\n        placementWallet = _placementWallet;\n        placementBps = _placementBps;\n    }\n\n    // \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\n    // Builder registry management\n    // \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\n\n    /// @notice Registers a new builder in the fund (legacy overload \u2014 component defaults to \"\").\n    /// @param wallet   Payment destination address.\n    /// @param shares   Relative weight (e.g., 100 = 1 standard share).\n    /// @param handle   GitHub handle or display name for the dashboard.\n    /// @return builderId  The new builder's array index.\n    function registerBuilder(address wallet, uint256 shares, string calldata handle)\n        external\n        onlyRole(DEFAULT_ADMIN_ROLE)\n        returns (uint256 builderId)\n    {\n        return _registerBuilderCore(wallet, shares, handle, \"\");\n    }\n\n    /// @notice Registers a new builder with explicit expert-domain attribution.\n    /// @param wallet     Payment destination address.\n    /// @param shares     Relative weight (e.g., 100 = 1 standard share).\n    /// @param handle     GitHub handle or display name for the dashboard.\n    /// @param component  Expert domain / code-space (e.g., \"Solidity-DeFi-Core\").\n    /// @return builderId  The new builder's array index.\n    function registerBuilder(\n        address wallet,\n        uint256 shares,\n        string calldata handle,\n        string calldata component\n    )\n        external\n        onlyRole(DEFAULT_ADMIN_ROLE)\n        returns (uint256 builderId)\n    {\n        return _registerBuilderCore(wallet, shares, handle, component);\n    }\n\n    /// @dev Core registration logic shared by both `registerBuilder` overloads.\n    function _registerBuilderCore(\n        address wallet,\n        uint256 shares,\n        string memory handle,\n        string memory component\n    )\n        internal\n        returns (uint256 builderId)\n    {\n        require(wallet != address(0), \"NexusBuilderFund: zero wallet\");\n        require(shares > 0, \"NexusBuilderFund: zero shares\");\n        require(builderIndex[wallet] == 0, \"NexusBuilderFund: already registered\");\n\n        builderId = builders.length;\n        builders.push(Builder({\n            wallet: wallet,\n            shares: shares,\n            handle: handle,\n            component: component,\n            totalClaimed: 0,\n            active: true\n        }));\n\n        builderIndex[wallet] = builderId + 1; // +1 so 0 means \"not registered\"\n        totalShares += shares;\n\n        // New builder starts claiming from the current deposit snapshot\n        _lastClaimSnapshot[builderId] = totalDeposited;\n\n        // Track component attribution\n        if (bytes(component).length > 0) {\n            _buildersByComponent[keccak256(bytes(component))].push(builderId);\n        }\n\n        emit BuilderRegistered(builderId, wallet, handle, shares, component);\n    }\n\n    /// @notice Updates a builder's share weight or active status.\n    /// @param builderId  Index into the builders array.\n    /// @param newShares  New share weight (0 = deactivate).\n    /// @param active     True to keep active, false to remove from pool.\n    function updateBuilder(uint256 builderId, uint256 newShares, bool active)\n        external\n        onlyRole(DEFAULT_ADMIN_ROLE)\n    {\n        require(builderId < builders.length, \"NexusBuilderFund: unknown builder\");\n\n        Builder storage b = builders[builderId];\n        totalShares = totalShares - (b.active ? b.shares : 0) + (active ? newShares : 0);\n        b.shares = newShares;\n        b.active = active;\n\n        emit BuilderUpdated(builderId, newShares, active);\n    }\n\n    // \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\n    // Fee deposit (open to anyone \u2014 API gateways, bridge wallets, users)\n    // \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\n\n    /// @dev Splits an incoming ETH payment: forwards placementBps/10000 to\n    ///      placementWallet immediately, and adds the remainder to totalDeposited\n    ///      (the builder pool).\n    ///\n    ///      `totalDeposited` intentionally tracks only the builder-pool portion \u2014\n    ///      NOT the gross received amount.  This is correct: `claimReward()` uses\n    ///      `totalDeposited` to calculate entitlements, and the contract balance\n    ///      already excludes the placed portion (forwarded out immediately).\n    ///      Tracking gross here would allow builders to claim funds that no longer\n    ///      exist in the contract, causing `claimReward()` to revert.\n    ///\n    ///      Reentrancy: `_handleDeposit` is internal-only.  Every external entry\n    ///      point that calls it (`depositFees`, `receive`) is already guarded by\n    ///      `nonReentrant`.  The external call to `placementWallet` therefore runs\n    ///      inside an active ReentrancyGuard lock, making re-entry impossible.\n    function _handleDeposit(uint256 amount) internal {\n        if (placementWallet != address(0) && placementBps > 0) {\n            uint256 placed = (amount * placementBps) / 10_000;\n            if (placed > 0) {\n                // CEI: credit pool with the builder portion BEFORE external call\n                totalDeposited += (amount - placed);\n                (bool ok,) = payable(placementWallet).call{value: placed}(\"\");\n                require(ok, \"NexusBuilderFund: placement transfer failed\");\n                emit PlacementSent(placementWallet, placed);\n                return;\n            }\n        }\n        totalDeposited += amount;\n    }\n\n    /// @notice Deposits ETH into the builder fund.\n    /// @param note  Human-readable label for this deposit (e.g., \"REST API batch\",\n    ///              \"Lightning bridge settlement\", \"GitHub Sponsors top-up\").\n    function depositFees(string calldata note) external payable nonReentrant {\n        require(msg.value > 0, \"NexusBuilderFund: zero deposit\");\n        _handleDeposit(msg.value);\n        emit FeesDeposited(msg.sender, msg.value, note);\n    }\n\n    /// @notice Accepts plain ETH transfers (e.g., from the signal-bus settlement wallet).\n    receive() external payable {\n        _handleDeposit(msg.value);\n        emit FeesDeposited(msg.sender, msg.value, \"direct transfer\");\n    }\n\n    // \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\n    // Usage recording (oracle-only)\n    // \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\n\n    /// @notice Records off-chain API usage for a given endpoint.\n    ///         Called by the Chainlink Automation upkeep or the Nexus oracle relayer.\n    /// @param endpoint  keccak256 of the endpoint name (e.g., keccak256(\"/api/v1/member\")).\n    /// @param callCount Number of calls to add to the running total.\n    function recordUsage(bytes32 endpoint, uint256 callCount)\n        external\n        onlyRole(ORACLE_ROLE)\n    {\n        require(callCount > 0, \"NexusBuilderFund: zero call count\");\n        usageByEndpoint[endpoint] += callCount;\n        totalUsageCalls += callCount;\n        emit UsageRecorded(endpoint, callCount, msg.sender);\n    }\n\n    // \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\n    // Reward claiming\n    // \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\n\n    /// @notice Returns the claimable ETH (wei) for a builder based on deposits\n    ///         made since their last claim.\n    /// @param builderId  Index into the builders array.\n    /// @return claimable  ETH in wei available to claim right now.\n    function pendingReward(uint256 builderId) public view returns (uint256 claimable) {\n        require(builderId < builders.length, \"NexusBuilderFund: unknown builder\");\n        Builder storage b = builders[builderId];\n        if (!b.active || totalShares == 0) return 0;\n\n        uint256 newDeposits = totalDeposited - _lastClaimSnapshot[builderId];\n        claimable = (newDeposits * b.shares) / totalShares;\n    }\n\n    /// @notice Claims all pending ETH rewards for the calling builder.\n    ///         If an NGTT token award rate is configured and the contract holds\n    ///         enough NGTT, a proportional NGTT bonus is also transferred.\n    ///         The caller must be a registered builder's wallet.\n    function claimReward() external nonReentrant {\n        uint256 idx = builderIndex[msg.sender];\n        require(idx != 0, \"NexusBuilderFund: not a registered builder\");\n        uint256 builderId = idx - 1;\n\n        uint256 amount = pendingReward(builderId);\n        require(amount > 0, \"NexusBuilderFund: nothing to claim\");\n        require(address(this).balance >= amount, \"NexusBuilderFund: insufficient balance\");\n\n        // Update snapshot BEFORE transfer (CEI pattern)\n        _lastClaimSnapshot[builderId] = totalDeposited;\n        builders[builderId].totalClaimed += amount;\n\n        (bool success,) = payable(msg.sender).call{value: amount}(\"\");\n        require(success, \"NexusBuilderFund: ETH transfer failed\");\n\n        emit RewardClaimed(builderId, msg.sender, amount);\n\n        // NGTT token bonus \u2014 sent after ETH transfer; failure is non-blocking\n        if (address(ngttToken) != address(0) && ngttRewardPerEthWei > 0) {\n            uint256 ngttAmount = (amount * ngttRewardPerEthWei) / 1e18;\n            if (ngttAmount > 0 && ngttToken.balanceOf(address(this)) >= ngttAmount) {\n                ngttToken.safeTransfer(msg.sender, ngttAmount);\n                emit NgttAwarded(builderId, msg.sender, ngttAmount);\n            }\n        }\n    }\n\n    // \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\n    // Chainlink price-feed helpers\n    // \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\n\n    /// @notice Returns the current ETH/USD price from Chainlink (8 decimals).\n    ///         Reverts if the feed is not configured or the price is stale/negative.\n    /// @return price  ETH price in USD \u00d7 10^8 (e.g., 3_000_00000000 = $3000).\n    function getEthUsdPrice() public view returns (uint256 price) {\n        require(address(ethUsdFeed) != address(0), \"NexusBuilderFund: ETH/USD feed not set\");\n        (, int256 answer,, uint256 updatedAt,) = ethUsdFeed.latestRoundData();\n        require(answer > 0, \"NexusBuilderFund: invalid ETH/USD price\");\n        require(block.timestamp - updatedAt <= 3600, \"NexusBuilderFund: ETH/USD price stale (>1h)\");\n        price = uint256(answer);\n    }\n\n    /// @notice Returns the current BTC/USD price from Chainlink (8 decimals).\n    /// @return price  BTC price in USD \u00d7 10^8.\n    function getBtcUsdPrice() public view returns (uint256 price) {\n        require(address(btcUsdFeed) != address(0), \"NexusBuilderFund: BTC/USD feed not set\");\n        (, int256 answer,, uint256 updatedAt,) = btcUsdFeed.latestRoundData();\n        require(answer > 0, \"NexusBuilderFund: invalid BTC/USD price\");\n        require(block.timestamp - updatedAt <= 3600, \"NexusBuilderFund: BTC/USD price stale (>1h)\");\n        price = uint256(answer);\n    }\n\n    /// @notice Converts the per-call USD-cent fee to wei at the current ETH/USD price.\n    /// @dev    Formula: wei = (feeUsdCents \u00d7 1e18) / (ethUsdPrice \u00d7 100)\n    ///         where ethUsdPrice has 8 decimals (i.e., divide by 10^8 first).\n    ///\n    ///         Example: fee = 1 USD-cent, ETH = $3 000\n    ///           wei = (1 \u00d7 1e18) / (3_000_00000000 \u00d7 100 / 1e8)\n    ///               = 1e18 / 300_000\n    ///               \u2248 3 333 333 333 wei  \u2248 0.0000033 ETH  \u2248 $0.01 \u2713\n    /// @return weiAmount  ETH (wei) equivalent of the current per-call fee.\n    function getFeeWei() public view returns (uint256 weiAmount) {\n        if (feePerCallUsdCents == 0) return 0;\n        uint256 ethPrice8 = getEthUsdPrice(); // USD per ETH \u00d7 10^8\n        // wei = (cents * 1e18) / (price_in_cents_per_ether)\n        // price in cents per ether = ethPrice8 * 100 / 1e8 = ethPrice8 / 1e6\n        weiAmount = (feePerCallUsdCents * 1e18 * 1e6) / (ethPrice8 * 100);\n    }\n\n    /// @notice Converts the per-call USD-cent fee to satoshis at the current BTC/USD price.\n    /// @dev    1 BTC = 100 000 000 satoshis.\n    ///         Formula: satoshis = (feeUsdCents \u00d7 1e8) / (btcUsdPrice \u00d7 100 / 1e8)\n    ///                           = (feeUsdCents \u00d7 1e16) / btcUsdPrice\n    ///\n    ///         Example: fee = 1 USD-cent, BTC = $60 000\n    ///           satoshis = (1 \u00d7 1e16) / 6_000_000_000_000\n    ///                    = 1e16 / 6e12 \u2248 1 666 satoshis \u2248 $0.01 \u2713\n    /// @return satoshis  BTC satoshi equivalent of the current per-call fee.\n    function getFeeSatoshis() public view returns (uint256 satoshis) {\n        if (feePerCallUsdCents == 0) return 0;\n        uint256 btcPrice8 = getBtcUsdPrice(); // USD per BTC \u00d7 10^8\n        // satoshis = (cents / price_per_satoshi_in_cents)\n        // price_per_satoshi_in_cents = btcPrice8 / (1e8 * 1e2) = btcPrice8 / 1e10\n        satoshis = (feePerCallUsdCents * 1e10) / btcPrice8;\n    }\n\n    // \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\n    // View helpers\n    // \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\n\n    /// @notice Returns the total number of registered builders (including inactive).\n    function builderCount() external view returns (uint256) {\n        return builders.length;\n    }\n\n    /// @notice Returns the builder IDs attributed to a given component/expert domain.\n    /// @param component  The component string (e.g., \"Solidity-DeFi-Core\").\n    /// @return ids  Array of builderIds that were registered with this component.\n    function buildersByComponent(string calldata component) external view returns (uint256[] memory ids) {\n        return _buildersByComponent[keccak256(bytes(component))];\n    }\n\n    /// @notice Returns complete info for a builder.\n    /// @param builderId  Index into the builders array.\n    function getBuilder(uint256 builderId) external view returns (Builder memory) {\n        require(builderId < builders.length, \"NexusBuilderFund: unknown builder\");\n        return builders[builderId];\n    }\n\n    /// @notice Returns the current ETH balance held in the fund.\n    function fundBalance() external view returns (uint256) {\n        return address(this).balance;\n    }\n\n    /// @notice Returns usage count for an endpoint given its string name.\n    /// @param endpointName  Plain-text endpoint name (e.g., \"/api/v1/member\").\n    function usageForEndpoint(string calldata endpointName) external view returns (uint256) {\n        return usageByEndpoint[keccak256(abi.encodePacked(endpointName))];\n    }\n\n    // \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\n    // Admin configuration\n    // \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\n\n    /// @notice Updates the Chainlink ETH/USD price feed address.\n    /// @param newFeed  New feed address (address(0) to disable).\n    function setEthUsdFeed(address newFeed) external onlyRole(DEFAULT_ADMIN_ROLE) {\n        ethUsdFeed = IAggregatorV3(newFeed);\n        emit PriceFeedUpdated(\"ETH/USD\", newFeed);\n    }\n\n    /// @notice Updates the Chainlink BTC/USD price feed address.\n    /// @param newFeed  New feed address (address(0) to disable).\n    function setBtcUsdFeed(address newFeed) external onlyRole(DEFAULT_ADMIN_ROLE) {\n        btcUsdFeed = IAggregatorV3(newFeed);\n        emit PriceFeedUpdated(\"BTC/USD\", newFeed);\n    }\n\n    /// @notice Updates the per-call fee in USD cents.\n    ///         Set to 0 to make the API free (fees deposited externally only).\n    /// @param newFeeUsdCents  New fee in USD cents (1 = $0.01 per API call).\n    function setFeePerCall(uint256 newFeeUsdCents) external onlyRole(DEFAULT_ADMIN_ROLE) {\n        feePerCallUsdCents = newFeeUsdCents;\n        emit FeePerCallUpdated(newFeeUsdCents);\n    }\n\n    /// @notice Configures the placement wallet and basis points.\n    ///         On each deposit, `bps / 10000` of the ETH is immediately forwarded\n    ///         to `wallet`, with the remainder staying in the builder pool.\n    /// @param wallet  Destination address (address(0) = disable auto-forward).\n    /// @param bps     Basis points to forward (0\u20135000; 5000 = 50%).\n    function setPlacementConfig(address wallet, uint256 bps) external onlyRole(DEFAULT_ADMIN_ROLE) {\n        require(bps <= 5000, \"NexusBuilderFund: placementBps > 50%\");\n        placementWallet = wallet;\n        placementBps = bps;\n        emit PlacementConfigUpdated(wallet, bps);\n    }\n\n    /// @notice Configures the NGTT token bonus awarded to builders on ETH claim.\n    /// @param token            NGTT token contract address (address(0) = disable).\n    /// @param rewardPerEthWei  NGTT tokens (18 dec) awarded per 1 ETH (1e18 wei) claimed.\n    ///                         E.g., 1000e18 = 1 000 NGTT per ETH.\n    function setNgttRewardConfig(address token, uint256 rewardPerEthWei)\n        external\n        onlyRole(DEFAULT_ADMIN_ROLE)\n    {\n        ngttToken = IERC20(token);\n        ngttRewardPerEthWei = rewardPerEthWei;\n        emit NgttRewardConfigUpdated(token, rewardPerEthWei);\n    }\n\n    // \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\n    // Extended view helpers\n    // \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\n\n    /// @notice Returns the NGTT token balance currently held by this contract\n    ///         (available for builder awards).\n    function ngttBalance() external view returns (uint256) {\n        if (address(ngttToken) == address(0)) return 0;\n        return ngttToken.balanceOf(address(this));\n    }\n\n    /// @notice Returns placement and NGTT reward configuration in one call.\n    function rewardConfig()\n        external\n        view\n        returns (\n            address _placementWallet,\n            uint256 _placementBps,\n            address _ngttToken,\n            uint256 _ngttRewardPerEthWei,\n            uint256 _ngttContractBalance\n        )\n    {\n        _placementWallet      = placementWallet;\n        _placementBps         = placementBps;\n        _ngttToken            = address(ngttToken);\n        _ngttRewardPerEthWei  = ngttRewardPerEthWei;\n        _ngttContractBalance  = (address(ngttToken) != address(0))\n            ? ngttToken.balanceOf(address(this))\n            : 0;\n    }\n}\n"
  },
  {
    "id": "nexus-lp-staking",
    "name": "NexusLPStaking",
    "fileName": "NexusLPStaking.sol",
    "category": "DeFi",
    "address": "0x1f9840a85d5aF5bf1D1762F925BDADdC4201F984",
    "description": "Synthetix-style LP token staking rewards contract. Continuous per-second reward accumulation funded via refillRewardPool.",
    "roles": [
      "Owner (refill, setRewardRate)",
      "Stakers"
    ],
    "features": [
      "Continuous rewards",
      "Exit-all in single tx",
      "Instant claim"
    ],
    "methods": [
      {
        "name": "deposit",
        "type": "write",
        "inputs": [
          {
            "name": "amount",
            "type": "uint256"
          }
        ],
        "description": "Stakes LP tokens to earn NGTT rewards."
      },
      {
        "name": "withdraw",
        "type": "write",
        "inputs": [
          {
            "name": "amount",
            "type": "uint256"
          }
        ],
        "description": "Withdraws staked LP tokens."
      },
      {
        "name": "claimRewards",
        "type": "write",
        "inputs": [],
        "description": "Claims accumulated NGTT staking rewards."
      },
      {
        "name": "exitAll",
        "type": "write",
        "inputs": [],
        "description": "Withdraws all LP tokens and claims all rewards in one tx."
      },
      {
        "name": "earned",
        "type": "read",
        "inputs": [
          {
            "name": "account",
            "type": "address"
          }
        ],
        "outputs": [
          {
            "name": "reward",
            "type": "uint256"
          }
        ],
        "description": "Calculates pending rewards for an account."
      }
    ],
    "sourceCode": "// SPDX-License-Identifier: MIT\npragma solidity ^0.8.20;\n\nimport \"@openzeppelin/contracts/access/Ownable.sol\";\nimport \"@openzeppelin/contracts/security/ReentrancyGuard.sol\";\nimport \"@openzeppelin/contracts/token/ERC20/utils/SafeERC20.sol\";\nimport \"@openzeppelin/contracts/token/ERC20/IERC20.sol\";\n\n/// @title NexusLPStaking\n/// @notice Liquidity-provider staking contract.  Users deposit LP tokens and\n///         earn NGTT rewards proportional to their share and time staked.\n///\n/// Reward mechanics (per-second accumulator pattern):\n///   - Owner sets a `rewardRate` (NGTT per second distributed across all stakers).\n///   - On every deposit/withdraw/harvest the global `rewardPerTokenStored`\n///     accumulator is updated.\n///   - Each user's earned balance is tracked via their `rewardPerTokenPaid`\n///     snapshot and a `pendingRewards` cache.\n///\n/// NES: this contract is a Nexus-authored surface governed by the\n/// Nexus Encryption Standard as documented in docs/NEXUS_ENCRYPTION_STANDARD.md.\ncontract NexusLPStaking is Ownable, ReentrancyGuard {\n    using SafeERC20 for IERC20;\n\n    // -------------------------------------------------------------------------\n    // Tokens\n    // -------------------------------------------------------------------------\n\n    /// @notice The LP token that users deposit.\n    IERC20 public immutable stakingToken;\n\n    /// @notice The NGTT reward token that users earn.\n    IERC20 public immutable rewardToken;\n\n    // -------------------------------------------------------------------------\n    // Reward state\n    // -------------------------------------------------------------------------\n\n    /// @notice NGTT reward tokens distributed per second across all stakers.\n    uint256 public rewardRate;\n\n    /// @notice Timestamp of the last reward accumulator update.\n    uint256 public lastUpdateTime;\n\n    /// @notice Accumulated reward per staked LP token (scaled by 1e18).\n    uint256 public rewardPerTokenStored;\n\n    // -------------------------------------------------------------------------\n    // User state\n    // -------------------------------------------------------------------------\n\n    struct UserInfo {\n        uint256 amount;              // LP tokens deposited\n        uint256 rewardPerTokenPaid;  // rewardPerTokenStored snapshot at last settlement\n        uint256 pendingRewards;      // Accrued but not yet claimed rewards\n    }\n\n    mapping(address => UserInfo) public userInfo;\n\n    /// @notice Total LP tokens deposited across all users.\n    uint256 public totalStaked;\n\n    // -------------------------------------------------------------------------\n    // Events\n    // -------------------------------------------------------------------------\n\n    /// @notice Emitted when a user deposits LP tokens.\n    event Deposited(address indexed user, uint256 amount);\n\n    /// @notice Emitted when a user withdraws LP tokens.\n    event Withdrawn(address indexed user, uint256 amount);\n\n    /// @notice Emitted when a user claims NGTT rewards.\n    event RewardClaimed(address indexed user, uint256 reward);\n\n    /// @notice Emitted when the owner updates the reward rate.\n    event RewardRateUpdated(uint256 oldRate, uint256 newRate);\n\n    /// @notice Emitted when the owner refills the reward pool.\n    event RewardPoolRefilled(uint256 amount);\n\n    // -------------------------------------------------------------------------\n    // Constructor\n    // -------------------------------------------------------------------------\n\n    /// @notice Deploys the staking contract.\n    /// @param _stakingToken Address of the LP token users deposit.\n    /// @param _rewardToken  Address of the NGTT reward token.\n    constructor(address _stakingToken, address _rewardToken) {\n        require(_stakingToken != address(0), \"NexusLPStaking: zero staking token\");\n        require(_rewardToken != address(0), \"NexusLPStaking: zero reward token\");\n        stakingToken = IERC20(_stakingToken);\n        rewardToken = IERC20(_rewardToken);\n        lastUpdateTime = block.timestamp;\n    }\n\n    // -------------------------------------------------------------------------\n    // Modifiers\n    // -------------------------------------------------------------------------\n\n    modifier updateReward(address account) {\n        rewardPerTokenStored = rewardPerToken();\n        lastUpdateTime = block.timestamp;\n        if (account != address(0)) {\n            UserInfo storage user = userInfo[account];\n            user.pendingRewards = earned(account);\n            user.rewardPerTokenPaid = rewardPerTokenStored;\n        }\n        _;\n    }\n\n    // -------------------------------------------------------------------------\n    // Core functions\n    // -------------------------------------------------------------------------\n\n    /// @notice Returns the current accumulated reward per staked LP token.\n    /// @return Reward per token (scaled by 1e18).\n    function rewardPerToken() public view returns (uint256) {\n        if (totalStaked == 0) {\n            return rewardPerTokenStored;\n        }\n        return rewardPerTokenStored + (\n            (block.timestamp - lastUpdateTime) * rewardRate * 1e18 / totalStaked\n        );\n    }\n\n    /// @notice Returns the total earned (but unclaimed) NGTT for an account.\n    /// @param account The user address.\n    /// @return Total earned NGTT (in 18-decimal units).\n    function earned(address account) public view returns (uint256) {\n        UserInfo storage user = userInfo[account];\n        return (user.amount * (rewardPerToken() - user.rewardPerTokenPaid)) / 1e18 + user.pendingRewards;\n    }\n\n    /// @notice Deposits LP tokens into the staking contract.\n    /// @param amount Number of LP tokens to stake (caller must approve first).\n    function deposit(uint256 amount) external nonReentrant updateReward(msg.sender) {\n        require(amount > 0, \"NexusLPStaking: zero amount\");\n        userInfo[msg.sender].amount += amount;\n        totalStaked += amount;\n        stakingToken.safeTransferFrom(msg.sender, address(this), amount);\n        emit Deposited(msg.sender, amount);\n    }\n\n    /// @notice Withdraws LP tokens from the staking contract.\n    /// @param amount Number of LP tokens to withdraw.\n    function withdraw(uint256 amount) external nonReentrant updateReward(msg.sender) {\n        require(amount > 0, \"NexusLPStaking: zero amount\");\n        require(userInfo[msg.sender].amount >= amount, \"NexusLPStaking: insufficient balance\");\n        userInfo[msg.sender].amount -= amount;\n        totalStaked -= amount;\n        stakingToken.safeTransfer(msg.sender, amount);\n        emit Withdrawn(msg.sender, amount);\n    }\n\n    /// @notice Claims all accumulated NGTT rewards.\n    function claimRewards() external nonReentrant updateReward(msg.sender) {\n        uint256 reward = userInfo[msg.sender].pendingRewards;\n        require(reward > 0, \"NexusLPStaking: no rewards\");\n        userInfo[msg.sender].pendingRewards = 0;\n        rewardToken.safeTransfer(msg.sender, reward);\n        emit RewardClaimed(msg.sender, reward);\n    }\n\n    /// @notice Withdraws all LP tokens and claims all pending rewards in one call.\n    function exitAll() external nonReentrant updateReward(msg.sender) {\n        uint256 amount = userInfo[msg.sender].amount;\n        uint256 reward = userInfo[msg.sender].pendingRewards;\n\n        userInfo[msg.sender].amount = 0;\n        userInfo[msg.sender].pendingRewards = 0;\n        totalStaked -= amount;\n\n        if (amount > 0) {\n            stakingToken.safeTransfer(msg.sender, amount);\n            emit Withdrawn(msg.sender, amount);\n        }\n        if (reward > 0) {\n            rewardToken.safeTransfer(msg.sender, reward);\n            emit RewardClaimed(msg.sender, reward);\n        }\n    }\n\n    // -------------------------------------------------------------------------\n    // Owner controls\n    // -------------------------------------------------------------------------\n\n    /// @notice Sets the NGTT reward distribution rate.\n    /// @param _rewardRate New rate in NGTT per second (18 decimals).\n    function setRewardRate(uint256 _rewardRate) external onlyOwner updateReward(address(0)) {\n        uint256 old = rewardRate;\n        rewardRate = _rewardRate;\n        emit RewardRateUpdated(old, _rewardRate);\n    }\n\n    /// @notice Deposits NGTT reward tokens into this contract to fund future rewards.\n    /// @param amount Amount of NGTT to deposit (owner must approve first).\n    function refillRewardPool(uint256 amount) external onlyOwner {\n        require(amount > 0, \"NexusLPStaking: zero amount\");\n        rewardToken.safeTransferFrom(msg.sender, address(this), amount);\n        emit RewardPoolRefilled(amount);\n    }\n}\n"
  },
  {
    "id": "nexus-fractal-vault",
    "name": "NexusFractalVault",
    "fileName": "NexusFractalVault.sol",
    "category": "DeFi",
    "address": "0x6B175474E89094C44Da98b954EedeAC495271d0F",
    "description": "ERC-4626 auto-compounding vault with configurable reinvestment basis points (maxReinvestBps).",
    "roles": [
      "Owner",
      "Vault Depositors"
    ],
    "features": [
      "ERC-4626 compliant",
      "Automated reinvestment",
      "Share-to-asset conversion"
    ],
    "methods": [
      {
        "name": "deposit",
        "type": "write",
        "inputs": [
          {
            "name": "assets",
            "type": "uint256"
          }
        ],
        "outputs": [
          {
            "name": "shares",
            "type": "uint256"
          }
        ],
        "description": "Deposits assets and mints vault shares."
      },
      {
        "name": "redeem",
        "type": "write",
        "inputs": [
          {
            "name": "shares",
            "type": "uint256"
          }
        ],
        "outputs": [
          {
            "name": "assets",
            "type": "uint256"
          }
        ],
        "description": "Burns vault shares and withdraws underlying assets."
      },
      {
        "name": "totalAssets",
        "type": "read",
        "inputs": [],
        "outputs": [
          {
            "name": "total",
            "type": "uint256"
          }
        ],
        "description": "Returns total underlying assets held in vault."
      }
    ],
    "sourceCode": "// SPDX-License-Identifier: MIT\npragma solidity ^0.8.20;\n\nimport \"@openzeppelin/contracts/token/ERC20/extensions/ERC20Permit.sol\";\nimport \"@openzeppelin/contracts/token/ERC20/utils/SafeERC20.sol\";\nimport \"@openzeppelin/contracts/token/ERC20/IERC20.sol\";\nimport \"@openzeppelin/contracts/access/Ownable.sol\";\nimport \"@openzeppelin/contracts/security/ReentrancyGuard.sol\";\n\n/// @title NexusFractalVault\n/// @notice ERC-4626-inspired compounding vault that recursively reinvests yield\n///         back into the underlying strategy at every harvest cycle.\n///\n/// Fractal compounding model:\n///   - Depositors receive fNGTT shares at the current net-asset-value (NAV).\n///   - The owner (DAO) calls harvestAndReinvest() periodically to credit newly\n///     earned yield back into totalAssets, increasing the share price.\n///   - Because the reinvested amount itself earns future yield, growth is\n///     compound (not linear) \u2014 approaching fractal compounding as the harvest\n///     interval shrinks toward zero.\n///   - Kelly-criterion-informed position: the vault never reinvests more than\n///     MAX_REINVEST_BPS (10 000 bps = 100%) of a single harvest, allowing the\n///     DAO to cap risk per cycle.\n///\n/// NES: this contract is a Nexus-authored surface governed by the\n/// Nexus Encryption Standard as documented in docs/NEXUS_ENCRYPTION_STANDARD.md.\ncontract NexusFractalVault is ERC20Permit, Ownable, ReentrancyGuard {\n    using SafeERC20 for IERC20;\n\n    // -------------------------------------------------------------------------\n    // Immutables\n    // -------------------------------------------------------------------------\n\n    /// @notice The underlying yield-bearing asset (NGTT).\n    IERC20 public immutable asset;\n\n    // -------------------------------------------------------------------------\n    // State\n    // -------------------------------------------------------------------------\n\n    /// @notice Total NGTT deposited by all users (base principal).\n    uint256 public totalPrincipal;\n\n    /// @notice Cumulative yield reinvested into the vault (compounds over time).\n    uint256 public totalReinvested;\n\n    /// @notice Number of completed harvest cycles.\n    uint256 public harvestCount;\n\n    /// @notice Maximum reinvestment fraction per harvest cycle, in basis points.\n    ///         10 000 bps = 100 % (reinvest all harvested yield). Updatable by owner.\n    uint256 public maxReinvestBps = 10_000;\n\n    // -------------------------------------------------------------------------\n    // Events\n    // -------------------------------------------------------------------------\n\n    /// @notice Emitted when a user deposits NGTT.\n    event Deposited(address indexed user, uint256 assets, uint256 shares);\n\n    /// @notice Emitted when a user redeems fNGTT shares.\n    event Redeemed(address indexed user, uint256 shares, uint256 assets);\n\n    /// @notice Emitted each harvest cycle.\n    event HarvestReinvested(\n        uint256 indexed cycle,\n        uint256 yieldAmount,\n        uint256 reinvestedAmount,\n        uint256 newTotalAssets\n    );\n\n    /// @notice Emitted when the max reinvestment fraction is updated.\n    event MaxReinvestBpsUpdated(uint256 newBps);\n\n    // -------------------------------------------------------------------------\n    // Constructor\n    // -------------------------------------------------------------------------\n\n    /// @notice Deploys the fractal vault.\n    /// @param _asset Address of the NGTT token.\n    constructor(address _asset)\n        ERC20(\"Nexus Fractal Vault Share\", \"fNGTT\")\n        ERC20Permit(\"Nexus Fractal Vault Share\")\n    {\n        require(_asset != address(0), \"NexusFractalVault: zero asset\");\n        asset = IERC20(_asset);\n    }\n\n    // -------------------------------------------------------------------------\n    // Vault accounting\n    // -------------------------------------------------------------------------\n\n    /// @notice Total NGTT managed by the vault (principal + all reinvested yield).\n    /// @return Total assets in NGTT.\n    function totalAssets() public view returns (uint256) {\n        return totalPrincipal + totalReinvested;\n    }\n\n    /// @notice Converts shares to the underlying NGTT amount at current NAV.\n    /// @param shares Number of fNGTT shares.\n    /// @return assets Equivalent NGTT.\n    function convertToAssets(uint256 shares) public view returns (uint256 assets) {\n        uint256 supply = totalSupply();\n        if (supply == 0) return shares;\n        return (shares * totalAssets()) / supply;\n    }\n\n    /// @notice Converts NGTT amount to shares at current NAV.\n    /// @param assets NGTT amount.\n    /// @return shares Equivalent fNGTT shares.\n    function convertToShares(uint256 assets) public view returns (uint256 shares) {\n        uint256 supply = totalSupply();\n        uint256 total = totalAssets();\n        if (supply == 0 || total == 0) return assets;\n        return (assets * supply) / total;\n    }\n\n    // -------------------------------------------------------------------------\n    // Deposit / redeem\n    // -------------------------------------------------------------------------\n\n    /// @notice Deposits NGTT and mints fNGTT shares at current NAV.\n    /// @param assets Amount of NGTT to deposit (caller must approve first).\n    /// @return shares Vault shares minted.\n    function deposit(uint256 assets) external nonReentrant returns (uint256 shares) {\n        require(assets > 0, \"NexusFractalVault: zero assets\");\n        shares = convertToShares(assets);\n        require(shares > 0, \"NexusFractalVault: zero shares computed\");\n\n        totalPrincipal += assets;\n        asset.safeTransferFrom(msg.sender, address(this), assets);\n        _mint(msg.sender, shares);\n\n        emit Deposited(msg.sender, assets, shares);\n    }\n\n    /// @notice Redeems fNGTT shares for proportional NGTT (principal + compound yield).\n    /// @param shares fNGTT shares to burn.\n    /// @return assets NGTT returned.\n    function redeem(uint256 shares) external nonReentrant returns (uint256 assets) {\n        require(shares > 0, \"NexusFractalVault: zero shares\");\n        require(balanceOf(msg.sender) >= shares, \"NexusFractalVault: insufficient shares\");\n\n        assets = convertToAssets(shares);\n        require(assets > 0, \"NexusFractalVault: zero assets computed\");\n\n        // Reduce principal and reinvested proportionally.\n        uint256 supply = totalSupply();\n        uint256 principalPortion = (totalPrincipal * shares) / supply;\n        uint256 reinvestedPortion = assets - principalPortion;\n\n        if (principalPortion > totalPrincipal) principalPortion = totalPrincipal;\n        if (reinvestedPortion > totalReinvested) reinvestedPortion = totalReinvested;\n\n        totalPrincipal -= principalPortion;\n        if (reinvestedPortion > 0) totalReinvested -= reinvestedPortion;\n\n        _burn(msg.sender, shares);\n        asset.safeTransfer(msg.sender, assets);\n\n        emit Redeemed(msg.sender, shares, assets);\n    }\n\n    // -------------------------------------------------------------------------\n    // Harvest and reinvest (DAO-only)\n    // -------------------------------------------------------------------------\n\n    /// @notice Credits a yield harvest and immediately reinvests it into the vault.\n    ///         The DAO transfers the harvested NGTT to this contract, then calls\n    ///         this function.  The reinvested amount increases totalAssets, making\n    ///         each share worth more on the next NAV calculation.\n    ///\n    /// @param yieldAmount Total yield harvested in this cycle (NGTT, 18 decimals).\n    /// @param reinvestBps  Fraction of yieldAmount to reinvest in basis points.\n    ///                     Must be \u2264 maxReinvestBps.  The remainder stays in the vault\n    ///                     as a fee buffer (redeemable by the DAO via governance).\n    function harvestAndReinvest(uint256 yieldAmount, uint256 reinvestBps)\n        external\n        onlyOwner\n        nonReentrant\n    {\n        require(yieldAmount > 0, \"NexusFractalVault: zero yield\");\n        require(reinvestBps <= maxReinvestBps, \"NexusFractalVault: reinvestBps too high\");\n\n        // Verify the tokens were actually transferred to this contract.\n        uint256 balance = asset.balanceOf(address(this));\n        require(\n            balance >= totalAssets() + yieldAmount,\n            \"NexusFractalVault: yield tokens not received\"\n        );\n\n        uint256 toReinvest = (yieldAmount * reinvestBps) / 10_000;\n        totalReinvested += toReinvest;\n        // Any remaining yield (yieldAmount - toReinvest) stays in the contract\n        // balance as a DAO fee buffer, redeemable only via governance.\n\n        harvestCount++;\n        emit HarvestReinvested(harvestCount, yieldAmount, toReinvest, totalAssets());\n    }\n\n    // -------------------------------------------------------------------------\n    // Owner configuration\n    // -------------------------------------------------------------------------\n\n    /// @notice Updates the maximum reinvestment fraction.\n    /// @param newBps New ceiling in basis points (1\u201310 000).\n    function setMaxReinvestBps(uint256 newBps) external onlyOwner {\n        require(newBps >= 1 && newBps <= 10_000, \"NexusFractalVault: bps out of range\");\n        maxReinvestBps = newBps;\n        emit MaxReinvestBpsUpdated(newBps);\n    }\n\n    // -------------------------------------------------------------------------\n    // View helpers\n    // -------------------------------------------------------------------------\n\n    /// @notice Estimates the compound growth factor after N harvest cycles\n    ///         at a fixed per-cycle yield rate r (expressed in basis points).\n    ///         Implements the standard compound formula: (1 + r)^N.\n    ///         Uses integer math with 1e18 precision.\n    /// @param ratePerCycleBps Per-cycle yield rate in basis points (e.g. 100 = 1 %).\n    /// @param cycles          Number of compounding cycles.\n    /// @return growthFactor18 Growth factor scaled by 1e18 (1e18 = 1\u00d7, 2e18 = 2\u00d7).\n    function estimateCompoundGrowth(uint256 ratePerCycleBps, uint256 cycles)\n        external\n        pure\n        returns (uint256 growthFactor18)\n    {\n        uint256 factor = 1e18; // Start at 1.0 (scaled)\n        uint256 rateScaled = 1e18 + (ratePerCycleBps * 1e14); // (1 + r) scaled\n        for (uint256 i = 0; i < cycles; i++) {\n            factor = (factor * rateScaled) / 1e18;\n        }\n        return factor;\n    }\n}\n"
  },
  {
    "id": "nexus-options-vault",
    "name": "NexusOptionsVault",
    "fileName": "NexusOptionsVault.sol",
    "category": "DeFi",
    "address": "0x0000000000004946c0e9F43F4Dee607b0eF1fA1c",
    "description": "Vault for options strategies and covered call underwriting. Credits premium income directly to share value.",
    "roles": [
      "Owner (recordPremiumIncome)",
      "Vault Depositors"
    ],
    "features": [
      "Premium yield distribution",
      "ERC-20 Permit support",
      "Yield compounding"
    ],
    "methods": [
      {
        "name": "recordPremiumIncome",
        "type": "write",
        "inputs": [
          {
            "name": "amount",
            "type": "uint256"
          }
        ],
        "description": "Credits option premium income into vault accounting."
      },
      {
        "name": "deposit",
        "type": "write",
        "inputs": [
          {
            "name": "assets",
            "type": "uint256"
          }
        ],
        "outputs": [
          {
            "name": "shares",
            "type": "uint256"
          }
        ],
        "description": "Deposits NGTT into options vault."
      },
      {
        "name": "redeem",
        "type": "write",
        "inputs": [
          {
            "name": "shares",
            "type": "uint256"
          }
        ],
        "outputs": [
          {
            "name": "assets",
            "type": "uint256"
          }
        ],
        "description": "Redeems options vault shares for assets."
      }
    ],
    "sourceCode": "// SPDX-License-Identifier: MIT\npragma solidity ^0.8.20;\n\nimport \"@openzeppelin/contracts/token/ERC20/extensions/ERC20Permit.sol\";\nimport \"@openzeppelin/contracts/token/ERC20/utils/SafeERC20.sol\";\nimport \"@openzeppelin/contracts/token/ERC20/IERC20.sol\";\nimport \"@openzeppelin/contracts/access/Ownable.sol\";\nimport \"@openzeppelin/contracts/security/ReentrancyGuard.sol\";\n\n/// @title NexusOptionsVault\n/// @notice ERC-4626-inspired vault that accumulates NGTT deposits and allows the\n///         owner (the DAO, via governance) to record premium income from off-chain\n///         covered-call sales, distributing that income proportionally to depositors.\n///\n/// Key design decisions:\n///   - Assets (NGTT) are deposited and a share token (vNGTT) is minted.\n///   - Premium income is credited via `recordPremiumIncome(amount)`, which\n///     increases the vault's `totalAssets()` so each share becomes worth more.\n///   - Depositors redeem shares for proportionally more NGTT as premiums accrue.\n///   - The vault does NOT automatically execute any on-chain options trades.\n///     The DAO executes off-chain covered-call sales and credits premiums here.\n///\n/// NES: this contract is a Nexus-authored surface governed by the\n/// Nexus Encryption Standard as documented in docs/NEXUS_ENCRYPTION_STANDARD.md.\ncontract NexusOptionsVault is ERC20Permit, Ownable, ReentrancyGuard {\n    using SafeERC20 for IERC20;\n\n    // -------------------------------------------------------------------------\n    // Immutables\n    // -------------------------------------------------------------------------\n\n    /// @notice The underlying asset deposited into the vault (NGTT).\n    IERC20 public immutable asset;\n\n    // -------------------------------------------------------------------------\n    // State\n    // -------------------------------------------------------------------------\n\n    /// @notice Total NGTT deposited by all users (excludes premium income).\n    uint256 public totalDeposited;\n\n    /// @notice Total premium income credited by the DAO.\n    uint256 public totalPremiumIncome;\n\n    // -------------------------------------------------------------------------\n    // Events\n    // -------------------------------------------------------------------------\n\n    /// @notice Emitted when a user deposits NGTT and receives vault shares.\n    event Deposited(address indexed user, uint256 assets, uint256 shares);\n\n    /// @notice Emitted when a user redeems vault shares for NGTT.\n    event Redeemed(address indexed user, uint256 shares, uint256 assets);\n\n    /// @notice Emitted when the DAO credits premium income to the vault.\n    event PremiumIncomeRecorded(uint256 amount, uint256 newTotalAssets);\n\n    // -------------------------------------------------------------------------\n    // Constructor\n    // -------------------------------------------------------------------------\n\n    /// @notice Deploys the options vault.\n    /// @param _asset Address of the NGTT token used as the underlying asset.\n    constructor(address _asset)\n        ERC20(\"Nexus Options Vault Share\", \"vNGTT\")\n        ERC20Permit(\"Nexus Options Vault Share\")\n    {\n        require(_asset != address(0), \"NexusOptionsVault: zero asset\");\n        asset = IERC20(_asset);\n    }\n\n    // -------------------------------------------------------------------------\n    // Vault accounting\n    // -------------------------------------------------------------------------\n\n    /// @notice Returns the total NGTT managed by this vault (deposits + premiums).\n    /// @return Total assets in NGTT (18 decimals).\n    function totalAssets() public view returns (uint256) {\n        return totalDeposited + totalPremiumIncome;\n    }\n\n    /// @notice Converts a share amount to the equivalent NGTT asset amount.\n    /// @param shares Number of vault shares.\n    /// @return assets Equivalent NGTT amount.\n    function convertToAssets(uint256 shares) public view returns (uint256 assets) {\n        uint256 supply = totalSupply();\n        if (supply == 0) return shares;\n        return (shares * totalAssets()) / supply;\n    }\n\n    /// @notice Converts an NGTT asset amount to the equivalent share amount.\n    /// @param assets NGTT amount.\n    /// @return shares Equivalent vault shares.\n    function convertToShares(uint256 assets) public view returns (uint256 shares) {\n        uint256 supply = totalSupply();\n        uint256 total = totalAssets();\n        if (supply == 0 || total == 0) return assets;\n        return (assets * supply) / total;\n    }\n\n    // -------------------------------------------------------------------------\n    // Deposit / redeem\n    // -------------------------------------------------------------------------\n\n    /// @notice Deposits NGTT and mints vault shares proportional to the current NAV.\n    /// @param assets Amount of NGTT to deposit (caller must approve first).\n    /// @return shares Number of vault shares minted.\n    function deposit(uint256 assets) external nonReentrant returns (uint256 shares) {\n        require(assets > 0, \"NexusOptionsVault: zero assets\");\n        shares = convertToShares(assets);\n        require(shares > 0, \"NexusOptionsVault: zero shares computed\");\n\n        totalDeposited += assets;\n        asset.safeTransferFrom(msg.sender, address(this), assets);\n        _mint(msg.sender, shares);\n\n        emit Deposited(msg.sender, assets, shares);\n    }\n\n    /// @notice Redeems vault shares and returns the proportional NGTT (plus accrued premiums).\n    /// @param shares Number of vault shares to burn.\n    /// @return assets Amount of NGTT returned.\n    function redeem(uint256 shares) external nonReentrant returns (uint256 assets) {\n        require(shares > 0, \"NexusOptionsVault: zero shares\");\n        require(balanceOf(msg.sender) >= shares, \"NexusOptionsVault: insufficient shares\");\n\n        assets = convertToAssets(shares);\n        require(assets > 0, \"NexusOptionsVault: zero assets computed\");\n\n        // Adjust accounting proportionally.\n        uint256 supply = totalSupply();\n        uint256 depositPortion = (totalDeposited * shares) / supply;\n        uint256 premiumPortion = assets - depositPortion;\n\n        if (depositPortion > totalDeposited) depositPortion = totalDeposited;\n        if (premiumPortion > totalPremiumIncome) premiumPortion = totalPremiumIncome;\n\n        totalDeposited -= depositPortion;\n        if (premiumPortion > 0) totalPremiumIncome -= premiumPortion;\n\n        _burn(msg.sender, shares);\n        asset.safeTransfer(msg.sender, assets);\n\n        emit Redeemed(msg.sender, shares, assets);\n    }\n\n    // -------------------------------------------------------------------------\n    // Premium income (DAO-only)\n    // -------------------------------------------------------------------------\n\n    /// @notice Credits premium income earned from off-chain covered-call sales.\n    ///         The DAO must transfer the NGTT (or equivalent) to this contract first,\n    ///         then call this function to update the accounting.\n    /// @param amount NGTT amount to credit as premium income.\n    function recordPremiumIncome(uint256 amount) external onlyOwner nonReentrant {\n        require(amount > 0, \"NexusOptionsVault: zero amount\");\n        // Verify the vault actually received the tokens before crediting.\n        uint256 actual = asset.balanceOf(address(this));\n        uint256 expected = totalDeposited + totalPremiumIncome + amount;\n        require(actual >= expected, \"NexusOptionsVault: tokens not received\");\n\n        totalPremiumIncome += amount;\n        emit PremiumIncomeRecorded(amount, totalAssets());\n    }\n}\n"
  },
  {
    "id": "nexus-rwa",
    "name": "NexusRWA",
    "fileName": "NexusRWA.sol",
    "category": "RWA",
    "address": "0x55d398326f99059fF775485246999027B3197955",
    "description": "ERC-721 tokenized real-world property deeds under Wyoming DAO LLC law. Stores IPFS deed CID, title hash, valuation in cents, and rental yield.",
    "roles": [
      "DEFAULT_ADMIN_ROLE",
      "APPRAISER_ROLE",
      "OPERATOR_ROLE"
    ],
    "features": [
      "Wyoming DAO LLC legal backing",
      "IPFS deed CID",
      "USD cent appraisals",
      "Rental yield streaming"
    ],
    "methods": [
      {
        "name": "getMetadata",
        "type": "read",
        "inputs": [
          {
            "name": "tokenId",
            "type": "uint256"
          }
        ],
        "outputs": [
          {
            "name": "metadata",
            "type": "tuple"
          }
        ],
        "description": "Retrieves legal deed CID, valuation, and rental yield."
      },
      {
        "name": "totalSupply",
        "type": "read",
        "inputs": [],
        "outputs": [
          {
            "name": "count",
            "type": "uint256"
          }
        ],
        "description": "Number of tokenized RWA deeds."
      }
    ],
    "sourceCode": "// SPDX-License-Identifier: MIT\npragma solidity ^0.8.20;\n\nimport \"@openzeppelin/contracts/token/ERC721/ERC721.sol\";\nimport \"@openzeppelin/contracts/access/AccessControl.sol\";\nimport \"@openzeppelin/contracts/security/ReentrancyGuard.sol\";\nimport \"@openzeppelin/contracts/utils/Counters.sol\";\n\n/// @title NexusRWA \u2014 Real-World Asset NFT\n/// @notice ERC-721 contract representing tokenized real-world property deeds\n///         and physical assets within the Nexus Protocol DAO ecosystem.\n///\n/// Each token encodes:\n///   - An IPFS/Arweave CID pointing to the full legal deed document.\n///   - A keccak256 hash of the title string for on-chain integrity checks.\n///   - A valuation in USD cents (updatable by APPRAISER_ROLE).\n///   - An active rental yield stream (set by OPERATOR_ROLE; actual payment\n///     is handled off-chain or via Superfluid streams).\n///\n/// Ownership of the NFT = beneficial ownership of the underlying LLC that\n/// holds the deed (Wyoming DAO LLC structure compatible with US property law).\n///\n/// NES: this contract is a Nexus-authored surface governed by the\n/// Nexus Encryption Standard as documented in docs/NEXUS_ENCRYPTION_STANDARD.md.\ncontract NexusRWA is ERC721, AccessControl, ReentrancyGuard {\n    using Counters for Counters.Counter;\n\n    // -------------------------------------------------------------------------\n    // Roles\n    // -------------------------------------------------------------------------\n\n    /// @notice May mint new RWA tokens (restricted to DAO or authorized minters).\n    bytes32 public constant MINTER_ROLE = keccak256(\"MINTER_ROLE\");\n\n    /// @notice May update valuations for existing tokens.\n    bytes32 public constant APPRAISER_ROLE = keccak256(\"APPRAISER_ROLE\");\n\n    /// @notice May update rental yield information.\n    bytes32 public constant OPERATOR_ROLE = keccak256(\"OPERATOR_ROLE\");\n\n    // -------------------------------------------------------------------------\n    // Token metadata\n    // -------------------------------------------------------------------------\n\n    struct AssetMetadata {\n        bytes32  titleHash;          // keccak256 of the legal title string\n        string   documentCid;        // IPFS/Arweave content identifier for deed\n        string   propertyAddress;    // Human-readable location (US or global)\n        uint256  valuationUsdCents;  // Appraised value in USD cents (0 = unset)\n        uint256  annualRentUsdCents; // Annual rental income in USD cents (0 = none)\n        bool     fractionalised;     // True if wrapped by NexusFractionalize\n        uint256  mintedAt;           // block.timestamp at mint\n    }\n\n    mapping(uint256 => AssetMetadata) private _metadata;\n    Counters.Counter private _tokenIdCounter;\n\n    // -------------------------------------------------------------------------\n    // Events\n    // -------------------------------------------------------------------------\n\n    /// @notice Emitted when a new RWA token is minted.\n    event AssetMinted(\n        uint256 indexed tokenId,\n        address indexed owner,\n        bytes32 titleHash,\n        string  documentCid,\n        string  propertyAddress\n    );\n\n    /// @notice Emitted when the on-chain valuation is updated.\n    event ValuationUpdated(uint256 indexed tokenId, uint256 newValueUsdCents);\n\n    /// @notice Emitted when the annual rent estimate is updated.\n    event RentUpdated(uint256 indexed tokenId, uint256 newAnnualRentUsdCents);\n\n    /// @notice Emitted when a token is marked as fractionalised.\n    event AssetFractionalised(uint256 indexed tokenId, address fractionContract);\n\n    // -------------------------------------------------------------------------\n    // Constructor\n    // -------------------------------------------------------------------------\n\n    /// @notice Deploys the RWA NFT contract.\n    /// @param admin The DEFAULT_ADMIN_ROLE holder (owner wallet).\n    constructor(address admin) ERC721(\"Nexus Real-World Asset\", \"NRWA\") {\n        require(admin != address(0), \"NexusRWA: zero admin\");\n        _grantRole(DEFAULT_ADMIN_ROLE, admin);\n        _grantRole(MINTER_ROLE, admin);\n        _grantRole(APPRAISER_ROLE, admin);\n        _grantRole(OPERATOR_ROLE, admin);\n    }\n\n    // -------------------------------------------------------------------------\n    // Minting\n    // -------------------------------------------------------------------------\n\n    /// @notice Mints a new RWA token to the specified owner.\n    /// @param to              Beneficial owner address.\n    /// @param titleString     Legal title string (will be hashed on-chain).\n    /// @param documentCid     IPFS/Arweave CID of the deed document.\n    /// @param propertyAddress Human-readable location string.\n    /// @param valuationUsdCents  Initial appraised value in USD cents (0 = TBD).\n    /// @return tokenId The newly minted token identifier.\n    function mintAsset(\n        address to,\n        string calldata titleString,\n        string calldata documentCid,\n        string calldata propertyAddress,\n        uint256 valuationUsdCents\n    ) external onlyRole(MINTER_ROLE) nonReentrant returns (uint256 tokenId) {\n        require(to != address(0), \"NexusRWA: zero recipient\");\n        require(bytes(documentCid).length > 0, \"NexusRWA: empty CID\");\n\n        _tokenIdCounter.increment();\n        tokenId = _tokenIdCounter.current();\n\n        bytes32 titleHash = keccak256(abi.encodePacked(titleString));\n\n        _metadata[tokenId] = AssetMetadata({\n            titleHash: titleHash,\n            documentCid: documentCid,\n            propertyAddress: propertyAddress,\n            valuationUsdCents: valuationUsdCents,\n            annualRentUsdCents: 0,\n            fractionalised: false,\n            mintedAt: block.timestamp\n        });\n\n        _safeMint(to, tokenId);\n\n        emit AssetMinted(tokenId, to, titleHash, documentCid, propertyAddress);\n    }\n\n    // -------------------------------------------------------------------------\n    // Metadata updates\n    // -------------------------------------------------------------------------\n\n    /// @notice Updates the USD valuation for a token.\n    /// @param tokenId           Token to update.\n    /// @param newValueUsdCents  New appraised value in USD cents.\n    function updateValuation(uint256 tokenId, uint256 newValueUsdCents)\n        external\n        onlyRole(APPRAISER_ROLE)\n    {\n        require(_exists(tokenId), \"NexusRWA: nonexistent token\");\n        _metadata[tokenId].valuationUsdCents = newValueUsdCents;\n        emit ValuationUpdated(tokenId, newValueUsdCents);\n    }\n\n    /// @notice Updates the annual rental yield estimate for a token.\n    /// @param tokenId                  Token to update.\n    /// @param newAnnualRentUsdCents    New annual rent in USD cents.\n    function updateRent(uint256 tokenId, uint256 newAnnualRentUsdCents)\n        external\n        onlyRole(OPERATOR_ROLE)\n    {\n        require(_exists(tokenId), \"NexusRWA: nonexistent token\");\n        _metadata[tokenId].annualRentUsdCents = newAnnualRentUsdCents;\n        emit RentUpdated(tokenId, newAnnualRentUsdCents);\n    }\n\n    /// @notice Marks a token as fractionalised and records the fraction contract.\n    /// @param tokenId          Token that has been fractionalised.\n    /// @param fractionContract Address of the NexusFractionalize contract.\n    function markFractionalised(uint256 tokenId, address fractionContract)\n        external\n        onlyRole(OPERATOR_ROLE)\n    {\n        require(_exists(tokenId), \"NexusRWA: nonexistent token\");\n        require(fractionContract != address(0), \"NexusRWA: zero fraction contract\");\n        _metadata[tokenId].fractionalised = true;\n        emit AssetFractionalised(tokenId, fractionContract);\n    }\n\n    // -------------------------------------------------------------------------\n    // View helpers\n    // -------------------------------------------------------------------------\n\n    /// @notice Returns full metadata for a token.\n    /// @param tokenId The token to query.\n    /// @return metadata The full AssetMetadata struct.\n    function getMetadata(uint256 tokenId) external view returns (AssetMetadata memory metadata) {\n        require(_exists(tokenId), \"NexusRWA: nonexistent token\");\n        return _metadata[tokenId];\n    }\n\n    /// @notice Returns the total number of RWA tokens minted.\n    /// @return count Total supply.\n    function totalSupply() external view returns (uint256 count) {\n        return _tokenIdCounter.current();\n    }\n\n    // -------------------------------------------------------------------------\n    // ERC-165 override\n    // -------------------------------------------------------------------------\n\n    /// @inheritdoc ERC721\n    function supportsInterface(bytes4 interfaceId)\n        public\n        view\n        override(ERC721, AccessControl)\n        returns (bool)\n    {\n        return super.supportsInterface(interfaceId);\n    }\n}\n"
  },
  {
    "id": "nexus-fractionalize",
    "name": "NexusFractionalize",
    "fileName": "NexusFractionalize.sol",
    "category": "RWA",
    "address": "0x8AC76a51cc950d9822D68b83fE1Ad97B32Cd580d",
    "description": "Locks an RWA NFT deed in a vault and mints fractional ERC-20 shares for collective ownership and secondary DEX trading.",
    "roles": [
      "Vault Deployer",
      "Custodian",
      "Fractional Shareholders"
    ],
    "features": [
      "Full NFT lockup",
      "18 decimal fractional ERC-20",
      "Redeem upon 100% share buyout"
    ],
    "methods": [
      {
        "name": "fractionalize",
        "type": "write",
        "inputs": [],
        "description": "Locks RWA NFT and mints fractional ERC-20 share tokens."
      },
      {
        "name": "redeem",
        "type": "write",
        "inputs": [],
        "description": "Burns all shares to reclaim the locked physical property deed NFT."
      },
      {
        "name": "ownershipBps",
        "type": "read",
        "inputs": [
          {
            "name": "account",
            "type": "address"
          }
        ],
        "outputs": [
          {
            "name": "bps",
            "type": "uint256"
          }
        ],
        "description": "Returns fractional ownership percentage in basis points."
      }
    ],
    "sourceCode": "// SPDX-License-Identifier: MIT\npragma solidity ^0.8.20;\n\nimport \"@openzeppelin/contracts/token/ERC20/ERC20.sol\";\nimport \"@openzeppelin/contracts/token/ERC721/IERC721.sol\";\nimport \"@openzeppelin/contracts/access/Ownable.sol\";\nimport \"@openzeppelin/contracts/security/ReentrancyGuard.sol\";\n\n/// @title NexusFractionalize\n/// @notice Wraps a single NexusRWA (ERC-721) token into transferable ERC-20\n///         fractional shares.  Each share represents proportional beneficial\n///         ownership of the underlying real-world asset.\n///\n/// Flow:\n///   1. The RWA NFT owner deploys this contract (or calls a factory).\n///   2. They call fractionalize(), transferring the NFT to this contract\n///      and receiving the full supply of ERC-20 shares.\n///   3. Shares can be traded freely on any ERC-20-compatible exchange.\n///   4. Any shareholder holding 100 % of shares can call redeem() to\n///      receive the underlying NFT back.\n///\n/// NES: this contract is a Nexus-authored surface governed by the\n/// Nexus Encryption Standard as documented in docs/NEXUS_ENCRYPTION_STANDARD.md.\ncontract NexusFractionalize is ERC20, Ownable, ReentrancyGuard {\n\n    // -------------------------------------------------------------------------\n    // Immutables\n    // -------------------------------------------------------------------------\n\n    /// @notice The NFT contract address.\n    IERC721 public immutable nftContract;\n\n    /// @notice The NFT token ID held in this vault.\n    uint256 public immutable nftTokenId;\n\n    // -------------------------------------------------------------------------\n    // State\n    // -------------------------------------------------------------------------\n\n    /// @notice Whether the NFT has been deposited and shares have been issued.\n    bool public fractionalised;\n\n    /// @notice Whether the vault has been redeemed (NFT returned to last holder).\n    bool public redeemed;\n\n    // -------------------------------------------------------------------------\n    // Events\n    // -------------------------------------------------------------------------\n\n    /// @notice Emitted when the NFT is deposited and shares are issued.\n    event Fractionalised(address indexed owner, uint256 shares);\n\n    /// @notice Emitted when all shares are burned and the NFT is returned.\n    event Redeemed(address indexed redeemer);\n\n    // -------------------------------------------------------------------------\n    // Constructor\n    // -------------------------------------------------------------------------\n\n    /// @notice Creates a fractionalization vault for a specific NFT.\n    /// @param _nftContract    Address of the NexusRWA contract.\n    /// @param _nftTokenId     Token ID to fractionalize.\n    /// @param _shareName      ERC-20 name for the fractional shares.\n    /// @param _shareSymbol    ERC-20 symbol for the fractional shares.\n    /// @param _totalShares    Total supply of fractional shares to mint (18 decimals).\n    constructor(\n        address _nftContract,\n        uint256 _nftTokenId,\n        string memory _shareName,\n        string memory _shareSymbol,\n        uint256 _totalShares\n    ) ERC20(_shareName, _shareSymbol) {\n        require(_nftContract != address(0), \"NexusFractionalize: zero NFT contract\");\n        require(_totalShares > 0, \"NexusFractionalize: zero total shares\");\n        nftContract = IERC721(_nftContract);\n        nftTokenId = _nftTokenId;\n        // Mint total supply to deployer; deployer then deposits the NFT.\n        _mint(msg.sender, _totalShares);\n    }\n\n    // -------------------------------------------------------------------------\n    // Core functions\n    // -------------------------------------------------------------------------\n\n    /// @notice Deposits the NFT into this vault and activates fractional shares.\n    ///         Caller must own the NFT and have approved this contract.\n    function fractionalize() external nonReentrant {\n        require(!fractionalised, \"NexusFractionalize: already fractionalised\");\n        require(!redeemed, \"NexusFractionalize: vault redeemed\");\n        require(\n            nftContract.ownerOf(nftTokenId) == msg.sender,\n            \"NexusFractionalize: caller does not own NFT\"\n        );\n\n        fractionalised = true;\n        nftContract.transferFrom(msg.sender, address(this), nftTokenId);\n\n        emit Fractionalised(msg.sender, totalSupply());\n    }\n\n    /// @notice Burns all outstanding shares and returns the underlying NFT.\n    ///         Caller must hold 100 % of the total share supply.\n    function redeem() external nonReentrant {\n        require(fractionalised, \"NexusFractionalize: not yet fractionalised\");\n        require(!redeemed, \"NexusFractionalize: already redeemed\");\n        require(\n            balanceOf(msg.sender) == totalSupply(),\n            \"NexusFractionalize: must hold 100% of shares\"\n        );\n\n        redeemed = true;\n        _burn(msg.sender, totalSupply());\n        nftContract.transferFrom(address(this), msg.sender, nftTokenId);\n\n        emit Redeemed(msg.sender);\n    }\n\n    // -------------------------------------------------------------------------\n    // View helpers\n    // -------------------------------------------------------------------------\n\n    /// @notice Returns the address that currently holds the NFT in custody.\n    /// @return custodian This contract's address if fractionalised, address(0) if redeemed.\n    function custodian() external view returns (address) {\n        if (fractionalised && !redeemed) {\n            return address(this);\n        }\n        return address(0);\n    }\n\n    /// @notice Returns the ownership percentage held by an account in basis points.\n    /// @param account The address to query.\n    /// @return bps Ownership percentage in basis points (10 000 = 100 %).\n    function ownershipBps(address account) external view returns (uint256 bps) {\n        uint256 supply = totalSupply();\n        if (supply == 0) return 0;\n        return (balanceOf(account) * 10_000) / supply;\n    }\n}\n"
  },
  {
    "id": "nexus-game-theory-token",
    "name": "NexusGameTheoryToken",
    "fileName": "NexusGameTheoryToken.sol",
    "category": "Token",
    "address": null,
    "description": "Base game theory token with multi-age gaming reward boosts, MCP groups, and profit pools.",
    "roles": [
      "Owner",
      "Players",
      "MCP Members"
    ],
    "features": [
      "7 Age Categories",
      "Boost Multipliers",
      "Profit Redistribution"
    ],
    "methods": [
      {
        "name": "completeGame",
        "type": "write",
        "inputs": [
          {
            "name": "_player",
            "type": "address"
          },
          {
            "name": "_baseReward",
            "type": "uint256"
          },
          {
            "name": "_ageGroupId",
            "type": "uint256"
          }
        ],
        "description": "Mints game completion rewards."
      },
      {
        "name": "activateBoost",
        "type": "write",
        "inputs": [
          {
            "name": "_user",
            "type": "address"
          },
          {
            "name": "_multiplier",
            "type": "uint256"
          }
        ],
        "description": "Activates 100x to 500x skill multiplier."
      }
    ],
    "sourceCode": "// SPDX-License-Identifier: MIT\npragma solidity ^0.8.20;\n\nimport \"@openzeppelin/contracts/token/ERC721/ERC721.sol\";\nimport \"@openzeppelin/contracts/token/ERC20/ERC20.sol\";\nimport \"@openzeppelin/contracts/access/Ownable.sol\";\nimport \"@openzeppelin/contracts/security/ReentrancyGuard.sol\";\nimport \"@openzeppelin/contracts/utils/Counters.sol\";\n\n/// @title Nexus Game Theory Token\n/// @notice Nexus-authored protocol token surface tracked under the Nexus Encryption Standard (NES).\n/// @dev NES is the repository designation for Nexus-owned security, signing, and protected-message\n/// conventions documented in docs/NEXUS_ENCRYPTION_STANDARD.md. Third-party imports retain their\n/// original licensing and ownership terms.\ncontract NexusGameTheoryToken is ERC20, Ownable, ReentrancyGuard {\n    using Counters for Counters.Counter;\n    \n    uint256 public constant INITIAL_SUPPLY = 1_000_000_000 * 10**18;\n    uint256 public constant BTC_BACKING_RATIO = 100;\n    uint256 public profitPool;\n    uint256 public totalDistributed;\n    \n    struct MCPGroup {\n        string name;\n        address[] members;\n        uint256 totalTokens;\n        uint256 gamesPlayed;\n        uint256 profitShare;\n        bool active;\n    }\n    \n    mapping(uint256 => MCPGroup) public mcpGroups;\n    mapping(address => uint256) public userToGroup;\n    mapping(address => uint256) public userProfits;\n    Counters.Counter private groupIdCounter;\n    \n    mapping(address => uint256) public gamesCompleted;\n    mapping(address => uint256) public skillLevel;\n    mapping(address => uint256) public lastPlayTimestamp;\n    \n    event MCPGroupCreated(uint256 indexed groupId, string name);\n    event GameCompleted(address indexed player, uint256 reward, uint256 skillIncrease);\n    event ProfitDistributed(address indexed recipient, uint256 amount);\n    event BTCValueUpdated(uint256 newBtcValue);\n    event BoostActivated(address indexed user, uint256 multiplier);\n    \n    constructor() ERC20(\"Nexus Game Theory Token\", \"NGTT\") {\n        _mint(msg.sender, INITIAL_SUPPLY);\n    }\n    \n    function createMCPGroup(string memory _name, address[] memory _members) external onlyOwner returns (uint256) {\n        require(_members.length > 0, \"Members list cannot be empty\");\n        for (uint256 i = 0; i < _members.length; i++) {\n            require(_members[i] != address(0), \"Member address cannot be zero\");\n        }\n\n        groupIdCounter.increment();\n        uint256 newGroupId = groupIdCounter.current();\n        \n        MCPGroup storage newGroup = mcpGroups[newGroupId];\n        newGroup.name = _name;\n        newGroup.members = _members;\n        newGroup.active = true;\n        \n        for (uint256 i = 0; i < _members.length; i++) {\n            userToGroup[_members[i]] = newGroupId;\n        }\n        \n        emit MCPGroupCreated(newGroupId, _name);\n        return newGroupId;\n    }\n    \n    function completeGame(address _player, uint256 _baseReward, uint256 _ageGroupId) external onlyOwner nonReentrant {\n        require(_player != address(0), \"Player address cannot be zero\");\n        require(_baseReward > 0, \"Reward must be positive\");\n        \n        uint256 skillMultiplier = 100 + (skillLevel[_player] / 10);\n        uint256 reward = (_baseReward * skillMultiplier) / 100;\n        \n        if (_ageGroupId <= 2) {\n            reward = (reward * 120) / 100;\n        }\n        \n        gamesCompleted[_player]++;\n        skillLevel[_player] += 10;\n        lastPlayTimestamp[_player] = block.timestamp;\n        \n        uint256 groupId = userToGroup[_player];\n        if (groupId > 0) {\n            mcpGroups[groupId].gamesPlayed++;\n            mcpGroups[groupId].totalTokens += reward;\n        }\n        \n        _mint(_player, reward);\n        emit GameCompleted(_player, reward, 10);\n    }\n    \n    function distributeProfits() external onlyOwner nonReentrant {\n        require(profitPool > 0, \"No profits to distribute\");\n        \n        uint256 totalActivity = 0;\n        for (uint256 i = 1; i <= groupIdCounter.current(); i++) {\n            if (mcpGroups[i].active) {\n                totalActivity += mcpGroups[i].gamesPlayed;\n            }\n        }\n        \n        require(totalActivity > 0, \"No activity recorded\");\n        \n        for (uint256 i = 1; i <= groupIdCounter.current(); i++) {\n            if (mcpGroups[i].active && mcpGroups[i].gamesPlayed > 0) {\n                uint256 groupShare = (profitPool * mcpGroups[i].gamesPlayed) / totalActivity;\n                mcpGroups[i].profitShare += groupShare;\n                \n                uint256 perMember = groupShare / mcpGroups[i].members.length;\n                for (uint256 j = 0; j < mcpGroups[i].members.length; j++) {\n                    address member = mcpGroups[i].members[j];\n                    userProfits[member] += perMember;\n                    emit ProfitDistributed(member, perMember);\n                }\n            }\n        }\n        \n        totalDistributed += profitPool;\n        profitPool = 0;\n    }\n    \n    function claimProfits() external nonReentrant {\n        uint256 amount = userProfits[msg.sender];\n        require(amount > 0, \"No profits to claim\");\n        \n        userProfits[msg.sender] = 0;\n        _mint(msg.sender, amount);\n        \n        emit ProfitDistributed(msg.sender, amount);\n    }\n    \n    function addProfitPool(uint256 _amount) external onlyOwner {\n        profitPool += _amount;\n    }\n    \n    function activateBoost(address _user, uint256 _multiplier) external onlyOwner {\n        require(_user != address(0), \"User address cannot be zero\");\n        require(_multiplier >= 100 && _multiplier <= 500, \"Invalid multiplier\");\n        skillLevel[_user] += (_multiplier - 100);\n        emit BoostActivated(_user, _multiplier);\n    }\n    \n    function getUserStats(address _user) external view returns (uint256 games, uint256 skill, uint256 profits, uint256 groupId) {\n        return (gamesCompleted[_user], skillLevel[_user], userProfits[_user], userToGroup[_user]);\n    }\n    \n    function getGroupStats(uint256 _groupId) external view returns (string memory name, uint256 memberCount, uint256 totalTokens, uint256 gamesPlayed, uint256 profitShare) {\n        MCPGroup memory group = mcpGroups[_groupId];\n        return (group.name, group.members.length, group.totalTokens, group.gamesPlayed, group.profitShare);\n    }\n}\n"
  }
];
