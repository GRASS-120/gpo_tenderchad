from fastapi import APIRouter

from app.api.api import analysis_router

router = APIRouter(prefix="/api/v1")
router.include_router(analysis_router)