from src.model.GuildModel import DiscordGuild
from src.model.CardModel import Card
from src.model.ItemModel import Item
from src.model.CardPackModel import CardPack
from src.model.MonsterModel import Monster
from src.model.UserModel import User

cogs = ["economy", "item", "inventory", "battle", "user", "misc", "utils", "events"]
objectTranslation = {
    'cardpack': CardPack,
    'card': Card,
    'item': Item
}


def validateProbability(string):
    total_probability = 0.0
    start = 0

    for i in range(len(string)):
        if string[i] == ' ':
            pair = string[start:i]
            code, percentage = pair.split(':')
            probability = float(percentage.replace('%', ''))
            total_probability += probability
            start = i + 1

    pair = string[start:]
    code, percentage = pair.split(':')
    probability = float(percentage.replace('%', ''))
    total_probability += probability

    return total_probability == 100


def checkDuplicates(string):
    codes = set()
    pairs = string.split()

    for pair in pairs:
        code, _ = pair.split(':')
        if code in codes:
            return True
        codes.add(code)

    return False
