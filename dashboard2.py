import streamlit as st
import pickle
import numpy as np

# Load AI model
model = pickle.load(
    open('xgboost_model.pkl', 'rb')
)

# Load scaler
scaler = pickle.load(
    open('scaler.pkl', 'rb')
)

# TITLE
st.title(
    "🏦 AI Banking Customer Retention Platform"
)

st.subheader(
    "Real-Time Customer Churn Intelligence"
)

# SIDEBAR
st.sidebar.title("AI Analytics Dashboard")

st.sidebar.info(
    """
    Enterprise Banking AI System

    Features:
    • Churn Prediction
    • Risk Analytics
    • Retention Intelligence
    """
)

# INPUTS
credit_score = st.number_input(
    "Credit Score",
    300,
    900
)

age = st.number_input(
    "Age",
    18,
    100
)

tenure = st.number_input(
    "Tenure",
    0,
    10
)

balance = st.number_input(
    "Balance"
)

products = st.number_input(
    "Number of Products",
    1,
    4
)

salary = st.number_input(
    "Estimated Salary"
)

# BUTTON
if st.button("Run AI Churn Analysis"):

    data = np.array([[
        credit_score,
        1,
        age,
        tenure,
        balance,
        products,
        1,
        1,
        salary,
        0,
        1
    ]])

    scaled_data = scaler.transform(data)

    prediction = model.predict(scaled_data)

    if prediction[0] == 1:

        st.error(
            "⚠️ High Churn Risk Customer"
        )

        st.write(
            "AI Recommendation: Immediate retention action required."
        )

    else:

        st.success(
            "✅ Low Churn Risk Customer"
        )

        st.write(
            "AI Insight: Customer retention probability is high."
        )

# KPI SECTION
st.subheader("Executive AI KPIs")

col1, col2, col3 = st.columns(3)

col1.metric(
    "AI Accuracy",
    "88%"
)

col2.metric(
    "Prediction Engine",
    "XGBoost AI"
)

col3.metric(
    "Analytics Type",
    "Real-Time"
)