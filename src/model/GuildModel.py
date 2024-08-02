from mongoengine import Document, StringField, ListField, ReferenceField, DateTimeField, EmbeddedDocumentListField, BooleanField, DictField
from src.model.UserModel import User
from src.model.MonsterModel import Monster
from src.model.CardPackModel import CardPack
from src.model.CardModel import Card
from src.model.ItemModel import Item
import datetime


class DiscordGuild(Document):
    _id = StringField(required=True)
    name = StringField(required=True)
    monsterCollection = EmbeddedDocumentListField(Monster)
    cardCollection = EmbeddedDocumentListField(Card)
    cardPackCollection = EmbeddedDocumentListField(CardPack)
    itemCollection = EmbeddedDocumentListField(Item)
    users = EmbeddedDocumentListField(User)
    data = DictField()
    premium = BooleanField(default=False)
    timeCreated = DateTimeField(default=datetime.datetime.now)
    meta = {'collection': 'guilds'}


    def addCardPackToUser(self, code, user, quantity=1) -> None:
        code = str(code)
        collection = self.users[user].cardPackCollection
        collection[code] = collection.get(code, 0) + quantity
        self.save()

    def userHasCardPacks(self, code, userIndex, quantity=1) -> bool:
        code = str(code)
        collection = self.users[userIndex].cardPackCollection
        return collection.get(code, 0) >= quantity

    def userHasCards(self, code, userIndex, quantity=1) -> bool:
        code = str(code)
        collection = self.users[userIndex].cardCollection
        return collection.get(code, 0) >= quantity

    def userHasItems(self, code, userIndex, quantity=1) -> bool:
        code = str(code)
        collection = self.users[userIndex].itemCollection
        return collection.get(code, 0) >= quantity

    def addCardToUser(self, code, user, quantity=1) -> None:
        code = str(code)
        collection = self.users[user].cardCollection
        collection[code] = collection.get(code, 0) + quantity
        self.save()

    def addItemToUser(self, code, user, quantity=1):
        code = str(code)
        collection = self.users[user].itemCollection
        collection[code] = collection.get(code, 0) + quantity
        self.save()


    @staticmethod
    def fetchGuild(Id) -> Document:
        guild: DiscordGuild = DiscordGuild.objects(_id=str(Id)).first()
        return guild


