import discord
import asyncio
from discord.ext import commands




class Moderation(commands.Cog):

    '''Moderate Commands'''

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, amount=1):
        '''clear messages'''
        async with ctx.typing():
            await asyncio.sleep(1)
        await ctx.channle.purge(limit=amount+1)


def setup(bot):
    bot.add_cog(Moderation(bot))