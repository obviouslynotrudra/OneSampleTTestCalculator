import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.preprocessing import LabelEncoder

# ---------------------------------
# App Title
# ---------------------------------
st.set_page_config(page_title="Naive Bayes Classifier", layout="centered")
st.title("🧠 Naive Bayes Classifier (Scikit-Learn)")
st.write("Upload a CSV dataset, train a Gaussian Naive Bayes model, and evaluate performance.")

# ---------------------------------
# File Upload
# ---------------------------------
uploaded_file = st.file_uploader("📂 Upload CSV File", type=["csv"])

if uploaded_file is not None:

    df = pd.read_csv(uploaded_file)

    st.subheader("📊 Dataset Preview")
    st.dataframe(df.head())

    # ---------------------------------
    # Select Target Column
    # ---------------------------------
    target_column = st.selectbox("🎯 Select Target Column", df.columns)

    # ---------------------------------
    # Encode categorical features
    # ---------------------------------
    df_encoded = df.copy()
    label_encoders = {}

    for col in df_encoded.columns:
        if df_encoded[col].dtype == "object":
            le = LabelEncoder()
            df_encoded[col] = le.fit_transform(df_encoded[col])
            label_encoders[col] = le

    X = df_encoded.drop(columns=[target_column])
    y = df_encoded[target_column]

    # ---------------------------------
    # Train-Test Split
    # ---------------------------------
    test_size = st.slider("📊 Test Size (%)", 10, 50, 30) / 100

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=42
    )

    # ---------------------------------
    # Model Training
    # ---------------------------------
    model = GaussianNB()
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)

    # ---------------------------------
    # Evaluation Metrics
    # ---------------------------------
    acc = accuracy_score(y_test, y_pred)
    cm = confusion_matrix(y_test, y_pred)

    st.subheader("📈 Model Performance")

    st.success(f"✅ Accuracy Score: {acc:.4f}")

    # ---------------------------------
    # Confusion Matrix Heatmap
    # ---------------------------------
    st.write("### 🔎 Confusion Matrix")

    fig_cm, ax_cm = plt.subplots()
    im = ax_cm.imshow(cm)

    ax_cm.set_xlabel("Predicted")
    ax_cm.set_ylabel("Actual")
    ax_cm.set_title("Confusion Matrix")

    for i in range(cm.shape[0]):
        for j in range(cm.shape[1]):
            ax_cm.text(j, i, cm[i, j], ha="center", va="center")

    st.pyplot(fig_cm)

    # ---------------------------------
    # Visualization (Only if 2 Features)
    # ---------------------------------
    if X.shape[1] == 2:
        st.subheader("📊 Before vs After Classification")

        # BEFORE (Actual)
        fig1, ax1 = plt.subplots()
        ax1.scatter(
            X_test.iloc[:, 0],
            X_test.iloc[:, 1],
            c=y_test
        )
        ax1.set_xlabel(X.columns[0])
        ax1.set_ylabel(X.columns[1])
        ax1.set_title("Actual Classes")
        st.pyplot(fig1)

        # AFTER (Predicted)
        fig2, ax2 = plt.subplots()
        ax2.scatter(
            X_test.iloc[:, 0],
            X_test.iloc[:, 1],
            c=y_pred
        )
        ax2.set_xlabel(X.columns[0])
        ax2.set_ylabel(X.columns[1])
        ax2.set_title("Predicted Classes")
        st.pyplot(fig2)

    else:
        st.info("📌 Scatter plot available only if dataset has exactly 2 feature columns.")

else:
    st.warning("Please upload a CSV file to begin.")