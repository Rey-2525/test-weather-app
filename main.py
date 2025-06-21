from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import requests

app = FastAPI()

# CORS設定（全てのオリジンからのアクセスを許可）
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # セキュリティ上は後で制限してもいい
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

API_KEY = "d72e36dfc0902f1533ed5c15c2ab90ab"  # ← 自分のOpenWeatherMap APIキーに置き換え

@app.get("/weather")
def get_weather(lat: float = 35.6895, lon: float = 139.6917):
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "lat": lat,
        "lon": lon,
        "appid": API_KEY,
        "units": "metric",
        "lang": "ja"  # 日本語の天気情報を取得
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

@app.get("/weather-forecast")
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
    for entry in data["list"][:4]:  # 3時間ごと × 4件 = 12時間分
        forecast.append({
            "time": entry["dt_txt"],
            "pop": round(entry.get("pop", 0) * 100)
        })

    return {"forecast": forecast}

