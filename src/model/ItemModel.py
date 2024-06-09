from mongoengine import EmbeddedDocument, StringField, IntField, ReferenceField, ListField, BooleanField, DateTimeField
from MonsterModel import Monster
import datetime


class Item(EmbeddedDocument):
    name = StringField(required=True)
    price = IntField(required=True)
    description = StringField(required=True)
    category = StringField(required=True)
    soldInShop = BooleanField(required=True)

    addRole = StringField()
    addCurrency = StringField(default="0")
    addXp = StringField(default="0")

    cooldown = IntField(required=True)  # In seconds
    spawnMonsters = ListField(ReferenceField(Monster))  # Note to work on this in the future during command creation
    imageUrl = StringField()
    timeCreated = DateTimeField(default=datetime.datetime.now)
    locked = BooleanField(default=False)

