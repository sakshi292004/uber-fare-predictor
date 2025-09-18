# Uber Fare Predictor

Uber Fare Predictor is a Streamlit application that estimates Uber ride fares based on pickup and dropoff locations, passenger count, and pickup time. The predictions are powered by a Random Forest regression model served via FastAPI.

## Project Overview

The application allows users, drivers, and companies to quickly calculate expected ride costs. By providing pickup and dropoff latitude/longitude, passenger count, and pickup time, the app returns a predicted fare in real-time.

## Features

- Predict fare for Uber rides using a trained machine learning model
- Interactive Streamlit frontend for user-friendly inputs
- FastAPI backend to serve predictions
- Responsive design with an easy-to-use interface
- Supports multiple passengers and different times of the day

## Screenshot

![Uber Fare Predictor](uberimage.jpeg)

## Tech Stack

- Python
- Streamlit for frontend
- FastAPI for backend API
- Scikit-learn for Random Forest Regression
- Joblib for model serialization
- Pandas and NumPy for data processing

