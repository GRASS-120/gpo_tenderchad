from fastapi import APIRouter, HTTPException
from typing import List

from app.service.service import Service
from app.messaging.publish import send_message

it_analysis_router = APIRouter(prefix="/it_analysis")

@it_analysis_router.get("/test", status_code=200)
async def test():
  send_message()
  return "test"
