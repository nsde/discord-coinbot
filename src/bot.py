import discord
from discord.ext import commands

TOKEN = "HIER DEN TOKEN EINFÜGEN"

bot = commands.Bot(command_prefix='!') # Command-Symbol

@bot.command(name='hallo')
async def halloSagen(ctx): # auf den Befehl "hören"
    await ctx.send("Hallo, du!")

@bot.command(name='bye')
async def byeSagen(ctx): # auf den Befehl "hören"
    await ctx.send("Bis dann!")

client.run(TOKEN) # Bot starten
