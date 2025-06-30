import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

async def generate_weather_explanation(data):
    location = data.get("location", "指定なし")
    weather = data.get("weather", "不明")
    temp = data.get("temp", "不明")
    humidity = data.get("humidity", "不明")
    pop = int(data.get("pop", 0) * 100)

    prompt = (
        f"次の天気データをもとに、日本語で自然な天気の解説文を100文字以内で作ってください。\n"
        f"場所: {location}、天気: {weather}、気温: {temp}℃、湿度: {humidity}％、降水確率: {pop}％"
    )

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
        max_tokens=100
    )

    return response.choices[0].message.content.strip()