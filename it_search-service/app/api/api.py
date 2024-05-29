from fastapi import APIRouter, HTTPException
from typing import List

from app.service.service import Service

it_search_router = APIRouter(prefix="/it_search")

@it_search_router.get("/search_tender", status_code=200)
async def search_tender(
    name: str | None = None,
    number: str | None = None,
    law: str | None = None,
    stage: str | None = None,
    min_price: str | None = None,
    max_price: str | None = None,
    placement_date: str | None = None,
    end_date: str | None = None,
  ):
  tender = await Service.get_searched_tender(name, number, law, stage, min_price, max_price, placement_date, end_date)

  if not tender:
    raise HTTPException(status_code=404, detail="No tender :(")
  return tender

@it_search_router.get("/elastic_query", status_code=200)
async def elastic_query():
  pass