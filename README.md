%%writefile README.md
# 💰 Smart Loan Eligibility Predictor

An interactive, end-to-end Machine Learning web application that predicts loan approval eligibility based on an applicant's financial and personal profile. Built using **Python**, **Scikit-Learn**, and **Streamlit**, this dashboard features a modern glassmorphism UI.

## 🚀 Live Demo
https://loanstatusprediction-5ify4giwbayzv6gwivdkdm.streamlit.app/

---

## 📊 Project Overview
Predicting loan eligibility manually is time-consuming and prone to human error. This project uses historical loan data to train a Support Vector Machine (SVM) classifier that instantly assesses an applicant's profile to predict whether a loan will be **Approved** or **Rejected**.

### Features Used for Prediction:
* **Applicant Profile:** Gender, Marital Status, Education Level, Dependents, Self-Employment status.
* **Financial Data:** Applicant Income, Co-applicant Income, Requested Loan Amount, Loan Term.
* **Credit History & Location:** Credit history guidelines met (Yes/No), Property Area (Rural, Semiurban, Urban).

---

## 🛠️ Tech Stack & Architecture

* **Frontend Dashboard:** [Streamlit](https://streamlit.io/) (with customized transparent CSS styling)
* **Machine Learning Framework:** [Scikit-Learn](https://scikit-learn.org/)
* **Model Pipeline:** Support Vector Machine (SVM) with a Linear Kernel
* **Deployment:** Streamlit Community Cloud

---

## 📁 Repository Structure

```text
├── app.py                  # Streamlit web application source code
├── loan_status_model.pkl   # Pre-trained SVM model (Pickle format)
├── requirements.txt        # System dependencies for deployment
└── README.md               # Project documentation
