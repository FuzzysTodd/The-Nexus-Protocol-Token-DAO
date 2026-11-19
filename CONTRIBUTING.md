# Contributing to The Nexus Protocol Token DAO

Thank you for contributing to The Nexus Protocol Token DAO (`NGTT`). As an institutional-grade financial protocol adhering to **ISO 9001:2015 Quality Management** and **IEEE 1012-2016 Software Verification & Validation**, all contributions are subject to rigorous verification.

---

## 1. Engineering Principles & Standards

### ISO 9001:2015 & IEEE Standards Compliance
1. **Clause 8.5.1 (Controlled Production):** All state mutations, on-chain transactions, and signal broadcasts must be deterministically reproducible and verified with sequential nonces.
2. **IEEE 1012-2016 (V&V):** Any new mathematical, cryptographic, or financial logic must be decoupled as pure functions in `src/dao/logic.ts` with matching unit tests in `src/dao/logic.test.ts`.
3. **IEEE 730-2014 (Software Quality Assurance):** Pull requests must maintain or improve test coverage (>90% threshold for Tier 1 modules).

### Anti-Degradation Rules
- **No Direct State Coupling:** React components must never contain inline mathematical solvers or raw financial calculations. All logic must flow through verified pure functions.
- **Protocol Envelope Adherence:** Numeric inputs on oracles and treasury adjustments must validate against `validateSignalBroadcast()` envelopes.
- **Residue Protection:** Basis point splits must use `calculatePayableSplit()` with zero dust leakage.

---

## 2. Pull Request Lifecycle

1. **Issue Identification & CAR Reference:**
   - Link your contribution to a designated Corrective Action Request (`CAR-ISO-01`, `CAR-IEEE-02`, etc.) or create a formal proposal if introducing new modules.
2. **Branching Standard:**
   - Branch names must follow standard format: `feat/cap-<description>`, `fix/consensus-<description>`, or `security/multisig-<description>`.
   - The default integration branches are `MASTER` and `main`.
3. **Verification Checklist Prior to PR Submission:**
   - [ ] `npx tsx --test src/dao/logic.test.ts` passes with 0 failures.
   - [ ] `npm run build` succeeds without compiler errors.
   - [ ] New methods include documentation comments with parameter types and return contracts.
   - [ ] No extraneous bundle files or secret keys committed.

---

## 3. Cryptographic Commit Protocol

All commits on release and governance branches must be attributed to authorized contributors and validated by CI:
```bash
git commit -S -m "feat(module): describe changes with reference to ISO/IEEE standard"
```

## 4. Reporting Security Vulnerabilities

To report a potential vulnerability regarding treasury reserves, timelock mechanics, or oracle consensus:
- Directly notify the Canonical Authority: `@FuzzysTodd` (`fuzzystodd@gmail.com`).
- Do NOT open public issues for unpatched vulnerabilities.
