from typing import List

from beanie.operators import In

from app.models.tender import Tender
from app.schemas.tender import TenderGetView
from app.models.federal_law import FederalLaw
from app.schemas.law import LawGetView
from app.models.purchase_stage import PurchaseStage
from app.schemas.stage import StageGetView


class CRUD:

    async def get_tender(tender_id: str) -> Tender:
        return await Tender.find_one(Tender.number == tender_id, fetch_links=True).project(TenderGetView)

    async def get_laws() -> List[FederalLaw]:
        return await FederalLaw.find_all().project(LawGetView).to_list()
    
    async def get_stages() -> List[PurchaseStage]:
        return await PurchaseStage.find_all().project(StageGetView).to_list()
    
    async def search_tender(search, stage, law) -> List[Tender]:
        return await Tender.find(In(Tender.description, [search]), fetch_links=True).project(TenderGetView).to_list()