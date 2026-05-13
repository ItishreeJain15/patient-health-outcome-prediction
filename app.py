import streamlit as st
import pickle
import pandas as pd

# Load Model
model = pickle.load(open("medical_model.pkl", "rb"))

# Page Config
st.set_page_config(
    page_title="Advanced Health Prediction System",
    page_icon="🩺",
    layout="centered"
)

# Custom CSS
st.markdown("""
<style>

.stApp {
    background: linear-gradient(to right, #0f172a, #1e3a8a, #2563eb);
    color: white;
}

/* Main Card */
.main-container {
    background: rgba(255,255,255,0.12);
    padding: 35px;
    border-radius: 20px;
    backdrop-filter: blur(12px);
    box-shadow: 0px 8px 32px rgba(0,0,0,0.3);
    margin-top: 20px;
}

/* Title */
h1 {
    text-align: center;
    color: white;
    font-size: 40px;
}

/* Labels */
label {
    color: white !important;
    font-weight: 600 !important;
    font-size: 16px !important;
}

/* Button */
.stButton>button {
    width: 100%;
    background-color: #22c55e;
    color: white;
    font-size: 18px;
    border-radius: 12px;
    height: 3em;
    border: none;
    font-weight: bold;
    transition: 0.3s;
}

.stButton>button:hover {
    background-color: #16a34a;
    transform: scale(1.02);
}

/* Result Cards */
.result-high {
    background-color: rgba(239,68,68,0.2);
    padding: 20px;
    border-radius: 15px;
    color: #fecaca;
    text-align: center;
    font-size: 24px;
    font-weight: bold;
    margin-top: 20px;
}

.result-low {
    background-color: rgba(34,197,94,0.2);
    padding: 20px;
    border-radius: 15px;
    color: #bbf7d0;
    text-align: center;
    font-size: 24px;
    font-weight: bold;
    margin-top: 20px;
}

.footer {
    text-align: center;
    color: #e2e8f0;
    margin-top: 20px;
    font-size: 14px;
}

</style>
""", unsafe_allow_html=True)

# Main Container
st.markdown('<div class="main-container">', unsafe_allow_html=True)

# Title
st.title("🩺 Advanced Health Prediction System")

st.write(
    "AI-powered healthcare assistant that predicts patient health outcomes "
    "using symptoms and medical profile information."
)

# Symptoms Section
st.subheader("🧾 Patient Symptoms")

fever = st.selectbox("🌡 Fever", ["Yes", "No"])
cough = st.selectbox("😷 Cough", ["Yes", "No"])
fatigue = st.selectbox("😴 Fatigue", ["Yes", "No"])
breathing = st.selectbox("🫁 Difficulty Breathing", ["Yes", "No"])

# Additional Symptoms (UI Enhancement)
headache = st.selectbox("🤕 Headache", ["Yes", "No"])
chest_pain = st.selectbox("❤️ Chest Pain", ["Yes", "No"])
body_pain = st.selectbox("🦴 Body Pain", ["Yes", "No"])

# Patient Information
st.subheader("👤 Patient Information")

age = st.slider("🎂 Age", 1, 100, 25)

gender = st.selectbox("👤 Gender", ["Male", "Female"])

blood_pressure = st.selectbox(
    "🩸 Blood Pressure",
    ["Low", "Normal", "High"]
)

cholesterol = st.selectbox(
    "🧪 Cholesterol Level",
    ["Low", "Normal", "High"]
)

# BMI Calculator
st.subheader("⚖ BMI Calculator")

height = st.number_input("📏 Height (in meters)", 1.0, 2.5, 1.7)

weight = st.number_input("🏋 Weight (in kg)", 20, 200, 65)

bmi = weight / (height ** 2)

st.info(f"Your BMI is: {bmi:.2f}")

# Input Data
input_data = {
    'Age': age,

    'Fever_Yes': 1 if fever == "Yes" else 0,
    'Cough_Yes': 1 if cough == "Yes" else 0,
    'Fatigue_Yes': 1 if fatigue == "Yes" else 0,
    'Difficulty Breathing_Yes': 1 if breathing == "Yes" else 0,

    'Gender_Male': 1 if gender == "Male" else 0,

    'Blood Pressure_Low': 1 if blood_pressure == "Low" else 0,
    'Blood Pressure_Normal': 1 if blood_pressure == "Normal" else 0,

    'Cholesterol Level_Low': 1 if cholesterol == "Low" else 0,
    'Cholesterol Level_Normal': 1 if cholesterol == "Normal" else 0,
}

input_df = pd.DataFrame([input_data])

# Prediction Button
if st.button("Predict Health Outcome"):

    prediction = model.predict(input_df)

    probability = model.predict_proba(input_df)[0][1] * 100

    # High Risk
    if prediction[0] == 1:

        st.markdown(
            f'<div class="result-high">⚠ High Health Risk Detected<br><br>Risk Probability: {probability:.2f}%</div>',
            unsafe_allow_html=True
        )

        st.warning(
            "The patient may require medical attention. "
            "Please consult a healthcare professional."
        )

        st.subheader("💡 Health Recommendations")

        st.write("✔ Monitor symptoms regularly")
        st.write("✔ Maintain proper hydration")
        st.write("✔ Take sufficient rest")
        st.write("✔ Consult a medical specialist")

    # Low Risk
    else:

        st.markdown(
            f'<div class="result-low">✅ Low Health Risk<br><br>Risk Probability: {100 - probability:.2f}%</div>',
            unsafe_allow_html=True
        )

        st.success(
            "The patient condition appears stable "
            "based on the provided information."
        )

        st.subheader("💡 Health Recommendations")

        st.write("✔ Maintain healthy diet")
        st.write("✔ Exercise regularly")
        st.write("✔ Stay hydrated")
        st.write("✔ Continue healthy lifestyle")

# Close Main Container
st.markdown("</div>", unsafe_allow_html=True)

# Footer
st.markdown(
    '<div class="footer">⚠ This system is for educational purposes only and does not replace professional medical advice.</div>',
    unsafe_allow_html=True
)