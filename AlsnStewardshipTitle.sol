// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

/**
 * ------------------------------------------------------------
 * ALSN STEWARDSHIP TITLE CONTRACT
 * ------------------------------------------------------------
 * A Stewardship Title represents:
 *  - A non-transferable cultural/land stewardship right
 *  - Assigned to a specific Steward (address)
 *  - Bound to a region (e.g., "atlanta-metro")
 *  - Weighted by a reparative priority score
 *
 * Features:
 *  - Issue Title
 *  - Revoke Title
 *  - Inherit Title (controlled succession)
 *  - Query Steward Titles
 *  - Query Title metadata
 *
 * Only ALSN Authority (council/foundation) can issue/revoke/inherit.
 * Titles are soulbound-like: cannot be transferred by the holder.
 * ------------------------------------------------------------
 */

contract AlsnStewardshipTitle {
    // ------------------------------------------------------------
    // EVENTS
    // ------------------------------------------------------------
    event TitleIssued(
        uint256 indexed titleId,
        address indexed steward,
        string regionId,
        uint256 reparativeScore
    );

    event TitleRevoked(
        uint256 indexed titleId,
        address indexed steward,
        string reason
    );

    event TitleInherited(
        uint256 indexed titleId,
        address indexed fromSteward,
        address indexed toSteward
    );

    // ------------------------------------------------------------
    // STATE
    // ------------------------------------------------------------
    struct Title {
        address steward;          // Current holder
        string regionId;          // ALSN region (e.g., "atlanta-metro")
        uint256 reparativeScore;  // Reparative justice priority
        bool active;              // Active or revoked
    }

    address public alsnAuthority; // ALSN council/foundation
    uint256 public nextTitleId;

    mapping(uint256 => Title) public titles;
    mapping(address => uint256[]) public stewardTitles;

    modifier onlyAuthority() {
        require(msg.sender == alsnAuthority, "Only ALSN authority");
        _;
    }

    // ------------------------------------------------------------
    // CONSTRUCTOR
    // ------------------------------------------------------------
    constructor(address _alsnAuthority) {
        alsnAuthority = _alsnAuthority;
        nextTitleId = 1;
    }

    // ------------------------------------------------------------
    // ISSUE TITLE
    // ------------------------------------------------------------
    function issueTitle(
        address steward,
        string calldata regionId,
        uint256 reparativeScore
    ) external onlyAuthority returns (uint256) {
        uint256 titleId = nextTitleId++;

        titles[titleId] = Title({
            steward: steward,
            regionId: regionId,
            reparativeScore: reparativeScore,
            active: true
        });

        stewardTitles[steward].push(titleId);

        emit TitleIssued(titleId, steward, regionId, reparativeScore);
        return titleId;
    }

    // ------------------------------------------------------------
    // REVOKE TITLE
    // ------------------------------------------------------------
    function revokeTitle(
        uint256 titleId,
        string calldata reason
    ) external onlyAuthority {
        Title storage t = titles[titleId];
        require(t.active, "Title not active");

        t.active = false;

        emit TitleRevoked(titleId, t.steward, reason);
    }

    // ------------------------------------------------------------
    // INHERIT TITLE (controlled succession)
    // ------------------------------------------------------------
    function inheritTitle(
        uint256 titleId,
        address newSteward
    ) external onlyAuthority {
        Title storage t = titles[titleId];
        require(t.active, "Title not active");

        address oldSteward = t.steward;
        t.steward = newSteward;

        stewardTitles[newSteward].push(titleId);

        emit TitleInherited(titleId, oldSteward, newSteward);
    }

    // ------------------------------------------------------------
    // VIEW HELPERS
    // ------------------------------------------------------------
    function getStewardTitles(address steward)
        external
        view
        returns (uint256[] memory)
    {
        return stewardTitles[steward];
    }

    function getTitle(uint256 titleId)
        external
        view
        returns (
            address steward,
            string memory regionId,
            uint256 reparativeScore,
            bool active
        )
    {
        Title storage t = titles[titleId];
        return (t.steward, t.regionId, t.reparativeScore, t.active);
    }
}

