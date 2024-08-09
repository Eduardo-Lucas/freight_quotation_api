import requests
from app.models.freight import FreightRequest, FreightResponse

from sqlalchemy.orm import Session
from app.models.freight import Freight

def create_freight(db: Session, freight_data: dict):
    db_freight = Freight(**freight_data)
    db.add(db_freight)
    db.commit()
    db.refresh(db_freight)
    return db_freight

def get_freight(db: Session, freight_id: int):
    return db.query(Freight).filter(Freight.id == freight_id).first()

def calculate_freight(request: FreightRequest) -> FreightResponse:
    # Simulação de cálculo de frete
    price = request.weight * 1.5  # Exemplo de lógica de preço
    response = FreightResponse(
        carrier="DHL", price=price, estimated_delivery="3-5 dias"
    )
    return response


def generate_shipping_label(request: dict) -> dict:
    # Simulação de geração de etiqueta
    label = f"Label-{request['order_id']}-{request['carrier']}"
    return {"label": label}
