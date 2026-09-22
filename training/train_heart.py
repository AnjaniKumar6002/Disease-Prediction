import os
import joblib
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix
)

# =========================
# Load Dataset
# =========================

print("Loading Heart Disease Dataset...")

df = pd.read_csv("datasets/heart_disease_uci.csv")

print(f"Dataset Shape: {df.shape}")

# =========================
# Target Conversion
# 0 = No Disease
# 1,2,3,4 = Disease
# =========================

df["num"] = df["num"].apply(lambda x: 0 if x == 0 else 1)

# =========================
# Drop Unnecessary Columns
# =========================

df.drop(columns=["id", "dataset"], inplace=True)

# =========================
# Remove Highly Missing Columns
# =========================

df.drop(columns=["ca", "thal"], inplace=True)

# =========================
# Handle Missing Values
# =========================

numeric_cols = [
    "trestbps",
    "chol",
    "thalch",
    "oldpeak"
]

categorical_cols = [
    "sex",
    "cp",
    "fbs",
    "restecg",
    "exang",
    "slope"
]

for col in numeric_cols:
    df[col].fillna(df[col].median(), inplace=True)

for col in categorical_cols:
    df[col].fillna(df[col].mode()[0], inplace=True)

# =========================
# One-Hot Encoding
# =========================

df = pd.get_dummies(
    df,
    columns=categorical_cols,
    drop_first=True
)

# =========================
# Features & Target
# =========================

X = df.drop("num", axis=1)
y = df["num"]

print("\nNumber of Features:", X.shape[1])

# =========================
# Train Test Split
# =========================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

# =========================
# Model
# =========================

model = RandomForestClassifier(
    n_estimators=200,
    random_state=42
)

print("\nTraining Model...")

model.fit(X_train, y_train)

# =========================
# Evaluation
# =========================

y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)

print("\n" + "=" * 50)
print("HEART DISEASE MODEL RESULTS")
print("=" * 50)

print(f"\nAccuracy: {accuracy:.4f}")

print("\nClassification Report:")
print(classification_report(y_test, y_pred))

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))

# =========================
# Save Model
# =========================

os.makedirs("models", exist_ok=True)

model_data = {
    "model": model,
    "features": X.columns.tolist()
}

joblib.dump(
    model_data,
    "models/heart_model.pkl"
)

print("\nModel Saved Successfully!")
print("Path: models/heart_model.pkl")

# =========================
# Feature Importance
# =========================

feature_importance = pd.DataFrame({
    "Feature": X.columns,
    "Importance": model.feature_importances_
})

feature_importance = feature_importance.sort_values(
    by="Importance",
    ascending=False
)

print("\nTop 10 Important Features:")
print(feature_importance.head(10))