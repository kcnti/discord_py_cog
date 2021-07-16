from config.function import *
import json
import random
import datetime
import discord
from discord.ext import commands


class Eco(commands.Cog):
    '''Economy Commands'''
    def __init__(self,bot):
        self.bot = bot

    @commands.command()
    @commands.cooldown(1, 86400, commands.BucketType.user)
    async def daily(self, ctx):
        '''
        Get your daily reward
        '''

        prize = random.randint(1, 100)
        await add_balance(ctx.author.id, prize)
        await ctx.send("<@{}> just got {} coins 🎉".format(ctx.author.id, prize))

    @daily.error
    async def daily_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            cd = round(error.retry_after)
            cd = str(datetime.timedelta(seconds=cd)).split(':')
            msg = "<@{}>, you must wait :stopwatch: **{}H {}M {}S** until your next daily".format(ctx.author.id, cd[0], cd[1], cd[2])
            await ctx.send(msg)

    @commands.command()
    async def tip(self, ctx, member: discord.Member, amount : int):
        '''Tip your friends | tip <tag> <amount>'''

        if not await remove_balance(ctx.author.id, amount):
            await ctx.send("Not enough")

        await add_balance(member.id, amount)
        await ctx.send(f"<@{ctx.author.id}> just tip <@{member.id}> for {amount} coins")

    @tip.error
    async def tip_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("tip <tag> <amount>")

    @commands.command()
    async def balance(self, ctx):
        bal = await check_balance(ctx.author.id)
        await ctx.send(f"You have {bal} coins")

def setup(bot):
    bot.add_cog(Eco(bot))