from fastapi import APIRouter, HTTPException
from typing import List

from app.service.service import Service

it_search_router = APIRouter(prefix="/it_search")

@it_search_router.get("/search_tender", status_code=200)
async def search_tender(search: str, law: str | None = None, stage: str | None = None):
  tender = await Service.get_searched_tender(search, law, stage)

  if not tender:
    raise HTTPException(status_code=404, detail="No tender :(")
  return tender

@it_search_router.get("/elastic_query", status_code=200)
async def elastic_query():
  pass