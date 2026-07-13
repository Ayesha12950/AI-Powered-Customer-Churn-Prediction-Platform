import streamlit as st
import pickle
import numpy as np
import pandas as pd
import plotly.express as px

# PAGE CONFIG
st.set_page_config(
    page_title="AI Banking Dashboard",
    layout="wide"
)

# LOAD MODEL
model = pickle.load(
    open('xgboost_model.pkl', 'rb')
)

# LOAD SCALER
scaler = pickle.load(
    open('scaler.pkl', 'rb')
)

# CUSTOM CSS
st.markdown("""
<style>

.main {
    background-color: #0E1117;
    color: white;
}

.stMetric {
    background-color: #1E1E1E;
    padding: 15px;
    border-radius: 10px;
}

div[data-testid="stSidebar"] {
    background-color: #111827;
}

</style>
""", unsafe_allow_html=True)

# SIDEBAR
st.sidebar.title("🏦 AI Banking Analytics")

st.sidebar.info(
    """
    Enterprise AI Platform

    Features:
    • Churn Prediction
    • Risk Intelligence
    • KPI Analytics
    • AI Insights
    """
)

# TITLE
st.title("🤖 AI-Powered Customer Retention Intelligence Platform")

st.markdown("---")

# KPI SECTION
col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Customers",
    "10,000"
)

col2.metric(
    "Churn Rate",
    "20.4%"
)

col3.metric(
    "AI Accuracy",
    "88%"
)

col4.metric(
    "Revenue Risk",
    "$2.1M"
)

st.markdown("---")

# CHARTS SECTION

chart_col1, chart_col2 = st.columns(2)

# PIE CHART
pie_data = pd.DataFrame({
    'Category': ['Retained', 'Churned'],
    'Count': [8000, 2000]
})

fig1 = px.pie(
    pie_data,
    names='Category',
    values='Count',
    title='Customer Retention Distribution',
    hole=0.5
)

chart_col1.plotly_chart(
    fig1,
    use_container_width=True
)

# BAR CHART
bar_data = pd.DataFrame({
    'Region': ['France', 'Germany', 'Spain'],
    'Churn': [810, 814, 413]
})

fig2 = px.bar(
    bar_data,
    x='Region',
    y='Churn',
    title='Geography-wise Churn Analysis'
)

chart_col2.plotly_chart(
    fig2,
    use_container_width=True
)

st.markdown("---")

# AI PREDICTION SECTION

st.subheader("🔍 Real-Time AI Churn Prediction")

input_col1, input_col2, input_col3 = st.columns(3)

with input_col1:

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

with input_col2:

    tenure = st.number_input(
        "Tenure",
        0,
        10
    )

    balance = st.number_input(
        "Balance"
    )

with input_col3:

    products = st.number_input(
        "Products",
        1,
        4
    )

    salary = st.number_input(
        "Estimated Salary"
    )

# BUTTON
if st.button("🚀 Run AI Analysis"):

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

    st.markdown("---")

    if prediction[0] == 1:

        st.error(
            "⚠️ HIGH CHURN RISK CUSTOMER"
        )

        st.write(
            "AI Insight: Immediate customer retention strategy recommended."
        )

    else:

        st.success(
            "✅ LOW CHURN RISK CUSTOMER"
        )

        st.write(
            "AI Insight: Customer retention probability is high."
        )

# AI BUSINESS INSIGHTS
st.markdown("---")

st.subheader("📈 AI Business Intelligence Insights")

insight_col1, insight_col2 = st.columns(2)

with insight_col1:

    st.info(
        """
        • Germany shows highest churn rate

        • Older customers have increased churn risk

        • Inactive users require retention campaigns
        """
    )

with insight_col2:

    st.warning(
        """
        • High balance customers need loyalty rewards

        • Improve customer engagement programs

        • Optimize banking relationship management
        """
    )