from pydantic import BaseModel

class FreightRequest(BaseModel):
    origin: str
    destination: str
    weight: float
    dimensions: str

class FreightResponse(BaseModel):
    carrier: str
    price: float
    estimated_delivery: str

class ShippingLabelRequest(BaseModel):
    order_id: str
    carrier: str
    address: str
