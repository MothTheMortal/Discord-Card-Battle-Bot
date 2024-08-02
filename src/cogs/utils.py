from discord.ext import commands
import discord
from discord import app_commands
from src.model.GuildModel import DiscordGuild
from src.model.CardModel import Card
from src.model.ItemModel import Item
from src.model.CardPackModel import CardPack
from src.model.MonsterModel import Monster
from src.model.UserModel import User
from src import config
import random


class UtilsCog(commands.Cog):
    def __init__(self, client):
        self.client = client


    @app_commands.command(name="add-card", description="Adds a Card.")
    async def add_card(self, ctx: discord.Interaction, name: str, description: str, category: str, code: str, tier: str, cooldown: int, health_damage: int,
                       spirit_damage: int, armor_damage: int, xp_value: str = "0" , image_url: str = ""):
        await ctx.response.defer()
        guild: DiscordGuild = DiscordGuild.objects(_id=str(ctx.guild.id)).first()

        if Card.checkIfExists(guild, code):
            return await ctx.edit_original_response(content="Card Already Exists (Duplicate Code)")


        damageType = []
        damage = {}

        if health_damage:
            damageType.append("Health")
            damage["health"] = health_damage
        if armor_damage:
            damageType.append("Armor")
            damage["armor"] = armor_damage
        if spirit_damage:
            damageType.append("Spirit")
            damage["spirit"] = spirit_damage



        newCard = Card(name=name, description=description, category=category, code=code, tier=tier, cooldown=cooldown, xpValue=xp_value, imageUrl=image_url, damageType=damageType, damage=damage)
        guild.cardCollection.append(newCard)
        guild.save()

        await ctx.response.send_message(f"{name} has been added to the card collection.")


    @app_commands.command(name="add-monster", description="Adds a Monster.")
    async def add_monster(self, ctx: discord.Interaction, name: str, code: str, description: str, category: str, spawn_channel: discord.TextChannel,
                          card_packs_dropped: str, cards_dropped: str, items_dropped: str, health_stat: int = 0,
                          armor_stat: int = 0, spirit_stat: int = 0, currency_dropped: str = "0", xp_dropped: str = "0",
                          players_rewarded: int = 3, spawn_interval: int = 1, despawn_time: int = 10, image_url: str = ""):
        await ctx.response.defer()
        guild: DiscordGuild = DiscordGuild.objects(_id=str(ctx.guild.id)).first()

        if Monster.checkIfExists(guild, code):
            return await ctx.edit_original_response(content="Monster Already Exists (Duplicate Code)")

        newMonster = Monster(name=name, code=code, description=description, category=category, healthStat=health_stat, armorStat=armor_stat, spiritStat=spirit_stat, spawnChannel=[str(spawn_channel.id)], spawnInterval=spawn_interval, despawnTime=despawn_time, currencyDrops=currency_dropped, xpDrops=xp_dropped, cardPackDrops=card_packs_dropped, cardDrops=cards_dropped, itemDrops=items_dropped, playersRewarded=players_rewarded, imageUrl=image_url)
        guild.monsterCollection.append(newMonster)
        guild.save()

        await ctx.response.send_message(f"{name} has been added to the monster collection.")


    @app_commands.command(name='add-cardpack', description="Adds a CardPack.")
    async def add_cardpack(self, ctx: discord.Interaction, name: str, code: str, description: str, category: str, price: int, cards: str, sold_in_shop: bool, image_url: str = ""):
        await ctx.response.defer()
        guild: DiscordGuild = DiscordGuild.objects(_id=str(ctx.guild.id)).first()

        # Check if unique card pack code
        if CardPack.checkIfExists(guild, code):
            return await ctx.edit_original_response(content="CardPack Already Exists (Duplicate Code).")  # Return Error


        for card in cards.split(" "):
            cardCode, _ = card.split(":")

            if not Card.checkIfExists(guild, cardCode):
                return await ctx.edit_original_response(content=f"Card {cardCode} not Found")  # Return Error


        if config.checkDuplicates(cards):
            return await ctx.edit_original_response(content="Duplicate cards detected")  # Return Duplicate Cards Error


        if not config.validateProbability(cards):
            return await ctx.edit_original_response(content="Probability Doesn't add up to 100%")  # Return probability error


        newCardPack = CardPack(name=name, code=code, category=category, description=description, price=price, cards=cards, soldInShop=sold_in_shop, imageUrl=image_url)
        guild.cardPackCollection.append(newCardPack)
        guild.save()

        await ctx.edit_original_response(content=f"Created Card Pack {name}")


    @app_commands.command(name='add-item', description="Adds an Item.")
    async def add_item(self, ctx: discord.Interaction, name: str, code: str, description: str, price: int, category: str,
                       sold_in_shop: bool, add_role: discord.Role = None, add_currency: str = "", add_xp: str = "",
                       spawn_monsters: str = None, image_url: str = ""):
        await ctx.response.defer()
        guild: DiscordGuild = DiscordGuild.objects(_id=str(ctx.guild.id)).first()


        if Item.checkIfExists(guild, code):
            return await ctx.edit_original_response(content="Item Already Exists (Duplicate Code)")

        for monster in spawn_monsters.split(" "):
            monsterCode, _ = monster.split(":")

            if not Monster.checkIfExists(guild, monsterCode):
                return await ctx.edit_original_response(content=f"Monster {MonsterCode} not Found")  # Return Error

        if config.checkDuplicates(spawn_monsters):
            return await ctx.edit_original_response(content="Duplicate cards detected")  # Return Duplicate Cards Error

        if config.validateProbability(spawn_monsters):
            return await ctx.edit_original_response(content="Probability Error")

        item = Item(name=name, code=code, category=category, description=description, price=price, soldInShop=sold_in_shop, addRole=str(add_role.id) if add_role else add_role, addCurrency=add_xp, addXp=add_xp, spawnMonsters=spawn_monsters, imageUrl=image_url)
        guild.itemCollection.append(item)
        guild.save()
        await ctx.edit_original_response(content="Item has been added to the item collection.")


async def setup(client):
    await client.add_cog(UtilsCog(client))