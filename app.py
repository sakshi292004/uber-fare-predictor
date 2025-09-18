from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd
import numpy as np
from datetime import datetime

app = FastAPI()

model = joblib.load("uber_fare_rf_model.pkl")

def haversine(lon1, lat1, lon2, lat2):
    lon1, lat1, lon2, lat2 = map(np.radians, [lon1, lat1, lon2, lat2])
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = np.sin(dlat/2)**2 + np.cos(lat1)*np.cos(lat2)*np.sin(dlon/2)**2
    return 2 * 6371 * np.arcsin(np.sqrt(a))

class RideData(BaseModel):
    pickup_latitude: float
    pickup_longitude: float
    dropoff_latitude: float
    dropoff_longitude: float
    passenger_count: int
    pickup_datetime: str

@app.post("/predict")
def predict_fare(data: RideData):
    distance = haversine(data.pickup_longitude, data.pickup_latitude,
                         data.dropoff_longitude, data.dropoff_latitude)
    dt = datetime.strptime(data.pickup_datetime, "%Y-%m-%d %H:%M:%S")
    input_df = pd.DataFrame([[distance, data.passenger_count, dt.hour, dt.weekday(), dt.month]],
                            columns=['distance_km','passenger_count','pickup_hour','pickup_weekday','pickup_month'])
    fare = model.predict(input_df)[0]
    return {"predicted_fare": round(fare, 2)}
