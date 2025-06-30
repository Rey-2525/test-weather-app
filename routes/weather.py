from fastapi import APIRouter
import requests
from utils.config import API_KEY

router = APIRouter()

@router.get("/weather")
def get_weather(lat: float = 35.6895, lon: float = 139.6917):
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "lat": lat,
        "lon": lon,
        "appid": API_KEY,
        "units": "metric",
        "lang": "ja"
    }
    response = requests.get(url, params=params)
    data = response.json()

    return {
        "location": data.get("name", "不明"),
        "weather": data["weather"][0]["description"],
        "temperature": data["main"]["temp"],
        "humidity": data["main"]["humidity"],
        "icon": data["weather"][0]["icon"]
    }

@router.get("/weather-forecast")
def get_forecast(lat: float = 35.6895, lon: float = 139.6917):
    url = "https://api.openweathermap.org/data/2.5/forecast"
    params = {
        "lat": lat,
        "lon": lon,
        "appid": API_KEY,
        "units": "metric"
    }
    response = requests.get(url, params=params)
    data = response.json()

    forecast = []
    for entry in data["list"][:4]:
        forecast.append({
            "time": entry["dt_txt"],
            "pop": round(entry.get("pop", 0) * 100)
        })

    return {"forecast": forecast}
