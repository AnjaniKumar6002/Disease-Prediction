import joblib
import pandas as pd

# =====================================
# Load Models
# =====================================

heart_data = joblib.load("models/heart_model.pkl")
diabetes_data = joblib.load("models/diabetes_model.pkl")
cancer_data = joblib.load("models/breast_cancer_model.pkl")

heart_model = heart_data["model"]
heart_features = heart_data["features"]

diabetes_model = diabetes_data["model"]
diabetes_features = diabetes_data["features"]

cancer_model = cancer_data["model"]
cancer_features = cancer_data["features"]


# =====================================
# Heart Disease Prediction
# =====================================

def predict_heart(patient_data: dict):

    df = pd.DataFrame([patient_data])

    df = pd.get_dummies(df)

    df = df.reindex(
        columns=heart_features,
        fill_value=0
    )

    probability = heart_model.predict_proba(df)[0][1]

    return round(probability * 100, 2)


# =====================================
# Diabetes Prediction
# =====================================

def predict_diabetes(patient_data: dict):

    df = pd.DataFrame([patient_data])

    df = df.reindex(
        columns=diabetes_features,
        fill_value=0
    )

    probability = diabetes_model.predict_proba(df)[0][1]

    return round(probability * 100, 2)


# =====================================
# Breast Cancer Prediction
# =====================================

def predict_cancer(patient_data: dict):

    df = pd.DataFrame([patient_data])

    df = df.reindex(
        columns=cancer_features,
        fill_value=0
    )

    # Cancer Risk = Malignant Probability
    probability = cancer_model.predict_proba(df)[0][0]

    return round(probability * 100, 2)


# =====================================
# Risk Category
# =====================================

def get_risk_level(probability):

    if probability < 30:
        return "Low Risk"

    elif probability < 70:
        return "Moderate Risk"

    return "High Risk"


# =====================================
# Combined Health Report
# =====================================

def generate_health_report(
    heart_input,
    diabetes_input,
    cancer_input
):

    heart_risk = predict_heart(heart_input)

    diabetes_risk = predict_diabetes(diabetes_input)

    cancer_risk = predict_cancer(cancer_input)

    return {
        "heart_risk": heart_risk,
        "heart_level": get_risk_level(heart_risk),

        "diabetes_risk": diabetes_risk,
        "diabetes_level": get_risk_level(diabetes_risk),

        "cancer_risk": cancer_risk,
        "cancer_level": get_risk_level(cancer_risk)
    }