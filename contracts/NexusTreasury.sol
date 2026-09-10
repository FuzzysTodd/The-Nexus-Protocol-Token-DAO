// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

/**
 * ------------------------------------------------------------
 * NEXUS TREASURY CONTRACT
 * ------------------------------------------------------------
 * Responsibilities:
 *  - Hold serviceToken balances
 *  - Pay Azure compute reimbursements
 *  - Pay validator rewards
 *  - Pay developer grants
 *  - Pay automation rebates
 *  - Track spending categories
 *  - Provide transparent on-chain accounting
 *
 * This contract works with:
 *  - NexusFeeMarket.sol (fee collection)
 *  - ValidatorPool.sol (validator payouts)
 *  - DeveloperFund.sol (dev grants)
 *  - NexusAutomation (Azure Functions)
 * ------------------------------------------------------------
 */

interface IERC20 {
    function transfer(address to, uint256 amount) external returns (bool);
}

contract NexusTreasury {
    // ------------------------------------------------------------
    // EVENTS
    // ------------------------------------------------------------
    event TreasuryFunded(address indexed from, uint256 amount);
    event AzurePaid(address indexed to, uint256 amount, string memo);
    event ValidatorPaid(address indexed pool, uint256 amount);
    event DeveloperGrantPaid(address indexed dev, uint256 amount, string memo);
    event AutomationRebatePaid(address indexed to, uint256 amount, string workflowId);

    // ------------------------------------------------------------
    // STATE
    // ------------------------------------------------------------
    IERC20 public serviceToken;

    address public owner;
    address public validatorPool;
    address public developerFund;

    // Spending categories
    uint256 public totalAzurePaid;
    uint256 public totalValidatorPaid;
    uint256 public totalDeveloperPaid;
    uint256 public totalAutomationRebates;

    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner");
        _;
    }

    // ------------------------------------------------------------
    // CONSTRUCTOR
    // ------------------------------------------------------------
    constructor(
        address _serviceToken,
        address _validatorPool,
        address _developerFund
    ) {
        serviceToken = IERC20(_serviceToken);
        validatorPool = _validatorPool;
        developerFund = _developerFund;
        owner = msg.sender;
    }

    // ------------------------------------------------------------
    // FUNDING (called by FeeMarket)
    // ------------------------------------------------------------
    function fundTreasury(uint256 amount) external {
        emit TreasuryFunded(msg.sender, amount);
    }

    // ------------------------------------------------------------
    // PAY AZURE (compute, storage, AI, networking)
    // ------------------------------------------------------------
    function payAzure(address payable azureWallet, uint256 amount, string calldata memo)
        external
        onlyOwner
    {
        require(serviceToken.transfer(azureWallet, amount), "Azure payment failed");
        totalAzurePaid += amount;

        emit AzurePaid(azureWallet, amount, memo);
    }

    // ------------------------------------------------------------
    // PAY VALIDATORS (reward distribution)
    // ------------------------------------------------------------
    function payValidators(uint256 amount) external onlyOwner {
        require(serviceToken.transfer(validatorPool, amount), "Validator payment failed");
        totalValidatorPaid += amount;

        emit ValidatorPaid(validatorPool, amount);
    }

    // ------------------------------------------------------------
    // PAY DEVELOPER GRANTS
    // ------------------------------------------------------------
    function payDeveloperGrant(address dev, uint256 amount, string calldata memo)
        external
        onlyOwner
    {
        require(serviceToken.transfer(dev, amount), "Developer grant failed");
        totalDeveloperPaid += amount;

        emit DeveloperGrantPaid(dev, amount, memo);
    }

    // ------------------------------------------------------------
    // PAY AUTOMATION REBATES (optional)
    // ------------------------------------------------------------
    function payAutomationRebate(address to, uint256 amount, string calldata workflowId)
        external
        onlyOwner
    {
        require(serviceToken.transfer(to, amount), "Rebate failed");
        totalAutomationRebates += amount;

        emit AutomationRebatePaid(to, amount, workflowId);
    }

    // ------------------------------------------------------------
    // VIEW FUNCTIONS
    // ------------------------------------------------------------
    function getTreasuryBalance() external view returns (uint256) {
        return serviceTokenBalance();
    }

    function serviceTokenBalance() public view returns (uint256) {
        return serviceTokenBalanceOf(address(this));
    }

    function serviceTokenBalanceOf(address account) public view returns (uint256) {
        return IERC20(serviceToken).balanceOf(account);
    }
}
