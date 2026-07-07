// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

contract GovernanceFailsafe {
    bool public emergencyMode;
    address public council;

    constructor(address _council) {
        council = _council;
    }

    modifier notEmergency() {
        require(!emergencyMode, "DAO in emergency mode");
        _;
    }

    function declareEmergency() external {
        require(msg.sender == council, "Not authorized");
        emergencyMode = true;
    }

    function revokeEmergency() external {
        require(msg.sender == council, "Not authorized");
        emergencyMode = false;
    }
}

