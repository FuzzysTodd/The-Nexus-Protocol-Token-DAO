// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

interface IERC20DF {
    function transfer(address to, uint256 amount) external returns (bool);
}

contract DeveloperFund {
    event GrantApproved(address indexed dev, uint256 amount, string memo);

    IERC20DF public serviceToken;
    address public owner;

    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner");
        _;
    }

    constructor(address _serviceToken) {
        serviceToken = IERC20DF(_serviceToken);
        owner = msg.sender;
    }

    function payGrant(address dev, uint256 amount, string calldata memo) external onlyOwner {
        require(serviceToken.transfer(dev, amount), "Grant transfer failed");
        emit GrantApproved(dev, amount, memo);
    }
}
