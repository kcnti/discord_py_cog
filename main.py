'''

CODED BY kcnti

Discord: Kanti#8338
Github: https://github.com/kcnti
Website: https://kanti.tk


'''



import os
import discord
from discord.ext import commands
from dotenv import load_dotenv


load_dotenv()
token = os.getenv("TOKEN")
intents = discord.Intents.default() # config on discord dev
intents.members = True
bot = commands.Bot(command_prefix="~", intents=intents)
bot.remove_command("help")

@bot.command()
async def reload(ctx):
    for i in os.listdir('./cogs'):
        if i.endswith('.py'):
            bot.unload_extension(f"cogs.{i[:-3]}")
            bot.load_extension(f"cogs.{i[:-3]}")

for i in os.listdir('./cogs'):
    if i.endswith('.py'):
            bot.load_extension(f"cogs.{i[:-3]}")

bot.run(token)
