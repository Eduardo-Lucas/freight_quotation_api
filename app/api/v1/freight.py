# app/api/v1/freight.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.services.freight_service import create_freight, get_freight
from app.models.freight import FreightRequest
from app.database import get_db

router = APIRouter()

@router.post("/freight/")
async def create_freight_record(request: FreightRequest, db: Session = Depends(get_db)):
    return create_freight(db, request.dict())

@router.get("/freight/{freight_id}")
async def read_freight_record(freight_id: int, db: Session = Depends(get_db)):
    freight = get_freight(db, freight_id)
    if not freight:
        raise HTTPException(status_code=404, detail="Freight not found")
    return freight
