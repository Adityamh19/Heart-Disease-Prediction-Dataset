# ❤️ Heart Disease Risk Prediction

An end-to-end Supervised Machine Learning project that predicts the 10-year risk of **Coronary Heart Disease (CHD)** based on clinical patient data.

## 🚀 Project Overview
This project addresses the challenge of identifying "Grey Area" cardiac risks—cases where patients may not have a history of disease but exhibit borderline clinical markers. By utilizing **Logistic Regression** and **StandardScaler Pipelines**, the model achieves a reliable **86.4% accuracy** in distinguishing between high-risk and healthy profiles.

## 🛠️ Tech Stack
* **Python:** Core language for data processing
* **Scikit-Learn:** Machine Learning (Logistic Regression, Pipelines, Scalers)
* **Pandas & Seaborn:** Data Cleaning, IQR Outlier Removal, and EDA
* **Streamlit:** Web App Deployment for real-time risk assessment

## 📊 Key Features
* **Clinical Interpretability:** Uses Logistic Regression to provide transparent coefficients, allowing healthcare providers to see exactly which biomarkers (like BP or Glucose) drive the risk score.
* **Pipeline Integration:** Automated feature scaling and model training to ensure consistent predictions across different environments.
* **Patient-Friendly Insights:** The web interface translates complex percentages into actionable insights and specific clinical reasons for the diagnosis.

## 🗺️ Project Pipeline
<img width="694" height="1305" alt="Heart Disease Project Flowchart" src="https://github.com/user-attachments/assets/781c076b-d845-41ae-aeea-bb7331650b99" />

---

## 📈 Model Performance & Selection

### **1. Performance Summary**
* **Selected Model:** Logistic Regression
* **Accuracy:** **~86.4%** — High reliability in predicting 10-year CHD risk.
* **ROC-AUC Score:** **~0.73** — Balanced ability to distinguish between risk profiles.
* **Clinical Robustness:** Unlike "black-box" models, this approach provides clear coefficients for defensible medical screening.

### **2. Why Logistic Regression?**
While ensemble methods like **Random Forest** (~86.6%) and **XGBoost** showed marginally higher accuracy in testing, **Logistic Regression** was selected due to:
* **Interpretability:** Vital for clinical trust; patients and doctors can understand the "why" behind a score.
* **Linear Risk Modeling:** Aligns with medical standards like the Framingham Risk Score.
* **Generalization:** More robust on structured clinical data, reducing the risk of overfitting.

---

## 🌐 Live Demo
Test your clinical metrics here:  
**[Heart Disease Risk Analyzer](https://heart-disease-prediction-dataset-fxthmfupnkkzy6maspegim.streamlit.app/)**

### 💤 Important Note on App Availability
If you are accessing the live demo and the website appears to be "sleeping":
* Please click the **"Yes, get this back up!"** button on the screen.
* This will wake up the server and restore the diagnostic tool within a few seconds.

---

## 🏁 How to Run Locally
1. Clone the repository:
   ```bash
   git clone [https://github.com/YOUR-USERNAME/heart-disease-risk-prediction.git](https://github.com/YOUR-USERNAME/heart-disease-risk-prediction.git)
