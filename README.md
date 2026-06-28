# fraud-detection-financial-transactions
Anomaly detection project to identify fraudulent financial transactions using machine learning.
# 🚨 Fraud Detection in Financial Transactions

## 📌 Overview

This project focuses on detecting fraudulent financial transactions using machine learning techniques. It applies anomaly detection algorithms to identify suspicious activities in highly imbalanced datasets.

---

## 🎯 Objective

* Detect fraudulent transactions from anonymized financial data
* Handle class imbalance effectively
* Build an anomaly detection model
* Develop a real-time alert dashboard

---

## 📊 Dataset

* Anonymized dataset with features: `A1 – A14`
* Target variable: `Class`

  * `0` → Normal Transaction
  * `1` → Fraudulent Transaction

---

## ⚙️ Technologies Used

* Python
* Pandas, NumPy
* Scikit-learn
* Imbalanced-learn (SMOTE)
* Streamlit

---

## 🔍 Methodology

### 1. Data Preprocessing

* Removed irrelevant columns (e.g., CustomerID)
* Checked missing values
* Performed feature scaling using StandardScaler

### 2. Handling Class Imbalance

* Applied SMOTE (Synthetic Minority Oversampling Technique)
* Balanced fraud and normal transaction classes

### 3. Model Building

* Used Isolation Forest for anomaly detection
* Trained model on balanced dataset

### 4. Evaluation

* Used:

  * Precision
  * Recall
  * F1-score
  * Confusion Matrix

### 5. Dashboard Development

* Built an interactive dashboard using Streamlit
* Features:

  * Upload dataset
  * View predictions
  * Fraud alert system

---

## 📊 Results

* Successfully detected anomalous transactions
* Improved fraud detection using imbalance handling
* Built a real-time fraud alert interface

---

## 🚀 How to Run

```bash
pip install -r requirements.txt
streamlit run dashboard/app.py
```

---

## 📁 Project Structure

```
fraud-detection-financial-transactions/
│── data/
│── notebooks/
│── src/
│── dashboard/
│   └── app.py
│── README.md
```

---

## 📌 Key Learnings

* Handling imbalanced datasets is critical in fraud detection
* Anomaly detection models are effective for rare events
* Visualization and dashboards improve real-world usability

---

## 👨‍💻 Author

**Kountik Das**
