# Nexus DAO Workflow Security Baseline

## Overview

This security baseline establishes security controls, permission boundaries, and audit gates for GitHub Actions workflows in the Nexus Protocol DAO repository.

## Core Rules

1. **Least-Privilege Permissions**: All workflows MUST default to `permissions: { contents: read }`. Elevated scopes (e.g. `id-token: write`) require explicit approval gates.
2. **Approval-Gated Deployment**: Deployment workflows (`deploy_secure.yml`, `financial-ops-automation.yml`) require human approval or multi-sig approval before executing state changes.
3. **Artifact Integrity**: Build outputs are generated in isolated jobs and passed as signed/versioned artifacts via `upload-artifact` / `download-artifact`.
4. **Deterministic Audit Logging**: All modernization events and workflow runs emit reports to `reports/` and `ops/reports/` for audit logging.
