import os
import joblib
import pandas as pd

from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix
)

# ==========================================
# Load Dataset
# ==========================================

print("Loading Breast Cancer Dataset...")

data = load_breast_cancer()

df = pd.DataFrame(
    data.data,
    columns=data.feature_names
)

# ==========================================
# Select Only UI Features
# ==========================================

selected_features = [
    "mean radius",
    "mean texture",
    "mean perimeter",
    "mean area",
    "mean smoothness"
]

X = df[selected_features]
y = pd.Series(data.target)

print("\nSelected Features:")
print(selected_features)

print(f"\nDataset Shape: {X.shape}")

# ==========================================
# Train Test Split
# ==========================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

# ==========================================
# Model
# ==========================================

model = LogisticRegression(
    max_iter=5000,
    random_state=42
)

print("\nTraining Model...")

model.fit(X_train, y_train)

# ==========================================
# Evaluation
# ==========================================

y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)

print("\n" + "=" * 50)
print("BREAST CANCER MODEL RESULTS")
print("=" * 50)

print(f"\nAccuracy: {accuracy:.4f}")

print("\nClassification Report:")
print(classification_report(y_test, y_pred))

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))

# ==========================================
# Save Model
# ==========================================

os.makedirs("models", exist_ok=True)

model_data = {
    "model": model,
    "features": selected_features
}

joblib.dump(
    model_data,
    "models/breast_cancer_model.pkl"
)

print("\nModel Saved Successfully!")
print("Path: models/breast_cancer_model.pkl")

# ==========================================
# Feature Importance
# ==========================================

feature_importance = pd.DataFrame({
    "Feature": selected_features,
    "Coefficient": abs(model.coef_[0])
})

feature_importance = feature_importance.sort_values(
    by="Coefficient",
    ascending=False
)

print("\nFeature Importance:")
print(feature_importance)

# ==========================================
# Class Labels
# ==========================================

print("\nTarget Names:")
print(data.target_names)

print("\nClass Meaning:")
print("0 = Malignant (Cancer)")
print("1 = Benign (Healthy)")