 Automated Student Marks Prediction with Cron + Streamlit

## 1. Project Overview
This project demonstrates an end‑to‑end pipeline for automating predictions using a **Linear Regression model** and visualizing results in a **Streamlit dashboard**.  
Key components:
- **Model training** (`model.pkl`)
- **Prediction script** (`predict_and_update.py`)
- **Automation with cron jobs** (runs every minute in WSL)
- **Visualization with Streamlit** (`app.py`)

---

## 2. Environment Setup
### 2.1 Create Project Structure
```
Linear_regression_model/
│── app.py
│── predict_and_update.py
│── model.pkl
│── data/
│    └── Student_Marks.csv
│    └── predictions_log.csv
│── venv_linux/
│── logs/
```

### 2.2 Create Virtual Environment
```bash
cd "/mnt/e/6 month internshio/Linear_regression_model"
python3 -m venv venv_linux
source venv_linux/bin/activate
pip install pandas scikit-learn matplotlib joblib streamlit kaggle
```


## 3. Prediction Script (`predict_and_update.py`)
### 3.1 Purpose
- Loads trained model
- Reads dataset
- Generates predictions
- Appends results to `predictions_log.csv`

### 3.2 Absolute Paths
Since cron runs from `~`, all file paths are absolute:
```python
BASE = "/mnt/e/6 month internshio/Linear_regression_model"
MODEL_PATH = f"{BASE}/model.pkl"
DATA_PATH = f"{BASE}/data/Student_Marks.csv"
LOG_PATH = f"{BASE}/data/predictions_log.csv"
```

### 3.3 Dynamic Inputs
To avoid repetitive logs, inputs are randomized:
```python
import random
number_courses = random.randint(1, 10)
time_study = round(random.uniform(0.0, 10.0), 1)
```

### 3.4 Logging
Each run appends a row:
```
timestamp, number_courses, time_study, predicted_marks
```

---

## 4. Cron Job Setup
### 4.1 Open Crontab
```bash
crontab -e
```
Choose `1` (Nano).

### 4.2 Add Cron Entry
```bash
* * * * * /mnt/e/6\ month\ internshio/Linear_regression_model/venv_linux/bin/python /mnt/e/6\ month\ internshio/Linear_regression_model/predict_and_update.py >> /mnt/e/6\ month\ internshio/Linear_regression_model/cron_log.txt 2>&1
```

### 4.3 Start Cron Service
```bash
sudo service cron start
```

### 4.4 Verify
```bash
tail -n 5 "/mnt/e/6 month internshio/Linear_regression_model/data/predictions_log.csv"
```
Shows new entries every minute.



## 5. Streamlit App (`app.py`)
### 5.1 Purpose
Interactive dashboard for:
- Model predictions (via sliders)
- Regression visualization
- Cron job predictions log

### 5.2 Key Sections
- **Interactive Prediction**
```python
courses = st.sidebar.slider("Number of Courses", 1, 10, 5)
hours = st.sidebar.slider("Study Hours", 0.0, 10.0, 5.0)
```

- **Regression Visualization**
Scatter plot + regression line + prediction marker.

- **Cron Job Log Viewer**
```python
st.subheader("📜 Cron Job Predictions Log")
log_df = pd.read_csv(LOG_PATH)
st.dataframe(log_df.tail(20))
st.line_chart(log_df.set_index("timestamp")["predicted_marks"])
```



## 6. Running the Demo
### 6.1 Start Streamlit
```bash
cd "/mnt/e/6 month internshio/Linear_regression_model"
./venv_linux/bin/streamlit run app.py
```

### 6.2 Open in Browser
Go to:
```
http://localhost:8501
```





## 7. Key Learnings
- **Absolute paths** are required for cron jobs in WSL.
- **Randomized inputs** ensure varied predictions.
- **Streamlit integration** makes automation results visible and interactive.
- **Cron + Streamlit** together demonstrate real‑time ML automation.



## 8. Next Improvements
- Add duplicate guard (skip logging if same as last row).
- Auto‑refresh Streamlit every minute.
- Style dashboard (highlight latest prediction, add summary stats).
- Extend to multiple models or datasets.

