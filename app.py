import streamlit as st
import numpy as np
import pickle

# Set page config for a professional look
st.set_page_config(page_title="Loan Status Predictor", page_icon="💰", layout="centered")

# Load the trained model safely
@st.cache_resource
def load_model():
    with open('loan_status_model.pkl', 'rb') as file:
        return pickle.load(file)

try:
    model = load_model()
except FileNotFoundError:
    st.error("Model file 'loan_status_model.pkl' not found. Please run your model saving code first.")
    st.stop()

# --- WEB PAGE UI ---
st.title("💰 Smart Loan Eligibility Predictor")
st.write("Fill out the quick profile assessment below to check your loan status eligibility instantly.")
st.markdown("---")

col1, col2 = st.columns(2)

with col1:
    gender = st.selectbox("Gender", options=["Male", "Female"])
    married = st.selectbox("Marital Status", options=["Married", "Unmarried/Single"])
    dependents = st.selectbox("Number of Dependents", options=["0", "1", "2", "3+"])
    education = st.selectbox("Education Level", options=["Graduate", "Not Graduate"])
    self_employed = st.selectbox("Self Employed?", options=["No", "Yes"])

with col2:
    applicant_income = st.number_input("Applicant Monthly Income ($)", min_value=0, value=3000, step=100)
    coapplicant_income = st.number_input("Co-applicant Monthly Income ($)", min_value=0, value=0, step=100)
    loan_amount = st.number_input("Desired Loan Amount (in thousands, e.g., 120 = $120,000)", min_value=1, value=120)
    loan_term = st.number_input("Loan Term (in days, e.g., 360 = 1 Year)", min_value=12, value=360, step=12)
    credit_history = st.selectbox("Credit History Guidelines Met?", options=["Yes (Good Credit Score)", "No (Poor/No Credit History)"])
    property_area = st.selectbox("Property Area Location", options=["Rural", "Semiurban", "Urban"])

st.markdown("---")

# --- CONVERTING APPLICANT SELECTIONS TO NUMERICAL VALUES ---
gender_val = 1 if gender == "Male" else 0
married_val = 1 if married == "Married" else 0
education_val = 1 if education == "Graduate" else 0
self_employed_val = 1 if self_employed == "Yes" else 0

if dependents == "3+":
    dependents_val = 4  
else:
    dependents_val = int(dependents)

credit_history_val = 1.0 if credit_history == "Yes (Good Credit Score)" else 0.0

area_mapping = {"Rural": 0, "Semiurban": 1, "Urban": 2}
property_area_val = area_mapping[property_area]

# --- PREDICTION ENGINE ---
if st.button("Analyze Loan Eligibility", type="primary", use_container_width=True):
    features = np.array([[
        gender_val, married_val, dependents_val, education_val, self_employed_val,
        applicant_income, coapplicant_income, loan_amount, loan_term,
        credit_history_val, property_area_val
    ]])
    
    prediction = model.predict(features)
    
    if prediction[0] == 1:
        st.success("🎉 **Congratulations!** Based on your financial parameters, your loan request profile is **APPROVED**.")
    else:
        st.error("🚫 **Loan Profile Notice:** Based on the submitted markers, your loan application does not meet requirement criteria at this time.")
