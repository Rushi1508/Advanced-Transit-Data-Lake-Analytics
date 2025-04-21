# delay_predictor_app.py
import streamlit as st
import pandas as pd
import numpy as np
import joblib
import datetime

# Load pre-trained model
model = joblib.load("delay_model.pkl")

# Load encoded data to map route/stop IDs to codes
merged = pd.read_csv("encoded_gtfs_data.csv")

features = ["hour", "minute", "stop_code", "route_code", "is_peak_hour",
            "stop_sequence", "num_stops_in_trip", "day_of_week"]

# Streamlit interface
st.title("GTFS Delay Predictor")

# Dropdowns for user input
selected_route = st.selectbox("Select Route", sorted(merged["route_id"].unique()))
selected_stop = st.selectbox("Select Stop", sorted(merged["stop_id"].unique()))
selected_hour = st.slider("Hour of Day", 0, 23, 8)
selected_minute = st.slider("Minute of Hour", 0, 59, 30)

# Handle code extraction safely
try:
    route_code = merged.loc[merged["route_id"] == selected_route, "route_code"].iloc[0]
    stop_code = merged.loc[merged["stop_id"] == selected_stop, "stop_code"].iloc[0]
except IndexError:
    st.error("Invalid route or stop selection. Please try again.")
    st.stop()

is_peak = 1 if 7 <= selected_hour <= 9 or 16 <= selected_hour <= 18 else 0

# Placeholder values for added features (optional: update if actual values become available)
stop_sequence = 5  # Assumed average position in trip
num_stops_in_trip = 10  # Assumed total number of stops
current_day = datetime.datetime.today().weekday()  # Monday = 0, Sunday = 6

# Predict delay
input_features = pd.DataFrame([[selected_hour, selected_minute, stop_code, route_code, is_peak,
                                stop_sequence, num_stops_in_trip, current_day]],
                               columns=features)
predicted_delay = model.predict(input_features)[0]

# Display output
if predicted_delay >= 0:
    st.success(f"Predicted Delay: {int(predicted_delay)} seconds (~{int(predicted_delay // 60)} minutes)")
else:
    st.info(f"Vehicle may arrive early by {-int(predicted_delay)} seconds (~{abs(int(predicted_delay) // 60)} minutes)")