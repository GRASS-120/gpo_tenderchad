from datetime import datetime
from pydantic import BaseModel


class TenderGetView(BaseModel):
    number: str
    description: str
    law: dict
    purchase_stage: str
    price: float
    placement_date: datetime
    start_date: datetime
    end_date: datetime

    class Settings:
        projection = {"number": "$number",
                      "description": "$description",
                      "law": {
                          "law": "$law.law",
                          "name": "$law.name", },
                      "purchase_stage": "$purchase_stage.stage",
                      "price": "$price",
                      "placement_date": "$placement_date",
                      "start_date": "$start_date",
                      "end_date": "$end_date",}
