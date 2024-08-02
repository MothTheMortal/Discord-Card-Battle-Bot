from discord.ext import commands
from discord import app_commands
from discord.app_commands import Choice
from src.model.CardModel import Card
from src.model.ItemModel import Item
from src.model.CardPackModel import CardPack
from src.model.GuildModel import DiscordGuild
from src.model.UserModel import User
import config
import discord


class ItemCog(commands.Cog):
    def __init__(self, client):
        self.client = client

    @app_commands.command(name="give", description="Give a user an object.")
    @app_commands.choices(select=
                            [
                                Choice(name="Card Pack", value='cardpack'),
                                Choice(name='Card', value='card'),
                                Choice(name='Item', value='item')
                            ])
    async def give(self, ctx: discord.Interaction, user: discord.Member, select: Choice[str], code: int, quantity: int = 1):
        await ctx.response.defer()
        guild: DiscordGuild = DiscordGuild.fetchGuild(ctx.guild.id)

        user, userIndex = User.checkIfExistsAndReturnWithIndex(guild, user.id)

        if not user:
            return await ctx.edit_original_response(content="User has not registered.")

        if select.value == "cardpack":

            cardPack = CardPack.checkIfExistAndReturn(guild, str(code))
            if not cardPack:
                return await ctx.edit_original_response(content="Card Pack not found.")

            guild.addCardPackToUser(code, userIndex, quantity)

            await ctx.edit_original_response(content=f"Added {quantity} x Card Pack: {cardPack.name} to {ctx.user.name}'s Bag")

        elif select.value == "card":

            card = Card.checkIfExistAndReturn(guild, str(code))
            if not card:
                return await ctx.edit_original_response(content="Card not found.")

            guild.addCardToUser(code, userIndex, quantity)

            await ctx.edit_original_response(content=f"Added {quantity} x Card: {card.name} to {ctx.user.name}'s Collection")

        else:

            item = Item.checkIfExistAndReturn(guild, str(code))

            if not item:
                return await ctx.edit_original_response(content="Item not found.")

            guild.addItemToUser(code, userIndex, quantity)

            await ctx.edit_original_response(content=f"Added {quantity} x Item: {item.name} to {ctx.user.name}'s Bag")



    @app_commands.command(name="remove", description="Remove an object from the user.")
    @app_commands.choices(select=
                          [
                              Choice(name="Card Pack", value='cardpack'),
                              Choice(name='Card', value='card'),
                              Choice(name='Item', value='item')
                          ])
    async def remove(self, ctx: discord.Interaction, user: discord.Member, select: Choice[str], code: int, quantity: int = 1):
        await ctx.response.defer()

        guild: DiscordGuild = DiscordGuild.fetchGuild(ctx.guild.id)

        user, userIndex = User.checkIfExistsAndReturnWithIndex(guild, user.id)

        if not user:
            return await ctx.edit_original_response(content="User has not registered.")

        if select.value == "cardpack":

            cardPack = CardPack.checkIfExistAndReturn(guild, str(code))
            if not cardPack:
                return await ctx.edit_original_response(content="Card Pack not found.")

            if not guild.userHasCardPacks(code, userIndex, quantity=quantity):
                return await ctx.edit_original_response(content=f"User does not have {quantity} x Card Pack: {cardPack.name}")


            guild.addCardPackToUser(code, userIndex, quantity * -1)

            await ctx.edit_original_response(content=f"Removed {quantity} x Card Pack: {cardPack.name} from {ctx.user.name}'s Bag")

        elif select.value == "card":

            card = Card.checkIfExistAndReturn(guild, str(code))
            if not card:
                return await ctx.edit_original_response(content="Card not found.")

            if guild.userHasCards(code, userIndex, quantity=quantity):
                return await ctx.edit_original_response(content=f"User does not have {quantity} x Card: {card.name}")

            guild.addCardToUser(code, userIndex, quantity * -1)

            await ctx.edit_original_response(content=f"Removed {quantity} x Card: {card.name} from {ctx.user.name}'s Collection")

        else:

            item = Item.checkIfExistAndReturn(guild, str(code))

            if not item:
                return await ctx.edit_original_response(content="Item not found.")

            if guild.userHasItems(code, userIndex, quantity=quantity):
                return await ctx.edit_original_response(content=f"User does not have {quantity} x Item: {item.name}")

            guild.addItemToUser(code, userIndex, quantity * -1)

            await ctx.edit_original_response(content=f"Removed {quantity} x Item: {item.name} to {ctx.user.name}'s Bag")


async def setup(client):
    await client.add_cog(ItemCog(client))
