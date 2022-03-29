import setter
import discord
from discord.commands import slash_command
from discord.ext import commands

class Information(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    with open('extension/data.txt','r') as f:
        datalist = [line.strip() for line in f]


    information_set = discord.SlashCommandGroup('lore', 'Commands which retrieve Nuremberg lore', guild_ids=[setter.GUILD_ID])

    @information_set.command(description='Information about Nuremberg')
    async def nuremberg(self, ctx: discord.ApplicationContext):
        return await ctx.respond('Command is currently WIP')

    
    # @information_set.command(description='Information about Totally')
    # async def totally(self, ctx: discord.ApplicationContext):
    #     return await ctx.respond('Command is currently WIP')

    # @information_set.command(description='Information about Patrick')
    # async def patrick(self, ctx: discord.ApplicationContext):
    #     return await ctx.respond('Command is currently WIP')

    # @information_set.command(description='Information about Dante')
    # async def dante(self, ctx: discord.ApplicationContext):
    #     return await ctx.respond('Command is currently WIP')

    # @information_set.command(description='Information about Gabe')
    # async def gabe(self, ctx: discord.ApplicationContext):
    #     return await ctx.respond('Command is currently WIP')

    # @information_set.command(description='Information about Check')
    # async def check(self, ctx: discord.ApplicationContext):
    #     return await ctx.respond('Command is currently WIP')
    


    @slash_command(
        guild_ids=[setter.GUILD_ID],
        description='is the bot working?'
        )
    async def ping(self, ctx: discord.ApplicationContext):
        return await ctx.respond('pong')

    f.close()

def setup(bot):
    bot.add_cog(Information(bot))
