from fastapi import APIRouter, HTTPException
from typing import List

from app.service.service import Service
from app.messaging.publish import send_message

analysis_router = APIRouter(prefix="/analysis")

@analysis_router.get("/configure", status_code=200)
async def configure_render_area():
  send_message()
  return "analysis"
