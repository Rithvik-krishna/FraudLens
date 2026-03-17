# FraudLens — Banking Fraud Detection using Anomaly Detection

## 🔍 Overview

FraudLens is an applied data science project designed to detect fraudulent transactions using anomaly detection and machine learning techniques. The system analyzes transaction data, identifies suspicious patterns, and presents insights through an interactive web application.

---

## 🚨 Problem Statement

Banking fraud is difficult to detect due to:

* Extremely imbalanced data (~0.17% fraud)
* Hidden behavioral patterns in transactions
* Limitations of rule-based detection systems

FraudLens addresses this by using anomaly detection and data-driven insights.

---

## 📊 Dataset

* **Source:** Credit Card Fraud Detection Dataset
* **Transactions:** 284,807
* **Features:** 31
* **Fraud Rate:** ~0.17%

## Dataset Note

Due to GitHub file size limitations, the dataset is not included in this repository.

You can download it from:
https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud

After downloading:
- Place `creditcard.csv` inside `raw_data/`
- Run the notebook to generate `cleaned.csv`

### Features:

* `Time` — seconds elapsed
* `Amount` — transaction value
* `V1–V28` — PCA-transformed features
* `Fraud` — target variable (0 = normal, 1 = fraud)

---

## ⚙️ Approach

### 1. Data Cleaning

* Checked for missing values and duplicates
* Verified dataset integrity

### 2. Feature Engineering

* Converted `Time` → `Hour`
* Scaled `Amount` using StandardScaler

### 3. Exploratory Data Analysis

* Class imbalance visualization
* Transaction amount distribution
* Fraud patterns over time
* Feature correlations

### 4. Models Used

* **Isolation Forest** (Anomaly Detection)
* **Logistic Regression** (Baseline)
* **Random Forest** (Best performer)

---

## 📈 Key Results

| Model                | Precision | Recall | F1 Score |
|---------------------|----------|--------|----------|
| Isolation Forest     | 0.12     | 0.12   | 0.12     |
| Logistic Regression | 0.87     | 0.50   | 0.63     |
| Random Forest        | 0.99     | 0.73   | 0.84     |

### Best Model: Random Forest
- **Recall:** 73.33%
- **Precision:** 98.51%
- **F1 Score:** 0.84

### Key Observation
Random Forest provides the best balance between precision and recall, making it the most effective model for fraud detection in this project.

### Why Recall Matters

Missing a fraudulent transaction (false negative) is more costly than falsely flagging a normal one.

---

## 🌐 Web Application

An interactive dashboard built using Streamlit to:

* Display dataset insights
* Visualize fraud patterns
* Compare model performance

---

## 🧠 Business Insights

* Fraud occurs even at small transaction amounts (card testing behavior)
* Fraud shows time-based irregularities
* Hidden patterns exist despite anonymized features
* High recall is critical for effective fraud detection

---

## ⚠️ Limitations

* Dataset is anonymized (V1–V28)
* Highly imbalanced data
* No real-time processing
* Limited user behavioral history

---

## 🚀 How to Run

### 1. Clone the repository

```
git clone <your-repo-link>
cd FraudLens
```

### 2. Install dependencies

```
pip install -r requirements.txt
```

### 3. Run the web app

```
cd website
streamlit run app.py
```

---

## 📁 Project Structure

```
FraudLens/
│
├── raw_data/
│   └── creditcard.csv
│
├── processed_data/
│   └── cleaned.csv
│
├── notebooks/
│   └── 01_data_understanding.ipynb
│
├── output/
│   ├── class_distribution.png
│   ├── amount_boxplot.png
│   ├── fraud_by_hour.png
│   ├── correlation_heatmap.png
│   ├── anomaly_scores.png
│   └── model_comparison.csv
│
├── website/
│   └── app.py
│
└── README.md
```

---

## 🎯 Conclusion

FraudLens demonstrates how anomaly detection and machine learning can be used to uncover hidden fraud patterns in highly imbalanced datasets, enabling better financial risk management.

---

## 👨‍💻 Author

Rithvik Krishna D K
