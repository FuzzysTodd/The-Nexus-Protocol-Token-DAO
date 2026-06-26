// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

/**
 * ------------------------------------------------------------
 * NEXUS FEE MARKET
 * ------------------------------------------------------------
 * This contract receives usage events from:
 *  - Azure Functions
 *  - Bots
 *  - Workflows
 *  - AI Agents
 *  - Telemetry
 *  - ALSN Automation
 *
 * Each usage event includes:
 *  - usageEventId
 *  - usageType
 *  - usageUnits
 *  - nexusWorkflowId
 *  - nexusServiceType
 *
 * The fee market converts usageUnits → serviceToken fees.
 * Fees are split between:
 *  - Validators
 *  - Nexus Treasury
 *  - (Optional) Developer Fund
 *
 * This is the economic engine of the Nexus chain.
 * ------------------------------------------------------------
 */

interface IERC20 {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function transfer(address to, uint256 amount) external returns (bool);
}

contract NexusFeeMarket {
    // ------------------------------------------------------------
    // EVENTS
    // ------------------------------------------------------------
    event UsageEventBilled(
        bytes32 indexed usageEventId,
        string usageType,
        uint256 usageUnits,
        uint256 feeAmount,
        address indexed payer
    );

    event FeeDistributed(
        uint256 validatorAmount,
        uint256 treasuryAmount,
        uint256 developerAmount
    );

    // ------------------------------------------------------------
    // STATE
    // ------------------------------------------------------------
    IERC20 public serviceToken;

    address public nexusTreasury;
    address public validatorPool;
    address public developerFund;

    uint256 public pricePerUnit = 1e15; // 0.001 token per unit (adjustable)

    uint256 public treasuryShare = 50;   // 50%
    uint256 public validatorShare = 40;  // 40%
    uint256 public developerShare = 10;  // 10%

    // ------------------------------------------------------------
    // MODIFIERS
    // ------------------------------------------------------------
    modifier onlyAuthorized() {
        // Azure Functions, bots, and automation gateways call this
        require(msg.sender == tx.origin, "No contracts allowed");
        _;
    }

    // ------------------------------------------------------------
    // CONSTRUCTOR
    // ------------------------------------------------------------
    constructor(
        address _serviceToken,
        address _nexusTreasury,
        address _validatorPool,
        address _developerFund
    ) {
        serviceToken = IERC20(_serviceToken);
        nexusTreasury = _nexusTreasury;
        validatorPool = _validatorPool;
        developerFund = _developerFund;
    }

    // ------------------------------------------------------------
    // BILLING FUNCTION
    // ------------------------------------------------------------
    function billUsageEvent(
        bytes32 usageEventId,
        string memory usageType,
        uint256 usageUnits
    ) external onlyAuthorized {
        uint256 feeAmount = usageUnits * pricePerUnit;

        // Pull tokens from payer
        require(
            serviceToken.transferFrom(msg.sender, address(this), feeAmount),
            "Fee transfer failed"
        );

        // Split fees
        uint256 treasuryAmount = (feeAmount * treasuryShare) / 100;
        uint256 validatorAmount = (feeAmount * validatorShare) / 100;
        uint256 developerAmount = (feeAmount * developerShare) / 100;

        // Distribute
        serviceToken.transfer(nexusTreasury, treasuryAmount);
        serviceToken.transfer(validatorPool, validatorAmount);
        serviceToken.transfer(developerFund, developerAmount);

        emit UsageEventBilled(
            usageEventId,
            usageType,
            usageUnits,
            feeAmount,
            msg.sender
        );

        emit FeeDistributed(
            validatorAmount,
            treasuryAmount,
            developerAmount
        );
    }

    // ------------------------------------------------------------
    // ADMIN FUNCTIONS
    // ------------------------------------------------------------
    function setPricePerUnit(uint256 newPrice) external {
        require(msg.sender == nexusTreasury, "Only treasury");
        pricePerUnit = newPrice;
    }

    function setShares(uint256 t, uint256 v, uint256 d) external {
        require(msg.sender == nexusTreasury, "Only treasury");
        require(t + v + d == 100, "Invalid split");
        treasuryShare = t;
        validatorShare = v;
        developerShare = d;
    }
}
