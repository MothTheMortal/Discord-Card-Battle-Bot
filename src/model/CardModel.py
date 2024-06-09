from mongoengine import EmbeddedDocument, StringField, IntField, ListField, DictField, DateTimeField, BooleanField
import datetime
connect("")


class Card(EmbeddedDocument):
    name = StringField(required=True)
    description = StringField(required=True)
    category = StringField(required=True)
    code = StringField(required=True)
    tier = StringField(required=True)

    damageType = ListField(required=True)  # Multiple Damage Types
    damage = DictField(required=True)  # Damage for Each Type

    cooldown = IntField(required=True)  # In seconds

    xpValue = IntField(required=True)
    imageUrl = StringField()
    timeCreated = DateTimeField(default=datetime.datetime.now)
    locked = BooleanField(default=False)

