import discord
from discord.ext import commands
from discord.ext.commands.errors import MissingPermissions


class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def help(self, ctx):
        string = ""
        for cog in self.bot.cogs:
            if cog in ["Events", "Help"]: continue
            string += f"\n**{cog}**\n"
            for i in self.bot.get_cog(cog).get_commands():
                if not i.hidden:
                    string += f"> {i}\n"

        embed = discord.Embed(
            title = "All Commands",
            description = string
        )
        await ctx.send(embed=embed)

    @help.error
    async def help_error(self, ctx, error):
        if isinstance(error, MissingPermissions):
            string = ""
            for cog in self.bot.cogs:
                if cog in ["Events", "Help", "Moderation"]: continue
                string += f"\n**{cog}**\n"
                for i in self.bot.get_cog(cog).get_commands():
                    if not i.hidden:
                        string += f"> {i}\n"

            embed = discord.Embed(
                title = "All Commands",
                description = string
            )
            await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Help(bot))