import setter
import discord
from discord.commands import slash_command
from discord.ext import commands

class Cryptography(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
    
    @slash_command(guild_ids=[setter.GUILD_ID],description='Caesar shift cipher')
    async def caesarshift(self, ctx: discord.ApplicationContext, message: str, cipher: int):
        chars_map = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        output = ""
        for i in message:
            if(i.isalpha() is False):
                output += i
                continue
            offset = chars_map.index(i.lower()) + cipher%26
            if(offset >= 26):
                offset = offset%26
            if(i.isupper()):
                output += (chars_map[offset].upper())
            else:
                output += (chars_map[offset])
        return await ctx.respond(output)
    
    @slash_command(guild_ids=[setter.GUILD_ID],description='Vigenere cipher')
    async def vigenerecipher(self, ctx: discord.ApplicationContext, message: str, cipher: int):
        chars_map = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        output = ""
        cipher_string = str(cipher)
        for counter, i in enumerate(message):
            if(i.isalpha() is False):
                output += i
                continue
            cipher_pos = len(cipher_string)
            offset = chars_map.index(i.lower()) + int(cipher_string[counter%cipher_pos])
            if(offset >= 26):
                offset = offset%26
            if(i.isupper()):
                output += (chars_map[offset].upper())
            else:
                output += (chars_map[offset])
        return await ctx.respond(output)
    
def setup(bot):
    bot.add_cog(Cryptography(bot))
