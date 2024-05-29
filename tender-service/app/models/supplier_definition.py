from beanie import Document, Indexed

class SupplierDefinition(Document):
    name: Indexed(str, unique=True)