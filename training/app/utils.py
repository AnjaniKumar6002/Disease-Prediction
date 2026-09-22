def get_risk_level(score):
    if score < 30:
        return "Low Risk"
    elif score < 70:
        return "Moderate Risk"
    return "High Risk"