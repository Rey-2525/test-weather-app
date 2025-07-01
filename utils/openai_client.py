import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

async def generate_weather_explanation(data):
    location = data.get("location", "指定なし")
    weather = data.get("weather", "不明")
    temp = data.get("temp", 0)
    humidity = data.get("humidity", 0)
    pop = int(data.get("pop", 0) * 100)

    prompt = (
        f"次のデータに基づいて、日本語で自然な天気解説文を作ってください。\n"
        f"場所: {location}、天気: {weather}、気温: {temp}℃、湿度: {humidity}％、降水確率: {pop}％。\n"
        f"やや親しみやすい口調で、天気の印象をわかりやすく100文字以内で表現してください。"
    )

    response = openai.ChatCompletion.create(
        model="gpt-4-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
        max_tokens=150
    )

    return response.choices[0].message.content.strip()


async def generate_clothing_advice(data):
    temp = data.get("temp", 0)
    humidity = data.get("humidity", 0)
    weather = data.get("weather", "不明")

    prompt = (
        f"天気: {weather}、気温: {temp}℃、湿度: {humidity}％の条件で、"
        f"その日の服装アドバイスを日本語で1文でください。"
        f"例：Tシャツがちょうどよい、軽い上着があると安心、など。"
    )

    response = openai.ChatCompletion.create(
        model="gpt-4-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.6,
        max_tokens=100
    )

    return response.choices[0].message.content.strip()
