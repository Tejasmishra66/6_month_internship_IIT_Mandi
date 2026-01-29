
# ML Model Showcase Dashboard

An interactive **Streamlit dashboard** showcasing multiple machine learning models trained on popular datasets.  
This project demonstrates end‑to‑end ML automation: training, saving artifacts, and serving predictions with a user‑friendly interface.

---

##  Features
- Dropdown to select a trained model
- Display of evaluation metrics (accuracy, R², silhouette score, explained variance, etc.)
- Visualizations: accuracy graphs, confusion matrices, feature importance plots, decision tree diagrams
- Random prediction from the dataset with model output
- Dataset integration for each model



##  Models Included
- **Decision Tree** – Iris dataset (tree plot + accuracy graph)
- **KMeans** – Iris dataset (silhouette plot)
- **KNN** – Diabetes dataset (accuracy bar)
- **Linear Regression** – Students Performance dataset (scatter plot)
- **Logistic Regression** – Diabetes dataset (confusion matrix)
- **Naive Bayes** – Spam/Ham SMS dataset (text classification)
- **PCA** – MNIST dataset (explained variance chart)
- **Random Forest** – Wine Quality dataset (feature importance plot)
- **SVM** – Breast Cancer dataset (confusion matrix)



## 📂 Project Structure
```
├── app.py                 # Streamlit dashboard
├── trained/               # Saved models + metrics + visualizations
│   ├── decision_tree/
│   ├── kmeans/
│   ├── knn/
│   ├── linear_regression/
│   ├── logistic_regression/
│   ├── naive_bayes/
│   ├── pca/
│   ├── random_forest/
│   └── svm/
├── data/                  # Datasets (downloaded via Kaggle or included)
```

Each model folder contains:
- `model.pkl` → trained model  
- `schema.json` → input/output schema  
- `metrics.json` → evaluation metrics  
- `training_graph.png` → visualization  



##  How to Run
1. Clone the repository:
   ```bash
   git clone https://github.com/<your-username>/<repo-name>.git
   cd <repo-name>
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```
4. Open the local URL shown in your terminal (usually `http://localhost:8501`).



##  Requirements
- Python 3.9+
- Streamlit
- Pandas
- Scikit-learn
- Matplotlib
- Joblib

Install all dependencies with:
```bash
pip install -r requirements.txt




