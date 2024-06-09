from mongoengine import Document, StringField, ListField, ReferenceField, DateTimeField, EmbeddedDocumentListField, BooleanField
from UserModel import User
from MonsterModel import Monster
from CardPackModel import CardPack
from CardModel import Card
from ItemModel import Item
import datetime

from src.model.CardModel import Card

connect("")

# Adding new Users
# user3 = User(username='JackDoe').save()
# guild1.update(push__users=user3)


class DiscordGuild(Document):
    _id = StringField(required=True)
    monsterCollection = EmbeddedDocumentListField(Monster)
    cardCollection = EmbeddedDocumentListField(Card)
    cardPackCollection = EmbeddedDocumentListField(CardPack)
    itemCollection = EmbeddedDocumentListField(Item)
    users = EmbeddedDocumentListField(User)

    premium = BooleanField(default=False)
    timeCreated = DateTimeField(default=datetime.datetime.now)
