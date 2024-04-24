from typing import List
from fastapi import APIRouter, HTTPException

from app.preset_data.init_tender_data import fill_database
from app.crud.crud import CRUD
from app.schemas.tender import TenderGetView
from app.schemas.law import LawGetView
from app.schemas.stage import StageGetView

tender_router = APIRouter(prefix="/tender")

@tender_router.get("/search", response_model = List[TenderGetView], status_code=200)
async def search(search: str, law: str | None = None, stage: str | None = None):
    results = await CRUD.search_tender(search, law, stage)
    return results

# насчет эндпоинта хз пока
@tender_router.get("/law", response_model = List[LawGetView], status_code=200)
async def get_law(law):
    res = await CRUD.get_one_law(law)
    if not res:
        raise HTTPException(status_code=404, detail="Item not found")
    return res

# насчет эндпоинта хз пока
@tender_router.get("/stage", response_model = List[StageGetView], status_code=200)
async def get_stage(stage):
    res = await CRUD.get_one_stage(stage)
    if not res:
        raise HTTPException(status_code=404, detail="Item not found")
    return res

@tender_router.get("/preset-database")
async def preset_database():
    await fill_database()

# @tender_router.get("/get/{tender_id}", response_model=TenderGetView, status_code=200)
# async def get_tender(tender_id: str):
#     tender = await CRUD.get_tender(tender_id)
#     if not tender:
#         raise HTTPException(status_code=404, detail="Item not found")
#     return tender

# @tender_router.get("/law/get/", response_model = List[LawGetView], status_code=200)
# async def get_laws():
#     laws = await CRUD.get_laws()
#     if not laws:
#         raise HTTPException(status_code=404, detail="Item not found")
#     return laws


# @tender_router.get("/stage/get/", response_model = List[StageGetView], status_code=200)
# async def get_stages():
#     laws = await CRUD.get_stages()
#     if not laws:
#         raise HTTPException(status_code=404, detail="Item not found")
#     return laws


