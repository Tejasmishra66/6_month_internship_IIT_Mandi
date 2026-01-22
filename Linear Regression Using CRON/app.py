import streamlit as st
import pandas as pd
import joblib
import matplotlib.pyplot as plt
import numpy as np

# Load trained model
model = joblib.load("model.pkl")

# Load dataset for visualization (constant)
df = pd.read_csv("data/Student_Marks.csv")

# --- Page Config ---
st.set_page_config(
    page_title="📊 Student Marks Predictor",
    page_icon="🎓",
    layout="centered",
    initial_sidebar_state="expanded"
)

# --- Title & Description ---
st.title("🎓 Student Marks Predictor")
st.markdown(
    """
    Adjust the sliders below to simulate study habits and see the predicted marks.  
    This app uses a trained **Linear Regression model** with two features:
    - Number of Courses
    - Study Hours
    """
)

# --- Sidebar for Inputs ---
st.sidebar.header("📥 Input Parameters")
courses = st.sidebar.slider("Number of Courses", 1, 10, 5)
hours = st.sidebar.slider("Study Hours", 0.0, 10.0, 5.0)

# --- Prediction ---
X = pd.DataFrame([[courses, hours]], columns=["number_courses", "time_study"])
pred = model.predict(X)[0]

# --- Display Result ---
st.subheader("📌 Prediction Result")
st.metric(label="Predicted Marks", value=f"{pred:.2f}")

# --- Visualization ---
st.subheader("📈 Dataset & Regression Line")

fig, ax = plt.subplots()

# Scatter plot of dataset (constant, does not change with sliders)
ax.scatter(df["time_study"], df["Marks"], color="blue", label="Actual Data")

# Regression line (changes with 'courses' slider)
study_range = np.linspace(df["time_study"].min(), df["time_study"].max(), 50)
line_X = pd.DataFrame({
    "number_courses": [courses] * len(study_range),
    "time_study": study_range
})
line_y = model.predict(line_X)

ax.plot(study_range, line_y, color="red", label="Regression Line")

# Highlight user prediction (changes with both sliders)
ax.scatter([hours], [pred], color="green", s=100, label="Your Prediction")

ax.set_xlabel("Study Hours")
ax.set_ylabel("Marks")
ax.legend()

st.pyplot(fig)

# --- Footer ---
st.markdown("---")
st.caption("Built with ❤️ using Streamlit and scikit-learn")

import pandas as pd
import streamlit as st

LOG_PATH = "/mnt/e/6 month internshio/Linear_regression_model/data/predictions_log.csv"

st.subheader("📜 Cron Job Predictions Log")

try:
    log_df = pd.read_csv(LOG_PATH)
    st.dataframe(log_df.tail(20))  # show last 20 entries
except FileNotFoundError:
    st.warning("No predictions log found yet. Cron job may not have run.")