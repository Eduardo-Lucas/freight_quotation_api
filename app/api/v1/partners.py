from fastapi import APIRouter

router = APIRouter()

@router.get("/partners/")
async def list_partners():
    return {"partners": ["DHL", "FedEx", "UPS"]}
