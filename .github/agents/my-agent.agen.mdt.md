---
# Fill in the fields below to create a basic custom agent for your repository.
# The Copilot CLI can be used for local testing: https://gh.io/customagents/cli
# To make this agent available, merge this file into the default repository branch.
# For format details, see: https://gh.io/customagents/config

name:
description: 
---| mfc: OK > (venv) Installation succeeded.
[Lint Source/Lint Source ] ✅ Success - Main Initialize MFC [1m2.473530356s]
[Lint Source/Lint Source ] ⭐ Run Main Lint the full source
[Lint Source/Lint Source ] ✅ Success - Main Lint the full source [3.918914682s]
[Lint Source/Lint Source ] ⭐ Run Main Looking for raw directives
| ./src/simulation/m_riemann_solvers.fpp: !$acc (create='[flux_gsrc_rsx_vf,flux_gsrc_rsy_vf,flux_gsrc_rsz_vf]')
[Lint Source/Lint Source ] ❌ Failure - Main Looking for raw directives [6.449387ms]
[Lint Source/Lint Source ] exit status 1
[Lint Source/Lint Source ] ⭐ Run Complete job
[Lint Source/Lint Source ] ✅ Success - Complete job
[Lint Source/Lint Source ] 🏁 Job failed
Error: Job 'Detect File Changes' failed

# My Agent

Describe what your agent does here...
