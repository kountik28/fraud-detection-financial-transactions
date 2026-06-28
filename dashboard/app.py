import streamlit as st
import pandas as pd
import numpy as np
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler

st.set_page_config(page_title="Fraud Detection Dashboard", layout="wide")

st.title("🚨 Fraud Detection Dashboard")

# Upload dataset
uploaded_file = st.file_uploader("Upload Transaction CSV", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)

    st.subheader("📊 Raw Data")
    st.write(df.head())

    # Drop ID if exists
    if 'CustomerID' in df.columns:
        df = df.drop('CustomerID', axis=1)

    # Separate features
    if 'Class' in df.columns:
        X = df.drop('Class', axis=1)
    else:
        X = df.copy()

    # Scaling
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    # Train model (simple version for dashboard)
    model = IsolationForest(contamination=0.02, random_state=42)
    model.fit(X_scaled)

    # Predict
    preds = model.predict(X_scaled)
    preds = np.where(preds == -1, 1, 0)

    df['Fraud_Prediction'] = preds

    st.subheader("🔍 Prediction Results")
    st.write(df.head())

    # Fraud Alerts
    fraud_cases = df[df['Fraud_Prediction'] == 1]

    st.subheader("🚨 Fraud Alerts")
    st.write(fraud_cases)

    st.write("Total Fraud Detected:", len(fraud_cases))