from beanie import Document, Indexed


class PurchaseStage(Document):
    stage: Indexed(str, unique=True)