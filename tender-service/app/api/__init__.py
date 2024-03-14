from fastapi import APIRouter

from app.api.tender_api import tender_router

router = APIRouter(prefix="/api/v1")
router.include_router(tender_router)