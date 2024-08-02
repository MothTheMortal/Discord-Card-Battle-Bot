from mongoengine import EmbeddedDocument, StringField, IntField, ListField, DictField, DateTimeField, BooleanField, Document
import datetime


class Card(EmbeddedDocument):
    name = StringField(required=True)
    description = StringField(required=True)
    category = StringField(required=True)
    code = StringField(required=True)
    tier = StringField(required=True)

    damageType = ListField(required=True)  # Multiple Damage Types
    damage = DictField(required=True)  # Damage for Each Type

    cooldown = IntField(required=True)  # In seconds
    xpValue = StringField(required=True)


    imageUrl = StringField()
    timeCreated = DateTimeField(default=datetime.datetime.now)
    locked = BooleanField(default=False)

    @staticmethod
    def checkIfExists(guild: Document, code: str) -> bool:
        for i in guild.cardCollection:
            if i.code == code:
                return True
        return False

    @staticmethod
    def checkIfExistAndReturn(guild, code: str) -> EmbeddedDocument:
        code = str(code)
        for i in guild.cardCollection:
            if i.code == code:
                return i
        return False

