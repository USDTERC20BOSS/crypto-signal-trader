from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import os
from routes import auth, settings, trading, pairs, status, signals, strategy, logs, webhook

app = FastAPI(title="POWER MS Trading Pro Backend")

# تحميل المتغيرات البيئية
load_dotenv()

# تهيئة Binance API
Binance_API_KEY = os.getenv('BINANCE_API_KEY')
Binance_API_SECRET = os.getenv('BINANCE_API_SECRET')

# إضافة middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router, prefix="/auth", tags=["Auth"])
app.include_router(settings.router, prefix="/settings", tags=["Settings"])
app.include_router(trading.router, prefix="/trade", tags=["Trading"])
app.include_router(pairs.router, prefix="/pairs", tags=["Pairs"])
app.include_router(status.router, prefix="/status", tags=["Status"])
app.include_router(signals.router, prefix="/signals", tags=["Signals"])
app.include_router(strategy.router, prefix="/strategy", tags=["Strategy"])
app.include_router(logs.router, prefix="/logs", tags=["Logs"])
app.include_router(webhook.router, prefix="/webhook", tags=["Webhook"])

@app.get("/")
async def root():
    return {"message": "Bienvenue à POWER MS Trading Pro Backend"}