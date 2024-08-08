from fastapi import APIRouter, Depends
from app.models.freight import FreightRequest, FreightResponse, ShippingLabelRequest
from app.services.freight_service import calculate_freight, generate_shipping_label
from app.auth.auth import get_current_user

router = APIRouter()

@router.post("/freight/", response_model=FreightResponse)
async def get_freight_quote(request: FreightRequest, user: str = Depends(get_current_user)):
    return calculate_freight(request)

@router.post("/shipping-label/", response_model=dict)
async def create_shipping_label(request: ShippingLabelRequest, user: str = Depends(get_current_user)):
    return generate_shipping_label(request.dict())
