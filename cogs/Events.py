import discord
import json
from config.function import *
from discord.ext import commands

class Events(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        await self.bot.change_presence(status=discord.Status.dnd, activity=discord.Activity(type=discord.ActivityType.playing, name="on Cogs"))
        print("Logged in as", self.bot.user)

    @commands.Cog.listener()
    async def on_member_join(self, member):
        with open('json/users.json', 'r') as f:
            users = json.load(f)

        await update_data(users, member)

        with open('json/users.json', 'w') as f:
            json.dump(users, f)

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return
        with open('json/users.json', 'r') as f:
            users = json.load(f)

        await update_data(users, message.author)
        await add_experience(users, message.author, 5)
        await level_up(users, message.author, message.channel)

        with open('json/users.json', 'w') as f:
            json.dump(users, f)


def setup(bot):
    bot.add_cog(Events(bot))