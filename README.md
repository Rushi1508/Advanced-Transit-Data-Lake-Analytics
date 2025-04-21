# 🚌 Real-Time Transit Delay Prediction using GTFS Data

This project implements a scalable, end-to-end machine learning system for predicting real-time delays in public transit using GTFS-static and GTFS-realtime datasets. It features an automated cloud-based ETL pipeline, feature engineering, model training, and real-time prediction interface using Python and Streamlit.

---

## 🚀 Project Overview

- **Goal:** Predict stop-level transit delays in real time using historical and live GTFS data.
- **Pipeline:** ETL → Feature Engineering → Model Training → Real-Time Inference
- **Tools:** AWS (S3, Glue, Athena, Lambda, ROSA), Python, scikit-learn, Streamlit
- **Data Source:** GTFS-static and GTFS-realtime feeds from transit agencies

---


## 📊 Features

- ✅ Real-time delay prediction using GTFS-realtime feeds
- ✅ Fully automated ETL with schema management (Glue + Athena)
- ✅ Feature-rich dataset (temporal, spatial, operational)
- ✅ Multiple model evaluation (RF, CatBoost, XGBoost, KNN, etc.)
- ✅ Streamlit dashboard for interactive predictions
- ✅ CLI tool for backend or batch prediction
- ✅ Scalable architecture with modular components

---

## 🧠 Machine Learning Models

| Model         | MAE (s) | RMSE (s) | R² Score |
|---------------|---------|----------|----------|
| Random Forest | 24.44   | 33.73    | 0.41     |
| CatBoost      | 26.39   | 34.28    | 0.39     |
| KNN           | 25.03   | 35.71    | 0.34     |
| XGBoost       | 25.41   | 36.94    | 0.29     |

📌 **Random Forest** was selected for deployment due to its superior accuracy and inference speed.

---


