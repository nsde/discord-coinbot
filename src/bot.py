import os
import sys
import yaml #pip install pyyaml
import random
import discord #pip install discord
import asyncio

from discord.ext import commands

# Some basic defenitions
CWD = os.getcwd()
TOKEN = open(CWD + '/config/token.txt').read()
print(TOKEN)

# Set token
def tokenError():
    print('Please type in a valid bot token.\n\nThe token can be found at config/token.txt. Remember to not give anyone access to this secret file!')
    token = ''
    token = input('Token: ')
    with open (CWD + '/config/token.txt', 'w') as f:
      f.write(token)

try:
    with open (CWD + '/config/token.txt') as f:
        token = f.read()
    print('Token loaded. Length: ' + str(len(token)))
    if token == '':
        tokenError()
except:
    tokenError()

# Load config
with open(CWD + '/config/config.yml') as f:
    config = yaml.load(f, Loader=yaml.FullLoader)

    def fixuml(x):
        '''Fix wrong coding of äüö (German language only)'''
        return x.replace('Ã¤','ä').replace('Ã¶','ö').replace('Ã¼', 'ü')

    def lang(x):
        return fixuml(random.choice(config['language'][x]))

    # Def bot
    client = commands.Bot(command_prefix = config['main']['prefix'])

with open(CWD + '/data/dailycoins.yml') as f:
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
@client.command(name='dailycoins', aliases=['dcoins'])
async def dailycoins(ctx):
    if ctx.message.author not in daily['blocked']['coins']:
        await ctx.send(lang('dailycoins') + '\n> +' + str(random.randint(config['currency']['rarity_normal']['min'], config['currency']['rarity_normal']['max'])) + ' ' + config['currency']['symbols']['currency_normal'])
        daily['blocked']['coins'].append(ctx.message.author)
        with open(CWD + '/config/daily.yml', 'w') as f:
            daily_list = []
            daily_list.append(daily)
            yaml.dump(daily_list, f)
    else:
        await ctx.send(config['currency']['symbols']['error'] + ' ' + lang('dailyerror'))

@client.command(name='tempcreate', aliases=['tcreate', 'tempc', 'tcc'], help='Create a temporary channel.', usage='[v|t] <time>(s) (<name>)')
async def tempchannel(ctx, ctype=None, timeout=None, cname=None):
  if cname is None:
    cname = f'⏳│{ctx.message.author.display_name[:13].lower()}-{timeout}'
  else:
    cname = "⏳│" + str(cname) 
  
  await ctx.send(f'''
  :wrench: Creating channel...
  > **Type:** {ctype}
  > **Timeout:** {timeout}
  > **Channel name:** {cname}
  ''', delete_after=3)


  if not ctype:
    await ctx.send(':x: **ERROR:** No channel type argument is given. Channel type can only be `t(ext)` or `v(oice)`.')
    return

  if timeout is None and ctype[0] != 'v':
    await ctx.send(':x: **ERROR:** Only voice channels don\'t need a timeout. Therefore, please give a valid timout argument.')
    return

  if ctype is None:
    await ctx.send(':x: **ERROR:** No channel type argument is given. Channel type can only be `t(ext)` or `v(oice)`.')
    return

  elif ctype[0] == 't':
    await ctx.send(f':white_check_mark: Created text channel ***#{cname}*** with timeout ***{timeout}***.')
    category = ctx.channel.category
    channel = await ctx.guild.create_text_channel(cname, category=category)
    if timeout[-1] == 's':
      timeout = timeout.replace('s', '')
      await asyncio.sleep(int(timeout))
      await channel.delete()
    elif timeout[-1] == 'm':
      timeout = timeout.replace('m', '')
      await asyncio.sleep(float(round(int(timeout)*60)))
      await channel.delete()
    else:
      await asyncio.sleep(float(round(int(timeout)*60)))
      await channel.delete()

  elif ctype[0] == 'v':
    await ctx.send(f':white_check_mark: Created voice channel ***#{cname}*** with timeout ***{timeout}***.')
    category = ctx.channel.category
    channel = await ctx.guild.create_voice_channel(cname, category=category)
    while True:
      if len(channel.members) == 0:
        if timeout[-1] == 's':
          timeout_temp = timeout.replace('s', '')
          await asyncio.sleep(int(timeout_temp))
          if len(channel.members) == 0:
            await channel.delete()
            break
        elif timeout[-1] == 'm':
          timeout_temp = timeout.replace('m', '')
          await asyncio.sleep(float(round(int(timeout_temp)*60)))
          if len(channel.members) == 0:
            await channel.delete()
            break
        else:
          await asyncio.sleep(float(round(int(timeout)*60)))
          if len(channel.members) == 0:
            await channel.delete()
            break
  else:
    await ctx.send(':x: **ERROR:** No channel type argument is given. Channel type can only be `t(ext)` or `v(oice)`.')
    return

@client.command(name='tempuserlimit', aliases=['tul', 'tempul', 'tcul'], help='Edit a voice channel\'s user limit.', usage='<limit>')
async def tempchannel(ctx, limit=None):
  if not limit:
    limit = 0
  limit = int(limit)
  channel = ctx.author.voice.channel
  if limit < 2:
    limit = len(channel.members)
  if ctx.author.voice and ctx.author.voice.channel:
    await channel.edit(user_limit=limit)
    await ctx.send(f'''
      :white_check_mark: New user limit for ***{channel.name}*** is **{limit}**.
      Keep in mind that users with certain permissions can bypass this restriction.''')
  else:
    await ctx.send(':x: **ERROR:** Please join a voice channel to change its userlimit and try again.')
    return

# Run
try:
    client.run(token)

except:
    print('ERROR: Unable to run the client. Did you input a invalid token?')
    sys.exit(0)