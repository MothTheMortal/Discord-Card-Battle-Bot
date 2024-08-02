from mongoengine import EmbeddedDocument, ReferenceField, BooleanField, StringField, IntField, ListField, DateTimeField, Document
import datetime


class CardPack(EmbeddedDocument):
    name = StringField(required=True)
    code = StringField(required=True)
    category = StringField(required=True)
    description = StringField(required=True)
    price = IntField(required=True)
    cards = StringField(required=True)
    soldInShop = BooleanField(required=True)
    imageUrl = StringField()
    timeCreated = DateTimeField(default=datetime.datetime.now)
    locked = BooleanField(default=False)

    @staticmethod
    def checkIfExists(guild, code: str) -> bool:
        for i in guild.cardPackCollection:
            if i.code == code:
                return True
        return False

    @staticmethod
    def checkIfExistAndReturn(guild, code: str) -> EmbeddedDocument:
        code = str(code)
        for i in guild.cardPackCollection:
            if i.code == code:
                return i
        return False
