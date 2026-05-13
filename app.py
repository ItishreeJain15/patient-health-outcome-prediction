import streamlit as st
import pickle
import pandas as pd

# Load trained model
model = pickle.load(open("medical_model.pkl", "rb"))

# Page Configuration
st.set_page_config(
    page_title="Patient Health Outcome Prediction",
    page_icon="🩺",
    layout="centered"
)

# Custom CSS Styling
st.markdown("""
<style>

.stApp {
    background: linear-gradient(to right, #0f172a, #1e3a8a, #2563eb);
    color: white;
}

/* Main Glass Container */
.main-container {
    background: rgba(255, 255, 255, 0.12);
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
    font-size: 42px;
}

/* Labels */
label {
    color: white !important;
    font-weight: 600 !important;
    font-size: 16px !important;
}

.stSelectbox label,
.stSlider label {
    color: white !important;
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

/* Positive Result */
.result-positive {
    background-color: rgba(239, 68, 68, 0.2);
    padding: 20px;
    border-radius: 15px;
    text-align: center;
    font-size: 24px;
    font-weight: bold;
    color: #fecaca;
    margin-top: 20px;
}

/* Negative Result */
.result-negative {
    background-color: rgba(34, 197, 94, 0.2);
    padding: 20px;
    border-radius: 15px;
    text-align: center;
    font-size: 24px;
    font-weight: bold;
    color: #bbf7d0;
    margin-top: 20px;
}

/* Footer */
.footer {
    text-align: center;
    color: #e2e8f0;
    margin-top: 25px;
    font-size: 14px;
}

</style>
""", unsafe_allow_html=True)

# Main Container Start
st.markdown('<div class="main-container">', unsafe_allow_html=True)

# Title
st.title("🩺 Patient Health Outcome Prediction")

st.write(
    "This AI-powered healthcare system predicts patient health outcomes "
    "using symptoms and medical profile information."
)

# Input Fields
fever = st.selectbox("🌡 Fever", ["Yes", "No"])

cough = st.selectbox("😷 Cough", ["Yes", "No"])

fatigue = st.selectbox("😴 Fatigue", ["Yes", "No"])

breathing = st.selectbox("🫁 Difficulty Breathing", ["Yes", "No"])

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

# Input Data Formatting
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

# Prediction
if st.button("Predict Health Outcome"):

    prediction = model.predict(input_df)

    if prediction[0] == 1:

        st.markdown(
            '<div class="result-positive">⚠ Positive Health Outcome Detected</div>',
            unsafe_allow_html=True
        )

        st.warning(
            "The patient may require medical attention. "
            "Please consult a healthcare professional."
        )

    else:

        st.markdown(
            '<div class="result-negative">✅ Negative Health Outcome</div>',
            unsafe_allow_html=True
        )

        st.success(
            "The patient condition appears stable "
            "based on the provided information."
        )

# End Container
st.markdown("</div>", unsafe_allow_html=True)

# Footer
st.markdown(
    '<div class="footer">⚠ This system is for educational purposes only and does not replace professional medical advice.</div>',
    unsafe_allow_html=True
)