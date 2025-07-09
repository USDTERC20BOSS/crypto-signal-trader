from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from models import TradeOrder
from datetime import datetime

router = APIRouter()

@router.get("/trades")
def get_trade_logs(db: Session = Depends(get_db)):
    logs = db.query(TradeOrder).order_by(TradeOrder.timestamp.desc()).limit(50).all()
    return [
        {
            "pair": log.pair,
            "side": log.side,
            "quantity": log.quantity,
            "price": log.price,
            "timestamp": log.timestamp.strftime("%Y-%m-%d %H:%M:%S")
        }
        for log in logs
    ]
