import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

st.set_page_config(page_title="Customer Segmentation App", layout="wide")

st.title("🛍️ Customer Segmentation using KMeans")

# Load dataset
df = pd.read_csv("Mall_Customers.csv")

st.subheader("📊 Dataset Preview")
st.dataframe(df.head())

# Show basic info
if st.checkbox("Show Dataset Info"):
    st.write("Shape:", df.shape)
    st.write(df.describe())

# -------------------------------
# Visualization Section
# -------------------------------
st.subheader("📈 Data Visualization")

col1, col2 = st.columns(2)

with col1: # Gender
    fig1, ax1 = plt.subplots() 
    df['Gender'].value_counts().plot(kind='bar', ax=ax1)
    ax1.set_title("Gender Distribution")
    st.pyplot(fig1)

with col2:
    fig2, ax2 = plt.subplots()
    ax2.hist(df['Age'])
    ax2.set_title("Age Distribution")
    st.pyplot(fig2)

# -------------------------------
# KMeans Clustering
# -------------------------------
st.subheader("🔍 KMeans Clustering")

X = df[['Annual Income (k$)', 'Spending Score (1-100)']]

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Elbow Method
wcss = []
for i in range(1, 11):
    kmeans_temp = KMeans(n_clusters=i, random_state=42)
    kmeans_temp.fit(X_scaled)
    wcss.append(kmeans_temp.inertia_)

fig4, ax4 = plt.subplots()
ax4.plot(range(1, 11), wcss, marker='o')
ax4.set_title("Elbow Method")
st.pyplot(fig4)

# Select K
k = st.slider("Select number of clusters (K)", 2, 10, 5)

kmeans = KMeans(n_clusters=k, random_state=42)
df['Cluster'] = kmeans.fit_predict(X_scaled)

# Cluster plot
fig5, ax5 = plt.subplots()
scatter = ax5.scatter(df['Annual Income (k$)'], df['Spending Score (1-100)'], c=df['Cluster'])
ax5.set_title("Customer Segmentation")
st.pyplot(fig5)

# Cluster summary
st.subheader("📌 Cluster Summary")
cluster_summary = df.groupby('Cluster')[['Age', 'Annual Income (k$)', 'Spending Score (1-100)']].mean()
st.dataframe(cluster_summary)

# -------------------------------
# Prediction Section (Logistic Regression)
# -------------------------------
st.subheader("🤖 Predict Customer Cluster")


X = df[['Annual Income (k$)', 'Spending Score (1-100)']]
y = df['Cluster']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = LogisticRegression(max_iter=200)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
acc = accuracy_score(y_test, y_pred)

st.write("Model Accuracy:", acc)

# User Input
income = st.number_input("Enter Annual Income")
score = st.number_input("Enter Spending Score")

if st.button("Predict Cluster"):
    result = model.predict([[income, score]])
    st.success(f"Predicted Cluster: {result[0]}")
