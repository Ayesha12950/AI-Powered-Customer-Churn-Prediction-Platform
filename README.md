# AI-Powered-Customer-Churn-Prediction-Platform
AI-powered customer churn prediction using XGBoost, Streamlit, and Power BI

# AI-Powered Customer Churn Prediction Platform

An AI-powered customer churn prediction platform that helps businesses identify customers who are likely to leave. The project combines Machine Learning (XGBoost), Streamlit, and Power BI to provide accurate predictions and interactive business insights.

---

## Project Overview

Customer churn is one of the biggest challenges for businesses. This project predicts whether a customer is likely to churn based on customer information such as age, balance, geography, tenure, credit score, and other banking features.

The system includes:
- Machine Learning model for churn prediction
- Interactive Streamlit web application
- Power BI dashboards for business analytics
- Data preprocessing and visualization

---

## Features

- Customer churn prediction using XGBoost
- Interactive Streamlit dashboard
- Power BI analytics dashboard
- Data preprocessing and feature scaling
- Model saved using Pickle
- User-friendly prediction interface
- Business insights through visualizations

---

## Technologies Used

| Technology | Purpose |
|------------|----------|
| Python | Programming Language |
| Pandas | Data Processing |
| NumPy | Numerical Operations |
| Scikit-learn | Data Preprocessing |
| XGBoost | Machine Learning Model |
| Streamlit | Web Application |
| Power BI | Business Dashboard |
| Pickle | Model Saving |

---

## Dataset

**Dataset Name:** Bank Customer Churn Dataset

The dataset contains customer information such as:

- Credit Score
- Geography
- Gender
- Age
- Tenure
- Balance
- Number of Products
- Has Credit Card
- Is Active Member
- Estimated Salary
- Exited (Target Variable)

Target Variable:

- **Exited**
  - 0 = Customer Stayed
  - 1 = Customer Churned

---

## Project Structure

```
AI-Powered-Customer-Churn-Prediction-Platform/
│
├── Churn_Modelling.csv
├── churn_prediction.py
├── dashboard2.py
├── dashboard3.py
├── xgboost_model.pkl
├── scaler.pkl
├── AI Powered Customer Churn Prediction.pbix
├── Untitled.ipynb
├── README.md
```

---

## Machine Learning Workflow

1. Data Collection
2. Data Cleaning
3. Data Preprocessing
4. Feature Scaling
5. Train-Test Split
6. XGBoost Model Training
7. Model Evaluation
8. Save Model
9. Predict Customer Churn
10. Display Results in Streamlit

---

## Power BI Dashboard

The Power BI dashboard provides:

- Customer Distribution
- Churn Analysis
- Balance Analysis
- Age Distribution
- Credit Score Analysis
- Geography-wise Churn
- Gender-wise Churn
- KPI Cards
- Interactive Filters and Slicers

---

## Streamlit Dashboard

The Streamlit application allows users to:

- Enter customer details
- Predict customer churn instantly
- View prediction results
- Display probability of churn
- Easy-to-use interface

---

## Model Used

**XGBoost Classifier**

Reasons for choosing XGBoost:

- High prediction accuracy
- Handles large datasets efficiently
- Prevents overfitting
- Fast training
- Excellent performance for classification tasks

---

## How to Run

### 1. Clone Repository

```bash
git clone https://github.com/Ayesha12950/AI-Powered-Customer-Churn-Prediction-Platform.git
```

### 2. Install Dependencies

```bash
pip install pandas numpy scikit-learn streamlit xgboost joblib
```

### 3. Run Streamlit App

```bash
streamlit run churn_prediction.py
```

---

## Results

- Accurate customer churn prediction
- Interactive business dashboard
- Easy-to-use prediction system
- Better customer retention insights
- Data-driven decision making

---

## Future Improvements

- Deploy on Streamlit Cloud
- Connect with real-time database
- Add Deep Learning models
- Email alerts for high-risk customers
- REST API integration
- Improve dashboard with additional KPIs

---

## Author

**Ayesha Javed Shaikh**

MCA Student | Data Analytics | Machine Learning | Power BI | Python

GitHub: https://github.com/Ayesha12950

---

## License

This project is developed for educational and learning purposes.
