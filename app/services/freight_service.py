import requests
from app.models.freight import FreightRequest, FreightResponse

def calculate_freight(request: FreightRequest) -> FreightResponse:
    # Simulação de cálculo de frete
    price = request.weight * 1.5  # Exemplo de lógica de preço
    response = FreightResponse(
        carrier="DHL",
        price=price,
        estimated_delivery="3-5 dias"
    )
    return response

def generate_shipping_label(request: dict) -> dict:
    # Simulação de geração de etiqueta
    label = f"Label-{request['order_id']}-{request['carrier']}"
    return {"label": label}
