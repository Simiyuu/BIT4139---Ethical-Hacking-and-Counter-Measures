def calculate_internal_risk(base_cvss, asset_criticality, internet_exposed):
    exposure_multiplier = 1.35 if internet_exposed else 0.85
    adjusted_score = base_cvss * (asset_criticality * 0.10) * exposure_multiplier
    
    final_score = round(min(10.0, adjusted_score), 2)
    
    if final_score >= 9.0: priority = "IMMEDIATE (P1)"
    elif final_score >= 7.0: priority = "HIGH (P2)"
    else: priority = "STANDARD (P3)"
    
    return {"calculated_risk_score": final_score, "patch_priority": priority}

print(calculate_internal_risk(base_cvss=9.8, asset_criticality=9, internet_exposed=False))