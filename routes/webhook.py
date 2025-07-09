from fastapi import APIRouter, Request, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models import Signal
from datetime import datetime, timedelta

router = APIRouter()

@router.post("/")
async def receive_tradingview_webhook(request: Request, db: Session = Depends(get_db)):
    try:
        data = await request.json()
        pair = data.get("pair")
        signal_type = data.get("signal_type", "").lower()
        source = "tradingview"
        if signal_type not in ["buy", "sell", "hold"]:
            raise HTTPException(status_code=400, detail="Type de signal invalide")
        signal = Signal(pair=pair, signal_type=signal_type, source=source)
        db.add(signal)
        db.commit()
        return {"message": "Signal TradingView enregistré"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/recent_rsi_signals")
def get_recent_rsi_signals(db: Session = Depends(get_db)):
    fifteen_minutes_ago = datetime.utcnow() - timedelta(minutes=15)
    signals = db.query(Signal).filter(
        Signal.timestamp >= fifteen_minutes_ago,
        Signal.source == "rsi"
    ).order_by(Signal.timestamp.desc()).all()

    return [
        {
            "pair": s.pair,
            "type": s.signal_type,
            "time": s.timestamp.strftime("%Y-%m-%d %H:%M:%S")
        } for s in signals
    ]
