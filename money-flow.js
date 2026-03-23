/**
 * Nexus Protocol Money Flow Calculator
 * Advanced revenue analysis and ROI calculations
 */

// Revenue stream configurations with realistic APY ranges
const REVENUE_STREAMS = {
    dividends: {
        name: "Dividend Distributions",
        minAPY: 0.05,
        maxAPY: 0.20,
        risk: "low",
        passive: true
    },
    gameToEarn: {
        name: "Game-to-Earn Rewards",
        minAPY: 0.50,
        maxAPY: 3.00,
        risk: "low",
        passive: false
    },
    nftStaking: {
        name: "NFT Staking",
        minAPY: 0.15,
        maxAPY: 0.40,
        risk: "low",
        passive: true
    },
    liquidityProvision: {
        name: "Liquidity Provision",
        minAPY: 0.30,
        maxAPY: 1.20,
        risk: "medium",
        passive: false
    },
    reflectionFees: {
        name: "Reflection Fees",
        minAPY: 0.08,
        maxAPY: 0.15,
        risk: "low",
        passive: true
    },
    buybackBurn: {
        name: "Buyback & Burn",
        minAPY: 0.10,
        maxAPY: 0.25,
        risk: "low",
        passive: true
    },
    mcpGroups: {
        name: "MCP Group Profits",
        minAPY: 0.20,
        maxAPY: 1.00,
        risk: "low",
        passive: false
    },
    arbitrage: {
        name: "Arbitrage Trading",
        minAPY: 1.00,
        maxAPY: 5.00,
        risk: "high",
        passive: false
    },
    governance: {
        name: "Governance Rewards",
        minAPY: 0.05,
        maxAPY: 0.15,
        risk: "low",
        passive: true
    },
    lending: {
        name: "Lending & Borrowing",
        minAPY: 0.08,
        maxAPY: 0.35,
        risk: "medium",
        passive: true
    }
};

// Strategy configurations
const STRATEGIES = {
    conservative: {
        name: "Conservative",
        allocation: {
            dividends: 0.30,
            reflectionFees: 0.25,
            nftStaking: 0.20,
            buybackBurn: 0.15,
            governance: 0.10
        },
        multiplier: 0.7 // More conservative estimates
    },
    balanced: {
        name: "Balanced",
        allocation: {
            dividends: 0.20,
            gameToEarn: 0.15,
            nftStaking: 0.15,
            liquidityProvision: 0.15,
            reflectionFees: 0.15,
            mcpGroups: 0.10,
            governance: 0.10
        },
        multiplier: 1.0 // Standard estimates
    },
    aggressive: {
        name: "Aggressive",
        allocation: {
            liquidityProvision: 0.25,
            arbitrage: 0.20,
            gameToEarn: 0.20,
            mcpGroups: 0.15,
            lending: 0.10,
            reflectionFees: 0.10
        },
        multiplier: 1.3 // Higher risk, higher reward
    },
    expert: {
        name: "Expert",
        allocation: {
            arbitrage: 0.25,
            liquidityProvision: 0.20,
            gameToEarn: 0.15,
            lending: 0.15,
            mcpGroups: 0.10,
            nftStaking: 0.10,
            governance: 0.05
        },
        multiplier: 1.5 // Maximum potential with expert execution
    }
};

// Timeframe multipliers
const TIMEFRAMES = {
    daily: { days: 1, label: "Daily" },
    weekly: { days: 7, label: "Weekly" },
    monthly: { days: 30, label: "Monthly" },
    yearly: { days: 365, label: "Yearly" }
};

/**
 * Calculate returns based on investment, strategy, and timeframe
 */
function calculateReturns() {
    const investment = parseFloat(document.getElementById('investment').value) || 0;
    const timeframe = document.getElementById('timeframe').value;
    const strategyType = document.getElementById('strategy').value;

    if (investment <= 0) {
        alert('Please enter a valid investment amount');
        return;
    }

    const strategy = STRATEGIES[strategyType];
    const timeConfig = TIMEFRAMES[timeframe];
    
    let totalReturn = 0;
    let passiveReturn = 0;
    
    // Calculate returns from each allocated stream
    for (const [streamKey, allocation] of Object.entries(strategy.allocation)) {
        const stream = REVENUE_STREAMS[streamKey];
        if (!stream) continue;

        // Use average APY, adjusted by strategy multiplier
        const avgAPY = (stream.minAPY + stream.maxAPY) / 2;
        const adjustedAPY = avgAPY * strategy.multiplier;
        
        // Calculate return for this stream
        const streamInvestment = investment * allocation;
        const yearlyReturn = streamInvestment * adjustedAPY;
        const periodReturn = (yearlyReturn / 365) * timeConfig.days;
        
        totalReturn += periodReturn;
        
        if (stream.passive) {
            passiveReturn += periodReturn;
        }
    }

    // Calculate metrics
    const roi = (totalReturn / investment) * 100;
    const annualizedReturn = (totalReturn / timeConfig.days) * 365;
    const apy = (annualizedReturn / investment) * 100;

    // Display results
    document.getElementById('results').style.display = 'grid';
    document.getElementById('total-return').textContent = formatCurrency(totalReturn);
    document.getElementById('roi').textContent = roi.toFixed(2) + '%';
    document.getElementById('apy').textContent = apy.toFixed(2) + '%';
    document.getElementById('passive').textContent = formatCurrency(passiveReturn);

    // Add success animation
    const resultsEl = document.getElementById('results');
    resultsEl.style.animation = 'none';
    setTimeout(() => {
        resultsEl.style.animation = 'fadeIn 0.5s ease-in';
    }, 10);
}

/**
 * Format number as currency
 */
function formatCurrency(amount) {
    if (amount >= 1000000) {
        return '$' + (amount / 1000000).toFixed(2) + 'M';
    } else if (amount >= 1000) {
        return '$' + (amount / 1000).toFixed(2) + 'K';
    } else {
        return '$' + amount.toFixed(2);
    }
}

/**
 * Calculate potential monthly income at different investment levels
 */
function calculateIncomeBreakdown(investment) {
    const results = {};
    
    for (const [strategyKey, strategy] of Object.entries(STRATEGIES)) {
        let monthlyIncome = 0;
        
        for (const [streamKey, allocation] of Object.entries(strategy.allocation)) {
            const stream = REVENUE_STREAMS[streamKey];
            if (!stream) continue;
            
            const avgAPY = (stream.minAPY + stream.maxAPY) / 2;
            const adjustedAPY = avgAPY * strategy.multiplier;
            const streamInvestment = investment * allocation;
            const yearlyReturn = streamInvestment * adjustedAPY;
            const monthlyReturn = yearlyReturn / 12;
            
            monthlyIncome += monthlyReturn;
        }
        
        results[strategyKey] = {
            monthly: monthlyIncome,
            yearly: monthlyIncome * 12,
            strategy: strategy.name
        };
    }
    
    return results;
}

/**
 * Calculate time to reach financial goals
 */
function calculateTimeToGoal(currentInvestment, monthlyContribution, targetIncome, strategy) {
    const strategyConfig = STRATEGIES[strategy];
    let months = 0;
    let investment = currentInvestment;
    const maxMonths = 120; // 10 years max
    
    while (months < maxMonths) {
        // Calculate monthly return
        let monthlyReturn = 0;
        
        for (const [streamKey, allocation] of Object.entries(strategyConfig.allocation)) {
            const stream = REVENUE_STREAMS[streamKey];
            if (!stream) continue;
            
            const avgAPY = (stream.minAPY + stream.maxAPY) / 2;
            const adjustedAPY = avgAPY * strategyConfig.multiplier;
            const streamInvestment = investment * allocation;
            const yearlyReturn = streamInvestment * adjustedAPY;
            monthlyReturn += yearlyReturn / 12;
        }
        
        // Check if we've reached the target
        if (monthlyReturn >= targetIncome) {
            return { months, investment, monthlyIncome: monthlyReturn };
        }
        
        // Add monthly contribution and returns
        investment += monthlyContribution + monthlyReturn;
        months++;
    }
    
    return { months: maxMonths, investment, monthlyIncome: 0, reachedGoal: false };
}

/**
 * Generate expert recommendations based on investment size
 */
function getExpertRecommendations(investment) {
    const recommendations = [];
    
    if (investment < 1000) {
        recommendations.push({
            title: "Start with Game-to-Earn",
            description: "Focus on playing games to accumulate NGTT tokens with zero additional investment. Aim for 100+ skill points for maximum multipliers.",
            priority: "high"
        });
        recommendations.push({
            title: "Compound Everything",
            description: "Reinvest 100% of earnings for the first 6 months to build your position faster.",
            priority: "high"
        });
    } else if (investment < 10000) {
        recommendations.push({
            title: "Balanced Passive Strategy",
            description: "Split between dividends (40%), reflections (30%), and NFT staking (30%) for steady passive income.",
            priority: "high"
        });
        recommendations.push({
            title: "Join MCP Groups",
            description: "Participate in profit pool distributions to boost your returns by 20-50%.",
            priority: "medium"
        });
    } else if (investment < 50000) {
        recommendations.push({
            title: "Add Liquidity Provision",
            description: "Allocate 25% to Uniswap V3 concentrated liquidity for 50-100% APY on that portion.",
            priority: "high"
        });
        recommendations.push({
            title: "Diversify Across Streams",
            description: "Use the Balanced or Aggressive strategy to maximize returns across 7+ revenue streams.",
            priority: "high"
        });
        recommendations.push({
            title: "Consider Governance",
            description: "Your holdings qualify you for Super Delegate status - apply for 3x governance rewards.",
            priority: "medium"
        });
    } else {
        recommendations.push({
            title: "Expert Strategy Stack",
            description: "Implement the Ultimate Hybrid Stack: Hold 40% for passive, 20% liquidity, 20% NFTs, 10% gaming, 10% arbitrage.",
            priority: "high"
        });
        recommendations.push({
            title: "Leverage Lending Protocols",
            description: "Use Aave to leverage your position 2-3x. Earn on collateral + borrowed funds for amplified returns.",
            priority: "high"
        });
        recommendations.push({
            title: "Automate Arbitrage",
            description: "Your capital qualifies for automated flash loan arbitrage. Expected 200-500% APY on allocated funds.",
            priority: "medium"
        });
        recommendations.push({
            title: "Whale Status Benefits",
            description: "You qualify for exclusive whale benefits. Contact DAO for treasury participation opportunities.",
            priority: "low"
        });
    }
    
    return recommendations;
}

/**
 * Format timeframe label
 */
function formatTimeframe(months) {
    if (months < 12) {
        return months + ' month' + (months !== 1 ? 's' : '');
    } else {
        const years = Math.floor(months / 12);
        const remainingMonths = months % 12;
        let result = years + ' year' + (years !== 1 ? 's' : '');
        if (remainingMonths > 0) {
            result += ' ' + remainingMonths + ' month' + (remainingMonths !== 1 ? 's' : '');
        }
        return result;
    }
}

// Add CSS animation for results
const style = document.createElement('style');
style.textContent = `
    @keyframes fadeIn {
        from {
            opacity: 0;
            transform: translateY(10px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
`;
document.head.appendChild(style);

// Auto-calculate on load if values are present
if (typeof window !== 'undefined') {
    window.addEventListener('DOMContentLoaded', () => {
        // Add event listeners for real-time updates
        const investment = document.getElementById('investment');
        const timeframe = document.getElementById('timeframe');
        const strategy = document.getElementById('strategy');
        
        if (investment && timeframe && strategy) {
            [investment, timeframe, strategy].forEach(el => {
                el.addEventListener('change', calculateReturns);
            });
            
            // Calculate initial results
            if (investment.value && parseFloat(investment.value) > 0) {
                calculateReturns();
            }
        }
    });
}

// Export functions for use in other modules
if (typeof module !== 'undefined' && module.exports) {
    module.exports = {
        REVENUE_STREAMS,
        STRATEGIES,
        TIMEFRAMES,
        calculateReturns,
        calculateIncomeBreakdown,
        calculateTimeToGoal,
        getExpertRecommendations,
        formatCurrency,
        formatTimeframe
    };
}
