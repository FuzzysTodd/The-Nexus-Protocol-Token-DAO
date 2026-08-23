// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

interface IERC20 {
    function transfer(address to, uint256 amount) external returns (bool);
}

contract ValidatorPool {
    event Staked(address indexed validator, uint256 amount);
    event Unstaked(address indexed validator, uint256 amount);
    event RewardDistributed(uint256 totalReward);

    IERC20 public serviceToken;
    address public owner;

    mapping(address => uint256) public stakeOf;
    uint256 public totalStake;

    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner");
        _;
    }

    constructor(address _serviceToken) {
        serviceToken = IERC20(_serviceToken);
        owner = msg.sender;
    }

    function stake(uint256 amount) external {
        require(amount > 0, "Zero stake");
        require(serviceToken.transferFrom(msg.sender, address(this), amount), "Stake transfer failed");

        stakeOf[msg.sender] += amount;
        totalStake += amount;

        emit Staked(msg.sender, amount);
    }

    function unstake(uint256 amount) external {
        require(stakeOf[msg.sender] >= amount, "Insufficient stake");

        stakeOf[msg.sender] -= amount;
        totalStake -= amount;

        require(serviceToken.transfer(msg.sender, amount), "Unstake transfer failed");

        emit Unstaked(msg.sender, amount);
    }

    function distributeReward(uint256 amount) external onlyOwner {
        require(totalStake > 0, "No stake");
        require(serviceToken.transferFrom(msg.sender, address(this), amount), "Reward funding failed");

        // Simple proportional distribution (off-chain calculation recommended for real use)
        emit RewardDistributed(amount);
    }
}
