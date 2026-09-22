import streamlit as st

from predictor import (
    predict_heart,
    predict_diabetes,
    predict_cancer
)

from utils import get_risk_level

from report_generator import generate_pdf_report


# ==================================================
# PAGE CONFIG
# ==================================================

st.set_page_config(
    page_title="Multi Disease Prediction System",
    page_icon="🏥",
    layout="wide"
)

# ==================================================
# SIDEBAR
# ==================================================

st.sidebar.title("🏥 Navigation")

st.sidebar.info(
    """
    Multi Disease Prediction System

    Models Included:
    ❤️ Heart Disease
    🩸 Diabetes
    🎗️ Breast Cancer

    Built using Machine Learning
    """
)

# ==================================================
# HEADER
# ==================================================

st.title("🏥 Multi Disease Prediction System")

st.markdown(
    "Predict the risk of Heart Disease, Diabetes, and Breast Cancer using Machine Learning."
)

# ==================================================
# PATIENT INFORMATION
# ==================================================

st.header("👤 Patient Information")

col1, col2, col3 = st.columns(3)

with col1:
    patient_name = st.text_input(
        "Patient Name",
        placeholder="Enter patient name"
    )

with col2:
    age = st.number_input(
        "Age",
        min_value=1,
        max_value=120,
        value=30
    )

with col3:
    gender = st.selectbox(
        "Gender",
        ["Male", "Female"]
    )

# ==================================================
# HEART DISEASE INPUTS
# ==================================================

st.header("❤️ Heart Disease Parameters")

c1, c2, c3 = st.columns(3)

with c1:
    chest_pain = st.selectbox(
        "Chest Pain Type",
        [
            "typical angina",
            "atypical angina",
            "non-anginal",
            "asymptomatic"
        ]
    )

    resting_bp = st.number_input(
        "Resting Blood Pressure",
        min_value=50,
        max_value=250,
        value=120
    )

with c2:
    cholesterol = st.number_input(
        "Cholesterol",
        min_value=50,
        max_value=600,
        value=200
    )

    max_heart_rate = st.number_input(
        "Maximum Heart Rate",
        min_value=50,
        max_value=250,
        value=150
    )

with c3:
    exercise_angina = st.selectbox(
        "Exercise Induced Angina",
        [False, True]
    )

    oldpeak = st.number_input(
        "Oldpeak",
        min_value=0.0,
        max_value=10.0,
        value=1.0
    )

# ==================================================
# DIABETES INPUTS
# ==================================================

st.header("🩸 Diabetes Parameters")

c1, c2 = st.columns(2)

with c1:

    pregnancies = st.number_input(
        "Pregnancies",
        min_value=0,
        value=0
    )

    glucose = st.number_input(
        "Glucose",
        min_value=0,
        value=120
    )

    blood_pressure = st.number_input(
        "Blood Pressure",
        min_value=0,
        value=80
    )

    skin_thickness = st.number_input(
        "Skin Thickness",
        min_value=0,
        value=20
    )

with c2:

    insulin = st.number_input(
        "Insulin",
        min_value=0,
        value=80
    )

    bmi = st.number_input(
        "BMI",
        min_value=0.0,
        value=25.0
    )

    dpf = st.number_input(
        "Diabetes Pedigree Function",
        min_value=0.0,
        value=0.5
    )

# ==================================================
# BREAST CANCER INPUTS
# ==================================================

st.header("🎗️ Breast Cancer Parameters")

st.info(
    "These parameters are typically obtained from medical examination and tumor measurements."
)

c1, c2 = st.columns(2)

with c1:

    mean_radius = st.number_input(
        "Mean Radius",
        value=14.0
    )

    mean_texture = st.number_input(
        "Mean Texture",
        value=19.0
    )

    mean_perimeter = st.number_input(
        "Mean Perimeter",
        value=90.0
    )

with c2:

    mean_area = st.number_input(
        "Mean Area",
        value=650.0
    )

    mean_smoothness = st.number_input(
        "Mean Smoothness",
        value=0.10
    )

# ==================================================
# PREDICT BUTTON
# ==================================================

if st.button("🔍 Predict Health Risks"):

    try:

        # -------------------------
        # Heart Input
        # -------------------------

        heart_input = {
            "age": age,
            "sex": gender,
            "cp": chest_pain,
            "trestbps": resting_bp,
            "chol": cholesterol,
            "thalch": max_heart_rate,
            "exang": exercise_angina,
            "oldpeak": oldpeak,
            "fbs": False,
            "restecg": "normal",
            "slope": "flat"
        }

        # -------------------------
        # Diabetes Input
        # -------------------------

        diabetes_input = {
            "Pregnancies": pregnancies,
            "Glucose": glucose,
            "BloodPressure": blood_pressure,
            "SkinThickness": skin_thickness,
            "Insulin": insulin,
            "BMI": bmi,
            "DiabetesPedigreeFunction": dpf,
            "Age": age
        }

        # -------------------------
        # Cancer Input
        # -------------------------

        cancer_input = {
            "mean radius": mean_radius,
            "mean texture": mean_texture,
            "mean perimeter": mean_perimeter,
            "mean area": mean_area,
            "mean smoothness": mean_smoothness
        }

        # -------------------------
        # Predictions
        # -------------------------

        heart_risk = predict_heart(heart_input)
        diabetes_risk = predict_diabetes(diabetes_input)
        cancer_risk = predict_cancer(cancer_input)

        overall_risk = round(
            (heart_risk + diabetes_risk + cancer_risk) / 3,
            2
        )

        # ==================================================
        # RESULTS
        # ==================================================

        st.header("📊 Health Risk Report")

        st.subheader("❤️ Heart Disease Risk")
        st.progress(min(int(heart_risk), 100))
        st.success(
            f"{heart_risk}% ({get_risk_level(heart_risk)})"
        )

        st.subheader("🩸 Diabetes Risk")
        st.progress(min(int(diabetes_risk), 100))
        st.success(
            f"{diabetes_risk}% ({get_risk_level(diabetes_risk)})"
        )

        st.subheader("🎗️ Breast Cancer Risk")
        st.progress(min(int(cancer_risk), 100))
        st.success(
            f"{cancer_risk}% ({get_risk_level(cancer_risk)})"
        )

        st.header("🏥 Overall Health Status")

        st.metric(
            "Overall Risk Score",
            f"{overall_risk}%"
        )

        st.info(
            f"Overall Risk Level: {get_risk_level(overall_risk)}"
        )

        # ==================================================
        # RECOMMENDATIONS
        # ==================================================

        st.header("💡 Recommendations")

        recommendations = []

        if heart_risk > 70:
            recommendations.append(
                "Consult a cardiologist and monitor cholesterol levels."
            )

        if diabetes_risk > 70:
            recommendations.append(
                "Monitor blood glucose and reduce sugar intake."
            )

        if cancer_risk > 70:
            recommendations.append(
                "Consult a specialist for additional screening."
            )

        if not recommendations:
            recommendations.append(
                "Maintain a healthy lifestyle and attend regular medical checkups."
            )

        for rec in recommendations:
            st.write("•", rec)

        # ==================================================
        # PDF REPORT
        # ==================================================

        pdf_path = generate_pdf_report(
            patient_name if patient_name else "Patient",
            heart_risk,
            diabetes_risk,
            cancer_risk,
            recommendations
        )

        with open(pdf_path, "rb") as pdf_file:

            st.download_button(
                label="📄 Download Health Report",
                data=pdf_file,
                file_name=f"{patient_name}_Health_Report.pdf",
                mime="application/pdf"
            )

    except Exception as e:

        st.error(f"Prediction Error: {e}")

# ==================================================
# DISCLAIMER
# ==================================================

st.markdown("---")

st.warning(
    "This application provides machine learning-based risk predictions and is not a substitute for professional medical diagnosis. Please consult a healthcare professional."
)