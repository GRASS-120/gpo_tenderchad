import pymongo

from datetime import datetime
from typing import List, Optional
from beanie import Document, Link, Indexed

from app.models.federal_law import FederalLaw
from app.models.purchase_stage import PurchaseStage
from app.models.key_word import KeyWord
from app.models.technology import Technology
from app.models.supplier_definition import SupplierDefinition

# так поиск идет по name или по keywords???? в аналитике по name

class Tender(Document):
    number: Indexed(str, unique=True)
    name: Indexed(str, index_type = pymongo.TEXT)  # name
    key_words: List[Link[KeyWord]]
    purchase_stage: Optional[Link[PurchaseStage]] = None
    stack_technologies: Optional[List[Link[Technology]]] = None 
    supplier_definition: Optional[Link[SupplierDefinition]] = None
    law: Optional[Link[FederalLaw]] = None
    platform_name: str
    customer_name : str = None
    platform_url: str
    percentage_application_security: int = 10
    price: float = 0
    type: str
    deadline: int = -1
    placement_date: Optional[datetime] = None
    start_date: Optional[datetime] = None
    end_date: Optional[datetime] = None
