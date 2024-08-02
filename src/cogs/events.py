from discord.ext import commands
from src.model.GuildModel import DiscordGuild
import discord


class EventsCog(commands.Cog):
    def __init__(self, client):
        self.client = client


    @commands.Cog.listener()
    async def on_guild_join(self, guild: discord.Guild):
        print(f"Joined guild: {guild.name}")
        guild = DiscordGuild(_id=str(guild.id), name=guild.name)
        guild.save()


async def setup(client):
    await client.add_cog(EventsCog(client))