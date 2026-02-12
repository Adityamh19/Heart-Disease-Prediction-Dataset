import streamlit as st
import pandas as pd
import joblib
import numpy as np

# 1. Load the saved model pipeline
model = joblib.load('heart_disease_pipeline.pkl')

# 2. Page Configuration
st.set_page_config(page_title="Heart Disease Risk Predictor", layout="centered")

# 3. Header
st.title("🏥 10-Year Cardiovascular Risk Predictor")
st.markdown("This dashboard uses Machine Learning to predict the 10-year risk of Coronary Heart Disease (CHD) based on clinical and behavioral factors.")
st.write("---")

# 4. Input Fields (Divided into columns for a clean UI)
st.sidebar.header("Patient Demographics & Behavior")
male = st.sidebar.selectbox("Sex", options=[0, 1], format_func=lambda x: "Male" if x == 1 else "Female")
age = st.sidebar.slider("Age", 30, 80, 50)
education = st.sidebar.selectbox("Education Level", options=[1, 2, 3, 4], help="1: Some High School, 2: High School, 3: College, 4: Degree")
currentSmoker = st.sidebar.radio("Current Smoker?", [0, 1], format_func=lambda x: "Yes" if x == 1 else "No")
cigsPerDay = st.sidebar.number_input("Cigarettes Per Day", min_value=0, max_value=70, value=0)

st.header("Clinical Measurements")
col1, col2 = st.columns(2)

with col1:
    BPMeds = st.selectbox("On BP Medication?", [0, 1], format_func=lambda x: "Yes" if x == 1 else "No")
    prevalentStroke = st.selectbox("Previous Stroke?", [0, 1], format_func=lambda x: "Yes" if x == 1 else "No")
    prevalentHyp = st.selectbox("Hypertensive?", [0, 1], format_func=lambda x: "Yes" if x == 1 else "No")
    diabetes = st.selectbox("Diabetes?", [0, 1], format_func=lambda x: "Yes" if x == 1 else "No")
    totChol = st.number_input("Total Cholesterol (mg/dL)", 100, 600, 230)

with col2:
    sysBP = st.number_input("Systolic BP", 80, 300, 130)
    diaBP = st.number_input("Diastolic BP", 40, 150, 80)
    BMI = st.number_input("BMI", 10.0, 60.0, 25.0)
    heartRate = st.number_input("Heart Rate", 40, 150, 75)
    glucose = st.number_input("Glucose Level", 40, 500, 80)

# 5. Prediction Logic
# Create a DataFrame with the exact column names the model was trained on
input_data = pd.DataFrame([[
    male, age, education, currentSmoker, cigsPerDay, BPMeds, 
    prevalentStroke, prevalentHyp, diabetes, totChol, sysBP, 
    diaBP, BMI, heartRate, glucose
]], columns=['male', 'age', 'education', 'currentSmoker', 'cigsPerDay', 'BPMeds', 
             'prevalentStroke', 'prevalentHyp', 'diabetes', 'totChol', 'sysBP', 
             'diaBP', 'BMI', 'heartRate', 'glucose'])

st.write("---")
if st.button("Analyze Heart Health Risk"):
    # Get prediction and probability
    prediction = model.predict(input_data)[0]
    probability = model.predict_proba(input_data)[0][1] * 100

    # Display Results
    if prediction == 1:
        st.error(f"⚠️ **High Risk:** There is a {probability:.1f}% chance of CHD in the next 10 years.")
        st.write("Recommendation: Consult a healthcare professional for a detailed cardiovascular screening.")
    else:
        st.success(f"✅ **Low Risk:** There is only a {probability:.1f}% chance of CHD in the next 10 years.")
        st.write("Recommendation: Maintain a healthy lifestyle and regular checkups.")

# Footer
st.info("Disclaimer: This is a student project for educational purposes and not a substitute for professional medical advice.")