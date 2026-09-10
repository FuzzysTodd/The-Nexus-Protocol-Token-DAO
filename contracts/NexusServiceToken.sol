// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

/**
 * ------------------------------------------------------------
 * NEXUS SERVICE TOKEN
 * ------------------------------------------------------------
 * Purpose:
 *  - Unit of account for:
 *      * Automation fees
 *      * AI calls
 *      * Workflow runs
 *      * Telemetry ingestion
 *      * Dashboard reads
 *  - Used by:
 *      * NexusFeeMarket
 *      * NexusTreasury
 *      * ValidatorPool
 *
 * This is NOT a meme token.
 * It is an infrastructure/service token.
 * ------------------------------------------------------------
 */

contract NexusServiceToken {
    // ------------------------------------------------------------
    // EVENTS
    // ------------------------------------------------------------
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);
    event MinterAdded(address indexed account);
    event MinterRemoved(address indexed account);

    // ------------------------------------------------------------
    // STATE
    // ------------------------------------------------------------
    string public name = "Nexus Service Token";
    string public symbol = "NST";
    uint8 public decimals = 18;

    uint256 public totalSupply;

    mapping(address => uint256) public balanceOf;
    mapping(address => mapping(address => uint256)) public allowance;
    mapping(address => bool) public isMinter;

    address public owner;

    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner");
        _;
    }

    modifier onlyMinter() {
        require(isMinter[msg.sender], "Only minter");
        _;
    }

    // ------------------------------------------------------------
    // CONSTRUCTOR
    // ------------------------------------------------------------
    constructor() {
        owner = msg.sender;
        isMinter[msg.sender] = true;
        emit MinterAdded(msg.sender);
    }

    // ------------------------------------------------------------
    // ERC-20 CORE
    // ------------------------------------------------------------
    function _transfer(address from, address to, uint256 value) internal {
        require(to != address(0), "Zero address");
        require(balanceOf[from] >= value, "Insufficient balance");

        unchecked {
            balanceOf[from] -= value;
            balanceOf[to] += value;
        }

        emit Transfer(from, to, value);
    }

    function transfer(address to, uint256 value) external returns (bool) {
        _transfer(msg.sender, to, value);
        return true;
    }

    function approve(address spender, uint256 value) external returns (bool) {
        allowance[msg.sender][spender] = value;
        emit Approval(msg.sender, spender, value);
        return true;
    }

    function transferFrom(address from, address to, uint256 value) external returns (bool) {
        require(allowance[from][msg.sender] >= value, "Allowance exceeded");

        unchecked {
            allowance[from][msg.sender] -= value;
        }

        _transfer(from, to, value);
        return true;
    }

    // ------------------------------------------------------------
    // MINTING (FOR TREASURY / BOOTSTRAP / REWARDS)
    // ------------------------------------------------------------
    function mint(address to, uint256 amount) external onlyMinter {
        require(to != address(0), "Zero address");

        totalSupply += amount;
        balanceOf[to] += amount;

        emit Transfer(address(0), to, amount);
    }

    // ------------------------------------------------------------
    // MINTER MANAGEMENT
    // ------------------------------------------------------------
    function addMinter(address account) external onlyOwner {
        isMinter[account] = true;
        emit MinterAdded(account);
    }

    function removeMinter(address account) external onlyOwner {
        isMinter[account] = false;
        emit MinterRemoved(account);
    }
}
