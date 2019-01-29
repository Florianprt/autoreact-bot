import discord
from discord.ext    import commands
from discord.ext.commands   import Bot
import asyncio
 
bot = commands.Bot(command_prefix='.')
 
@bot.event
async def on_ready():
    print ("ready")
 
 
@bot.event
async def on_message(message):
    if(message.channel.id == "530929543511539732") and(message.content == 'Dominion') :
        await bot.add_reaction(message, ":yes:531642641671258112")
        await bot.add_reaction(message, ":maybe:531642639406333953")
        await bot.add_reaction(message, ":no:531641945848676353")
 
 
bot.run("NTM5NTkxMDAxMDExMTI2Mjg1.DzEk7Q.s1mijnK5y2QqM0SIlSXUosEl7w8")
