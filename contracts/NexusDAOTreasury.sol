// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

import "@openzeppelin/contracts/access/AccessControl.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/token/ERC20/utils/SafeERC20.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

/// @title NexusDAOTreasury
/// @notice DAO-controlled treasury that holds ETH and ERC-20 tokens.
/// @dev All fund-movement functions are restricted to EXECUTOR_ROLE, which is
///      assigned exclusively to the NexusDAOTimelock after deployment.  No
///      funds can therefore leave the treasury without a successful on-chain
///      governance vote followed by the mandatory timelock delay.
///
///      NES: this contract is a Nexus-authored surface governed by the
///      Nexus Encryption Standard as documented in docs/NEXUS_ENCRYPTION_STANDARD.md.
///
/// Access model:
///   - DEFAULT_ADMIN_ROLE  : deployment-time admin (owner wallet); manages role grants.
///   - EXECUTOR_ROLE       : granted to NexusDAOTimelock; the only role that may
///                           transfer ETH or ERC-20 tokens out of the treasury.
///   - GUARDIAN_ROLE       : granted to Owner and/or Super Delegates; may pause
///                           treasury operations in an emergency.
///
/// Deployment:
///   1. Deploy NexusDAOTreasury(admin = owner wallet).
///   2. After the Timelock is deployed, call
///        treasury.grantRole(EXECUTOR_ROLE, timelockAddress)
///   3. Optionally grant GUARDIAN_ROLE to the owner and each Super Delegate.
contract NexusDAOTreasury is AccessControl, ReentrancyGuard {
    using SafeERC20 for IERC20;

    // -------------------------------------------------------------------------
    // Roles
    // -------------------------------------------------------------------------

    /// @notice Role required to transfer ETH or tokens out of the treasury.
    ///         Assigned exclusively to NexusDAOTimelock.
    bytes32 public constant EXECUTOR_ROLE = keccak256("EXECUTOR_ROLE");

    /// @notice Role that can pause and unpause treasury operations.
    ///         Assigned to Owner and Super Delegates for emergency response.
    bytes32 public constant GUARDIAN_ROLE = keccak256("GUARDIAN_ROLE");

    // -------------------------------------------------------------------------
    // State
    // -------------------------------------------------------------------------

    /// @notice Whether treasury transfers are currently paused.
    bool public paused;

    // -------------------------------------------------------------------------
    // Events
    // -------------------------------------------------------------------------

    /// @notice Emitted when ETH is deposited into the treasury.
    event ETHDeposited(address indexed sender, uint256 amount);

    /// @notice Emitted when ETH is transferred out of the treasury by governance.
    event ETHTransferred(address indexed recipient, uint256 amount, string reason);

    /// @notice Emitted when an ERC-20 token is deposited into the treasury.
    event ERC20Deposited(address indexed token, address indexed sender, uint256 amount);

    /// @notice Emitted when an ERC-20 token is transferred out of the treasury.
    event ERC20Transferred(address indexed token, address indexed recipient, uint256 amount, string reason);

    /// @notice Emitted when the treasury is paused by a guardian.
    event TreasuryPaused(address indexed guardian);

    /// @notice Emitted when the treasury is unpaused by a guardian.
    event TreasuryUnpaused(address indexed guardian);

    // -------------------------------------------------------------------------
    // Modifiers
    // -------------------------------------------------------------------------

    /// @dev Reverts if the treasury is currently paused.
    modifier whenNotPaused() {
        require(!paused, "NexusDAOTreasury: paused");
        _;
    }

    // -------------------------------------------------------------------------
    // Constructor
    // -------------------------------------------------------------------------

    /// @notice Deploys the treasury and grants the deployer DEFAULT_ADMIN_ROLE.
    /// @param admin Address that holds DEFAULT_ADMIN_ROLE.  This should be the
    ///        owner wallet (`0x33ffc308e693a5b49e0ee0241f41f03ccef495f2`).
    constructor(address admin) {
        require(admin != address(0), "NexusDAOTreasury: zero admin");
        _grantRole(DEFAULT_ADMIN_ROLE, admin);
        _grantRole(GUARDIAN_ROLE, admin);
    }

    // -------------------------------------------------------------------------
    // Receive / deposit
    // -------------------------------------------------------------------------

    /// @notice Accepts ETH deposits directly.
    receive() external payable {
        emit ETHDeposited(msg.sender, msg.value);
    }

    /// @notice Accepts ETH via an explicit call (same as receive).
    fallback() external payable {
        emit ETHDeposited(msg.sender, msg.value);
    }

    /// @notice Convenience function to deposit ERC-20 tokens into the treasury.
    /// @param token  The ERC-20 token address.
    /// @param amount Amount to deposit (caller must have approved this contract first).
    function depositERC20(address token, uint256 amount) external nonReentrant {
        require(token != address(0), "NexusDAOTreasury: zero token address");
        require(amount > 0, "NexusDAOTreasury: zero amount");
        IERC20(token).safeTransferFrom(msg.sender, address(this), amount);
        emit ERC20Deposited(token, msg.sender, amount);
    }

    // -------------------------------------------------------------------------
    // ETH transfers (governance-only)
    // -------------------------------------------------------------------------

    /// @notice Transfers ETH to the specified recipient.
    ///         Can only be called by the NexusDAOTimelock (EXECUTOR_ROLE).
    /// @param recipient Destination address.
    /// @param amount    Amount of ETH in wei.
    /// @param reason    Human-readable description for audit logging.
    function transferETH(address payable recipient, uint256 amount, string calldata reason)
        external
        nonReentrant
        whenNotPaused
        onlyRole(EXECUTOR_ROLE)
    {
        require(recipient != address(0), "NexusDAOTreasury: zero recipient");
        require(amount > 0, "NexusDAOTreasury: zero amount");
        require(address(this).balance >= amount, "NexusDAOTreasury: insufficient ETH");

        (bool success,) = recipient.call{value: amount}("");
        require(success, "NexusDAOTreasury: ETH transfer failed");

        emit ETHTransferred(recipient, amount, reason);
    }

    // -------------------------------------------------------------------------
    // ERC-20 transfers (governance-only)
    // -------------------------------------------------------------------------

    /// @notice Transfers ERC-20 tokens to the specified recipient.
    ///         Can only be called by the NexusDAOTimelock (EXECUTOR_ROLE).
    /// @param token     The ERC-20 token address.
    /// @param recipient Destination address.
    /// @param amount    Token amount (in token's native decimals).
    /// @param reason    Human-readable description for audit logging.
    function transferERC20(
        address token,
        address recipient,
        uint256 amount,
        string calldata reason
    ) external nonReentrant whenNotPaused onlyRole(EXECUTOR_ROLE) {
        require(token != address(0), "NexusDAOTreasury: zero token address");
        require(recipient != address(0), "NexusDAOTreasury: zero recipient");
        require(amount > 0, "NexusDAOTreasury: zero amount");

        IERC20(token).safeTransfer(recipient, amount);
        emit ERC20Transferred(token, recipient, amount, reason);
    }

    // -------------------------------------------------------------------------
    // Emergency controls (guardian)
    // -------------------------------------------------------------------------

    /// @notice Pauses all outgoing transfers.  Called by a guardian in an emergency.
    function pause() external onlyRole(GUARDIAN_ROLE) {
        require(!paused, "NexusDAOTreasury: already paused");
        paused = true;
        emit TreasuryPaused(msg.sender);
    }

    /// @notice Unpauses the treasury after an emergency is resolved.
    function unpause() external onlyRole(GUARDIAN_ROLE) {
        require(paused, "NexusDAOTreasury: not paused");
        paused = false;
        emit TreasuryUnpaused(msg.sender);
    }

    // -------------------------------------------------------------------------
    // View helpers
    // -------------------------------------------------------------------------

    /// @notice Returns the current ETH balance held by the treasury.
    /// @return ETH balance in wei.
    function ethBalance() external view returns (uint256) {
        return address(this).balance;
    }

    /// @notice Returns the current balance of an ERC-20 token held by the treasury.
    /// @param token The ERC-20 token address.
    /// @return Token balance in the token's native decimals.
    function tokenBalance(address token) external view returns (uint256) {
        return IERC20(token).balanceOf(address(this));
    }
}
