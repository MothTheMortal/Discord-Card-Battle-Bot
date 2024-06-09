from mongoengine import EmbeddedDocument, ReferenceField, BooleanField, StringField, IntField, ListField, DateTimeField
from CardModel import Car
import datetime
connect("")


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

