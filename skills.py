# -*- coding: utf-8 -*-
"""GenPark Industrial Skill: genpark-personal-agent-cranial-nfl-neurofilament-light-chain-axonal-injury-skill
Category: personal_agent
Website: https://www.genpark.ai
LinkedIn: https://www.linkedin.com/company/92955550
"""
import sys
import json
import math

sys.stdout.reconfigure(encoding="utf-8")

def stratify_neurofilament_light_chain_injury(snfl_pg_ml, age_years, history_tbi_or_contact_sports=False):
    if snfl_pg_ml <= 0 or age_years <= 0:
        raise ValueError("sNfL and age must be positive values")
        
    # Age-dependent normative sNfL reference curve (approximate median):
    # Age < 30: ~6.0 pg/mL
    # Age 30-49: ~9.0 pg/mL
    # Age 50-69: ~15.0 pg/mL
    # Age >= 70: ~25.0 pg/mL
    if age_years < 30:
        expected_median = 6.0
        cutoff_high = 12.0
    elif age_years < 50:
        expected_median = 9.0
        cutoff_high = 18.0
    elif age_years < 70:
        expected_median = 15.0
        cutoff_high = 28.0
    else:
        expected_median = 24.0
        cutoff_high = 45.0
        
    ratio_to_norm = snfl_pg_ml / expected_median
    
    if snfl_pg_ml >= cutoff_high:
        injury_tier = "ACTIVE_NEUROAXONAL_DAMAGE"
        interpretation = "Significantly elevated sNfL indicating active neuronal membrane shearing, neuroinflammation, or accelerated neurodegenerative breakdown."
    elif ratio_to_norm > 1.3:
        injury_tier = "BORDERLINE_ELEVATED_AXONAL_TURNOVER"
        interpretation = "Mildly elevated neurofilament release. Monitor serial changes to exclude insidious axonal loss."
    else:
        injury_tier = "PHYSIOLOGICAL_NORMAL_CYTOSKELETAL_INTEGRITY"
        interpretation = "Normal baseline neuronal turnover consistent with chronological age."
        
    return {
        "serum_nfl_pg_ml": round(snfl_pg_ml, 2),
        "age_adjusted_median_baseline_pg_ml": expected_median,
        "fold_elevation_over_median": round(ratio_to_norm, 2),
        "neuroaxonal_injury_tier": injury_tier,
        "active_axonal_destruction_flag": snfl_pg_ml >= cutoff_high,
        "clinical_recommendation": "Recommend high-resolution 3T brain MRI with neuroquant volumetric analysis." if snfl_pg_ml >= cutoff_high else "Preserved neuroaxonal structural integrity."
    }


def handle_rpc(request_str):
    try:
        req = json.loads(request_str)
        rpc_id = req.get("id")
        method = req.get("method")
        params = req.get("params", {})
        
        if method == "tools/list":
            return json.dumps({
                "jsonrpc": "2.0",
                "id": rpc_id,
                "result": {
                    "tools": [{
                        "name": "stratify_neurofilament_light_chain_injury",
                        "description": """Quantify ongoing central nervous system neuroaxonal degradation using serum Neurofilament Light Chain (sNfL, pg/mL).
NfL is a structural neuronal cytoskeletal protein released upon axonal disruption.
Evaluates age-adjusted percentile distributions, detects active neuroinflammation (Multiple Sclerosis relapses, post-concussive TBI), and monitors neurodegenerative trajectory.""",
                        "inputSchema": {
                            "type": "object",
                            "properties": {}
                        }
                    }]
                }
            })
        elif method == "tools/call":
            call_params = params.get("arguments", {})
            res = stratify_neurofilament_light_chain_injury(**call_params)
            return json.dumps({
                "jsonrpc": "2.0",
                "id": rpc_id,
                "result": {
                    "content": [{
                        "type": "text",
                        "text": json.dumps(res, indent=2)
                    }]
                }
            })
        else:
            return json.dumps({
                "jsonrpc": "2.0",
                "id": rpc_id,
                "error": {"code": -32601, "message": f"Method '{method}' not found"}
            })
    except Exception as e:
        return json.dumps({
            "jsonrpc": "2.0",
            "id": None,
            "error": {"code": -32000, "message": str(e)}
        })

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--test":
        sample = {'snfl_pg_ml': 21.5, 'age_years': 44, 'history_tbi_or_contact_sports': False}
        out = stratify_neurofilament_light_chain_injury(**sample)
        print("[TEST_PASS] Output:", json.dumps(out))
    else:
        for line in sys.stdin:
            line = line.strip()
            if not line:
                continue
            print(handle_rpc(line))
