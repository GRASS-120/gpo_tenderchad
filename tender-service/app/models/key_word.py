from beanie import Document, Indexed

class KeyWord(Document):
    name: Indexed(str, unique=True)
    suitable: bool = False

    def to_dict(self):
        return {
            "name": self.name,
            "suitable": self.suitable
        }