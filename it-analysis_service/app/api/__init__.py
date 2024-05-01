from fastapi import APIRouter

from app.api.api import it_analysis_router

router = APIRouter(prefix="/api/v1")
router.include_router(it_analysis_router)