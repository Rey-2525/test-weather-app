from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from routes import weather, view, explanation  # explanation は後で

app = FastAPI()

# CORS設定
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ルーター登録
app.include_router(weather.router)
app.include_router(view.router)
app.include_router(explanation.router)

# 静的ファイル（CSS等）
app.mount("/static", StaticFiles(directory="static"), name="static")