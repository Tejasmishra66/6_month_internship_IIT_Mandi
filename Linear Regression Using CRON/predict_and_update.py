import os
import pandas as pd
import joblib
from datetime import datetime

# --- Absolute base path to your project ---
BASE = "/mnt/e/6 month internshio/Linear_regression_model"

# --- Paths ---
MODEL_PATH = os.path.join(BASE, "model.pkl")
DATA_PATH = os.path.join(BASE, "data", "Student_Marks.csv")
LOG_PATH = os.path.join(BASE, "data", "predictions_log.csv")

# --- Load model and data ---
model = joblib.load(MODEL_PATH)
df = pd.read_csv(DATA_PATH)

# --- Example input (replace with your logic or parameters) ---
import random

number_courses = random.randint(1, 10)  # 1 to 10 courses
time_study = round(random.uniform(0.0, 10.0), 1)  # 0.0 to 10.0 hours

X = pd.DataFrame([[number_courses, time_study]], columns=["number_courses", "time_study"])
pred = float(model.predict(X)[0])

# --- Append to log (create if missing) ---
ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
row = {"timestamp": ts, "number_courses": number_courses, "time_study": time_study, "predicted_marks": pred}

# Ensure directory exists
os.makedirs(os.path.dirname(LOG_PATH), exist_ok=True)

# Write header if file doesn't exist
write_header = not os.path.exists(LOG_PATH)
pd.DataFrame([row]).to_csv(LOG_PATH, mode="a", header=write_header, index=False)

print(f"Logged: {row}")