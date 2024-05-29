from datetime import datetime
from pydantic import BaseModel
from bson import ObjectId
# from pydantic.json import ENCODERS_BY_TYPE

# Кастомный сериализатор для ObjectId
# ENCODERS_BY_TYPE[ObjectId] = str

class TenderGetView(BaseModel):
    number: str
    name: str
    key_words: list
    stack_technologies: list
    supplier_definition: str
    platform_name: str
    customer_name: str
    platform_url: str
    percentage_application_security: int
    type: str
    deadline: int
    law: dict
    purchase_stage: str
    price: float
    placement_date: datetime
    start_date: datetime
    end_date: datetime

    class Settings:
        projection = {"number": "$number",
                      "name": "$name",
                      "key_words": {
                          "$map": {
                              "input": "$key_words",
                              "as": "kw",
                              "in": {
                                  "name": "$$kw.name",
                                  "suitable": "$$kw.suitable"
                              }
                          }
                      },
                      "stack_technologies": {
                          "$map": {
                              "input": "$stack_technologies",
                              "as": "st",
                              "in": {
                                  "name": "$$st.name"
                              }
                          }
                      },
                      "supplier_definition": "$supplier_definition.name",
                      "platform_name": "$platform_name",
                      "customer_name": "$customer_name",
                      "platform_url": "$platform_url",
                      "percentage_application_security": "$percentage_application_security",
                      "deadline": "$deadline",
                      "type": "$type",
                      "law": {
                          "law": "$law.law",
                          "name": "$law.name", },
                      "purchase_stage": "$purchase_stage.stage",
                      "price": "$price",
                      "placement_date": "$placement_date",
                      "start_date": "$start_date",
                      "end_date": "$end_date",}
        
    # class Config:
    #     json_encoders = {
    #         ObjectId: str
    #     }