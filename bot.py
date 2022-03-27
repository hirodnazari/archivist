import discord
from discord.ext import commands
import setter
import os

print('The archivist is waking up')

bot = commands.Bot(intents=discord.Intents.default())

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game('sort the info'))
    print('The archivist is ready to go')

bot.run(setter.TOKEN)