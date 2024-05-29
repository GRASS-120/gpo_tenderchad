from beanie import Document, Indexed

class Technology(Document):
    name: Indexed(str, unique=True)