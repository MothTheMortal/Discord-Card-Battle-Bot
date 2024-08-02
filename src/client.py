from discord.ext import commands
import discord
import mongoengine
import config


class CardBattleBot(commands.Bot):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        mongoengine.connect('CardBot', host=kwargs['mongodb_uri'])

    async def on_ready(self):
        print(f"Logged in as {self.user}")

    async def setup_hook(self):
        for cog in config.cogs:
            await self.load_extension(f"cogs.{cog}")
