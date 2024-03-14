from pydantic import BaseModel

class StageGetView(BaseModel):
    stage: str
