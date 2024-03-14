import pymongo

from datetime import datetime

from beanie import Document, Link, Indexed

from app.models.federal_law import FederalLaw
from app.models.purchase_stage import PurchaseStage

class Tender(Document):
    number: Indexed(str, unique=True)
    description: Indexed(str, index_type = pymongo.TEXT)
    law: Link[FederalLaw]
    purchase_stage: Link[PurchaseStage]
    price: float
    placement_date: datetime
    start_date: datetime
    end_date: datetime
