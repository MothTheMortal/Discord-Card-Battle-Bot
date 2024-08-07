import discord
from client import CardBattleBot
from dotenv import load_dotenv
from os import getenv

if __name__ == "__main__":
    load_dotenv()

    client = CardBattleBot(command_prefix="?", case_insensitive=True, intents=discord.Intents.all(), help_command=None, mongodb_uri=getenv('MONGODB'))
    client.run(getenv('BOT_TOKEN'))
