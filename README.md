
# 🏥 Multi-Disease Prediction System

A Machine Learning-powered healthcare analytics platform that predicts the risk of multiple diseases using patient medical parameters.

## 🚀 Features

❤️ **Heart Disease Risk Prediction**
🎗️ **Breast Cancer Risk Prediction**
📊 **Overall Health Risk Assessment**
💡 **Personalized Health Recommendations**
📄 **PDF Report Generation**
🌐 **Interactive Streamlit Dashboard**

---

## 🛠️ Tech Stack

### Frontend

* Streamlit

### Backend

* Python

### Machine Learning

* Scikit-Learn
* Random Forest Classifier
* Logistic Regression

### Data Processing

* Pandas
* NumPy

### Report Generation

* ReportLab

---

## 📂 Project Structure

```text
DISEASE_PREDICTION/
│
├── app/
│   ├── app.py
│   ├── predictor.py
│   ├── report_generator.py
│   └── utils.py
│
├── datasets/
│   └── heart_disease_uci.csv
│
├── models/
│   ├── heart_model.pkl
│   └── breast_cancer_model.pkl
│
├── training/
│   ├── train_heart.py
│   └── train_cancer.py
│
├── reports/
│
├── requirements.txt
├── .gitignore
└── README.md
```

---

## 🤖 Machine Learning Models

| Disease           | Algorithm           | Accuracy |
| ----------------- | ------------------- | -------: |
| ❤️ Heart Disease  | Random Forest       |   84.24% |
| 🎗️ Breast Cancer | Logistic Regression |     90%+ |

> **Note:** Accuracy values depend on the dataset, preprocessing, train-test split, and model configuration used during training.

---

## 📊 Input Parameters

### ❤️ Heart Disease

* Age
* Gender
* Chest Pain Type
* Blood Pressure
* Cholesterol
* Maximum Heart Rate
* Exercise-Induced Angina
* Oldpeak

### 🎗️ Breast Cancer

* Mean Radius
* Mean Texture
* Mean Perimeter
* Mean Area
* Mean Smoothness

---

## ⚙️ Installation

### Clone the repository

```bash
git clone https://github.com/aavati-sivasankar/CodeAlpha_Multi_Disease_Prediction.git
cd CodeAlpha_Multi_Disease_Prediction
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run the application

```bash
streamlit run app/app.py
```

---

## 📄 Generated Report

The system generates a downloadable PDF report containing:

* Patient Information
* Heart Disease Risk
* Breast Cancer Risk
* Overall Health Risk
* Personalized Recommendations

---

## 📸 Dashboard Preview

Add screenshots of your Streamlit dashboard here after deployment.

---

## 🎯 Future Improvements

* Additional disease prediction models
* Doctor recommendation system
* Cloud deployment
* User authentication
* Database integration
* Medical history tracking
* Improved model accuracy
* Real-time health analytics

Github link: https://github.com/AnjaniKumar6002


