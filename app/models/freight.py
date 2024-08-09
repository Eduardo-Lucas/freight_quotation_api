# app/models/freight.py
from sqlalchemy import Column, Integer, String, Float
from app.database import Base

class Freight(Base):
    __tablename__ = "freights"

    id = Column(Integer, primary_key=True, index=True)
    origin = Column(String, index=True)
    destination = Column(String, index=True)
    weight = Column(Float)
    dimensions = Column(String)
    carrier = Column(String)
    price = Column(Float)
    estimated_delivery = Column(String)
