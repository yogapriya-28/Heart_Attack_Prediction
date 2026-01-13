
import streamlit as st
import numpy as np
import pickle
from sklearn.preprocessing import LabelEncoder

# ==============================
# Streamlit page config
# ==============================
st.set_page_config(page_title="❤️ Heart Attack Prediction", layout="wide")
st.title("❤️ Heart Attack Risk Prediction Dashboard")

# ==============================
# Load trained model
# ==============================
with open('heart_model.pkl', 'rb') as f_model:
    model = pickle.load(f_model)

# ==============================
# Sidebar Inputs
# ==============================
with st.sidebar:
    st.header("🔧 Input Parameters")

age = st.sidebar.number_input("Age", 18, 90, 50)
sex = st.sidebar.selectbox("Sex", ["Male","Female"])
cholesterol = st.sidebar.number_input("Cholesterol (mg/dL)", 100, 500, 200)
systolic = st.sidebar.number_input("Systolic BP", 80, 200, 120)
diastolic = st.sidebar.number_input("Diastolic BP", 60, 140, 80)
heart_rate = st.sidebar.number_input("Heart Rate", 40, 200, 70)
diabetes = st.sidebar.selectbox("Diabetes (0=No,1=Yes)", [0,1])
smoking = st.sidebar.selectbox("Smoking (0=No,1=Yes)", [0,1])
obesity = st.sidebar.selectbox("Obesity (0=No,1=Yes)", [0,1])
alcohol = st.sidebar.selectbox("Alcohol (0=No,1=Yes)", [0,1])
exercise_hours = st.sidebar.number_input("Exercise Hours/Week", 0, 20, 5)
diet = st.sidebar.selectbox("Diet", ["Poor","Average","Good"])
stress = st.sidebar.number_input("Stress Level (1-10)", 1, 10, 5)
sedentary_hours = st.sidebar.number_input("Sedentary Hours/Day", 0.0, 12.0, 5.0)
bmi = st.sidebar.number_input("BMI", 15.0, 50.0, 25.0)
triglycerides = st.sidebar.number_input("Triglycerides", 30, 800, 150)
activity_days = st.sidebar.number_input("Active Days/Week", 0, 7, 3)
sleep_hours = st.sidebar.number_input("Sleep Hours/Day", 4, 12, 7)
country = st.sidebar.selectbox("Country", ["Germany","Canada","USA","France","Argentina","Thailand","India"])
continent = st.sidebar.selectbox("Continent", ["Europe","North America","Asia","South America"])
hemisphere = st.sidebar.selectbox("Hemisphere", ["Northern Hemisphere","Southern Hemisphere"])

# ==============================
# Encode categorical variables
# ==============================
le_sex = LabelEncoder().fit(["Male","Female"])
sex = le_sex.transform([sex])[0]

le_diet = LabelEncoder().fit(["Poor","Average","Good"])
diet = le_diet.transform([diet])[0]

le_country = LabelEncoder().fit(["Germany","Canada","USA","France","Argentina","Thailand","India"])
country = le_country.transform([country])[0]

le_continent = LabelEncoder().fit(["Europe","North America","Asia","South America"])
continent = le_continent.transform([continent])[0]

le_hemisphere = LabelEncoder().fit(["Northern Hemisphere","Southern Hemisphere"])
hemisphere = le_hemisphere.transform([hemisphere])[0]

# ==============================
# Dummy features to match 25-feature model
# ==============================
# If your model expects 25 features and you have 21 real features,
# we add 4 dummy zeros. Replace these with real inputs if needed.
feature4, feature5, feature6, feature7 = 0, 0, 0, 0

# ==============================
# Prediction & Risk Classification
# ==============================
if st.button("🔍 Predict Risk"):
    features = np.array([[age, sex, cholesterol, heart_rate, diabetes,
                          smoking, obesity, alcohol, exercise_hours, diet,
                          stress, sedentary_hours, bmi, triglycerides, activity_days,
                          sleep_hours, country, continent, hemisphere, systolic, diastolic,
                          feature4, feature5, feature6, feature7]])

    probability = model.predict_proba(features)[0][1] * 100  # percentage

    # Medical-standard risk levels
    if probability < 5:
        risk_level = "Low Risk"
        st.success(f"✅ {risk_level}. Probability: {probability:.2f}%")
    elif 5 <= probability < 7.5:
        risk_level = "Borderline Risk"
        st.warning(f"⚠️ {risk_level}. Probability: {probability:.2f}%")
    elif 7.5 <= probability < 20:
        risk_level = "Intermediate Risk"
        st.warning(f"⚠️ {risk_level}. Probability: {probability:.2f}%")
    else:
        risk_level = "High Risk"
        st.error(f"⚠️ {risk_level}! Probability: {probability:.2f}%")

# ==============================
# KPI Metrics
# ==============================
col1, col2, col3 = st.columns(3)
col1.metric("Average Cholesterol", f"{cholesterol:.1f} mg/dL")
col2.metric("BMI", f"{bmi:.1f}")
col3.metric("Heart Rate", f"{heart_rate} bpm")

# ==============================
# Footer
# ==============================
st.markdown("---")
st.markdown("Developed by: Yogapriya | Heart Health Prediction System")
