from mongoengine import EmbeddedDocument, StringField, IntField, ReferenceField, ListField, BooleanField, DateTimeField, Document
import datetime


class Item(EmbeddedDocument):
    name = StringField(required=True)
    code = StringField(required=True)
    price = IntField(required=True)
    description = StringField(required=True)
    category = StringField(required=True)
    soldInShop = BooleanField(required=True)

    addRole = StringField()
    addCurrency = StringField(default="")
    addXp = StringField(default="")
    spawnMonsters = StringField(default="")
    imageUrl = StringField()

    timeCreated = DateTimeField(default=datetime.datetime.now)
    locked = BooleanField(default=False)

    @staticmethod
    def checkIfExists(guild: Document, code: str) -> bool:
        for i in guild.itemCollection:
            if i.code == code:
                return True
        return False

    @staticmethod
    def checkIfExistAndReturn(guild, code: str) -> EmbeddedDocument:
        code = str(code)
        for i in guild.itemCollection:
            if i.code == code:
                return i
        return False

