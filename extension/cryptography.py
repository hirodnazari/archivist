import setter
import discord
from discord.commands import slash_command
from discord.ext import commands

class Cryptography(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
    
    @slash_command(guild_ids=[setter.GUILD_ID],description='Caesar shift')
    async def caesarshift(self, ctx: discord.ApplicationContext, message: str, cipher: int):
        output = ""
        chars_map = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        for i in message:

            if(i.isalpha() is False):
                    output += i
                    continue
            curr_pos = chars_map.index(i.lower())
            offset = curr_pos + cipher%26
            if(curr_pos + cipher%26 >= 26):
                offset = offset%26
            if(i.isupper()):
                output += (chars_map[offset].upper())
            else:
                output += (chars_map[offset])
    
        return await ctx.respond(output)

def setup(bot):
    bot.add_cog(Cryptography(bot))
