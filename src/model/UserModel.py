from mongoengine import EmbeddedDocument, StringField, DictField, ListField, DateTimeField, EmbeddedDocumentListField, FloatField, IntField
from CardPackModel import CardPack
from CardModel import Card
from ItemModel import Item
import datetime
connect("")


class User(EmbeddedDocument):
    _id = StringField(required=True)
    cardCollection = ListField(StringField())
    cardPackCollection = ListField(StringField())
    itemCollection = ListField(StringField())

    balance = FloatField(default=0)
    xp = IntField(default=0)


    referred = StringField()
    userLogs = DictField(default={
        "logs": [],
        "monstersKilled": 0,
        "itemsUsed": 0,
        "cardPacksUsed": 0,
    })

    timeCreated = DateTimeField(default=datetime.datetime.now)