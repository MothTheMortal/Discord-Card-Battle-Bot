from discord.ext import commands
import discord
from discord import app_commands, Interaction
from src.model.UserModel import User
from src.model.GuildModel import DiscordGuild


class UserCog(commands.Cog):
    def __init__(self, client):
        self.client = client


    @app_commands.command(name="register", description="Registers you to the bot.")
    async def register(self, ctx: Interaction, referred_user: discord.Member = None):
        await ctx.response.defer()


        guild: DiscordGuild = DiscordGuild.objects(_id=str(ctx.guild.id)).first()

        if User.checkIfExists(guild, str(ctx.user.id)):
            return await ctx.edit_original_response(content="You are already registered.")

        if referred_user == ctx.user:
            return await ctx.edit_original_response(content="You cannot refer yourself.")

        user = User(_id=str(ctx.user.id), referred=str(referred_user.id) if referred_user else "")
        guild.users.append(user)
        guild.save()
        await ctx.edit_original_response(content="Registration successful")


async def setup(client):
    await client.add_cog(UserCog(client))