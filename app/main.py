from fastapi import FastAPI
from app.api.v1 import freight, partners
from app.utils import token
from app.config import settings

app = FastAPI()

app.include_router(token.router, prefix="/api/v1")
app.include_router(freight.router, prefix=settings.API_V1_STR, tags=["Freight"])
app.include_router(partners.router, prefix=settings.API_V1_STR, tags=["Partners"])


@app.get("/")
async def root():
    return {"message": "Freight Quotation API"}
