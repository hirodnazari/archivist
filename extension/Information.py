import setter
import discord
from discord.commands import slash_command
from discord.ext import commands

class Information(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @slash_command(
        guild_ids=[setter.GUILD_ID],
        description='is the bot working?'
        )
    async def ping(self, ctx: discord.ApplicationContext):
        return await ctx.respond('pong')

def setup(bot):
    bot.add_cog(Information(bot))
