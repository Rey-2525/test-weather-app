from fastapi import APIRouter, Request
from utils.openai_client import generate_weather_explanation

router = APIRouter()

@router.post("/explanation")
async def explanation(request: Request):
    data = await request.json()
    result = await generate_weather_explanation(data)
    return {"explanation": result}