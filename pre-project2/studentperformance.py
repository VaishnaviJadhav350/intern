import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor

from sklearn.metrics import r2_score

# -------------------------------
# 🎓 Title
# -------------------------------
st.title("🎓 Student Performance Prediction App")

# -------------------------------
# 📂 Load Dataset
# -------------------------------
df = pd.read_csv("student-mat.csv")

st.subheader("📊 Dataset Preview")
st.write(df.head())

# -------------------------------
# 🔄 Data Preprocessing
# -------------------------------
df = pd.get_dummies(df, drop_first=True) # One-hot encoding for categorical variables  //convert categorical data to numeric

X = df.drop("G3", axis=1) # Features (all columns except G3)
y = df["G3"]

# -------------------------------
# ✂ Train-Test Split
# -------------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# -------------------------------
# 📏 Scaling
# -------------------------------
scaler = StandardScaler() # Scale features to have mean=0 and std=1 for better model performance
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# -------------------------------
# 🤖 Model Selection
# -------------------------------
model_name = st.selectbox(
    "Select Model",
    ["Linear Regression", "Decision Tree", "Random Forest"]
)  # Allow user to select which model to use for prediction

if model_name == "Linear Regression":
    model = LinearRegression()
elif model_name == "Decision Tree":
    model = DecisionTreeRegressor()
else:
    model = RandomForestRegressor()

# Train
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

# Score
score = r2_score(y_test, y_pred) # R2 score to evaluate model performance (how well the model explains the variance in the data)

st.subheader("📈 Model Performance")
st.write(f"R2 Score: {score:.2f}") # Display the R2 score in the Streamlit app to show how well the model is performing in predicting student grades

# -------------------------------
# 📊 Graph 1: Actual vs Predicted
# -------------------------------
st.subheader("📊 Actual vs Predicted")

fig, ax = plt.subplots()
ax.scatter(y_test, y_pred, alpha=0.6)
ax.set_xlabel("Actual G3")
ax.set_ylabel("Predicted G3")
ax.set_title("Actual vs Predicted Graph")

st.pyplot(fig) # Display the scatter plot of actual vs predicted values in the Streamlit app to visually assess how well the model's predictions align with the actual student grades

# -------------------------------
# 🌳 Graph 2: Feature Importance
# -------------------------------
if model_name == "Random Forest":
    st.subheader("🌳 Feature Importance")

    importances = model.feature_importances_
    feature_names = X.columns

    imp_df = pd.DataFrame({
        "Feature": feature_names,
        "Importance": importances
    }).sort_values(by="Importance", ascending=False).head(10)

    fig2, ax2 = plt.subplots()
    ax2.barh(imp_df["Feature"], imp_df["Importance"]) # Create a horizontal bar chart to display the top 10 most important features based on the feature importance scores from the Random Forest model
    ax2.invert_yaxis() 
    ax2.set_title("Top 10 Features")

    st.pyplot(fig2)

# -------------------------------
# 🔮 Prediction Section
# -------------------------------
st.subheader("🔮 Predict Student Grade")

# Simple important features
input_features = ["age", "studytime", "failures", "absences", "G1", "G2"]

user_input = []

for col in input_features:
    val = st.number_input(f"{col}", value=0)
    user_input.append(val)

if st.button("Predict"):

    input_df = pd.DataFrame([user_input], columns=input_features)

    # full feature structure
    full_input = pd.DataFrame(columns=X.columns)
    full_input.loc[0] = 0

    for col in input_features:
        if col in full_input.columns:
            full_input[col] = input_df[col]

    # scale
    full_input = scaler.transform(full_input)

    prediction = model.predict(full_input)

    st.success(f"🎯 Predicted Final Grade (G3): {prediction[0]:.2f}")