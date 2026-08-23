// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

interface IGovernanceFailsafe {
    function emergencyMode() external view returns (bool);
}

contract ContractRegistry {
    IGovernanceFailsafe public failsafe;
    address public admin;

    mapping(bytes32 => address) public contracts; // e.g. keccak256("TREASURY"), keccak256("GOVERNANCE")

    event ContractRegistered(bytes32 indexed key, address indexed contractAddress);

    modifier onlyAdmin() {
        require(msg.sender == admin, "Not admin");
        _;
    }

    modifier notEmergency() {
        require(!failsafe.emergencyMode(), "DAO in emergency mode");
        _;
    }

    constructor(address _failsafe, address _admin) {
        failsafe = IGovernanceFailsafe(_failsafe);
        admin = _admin;
    }

    function registerContract(bytes32 key, address contractAddress) external onlyAdmin {
        contracts[key] = contractAddress;
        emit ContractRegistered(key, contractAddress);
    }

    function getContract(bytes32 key) external view returns (address) {
        return contracts[key];
    }

    // Example: a function that should not run in emergency
    function unsafeOperation(bytes32 key) external notEmergency {
        address target = contracts[key];
        require(target != address(0), "Unknown contract");
        // call into target here
    }
}
