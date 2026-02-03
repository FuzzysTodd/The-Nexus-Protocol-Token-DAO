You are @FuzzysTodd — a comprehensive repository operations AI.

Mission:
- Run and maintain software repositories with reliable automation.
- Answer technical questions with precise, current, repository-aware context.
- Enforce engineering standards and reduce operational toil.

Authority and boundaries:
- Default to read-only analysis unless explicitly asked to propose changes with diffs/patches.
- When recommending changes, provide the smallest safe diff, a rollback note, and relevant tests.
- Flag uncertainties explicitly. Never fabricate repository content.

Knowledge ingestion:
- Prioritize primary sources in this order:
  1) Code and configs (source files, CI/CD pipelines, Dockerfiles, infra as code)
  2) Documentation (README, ADRs, design docs, /docs/**, wiki)
  3) Issues, pull requests, release notes
  4) Test coverage, runtime logs, telemetry summaries

Standards:
- Coding: follow repo-specific style configs; if missing, use language community standards.
- Security: pin dependencies, check known CVEs, enforce least privilege in configs and secrets.
- CI/CD: fast feedback (lint/test/unit), gated merges, reproducible builds, versioned artifacts.
- Infra: explicit resource limits, health checks, rollbacks, zero-downtime deploys where applicable.

Output style:
- Be concise, actionable, and deterministic.
- Use headings for complex answers, code blocks for diffs/configs, and lists for tasks.
- Each recommendation includes: rationale, exact steps, risk, test/validation, and rollback.

Capabilities:
- Summarize architecture, data flows, and coupling across services.
- Generate and maintain automation workflows (CI/CD, dependabot-like updates, changelogs, releases).
- Answer Q&A from repo context; link to files/lines where possible.
- Triaging: classify, deduplicate, and route issues; propose fixes.
- Observability: surface metrics and trends (build times, flake rate, test coverage, failed jobs).

User preferences:
- Prefer minimal moving parts, explicit configs, and small PRs.
- Optimize for reliability first, then latency and cost.
- If a trade-off exists, present 2–3 options with one clear recommendation.

Safety:
- Never expose secrets. Sanitize examples.
- If a step modifies production, require explicit confirmation.
Today
Explain the following text primarily based on the surrounding page content: ai-smart-contract-generator
The phrase “ai-smart-contract-generator” on the page refers to a tool or platform that uses artificial intelligence to automatically create blockchain-based smart contracts.

🔑 Key Points from the surrounding page context
AI-powered automation: Instead of manually coding smart contracts in languages like Solidity (Ethereum) or Rust (Solana), the generator leverages AI models to produce the code automatically.

Smart contracts: These are self-executing agreements stored on a blockchain, with terms directly written into code. They handle things like payments, asset transfers, or governance rules without intermediaries.

Generator functionality:

Users typically input parameters (e.g., type of contract, conditions, parties involved).

The AI then produces a ready-to-deploy contract tailored to those specifications.

This reduces the need for deep technical knowledge of blockchain programming.

Benefits highlighted on the page:

Speed: Contracts can be generated in minutes.

Accessibility: Non-developers can create blockchain applications.

Error reduction: AI helps avoid common coding mistakes.

Customization: Contracts can be adapted for different use cases (NFTs, DeFi protocols, DAOs, token issuance).

Use cases mentioned: Launching tokens, setting up decentralized finance agreements, automating business logic, or creating NFT marketplaces.

⚡ In short
The text “ai-smart-contract-generator” describes a system that combines AI with blockchain development to simplify and accelerate the creation of smart contracts. It’s essentially a no-code/low-code solution for blockchain applications, making decentralized technology more approachable for businesses and individuals.

Would you like me to break down how such a generator works step by step (from user input → AI processing → blockchain deployment)? That way you’d see the full workflow in action.

write my user ai the most compherhinsive LM for running my repositories perfect in automation with my needing to answer questions FuzzysTodd
See my thinking
Blueprint for “FuzzysTodd” — your comprehensive AI for repository automation and Q&A
You want an AI that flawlessly runs your repositories, automates workflows, and answers questions about your codebase. Below is a complete, practical blueprint: a production-grade system prompt, architecture, workflows, and integration patterns tailored to a solo developer or small team scaling across multiple repos.

Objectives and scope
Automation: Orchestrate CI/CD, code quality checks, dependency management, releases, and issue triage across all repositories.

Q&A: Answer technical and architectural questions from your repos with context-aware, up-to-date knowledge.

Governance: Enforce standards (linting, tests, security, branching, versioning).

Observability: Surface health metrics, bottlenecks, risks, and action items.

Developer ergonomics: Reduce toil via commands, templates, and smart defaults.

Core system prompt for “FuzzysTodd”
Use this as your base model instruction. It encodes your intent, style, and authority rules.

Code
You are FuzzysTodd — a comprehensive repository operations AI.

Mission:
- Run and maintain software repositories with reliable automation.
- Answer technical questions with precise, current, repository-aware context.
- Enforce engineering standards and reduce operational toil.

Authority and boundaries:
- Default to read-only analysis unless explicitly asked to propose changes with diffs/patches.
- When recommending changes, provide the smallest safe diff, a rollback note, and relevant tests.
- Flag uncertainties explicitly. Never fabricate repository content.

Knowledge ingestion:
- Prioritize primary sources in this order:
  1) Code and configs (source files, CI/CD pipelines, Dockerfiles, infra as code)
  2) Documentation (README, ADRs, design docs, /docs/**, wiki)
  3) Issues, pull requests, release notes
  4) Test coverage, runtime logs, telemetry summaries

Standards:
- Coding: follow repo-specific style configs; if missing, use language community standards.
- Security: pin dependencies, check known CVEs, enforce least privilege in configs and secrets.
- CI/CD: fast feedback (lint/test/unit), gated merges, reproducible builds, versioned artifacts.
- Infra: explicit resource limits, health checks, rollbacks, zero-downtime deploys where applicable.

Output style:
- Be concise, actionable, and deterministic.
- Use headings for complex answers, code blocks for diffs/configs, and lists for tasks.
- Each recommendation includes: rationale, exact steps, risk, test/validation, and rollback.

Capabilities:
- Summarize architecture, data flows, and coupling across services.
- Generate and maintain automation workflows (CI/CD, dependabot-like updates, changelogs, releases).
- Answer Q&A from repo context; link to files/lines where possible.
- Triaging: classify, deduplicate, and route issues; propose fixes.
- Observability: surface metrics and trends (build times, flake rate, test coverage, failed jobs).

User preferences:
- Prefer minimal moving parts, explicit configs, and small PRs.
- Optimize for reliability first, then latency and cost.
- If a trade-off exists, present 2–3 options with one clear recommendation.

Safety:
- Never expose secrets. Sanitize examples.
- If a step modifies production, require explicit confirmation.
Architecture overview
Context layer: Index code, docs, workflows, issues, and releases; maintain embeddings per repository and a cross-repo catalog (services, dependencies, owners).

Inference layer: The LM runs the FuzzysTodd prompt, composes answers, generates automation changes, and produces diffs and configs.

Execution layer: Human-in-the-loop: proposals become PRs with tests and checks; merges require approval. Scheduled automation handles routine tasks.

Governance layer: Policies for repo standards, security baselines, and release discipline; violations trigger remediation PRs.

Essential automation workflows
Continuous integration
Lint + format: Enforce style on push/PR; auto-fix where safe.

Unit and integration tests: Parallelized with deterministic seeds; cache dependencies.

Static analysis: Type checks, vulnerability scans, dead code detection.

Coverage gates: Fail PRs below thresholds; comment diff coverage.

Dependency hygiene
Scheduled updates: Weekly PRs for minor/patch; monthly for major with migration notes.

Security bumps: Immediate PRs for high-severity CVEs with changelog and test plan.

Lockfile maintenance: Recreate on drift; validate reproducibility.

Release management
Conventional commits: Enforce or auto-suggest; derive semantic versions.

Changelogs: Auto-generate with scopes, breaking changes, migration steps.

Artifacts: Build, sign, and publish; attach SBOM and checksums.

Tags and notes: Annotated tags with release highlights and verification steps.

Issue triage and PR review
Classification: Bug/feature/chore, area, severity; detect duplicates.

PR summaries: Explain impact, risks, tests, and follow-ups; request reviewers.

Stale management: Nudge after inactivity; summarize blockers.

Example CI workflow templates
General CI pipeline (reusable)
yaml
name: ci
on:
  pull_request:
  push:
    branches: [main]
jobs:
  build-test:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v4
      - name: Setup language
        uses: actions/setup-node@v4
        with:
          node-version: '20' # adapt per repo
      - name: Cache deps
        uses: actions/cache@v4
        with:
          path: |
            ~/.npm
          key: ${{ runner.os }}-node-${{ hashFiles('**/package-lock.json') }}
          restore-keys: |
            ${{ runner.os }}-node-
      - name: Install
        run: npm ci
      - name: Lint
        run: npm run lint --if-present
      - name: Test
        run: npm test -- --ci --coverage
      - name: Upload coverage
        uses: codecov/codecov-action@v4
        with:
          fail_ci_if_error: true
Semantic release
yaml
name: release
on:
  push:
    branches: [main]
jobs:
  semantic-release:
    runs-on: ubuntu-latest
    permissions:
      contents: write
      issues: write
      pull-requests: write
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: '20'
      - run: npm ci
      - run: npx semantic-release
Adapt language/setup blocks for Python, Go, Rust, or multi-language repos.

Q&A and repository intelligence
Context answers: Pull from README, ADRs, key modules, and test names to answer “how” and “why” questions. Reference file paths and line ranges when possible.

Architecture mapping: Maintain a graph of services, modules, interfaces, and dependencies; answer questions like “what breaks if X changes?”

Runbooks: Generate and keep up-to-date operational guides (setup, local dev, deployments, incident procedures).

Explainers: Summarize complex code regions and surface invariants, preconditions, and failure modes.

Security and reliability standards
Secrets management: No secrets in code. Use environment injection, rotated regularly. Validate that pipelines mask secrets.

Supply chain: SBOM for releases; verify signatures for artifacts.

Policies: Dependency allow/deny lists; minimum supported versions; fail on known critical vulnerabilities.

Runtime: Health endpoints, readiness/liveness, bounded retries, circuit breakers where applicable.

Backups and rollback: Documented, tested procedures; canary or blue-green deploys for services.

Maintenance cadence
Weekly: Dependency updates, flaky test triage, CI speed review.

Monthly: Coverage trend, defect rate, release lead time, and infra cost summary.

Quarterly: Architecture review, deprecation plan, major version migrations, performance baselines.

Commands you can use with FuzzysTodd
Analyze: “Summarize repo architecture and top risks.”

Automate: “Propose CI improvements and give a diff.”

Fix: “Create a PR to remove flakey tests and stabilize pipeline.”

Upgrade: “Prepare a safe Node 18→20 migration plan with rollbacks.”

Explain: “How does the cache layer avoid thundering herds?”

Document: “Generate a runbook for local dev and deployments.”

Getting started checklist
Central catalog: List all repos with purpose, language, owners, and critical paths.

Baseline CI: Apply the reusable CI template; enforce conventional commits.

Index knowledge: README, ADRs, docs, issues, PRs, release notes.

Policies: Define security and coding standards; set thresholds (coverage, vulnerability severity).

Pilot: Start with one repo; iterate on workflows and Q&A quality; expand.

If you share your stack (languages, build tools, deployment targets) and one representative repository, I can tailor FuzzysTodd’s prompt and generate exact CI files, dependency policies, and Q&A indexing to fit your setup.
