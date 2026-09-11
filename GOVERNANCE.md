# Nexus DAO Governance

## 1. Purpose

Nexus DAO governs the Nexus ecosystem, including its smart contracts, treasury, and strategic direction, through transparent, on-chain, community-driven processes.

This document defines roles, powers, and processes. No single individual or entity has unilateral control over the protocol or treasury.

---

## 2. Core Principles

- **Decentralization:** Final authority rests with token holders voting on-chain.
- **Accountability:** All major actions are traceable to proposals and votes.
- **Least privilege:** Powers are scoped and limited to what is strictly necessary.
- **Safety:** Emergency mechanisms exist but are time-bound and revocable.
- **Transparency:** Governance rules and changes are publicly documented.

---

## 3. Roles

### 3.1 Token Holders (NGTT)

- **Role:** Electorate.
- **Powers:**
  - Create governance proposals (subject to threshold).
  - Vote on proposals.
  - Elect and remove stewards, multisig signers, and councils.
  - Approve or reject treasury allocations and protocol upgrades.

### 3.2 Delegates

- **Role:** Represent token holders who delegate voting power.
- **Powers:**
  - Vote on proposals using delegated NGTT.
  - Publish rationale for major votes.

### 3.3 Stewards (Including Founding Steward)

- **Role:** Operational contributors responsible for implementation and maintenance.
- **Powers:**
  - Draft proposals.
  - Implement passed proposals (code, infra, documentation).
- **Limits:**
  - No unilateral control over treasury.
  - No ability to bypass DAO votes.
  - No special voting rights beyond their NGTT holdings.

> The founding steward (Todd) is recognized for initial contributions but **does not hold any special or permanent control rights**.

### 3.4 Multisig (Gnosis Safe)

- **Role:** Execution layer for approved actions.
- **Powers:**
  - Execute transactions approved by DAO proposals (treasury transfers, upgrades).
  - Perform routine operational transactions within defined limits.
- **Limits:**
  - Configured as N-of-M signers.
  - Cannot override or ignore passed DAO votes.
  - High-risk actions (upgrades, large transfers) require explicit DAO approval.

### 3.5 Emergency Council (Optional)

- **Role:** Respond to critical incidents (exploits, bugs, attacks).
- **Powers:**
  - Temporarily pause contracts or specific functions.
  - Trigger incident response procedures.
- **Limits:**
  - Powers are time-bound and must be ratified or reversed by DAO vote.
  - Scope limited to predefined emergency actions (e.g., pause, parameter caps).

---

## 4. Governance Process

### 4.1 Proposal Lifecycle

1. **Draft:** Proposal written and shared off-chain (forum, docs).
2. **Submission:** On-chain proposal created by eligible token holder or delegate.
3. **Discussion:** Optional off-chain discussion period.
4. **Voting:** Token holders vote for/against/abstain.
5. **Queue (if timelock used):** Passed proposals enter a delay period.
6. **Execution:** Multisig or executor contract performs the approved action.

### 4.2 Proposal Types

- **Standard Proposals:**
  - Parameter changes.
  - Budget allocations.
  - Role changes (add/remove stewards, signers).
- **High-Risk Proposals:**
  - Protocol upgrades.
  - Large treasury transfers.
  - New token issuance.
  - Require higher quorum and approval thresholds.
- **Emergency Proposals (if enabled):**
  - Shorter voting period.
  - Limited to predefined emergency actions.
  - Must be followed by a post-mortem and ratification proposal.

---

## 5. Treasury Governance

- All treasury assets are held in one or more Gnosis Safes controlled by the DAO.
- **Spending rules:**
  - Small operational expenses may be pre-approved via budget proposals.
  - Large or unusual expenses require specific proposals.
- **Reserves:**
  - A portion of funds is held in low-risk assets for stability.
- **Reporting:**
  - Regular treasury reports are published (e.g., quarterly).

---

## 6. Founding Contributor & Compensation

The DAO acknowledges that early contributors may have funded infrastructure, tools, and labor out-of-pocket.

- Compensation for founding contributors is:
  - Proposed via formal DAO proposals.
  - Approved or rejected by token holder vote.
  - Structured to avoid granting special control rights.

---

## 7. Risk & Disclaimer

- Nexus DAO and its contributors do not guarantee profits or outcomes.
- Participation involves technical and financial risk.
- All software is experimental and may contain bugs.
- Users are responsible for their own decisions and risk management.

---

## 8. Amendments

This document may be amended only via DAO governance proposals approved by token holders.
