from pydantic import BaseModel

class LawGetView(BaseModel):
    law: str
    name: str
