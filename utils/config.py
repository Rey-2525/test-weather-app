import os
from dotenv import load_dotenv
load_dotenv()

# OpenWeatherMapのAPIキーを環境変数から取得
API_KEY = os.environ.get("OPENWEATHER_API_KEY")