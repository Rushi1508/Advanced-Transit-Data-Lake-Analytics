# predict_delay.py
import pandas as pd
import numpy as np
import joblib
import datetime

# Load trained model
model = joblib.load("rf_real_delay_model.pkl")  # make sure this is saved

# Function to extract features from inputs
def extract_features(stop_id: str, timestamp: datetime.datetime) -> pd.DataFrame:
    hour = timestamp.hour
    minute = timestamp.minute
    day_of_week = timestamp.weekday()
    is_peak_hour = 1 if 7 <= hour <= 9 or 16 <= hour <= 18 else 0

    # Encode stop_id to stop_code (same mapping as training)
    stop_code_mapping = joblib.load("stop_code_mapping.pkl")
    stop_code = stop_code_mapping.get(stop_id, -1)  # fallback for unknown stop_id

    features = pd.DataFrame([[hour, minute, day_of_week, is_peak_hour, stop_code]],
                            columns=["hour", "minute", "day_of_week", "is_peak_hour", "stop_code"])
    return features

# Prediction function
def predict_delay(stop_id: str, timestamp: datetime.datetime) -> float:
    features = extract_features(stop_id, timestamp)
    delay = model.predict(features)[0]
    return delay

# Example usage
if __name__ == "__main__":
    test_stop_id = "103S"
    test_time = datetime.datetime.strptime("2025-03-30 01:00:00", "%Y-%m-%d %H:%M:%S")
    predicted_delay = predict_delay(test_stop_id, test_time)
    print(f"Predicted delay at stop {test_stop_id}: {int(predicted_delay)} seconds (~{int(predicted_delay)//60} min)")
