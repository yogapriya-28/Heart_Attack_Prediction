# ❤️ Heart Attack Risk Prediction

## 📌 Project Overview
Heart Attack Risk Prediction is a **machine learning–based healthcare analytics project** designed to predict the likelihood of a heart attack using patient medical, lifestyle, and demographic data.

The project demonstrates **end-to-end data science workflow**, including:
- Data analysis
- Feature engineering
- Machine learning model building
- Model deployment using **Streamlit**

This project is intended for **educational and portfolio purposes**.

---

## 🎯 Problem Statement
Heart attacks are one of the leading causes of death worldwide. Early risk prediction can help individuals take preventive measures by identifying high-risk factors such as lifestyle habits, medical history, and physiological parameters.

---

## 🗂️ Dataset Description
- **Total Records:** 8,763  
- **Total Features:** 26  
- **Target Variable:** `Heart Attack Risk`  
  - `0` → Low Risk  
  - `1` → High Risk  
- **Missing Values:** None  

### Key Features
- Age, Sex
- Cholesterol
- Blood Pressure (Systolic & Diastolic)
- Heart Rate
- Diabetes
- Smoking
- Obesity
- Alcohol Consumption
- Exercise Hours
- Diet
- Stress Level
- Sedentary Hours
- BMI
- Triglycerides
- Physical Activity Days
- Sleep Hours
- Country, Continent, Hemisphere

---

## 🧠 Machine Learning Workflow

### 1️⃣ Data Preprocessing
- Verified missing values (none found)
- Split blood pressure into:
  - `Systolic_BP`
  - `Diastolic_BP`
- Encoded categorical variables using `LabelEncoder`
- Removed irrelevant columns (`Patient ID`)

### 2️⃣ Exploratory Data Analysis (EDA)
- Gender-wise comparison of:
  - Smoking
  - Alcohol Consumption
  - Diabetes
- Numerical feature distribution analysis
- Summary statistics using `.describe()`

### 3️⃣ Feature Engineering
- Converted categorical variables into numerical form
- Selected relevant features for model training

### 4️⃣ Model Training
- Algorithm: **Random Forest Classifier**
- Train/Test Split: **80% / 20%**
- Model stored as `heart_model.pkl`

### 5️⃣ Model Deployment
- Interactive dashboard built using **Streamlit**
- Deployed via **Ngrok** for public access

---

## 📊 Exploratory Data Analysis Insights
- Male patients show higher proportions of:
  - Smoking
  - Alcohol consumption
  - Diabetes
- Higher **BMI**, **sedentary hours**, and **stress levels** increase heart attack risk
- Lifestyle habits play a crucial role in cardiovascular health

---

## 🛠️ Tech Stack
- **Language:** Python
- **Libraries:**
  - pandas
  - numpy
  - matplotlib
  - scikit-learn
  - streamlit
  - pickle
- **Tools:**
  - Google Colab
  - Ngrok
  - GitHub

---

## 📁 Project Structure
Heart_Attack_Prediction/
│
├── README.md
├── heartattack_risk.ipynb # Data analysis & model training
├── heart_app.py # Streamlit web application
├── heart_model.pkl # Trained ML model
└── dataset/
└── heart_attack_prediction_dataset.csv

---


---

## 🚀 Streamlit Application Features
- User-friendly sidebar inputs
- Real-time heart attack risk prediction
- Risk probability percentage
- Medical-standard risk classification:
  - Low Risk
  - Borderline Risk
  - Intermediate Risk
  - High Risk
- KPI display:
  - Cholesterol
  - BMI
  - Heart Rate

---





