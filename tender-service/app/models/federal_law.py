from beanie import Document, Indexed


class FederalLaw(Document):
    law: Indexed(str, unique=True)
    name: str