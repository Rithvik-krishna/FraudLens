import streamlit as st
import pandas as pd
import os

# -------------------- PAGE CONFIG --------------------
st.set_page_config(
    page_title="FraudLens",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -------------------- LOAD DATA --------------------
@st.cache_data
def load_data():
    try:
        url = "https://drive.google.com/uc?id=1Qunc39H0nwcuMEq-CTtRvko3mwvoNZUS"
        df = pd.read_csv(url)

        # Fix column name
        if 'Class' in df.columns:
            df.rename(columns={'Class': 'Fraud'}, inplace=True)

        return df
    except Exception as e:
        return None

df = load_data()

# -------------------- SIDEBAR --------------------
st.sidebar.title("FraudLens")
st.sidebar.markdown("Fraud Detection Dashboard")

page = st.sidebar.radio(
    "Navigate",
    ["Home", "Data Overview", "Analysis", "Insights", "Conclusion"]
)

# -------------------- HELPER --------------------
def show_image(path, title):
    st.write(f"### {title}")
    if os.path.exists(path):
        st.image(path, use_container_width=True)
    else:
        st.warning(f"{title} not available")

# -------------------- HOME --------------------
if page == "Home":
    st.title("FraudLens")
    st.subheader("Banking Fraud Detection using Anomaly Detection")
    st.divider()

    st.markdown("""
    ### 💼 Business Context
    Every ₹1Cr in transactions has ~₹17K fraud.

    Fraud is rare but financially significant, making early detection critical.

    ### ⚠️ Problem
    Fraud patterns are hidden in massive transaction data and cannot be detected using simple rules.

    ### 💡 Solution
    FraudLens uses data analysis and anomaly detection techniques to identify suspicious transactions.

    ### 🎯 Goal
    Detect unusual behavior early and reduce financial risk.
    """)

# -------------------- DATA OVERVIEW --------------------
elif page == "Data Overview":
    st.title("Data Overview")
    st.divider()

    if df is None:
        st.error("Dataset failed to load. Check internet or Google Drive link.")
    else:
        fraud_count = int(df['Fraud'].sum())
        total = len(df)
        fraud_percent = (fraud_count / total) * 100

        col1, col2, col3 = st.columns(3)
        col1.metric("Total Transactions", f"{total:,}")
        col2.metric("Fraud Cases", f"{fraud_count:,}")
        col3.metric("Fraud %", f"{fraud_percent:.4f}%")

        st.divider()

        st.write("### Dataset Preview")
        st.dataframe(df.head())

        st.write("### Class Distribution")
        st.bar_chart(df['Fraud'].value_counts())

# -------------------- ANALYSIS --------------------
elif page == "Analysis":
    st.title("Exploratory Analysis")
    st.divider()

    show_image("output/amount_boxplot.png", "Transaction Amount Distribution")
    show_image("output/class_distribution.png", "Fraud Distribution")
    show_image("output/fraud_by_hour.png", "Fraud by Hour")
    show_image("output/correlation_heatmap.png", "Feature Correlation")

# -------------------- INSIGHTS --------------------
elif page == "Insights":
    st.title("Key Insights")
    st.divider()

    st.markdown("""
    ### 1. Fraud is Rare but High Impact
    Only ~0.17% of transactions are fraudulent.
    """)
    show_image("output/class_distribution.png", "Class Distribution")

    st.markdown("""
    ### 2. Fraud Occurs at Small Amounts
    Indicates card testing behavior.
    """)
    show_image("output/amount_boxplot.png", "Amount Distribution")

    st.markdown("""
    ### 3. Time-Based Fraud Patterns
    Fraud occurs during specific hours.
    """)
    show_image("output/fraud_by_hour.png", "Fraud by Hour")

    st.markdown("""
    ### 4. Hidden Feature Patterns
    Certain features strongly correlate with fraud.
    """)
    show_image("output/correlation_heatmap.png", "Correlation Heatmap")

    st.markdown("""
    ### 5. Model Performance
    Random Forest performs best with strong recall and precision.
    """)

    try:
        comparison = pd.read_csv("output/model_comparison.csv")
        st.dataframe(comparison)
    except:
        st.warning("Model comparison file not found")

# -------------------- CONCLUSION --------------------
elif page == "Conclusion":
    st.title("Conclusion & Recommendations")
    st.divider()

    st.markdown("""
    ### ✅ Key Takeaways
    - Fraud detection requires anomaly-based approaches  
    - Fraud patterns are subtle and not rule-based  
    - High recall is critical for minimizing loss  

    ### 💼 Business Recommendations
    - Implement real-time anomaly detection systems  
    - Monitor low-value transactions for card testing  
    - Use ensemble models like Random Forest  

    ### ⚠️ Limitations
    - Dataset is anonymized (V1–V28)  
    - Highly imbalanced data  
    - No real-time system implemented  

    ### 🚀 Next Steps
    - Deploy real-time fraud detection  
    - Integrate user behavior tracking  
    - Improve model tuning and features  
    """)