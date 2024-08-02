from mongoengine import EmbeddedDocument, StringField, DictField, ListField, DateTimeField, EmbeddedDocumentListField, FloatField, IntField, Document
import datetime


class User(EmbeddedDocument):
    _id = StringField(required=True)
    referred = StringField()


    cardCollection = DictField()
    cardPackCollection = DictField()
    itemCollection = DictField()

    balance = FloatField(default=0)
    xp = IntField(default=0)


    userLogs = DictField(default={
        "logs": [],
        "monstersKilled": 0,
        "itemsUsed": 0,
        "cardPacksUsed": 0,
    })

    timeCreated = DateTimeField(default=datetime.datetime.now)

    @staticmethod
    def checkIfExists(guild, userId: str) -> bool:
        for i in guild.users:
            if i._id == userId:
                return True
        return False

    @staticmethod
    def checkIfExistsAndReturnWithIndex(guild, userId) -> bool:
        userId = str(userId)
        for index, i in enumerate(guild.users):
            if i._id == userId:
                return i, index
        return False, False
