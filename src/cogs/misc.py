from typing import Any

from discord.ext import commands
import discord
from src.model.GuildModel import DiscordGuild
from src.model.CardModel import Card
from src.model.ItemModel import Item
from src.model.CardPackModel import CardPack
from src.model.MonsterModel import Monster
from src.model.UserModel import User
from discord import app_commands, ui, Interaction, PartialEmoji


class MiscCog(commands.Cog):
    def __init__(self, client):
        self.client = client

    #  Test Command
    # @app_commands.command(name="test", description="Testing command")
    # async def test(self, ctx):
    #
    #     monster = {
    #         "name": "",
    #         "code": "",
    #         "description": "",
    #         "category": "",
    #         "spawn_channel": "",
    #
    #         "card_packs_dropped": "",
    #         "cards_dropped": "",
    #         "items_dropped": "",
    #         "health_stat": 0,
    #
    #         "armor_stat": 0,
    #         "spirit_stat": 0,
    #         "currency_dropped": "",
    #         "xp_dropped": "",
    #
    #         "players_rewarded": 0,
    #         "spawn_interval": 0,
    #         "despawn_time": 0,
    #         "image_url": ""
    #     }
    #
    #
    #     class monsterCreation1(ui.Modal, title="Create a monster (Part 1/4)"):
    #         name = ui.TextInput(label="Name", row=0)
    #         code = ui.TextInput(label="Code", row=1)
    #         description = ui.TextInput(label="Description", style=discord.TextStyle.paragraph, row=2)
    #         category = ui.TextInput(label="Category", row=3)
    #         spawn_channel = ui.TextInput(label="Spawn Channel ID", row=4)
    #
    #         async def on_submit(self, ctx: discord.Interaction):
    #             monster['name'] = self.name.value
    #             monster['code'] = self.code.value
    #             monster['description'] = self.description.value
    #             monster['category'] = self.category.value
    #             monster['spawn_channel'] = self.spawn_channel.value
    #             print()
    #             print(monster)
    #             await ctx.response.defer()
    #
    #
    #
    #     class monsterCreation2(ui.Modal, title="Create a monster (Part 2/4)"):
    #         card_packs_dropped = ui.TextInput(label="Card Packs Dropped", row=0)
    #         cards_dropped = ui.TextInput(label="Cards Dropped", row=1)
    #         items_dropped = ui.TextInput(label="Items Dropped", row=2)
    #         health_stat = ui.TextInput(label="Health Stat", row=3)
    #         armor_stat = ui.TextInput(label="Armor Stat", row=4)
    #
    #         async def on_submit(self, ctx: discord.Interaction):
    #             monster['card_packs_dropped'] = self.card_packs_dropped.value
    #             monster['cards_dropped'] = self.cards_dropped.value
    #             monster['items_dropped'] = self.items_dropped.value
    #             monster['health_stat'] = self.health_stat.value
    #             monster['armor_stat'] = self.armor_stat.value
    #             print()
    #             print(monster)
    #             await ctx.response.defer()
    #
    #
    #     class monsterCreation3(ui.Modal, title="Create a monster (Part 3/4)"):
    #         spirit_stat = ui.TextInput(label="Spirit Stat", row=0)
    #         currency_dropped = ui.TextInput(label="Currency Dropped", row=1)
    #         xp_dropped = ui.TextInput(label="XP Dropped", row=2)
    #         players_rewarded = ui.TextInput(label="Players Rewarded", row=3)
    #         spawn_interval = ui.TextInput(label="Spawn Interval", row=4)
    #
    #         async def on_submit(self, ctx: discord.Interaction):
    #             monster['spirit_stat'] = self.spirit_stat.value
    #             monster['currency_dropped'] = self.currency_dropped.value
    #             monster['xp_dropped'] = self.xp_dropped.value
    #             monster['players_rewarded'] = self.players_rewarded.value
    #             monster['spawn_interval'] = self.spawn_interval.value
    #             print()
    #             print(monster)
    #             await ctx.response.defer()
    #
    #     class monsterCreation4(ui.Modal, title="Create a monster (Part 4/4)"):
    #         despawn_time = ui.TextInput(label="Despawn Time", row=0)
    #         image_url = ui.TextInput(label="Image URL", row=1)
    #
    #         async def on_submit(self, ctx: discord.Interaction):
    #             monster['despawn_time'] = self.despawn_time.value
    #             monster['image_url'] = self.image_url.value
    #             print()
    #             print(monster)
    #             await ctx.response.defer()
    #
    #     class monsterCreation(ui.View):
    #         def __init__(self):
    #             super().__init__(timeout=None)
    #
    #             for i in range(1, 5):
    #                 self.add_item(self.button(f"Part {i}"))
    #             self.add_item(self.finishButton("Create"))
    #
    #         class finishButton(ui.Button):
    #             def __init__(self, label):
    #                 super().__init__(label=label, style=discord.ButtonStyle.success, row=1)
    #
    #             async def callback(self, ctx: discord.Interaction):
    #                 newMonster = Monster(name=monster["name"], code=monster["code"],
    #                                      description=monster["description"], category=monster["category"],
    #                                      healthStat=monster["health_stat"], armorStat=monster["armor_stat"],
    #                                      spiritStat=monster["spirit_stat"],
    #                                      spawnChannel=monster["spawn_channel"],
    #                                      spawnInterval=monster["spawn_interval"],
    #                                      despawnTime=monster["despawn_time"],
    #                                      currencyDrops=monster["currency_dropped"],
    #                                      xpDrops=monster["xp_dropped"],
    #                                      cardPackDrops=monster["card_packs_dropped"],
    #                                      cardDrops=monster["cards_dropped"],
    #                                      itemDrops=monster["items_dropped"],
    #                                      playersRewarded=monster["players_rewarded"],
    #                                      imageUrl=monster["image_url"])
    #                 guild = guild = DiscordGuild(_id=str(ctx.guild.id), name=ctx.guild.name)
    #                 monsterCollection.append(newMonster)
    #                 guild.save()
    #                 await ctx.response.send_message("Monster created!")
    #
    #
    #
    #         class button(ui.Button):
    #             def __init__(self, label):
    #                 super().__init__(label=label)
    #
    #             async def callback(self, ctx: discord.Interaction):
    #                 monster = {
    #                     '1': monsterCreation1(),
    #                     '2': monsterCreation2(),
    #                     '3': monsterCreation3(),
    #                     '4': monsterCreation4(),
    #                 }
    #                 await ctx.response.send_modal(monster.get(list(self.label)[-1]))
    #                 self.emoji = PartialEmoji.from_str('✅')
    #                 self.style = discord.ButtonStyle.success
    #                 await ctx.message.edit(view=self.view)
    #
    #
    #     view = monsterCreation()
    #     await ctx.response.send_message(view=view)


    @app_commands.command(name="reload-commands", description="Reloading commands")
    async def reload_commands(self, ctx: discord.Interaction):
        synced = await self.client.tree.sync()
        await ctx.response.defer()
        print(f"Loaded {len(synced)} commands")
        await ctx.edit_original_response(content=f"Loaded {len(synced)} commands")


    @app_commands.command(name="test", description="Test")
    async def test(self, ctx: discord.Interaction):
        await ctx.response.send_message("Test", ephemeral=True)

        view = discord.ui.View()
        view.add_item(discord.ui.Button(label="test", style=discord.ButtonStyle.success, emoji="✅"))

        await ctx.edit_original_response(content="", view=view)







async def setup(client):
    await client.add_cog(MiscCog(client))