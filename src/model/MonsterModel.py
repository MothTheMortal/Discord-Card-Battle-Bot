from mongoengine import EmbeddedDocument, ReferenceField, BooleanField, StringField, IntField, ListField
from CardPackModel import CardPack
from ItemModel import Item
from CardModel import Card
import datetime


class Monster(EmbeddedDocument):
    name = StringField(required=True)
    code = StringField(required=True)
    healthStat = IntField(required=False, default=0)
    armorStat = IntField(required=False, default=0)
    spiritStat = IntField(required=False, default=0)
    spawnChannel = ListField(required=True)
    spawnInterval = IntField(required=False, default=1)  # In seconds
    despawnTime = IntField(required=False, default=10)   # In seconds

    currencyDrops = StringField(required=False, default="0")  # Amount drops will follow direct or range input
    xpDrops = StringField(required=False, default="0")

    cardPackDrops = StringField(required=True)  # Item Drops will follow Probability String Format
    cardDrops = StringField(required=True)
    itemDrops = StringField(required=True)

    playersRewarded = IntField(default=3)
    imageUrl = StringField()
    timeCreated = DateTimeField(default=datetime.datetime.now)
    locked = BooleanField(default=False)

