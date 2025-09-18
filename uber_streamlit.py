# uber_streamlit.py
import streamlit as st
import requests
from datetime import datetime

# Page config
st.set_page_config(page_title="Uber Fare Predictor", page_icon="🚖")

# Inject CSS for orange background, yellow button, and heading
st.markdown(
    """
    <style>
    /* Orange background for Streamlit app */
    .reportview-container {
        background-color: #ff9800;
    }
    /* Yellow button */
    .stButton>button {
        background-color: #fff176;
        color: black;
        font-size: 18px;
        font-weight: bold;
        border-radius: 10px;
        padding: 10px 20px;
    }
    /* Heading style */
    h1 {
        text-align: center;
        color: #d84315;
        font-family: 'Arial', sans-serif;
        font-weight: bold;
        margin-bottom: 10px;
    }
    /* Center the image */
    .center-img {
        display: flex;
        justify-content: center;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Heading
st.markdown("<h1>🚖 Uber Fare Predictor</h1>", unsafe_allow_html=True)

# Banner Image (centered using Streamlit columns)
col1, col2, col3 = st.columns([1,2,1])
with col2:
    st.image("uberimage.jpeg", width=400)  # make sure this path is correct

# Description
st.markdown(
    """
    <p style='text-align: center; font-size: 20px; color: black;'>
    This app predicts the estimated fare for an Uber ride based on pickup and dropoff locations, passenger count, and pickup time.<br>
    It helps users, drivers, and companies understand expected ride costs quickly and efficiently.
    </p>
    """,
    unsafe_allow_html=True
)

# User Inputs
pickup_lat = st.number_input("Pickup Latitude", value=40.758896)
pickup_lon = st.number_input("Pickup Longitude", value=-73.985130)
dropoff_lat = st.number_input("Dropoff Latitude", value=40.761581)
dropoff_lon = st.number_input("Dropoff Longitude", value=-73.981740)
passenger_count = st.number_input("Passenger Count", min_value=1, max_value=6, value=2)
pickup_datetime = st.text_input("Pickup Date & Time (YYYY-MM-DD HH:MM:SS)", value="2025-09-18 14:30:00")

# Predict Fare Button
if st.button("Predict Fare"):
    data = {
        "pickup_latitude": pickup_lat,
        "pickup_longitude": pickup_lon,
        "dropoff_latitude": dropoff_lat,
        "dropoff_longitude": dropoff_lon,
        "passenger_count": passenger_count,
        "pickup_datetime": pickup_datetime
    }

    try:
        response = requests.post("http://127.0.0.1:8000/predict", json=data)
        if response.status_code == 200:
            fare = response.json()["predicted_fare"]
            st.success(f"Estimated Fare: ${fare}")
        else:
            st.error("Error: Could not get prediction from API.")
    except Exception as e:
        st.error(f"Error: {e}")
