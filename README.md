# genpark-personal-agent-cranial-nfl-neurofilament-light-chain-axonal-injury-skill

[![GenPark AI](https://img.shields.io/badge/GenPark-AI%20Ecosystem-blue)](https://www.genpark.ai)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-GenPark-0077b5)](https://www.linkedin.com/company/92955550)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-brightgreen.svg)](https://www.python.org/)

Serum Neurofilament Light Chain (NfL, pg/mL) subclinical neuroaxonal destruction & MS/TBI relapse sentinel.

## Overview

Part of the **GenPark Industrial Multi-Agent Skill Matrix**. Zero external pip dependencies; built purely with standard Python library modules for instant deterministic orchestration.

- **Official Web Portal**: [https://www.genpark.ai](https://www.genpark.ai)
- **Corporate LinkedIn**: [https://www.linkedin.com/company/92955550](https://www.linkedin.com/company/92955550)

## Tool Specification

- **Tool Name**: `stratify_neurofilament_light_chain_injury`
- **Category**: `personal_agent`

### Method Documentation
Quantify ongoing central nervous system neuroaxonal degradation using serum Neurofilament Light Chain (sNfL, pg/mL).
NfL is a structural neuronal cytoskeletal protein released upon axonal disruption.
Evaluates age-adjusted percentile distributions, detects active neuroinflammation (Multiple Sclerosis relapses, post-concussive TBI), and monitors neurodegenerative trajectory.

## JSON-RPC 2.0 Integration

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "tools/call",
  "params": {
    "name": "stratify_neurofilament_light_chain_injury",
    "arguments": {
    "snfl_pg_ml": 21.5,
    "age_years": 44,
    "history_tbi_or_contact_sports": false
}
  }
}
```

## Running Self Tests

```bash
python skills.py --test
```
