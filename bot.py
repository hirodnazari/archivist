import discord
from discord.ext import commands
import setter
import os

print('The archivist is waking up')

bot = commands.Bot(intents=discord.Intents.all())

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game('sort the info'))
    print('The archivist is ready to go')

for file in os.listdir('extension'):
    if not file.endswith('.py'):
        continue
    extension = file[:-3]
    print(f'loading extension.{extension}... ', end='')
    try:
        bot.load_extension('extension.' + extension)
    except Exception as e:
        exc = f'{type(e).__name__}: {e}'
        print(f'Failed to load extension {extension}\n{exc}')
    print('done')

bot.run(setter.TOKEN)