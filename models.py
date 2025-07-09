from sqlalchemy import Column, Integer, String, Boolean, Float, DateTime
from database import Base
from datetime import datetime

class ActivationCode(Base):
    __tablename__ = "activation_codes"
    id = Column(Integer, primary_key=True, index=True)
    code = Column(String, unique=True, index=True)
    is_active = Column(Boolean, default=False)

class APISettings(Base):
    __tablename__ = "api_settings"
    id = Column(Integer, primary_key=True, index=True)
    api_key = Column(String)
    api_secret = Column(String)

class BotConfig(Base):
    __tablename__ = "bot_config"
    id = Column(Integer, primary_key=True, index=True)
    profit_percent = Column(Float, default=5.0)
    stop_loss_percent = Column(Float, default=5.0)
    strategy = Column(String, default="RSI")
    market = Column(String, default="all")

class TradeOrder(Base):
    __tablename__ = "trade_orders"
    id = Column(Integer, primary_key=True, index=True)
    pair = Column(String)
    side = Column(String)
    price = Column(Float)
    quantity = Column(Float)
    timestamp = Column(DateTime, default=datetime.utcnow)

class Signal(Base):
    __tablename__ = "signals"
    id = Column(Integer, primary_key=True, index=True)
    pair = Column(String)
    signal_type = Column(String)
    source = Column(String)
    timestamp = Column(DateTime, default=datetime.utcnow)