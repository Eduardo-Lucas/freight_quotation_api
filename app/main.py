from fastapi import FastAPI, Depends
from contextlib import asynccontextmanager
from app.api.v1 import freight, partners
from app.utils import token
from app.config import settings
from sqlalchemy.orm import Session
from app.database import SessionLocal, engine, database

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@asynccontextmanager
async def lifespan(app: FastAPI):
    await database.connect()
    yield
    await database.disconnect()

app = FastAPI(lifespan=lifespan)

app.include_router(token.router, prefix="/api/v1")
app.include_router(freight.router, prefix=settings.API_V1_STR, tags=["Freight"])
app.include_router(partners.router, prefix=settings.API_V1_STR, tags=["Partners"])


@app.get("/")
async def root():
    return {"message": "Freight Quotation API"}
