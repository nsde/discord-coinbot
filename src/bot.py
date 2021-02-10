# Load modules
try:
    import os
    import sys
    import json
    import yaml
    import random
    import discord

    from discord.ext import commands

except:
    print("Couldn't load all the libaries. Please install the libaries listed in <root>/requirements.txt.")
    sys.exit(0)

# Some basic defenitions
CWD = os.getcwd()
TOKEN = open(CWD + "\\config\\token.txt").read()
print(TOKEN)

# Set token
def tokenError():
    print("Please type in a valid bot token.\n\nThe token can be found at config/token.txt. Remember to not give anyone access to this secret file!")
    set_token = input("Token: ")
    with open (CWD + "\\config\\token.txt", "w") as f:
        token = f.write(set_token)

try:
    with open (CWD + "\\config\\token.txt") as f:
        token = f.read()
    print("Token loaded. Length: " + str(len(token)))

    if token == "":
        tokenError()

except:
    tokenError()

# Load config
with open(CWD + '\\config\\config.yml') as f:
    config = yaml.load(f, Loader=yaml.FullLoader)

    def fixuml(x):
        """Fix wrong coding of äüö (German language only)"""
        return x.replace("Ã¤","ä").replace("Ã¶","ö").replace("Ã¼", "ü")

    def lang(x):
        return fixuml(random.choice(config["language"][x]))

    print(config)        

    # Def bot
    client = commands.Bot(command_prefix = config["main"]["prefix"])

with open(CWD + '\\data\\dailycoins.yml') as f:
    daily = yaml.load(f, Loader=yaml.FullLoader)

# Bot
@client.event
async def on_ready():
    print(f'\nLogged in as {client.user}\n')


@client.command(name='ping')
async def ping(ctx):
    await ctx.send('Ping!')


@client.command(name='say')
async def say(ctx, *args):
    var = ''
    for s in args:
        var += f'{s} '
    await ctx.send(var)


@client.command(name='user')
async def user(ctx):
    user = ctx.message.author
    mention = ctx.message.author.mention
    id = ctx.message.author.id
    await ctx.send(user)
    await ctx.send(mention)
    await ctx.send(id)


@client.command(name='stop')
@commands.has_permissions(administrator=True)
async def stop_bot(ctx):
    await ctx.send('Bot stoppt...')
    await client.close()

# Commands
@client.command(name='dailycoins', aliases=["dcoins"])
async def dailycoins(ctx):
    if ctx.message.author not in daily["blocked"]["coins"]:
        await ctx.send(lang("dailycoins") + "\n> +" + str(random.randint(config["currency"]["rarity_normal"]["min"], config["currency"]["rarity_normal"]["max"])) + " " + config["currency"]["symbols"]["currency_normal"])
        daily["blocked"]["coins"].append(ctx.message.author)
        with open(CWD + '\\config\\daily.yml', 'w') as f:
            daily_list = []
            daily_list.append(daily)
            yaml.dump(daily_list, f)
    else:
        await ctx.send(config["currency"]["symbols"]["error"] + " " + lang("dailyerror"))

# Run
try:
    client.run(token)

except:
    print("ERROR: Unable to run the client. Did you input a invalid token?")
    sys.exit(0)