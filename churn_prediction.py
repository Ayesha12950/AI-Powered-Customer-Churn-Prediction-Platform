import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split

from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler

from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix
)

from xgboost import XGBClassifier

import pickle


# LOAD DATASET
df = pd.read_csv("Churn_Modelling.csv")


# VIEW DATA
print(df.head())


# DATASET INFO
print(df.info())


# NULL VALUES
print(df.isnull().sum())


# REMOVE COLUMNS
df = df.drop(
    ['RowNumber',
     'CustomerId',
     'Surname'],
    axis=1
)


# KPI ANALYTICS
print("Total Customers:", len(df))

print(df['Exited'].value_counts())


# CHURN VISUALIZATION
plt.figure(figsize=(6,4))

sns.countplot(
    x='Exited',
    data=df
)

plt.title("Customer Churn Distribution")

plt.show()


# ENCODE DATA
le_gender = LabelEncoder()

df['Gender'] = le_gender.fit_transform(
    df['Gender']
)

df = pd.get_dummies(
    df,
    columns=['Geography'],
    drop_first=True
)


# FEATURES & TARGET
X = df.drop('Exited', axis=1)

y = df['Exited']


# SCALING
scaler = StandardScaler()

X_scaled = scaler.fit_transform(X)


# TRAIN TEST SPLIT
X_train, X_test, y_train, y_test = train_test_split(
    X_scaled,
    y,
    test_size=0.2,
    random_state=42
)


# XGBOOST MODEL
model = XGBClassifier()

model.fit(X_train, y_train)


# PREDICTION
y_pred = model.predict(X_test)


# ACCURACY
accuracy = accuracy_score(
    y_test,
    y_pred
)

print("AI Model Accuracy:", accuracy)


# CLASSIFICATION REPORT
print(classification_report(
    y_test,
    y_pred
))


# CONFUSION MATRIX
cm = confusion_matrix(
    y_test,
    y_pred
)

plt.figure(figsize=(6,5))

sns.heatmap(
    cm,
    annot=True,
    fmt='d',
    cmap='Blues'
)

plt.title("AI Churn Prediction Matrix")

plt.xlabel("Predicted")

plt.ylabel("Actual")

plt.show()


# SAVE MODEL
pickle.dump(
    model,
    open('xgboost_model.pkl', 'wb')
)

pickle.dump(
    scaler,
    open('scaler.pkl', 'wb')
)

print("AI Model Saved Successfully")