import discord
import requests
import datetime
import random
from discord.ext import commands
from itertools import cycle

class Commands(commands.Cog):
    """All Available Commands"""
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def covid(self, ctx, country="Thailand"):
        """Covid Today (Thailand by default)"""
        try:
            skipped = [
                'updated',
                'countryInfo',
                'activePerOneMillion',
                'recoveredPerOneMillion',
                'criticalPerOneMillion',
                'oneTestPerPeople',
                'oneDeathPerPeople',
                'oneCasePerPeople',
                'testsPerOneMillion',
                'tests',
                'deathsPerOneMillion',
                'casePerOneMillion'
            ]
            url = f"https://disease.sh/v3/covid-19/countries/{country}?yesterday=false&twoDaysAgo=false&strict=true&allowNull=false"
            data = requests.get(url)
            data = data.json()

            pfp = ctx.author.avatar_url
            embed = discord.Embed(
                title = "Covid-19 Today",
                description = f"[**API**]({url})",
            )

            embed.set_author(name=ctx.author.name, url=pfp, icon_url=pfp)
            embed.set_thumbnail(url=data['countryInfo']['flag'])
            embed.timestamp = datetime.datetime.utcnow()
            embed.set_footer(text='Covid-19', icon_url=self.bot.user.avatar_url)

            for i in data:
                if i in skipped:
                    continue
                embed.add_field(name=i, value=data[i], inline=True)
            
            await ctx.send(embed=embed)
        except:
            await ctx.send("Country not found or API error")
            raise

    @commands.command()
    async def poke(self, ctx, member: discord.Member, time=1):
        """Poke your friend"""
        try:
            if time > 5: return

            vc = ctx.guild.voice_channels
            listvc = []
            for i in vc: 
                listvc.append(i.id) # get all vc in guild
            fch_id = ctx.message.author.voice.channel # get user vc

            if listvc.index(fch_id.id)+1 >= len(listvc):
                sindex = listvc.index(fch_id.id) - 1
            else:
                sindex = listvc.index(fch_id.id) + 1
            
            sch = self.bot.get_channel(listvc[sindex])
            fch = self.bot.get_channel(fch_id.id)

            for i in range(time):
                await member.move_to(sch)
                await member.move_to(fch)

        except:
            await ctx.send("User is not connected")

    @commands.command()
    async def lookup(self, ctx, member: discord.Member):
        '''lookup your discord'''
        try:
            user = await self.bot.fetch_user(member.id)
            pfp = member.avatar_url
            embed = discord.Embed(
                title = f"Discord Lookup | {member.name}"
            )
            embed.add_field(
                name="uid",
                value=f"{user.id}",
                inline=False
            )
            embed.add_field(
                name="name",
                value=f"{user.name}#{user.discriminator}",
                inline=False
            )
            embed.add_field(
                name="created_at",
                value=f"{user.created_at}",
                inline=False
            )
            embed.set_image(
                url=pfp
            )
            embed.timestamp = datetime.datetime.utcnow()
            embed.set_footer(text='Discord Lookup', icon_url=pfp)
            await ctx.send(embed=embed)
        except:
            await ctx.send("Unable to fetch user information")


def setup(bot):
    bot.add_cog(Commands(bot))

