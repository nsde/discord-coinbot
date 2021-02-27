import os
import sys
import yaml #pip install pyyaml
import time
import pytube #pip install pytube | for downloading YouTube videos and reading their data
import random
import shutil
#pip install PyNaCl
import discord #pip install discord
import asyncio
import datetime
import meme_get #pip install meme_get | for gags/jokes-commands
import deep_translator #pip install deep_translator | for translating-commands

import youtubesearchpython as ysp #pip install youtube-search-python | for YouTube-Search

from discord.ext import commands #pip install discord.py | For an advanced version of the "normal" discord libary

# stuff
CWD = os.getcwd()
TOKEN = open(CWD + '/config/token.txt').read()

# temp
temp_path = CWD + '/temp'
try:
  shutil.rmtree(temp_path)
  os.mkdir(temp_path)
except Exception as e:
  print('Temp error\n\n', e)

# set token
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
  config = yaml.load(f, Loader=yaml.SafeLoader)

  def fixuml(x):
      '''Fix wrong coding of äüö (German language only)'''
      return x.replace('Ã¤','ä').replace('Ã¶','ö').replace('Ã¼', 'ü')

  def lang(x):
      return fixuml(random.choice(config['language'][x]))

  # Def bot
  client = commands.Bot(command_prefix = config['main']['prefix'])

with open(CWD + '/data/dailycoins.yml') as f:
  daily = yaml.load(f, Loader=yaml.SafeLoader)

# Bot
@client.event
async def on_ready():
  print(f'\nLogged in as {client.user}\n')
  await client.change_presence(activity=discord.Game(name='.help | visit bit.ly/nevi'))

# @client.event
# async def on_command_error(ctx, error):
#   error_msg = 'Unknown error.'

#   if isinstance(error, commands.MissingRequiredArgument):
#     error_msg = 'Please follow the syntax.\nYou can use `.help <command>` for information.'
#   if isinstance(error, commands.TooManyArguments):
#     error_msg = 'You passed too many arguments. You can use `.help` for information'
#   if isinstance(error, commands.Cooldown):
#     error_msg = 'Please wait. You are on a cooldown.'
#   # if isinstance(error, commands.CommandError):
#   #   error_msg = 'There was an error with this command.'
#   if isinstance(error, commands.MessageNotFound):
#     error_msg = 'I couldn\'t find this message.'
#   if isinstance(error, commands.ChannelNotFound):
#     error_msg = 'I couldn\'t find this channel.'
#   if isinstance(error, commands.UserInputError):
#     error_msg = 'I couldn\'t find this user.'
#   if isinstance(error, commands.ChannelNotFound):
#     error_msg = 'I couldn\'t find this channel.'
#   if isinstance(error, commands.NoPrivateMessage):
#     error_msg = 'Sorry, I can\'t send you private messages.\nLooks like you have disabled them.'
#   if isinstance(error, commands.MissingPermissions):
#     error_msg = 'Sorry, you don\'t have the role permissions for this.'
#   if isinstance(error, commands.BotMissingPermissions):
#     error_msg = 'Sorry, I don\'t have permissions to do this.'
#   if isinstance(error, commands.ExtensionError):
#     error_msg = 'I apologize, but I couldn\'t load the needed extension.'
#   if isinstance(error, commands.CheckFailure):
#     error_msg = 'Sorry, you don\'t have the permissions for this.'
#   if isinstance(error, commands.BadArgument):
#     error_msg = 'You gave an invalid agument. Please check if it\'s correct.'

#   await ctx.send(f':x: **ERROR**\n{error_msg}')

@client.command(name='stats', help='Get statistics about this bot.')
async def stats(ctx):
  await ctx.send(f':heart: A big **thank you** for **{len(client.guilds)}** servers using my bot!')

@client.command(name='ping', help='Get statistics about the connection and latency.')
async def ping(ctx):
  old = time.mktime(ctx.channel.last_message.created_at.timetuple())
  new = datetime.datetime.timestamp(datetime.datetime.now())

  voice = discord.utils.get(client.voice_clients, guild=ctx.guild)

  await ctx.send('**__Ping Stats__**')
  await ctx.send('> :desktop: **Client:** ' + str(round(client.latency * 1000, 2)) + 'ms')
  # await ctx.send('> :chart_with_upwards_trend: **Response time:** ' + str(round(((new - old) - 3000 ) * 1, 2)) + 'ms')
  try:
    await ctx.send('> :loud_sound: **Audio latency:** ' + str(round(voice.latency * 1000, 2)) + 'ms')
  except:
    await ctx.send('> :loud_sound: **Audio latency:** *[deactivated]*')
  

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
  msg_id = ctx.message.author.id
  await ctx.send(user)
  await ctx.send(mention)
  await ctx.send(msg_id)

@client.command(name='terminate')
@commands.has_permissions(administrator=True)
async def quit(ctx):
  await ctx.send('Terminating Bot...')
  await client.close()

@client.command(name='translate', aliases=['tl'], help='Translate a text!', usage='<to_lang> <text>')
async def translate(ctx, *args):
  to_lang = args[0].lower()
  text = ' '.join(args[1:])
  translated = deep_translator.GoogleTranslator(source='auto', target=to_lang).translate(text)
  await ctx.send(translated)

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

@client.command(name='meme', help='Shows a random meme. Specify "load count" to a high number to get more unique memes.', usage='(load_count)')
async def meme(ctx, load_count=None):
  meme_loader = meme_get.RedditMemes()
  if not load_count:
    load_count = 100
  meme_list = meme_loader.get_memes(load_count)

  meme_data = random.choice(meme_list)
  if meme_data._caption:
    caption = meme_data._caption
  else:
    caption = ''
  await ctx.send(caption + meme_data._pic_url)

@client.command(name='tempcreate', aliases=['tcreate', 'tempc', 'tcc'], help='Creates a temporary channel.', usage='[v|t] <time>(s) (x)')
async def tempchannel(ctx, ctype=None, timeout=None, afk_timer=None):
  cname = f'⏳│{ctx.message.author.display_name[:13].lower()}-{timeout}'
  
  if not afk_timer:
    afk_timer = True
  else:
    afk_timer = False

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

  if timeout[-1] == 's':
    timeout = int(timeout.replace('s', ''))
  else:
    timeout = int(timeout.replace('m', ''))
    timeout *= 60

  category = ctx.channel.category

  if ctype[0] == 't':
    await ctx.send(f':white_check_mark: Created text channel ***#{cname}*** with timeout ***{timeout}***.')
    
    try:
      channel = await ctx.guild.create_text_channel(cname, category=category)
    except discord.errors.Forbidden as e:
      await ctx.send(f':x: **ERROR:** Sorry, I don\'t have the permissions for this. Error:\n{e}')
      return

    if afk_timer:
      # checks if there are new messages
      difference = 0
      last_saved = 0 # last 'saved' message id
      while difference <= timeout:
        # check
        await asyncio.sleep(1)
        if channel.last_message_id:
          # the channel is not empty
          message = channel.last_message_id
          if last_saved == message:
            # same message
            difference += 1
          else:
            # new message
            difference = 0
            last_saved = message
        else:
          # the channel is empty
          difference += 1
    else:
      await asyncio.sleep(timeout)
    await channel.delete()


  elif ctype[0] == 'v':
    try:
      channel = await ctx.guild.create_voice_channel(cname, category=category)
      await ctx.send(f':white_check_mark: Created voice channel ***#{cname}*** with timeout ***{timeout}***.')
    except discord.errors.Forbidden as e:
      await ctx.send(f':x: **ERROR:** Sorry, I don\'t have the permissions for this. Error:\n{e}')
      return

    if afk_timer:
      timer = 0
      while timer < timeout:
        await asyncio.sleep(1)     
        if len(channel.members) == 0:
          timer += 1
        else:
          timer = 0
    else:
      await asyncio.sleep(timeout)
    await channel.delete()

    '''Code by @beban09'''
    # while True:
    #   if len(channel.members) == 0:
    #     if timeout[-1] == 's':
    #       timeout_temp = timeout.replace('s', '')
    #       await asyncio.sleep(int(timeout_temp))
    #       if len(channel.members) == 0:
    #         await channel.delete()
    #         break
    #     elif timeout[-1] == 'm':
    #       timeout_temp = timeout.replace('m', '')
    #       await asyncio.sleep(float(round(int(timeout_temp)*60)))
    #       if len(channel.members) == 0:
    #         await channel.delete()
    #         break
    #     else:
    #       await asyncio.sleep(float(round(int(timeout)*60)))
    #       if len(channel.members) == 0:
    #         await channel.delete()
    #         break

  else:
    await ctx.send(':x: **ERROR:** No channel type argument is given. Channel type can only be `t(ext)` or `v(oice)`.')
    return

@client.command(name='tempuserlimit', aliases=['tul', 'tempul', 'tcul'], help='Edits a voice channel\'s user limit.', usage='<limit>')
async def tempuserlimit(ctx, limit=None):
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

@client.command(name='execute', aliases=['exe', 'exec', 'exc'], help='Execute Python code.', usage='<code>')
async def execute(ctx, code):
  try:
    output = exec(code.replace('&', ' '))
  except Exception as e:
    output = f'There was an error executing this command:\n{e}\nTip: Use `&` to make spaces.'

  await ctx.send(
  f'''
  ```py
  {output}
  ```
  ''')

@client.command(name='playsong', aliases=['play', 'psong', 'ps'], help='Executes Python code.', usage='<search>')
async def playsong(ctx, *args):
  print('Start')

  if not args:
    await  ctx.send(':x: **ERROR** No argument for the search term given.')
    return    
  try:
    result = ysp.VideosSearch(' '.join(args), limit=1).result()['result'][0]
  except Exception as e:
    await  ctx.send(f':x: **ERROR** Sorry, I couldn\'t find videos on YouTube with that search term. Error:\n`{e}`')
    return

  print('Before video check')


  url = result['link']

  data = ysp.Video.getInfo(url, mode=ysp.ResultMode.dict)

  video_id = data['id']
  title = data['title']
  views = data['viewCount']['text']

  if int(views) > 1000000000:
    views = str(round(int(views)/1000000000, 1)) + 'b'

  elif int(views) > 1000000:
    views = str(round(int(views)/1000000, 1)) + 'm'

  elif int(views) > 1000:
    views = str(round(int(views)/1000, 1)) + 'k'
  
  views = views.replace('.', ',')

  channel = data['channel']['name']
  upload_date = data['uploadDate']
  description = data['description'][:100] + ' *[...]*'

  easteregg_videos = ['dQw4w9WgXcQ', 'ub82Xb1C8os', 'iik25wqIuFo', 'YddwkMJG1Jo', '8ybW48rKBME', 'dRV6NaciZVk', 'QB7ACr7pUuE', 'll-mQPDCn-U', 'ehSiEHFY5v4', '-51AfyMqnpI',
  'Tt7bzxurJ1I', 'fC7oUOUEEi4', 'O91DT1pR1ew']

  if video_id in easteregg_videos:
    description = 'No, not again.'

  print('Before embed')

  embed = discord.Embed(title=title, colour=discord.Colour(0x20b1d5), url=url, description=description)
  # embed.set_thumbnail(url=thumbnail)
  embed.add_field(name='__Channel__', value=channel, inline=True)
  # embed.add_field(name='__Duration__', value=duration], inline=True)
  embed.add_field(name='__Views__', value=views, inline=True)
  embed.add_field(name='__Uploaded__', value=upload_date, inline=True)
  
  globals()['embed'] = embed
  await ctx.send(embed=embed)

# ==============================================================================================================

  print('After embed')

  filetype = 'webm'
  filename = video_id

  song_there = os.path.isfile(CWD + '\\temp\\' + filename + '.' + filetype)
  try:
      if song_there:
          os.remove(CWD + '\\temp\\' + filename + '.' + filetype)
  except PermissionError:
      await ctx.send(':x: **ERROR** Wait for the current playing music to end or use the \'stop\' command')
      return

  print('After song overwrite check')

  try:
    channel = ctx.author.voice.channel
  except:
    await ctx.send(':x: **ERROR:** Please join a voice channel and try again.')
    return

  if ctx.author.voice and ctx.author.voice.channel:
    pass
  else:
    await ctx.send(':x: **ERROR:** Please join a voice channel and try again.')
    return
  
  print('Before client connect')

  try:
    await channel.connect()
  except:
    pass

  # Download

  print('Before download')

  video_stream = pytube.YouTube(url).streams.filter(file_extension=filetype, only_audio=True).first()

  await ctx.send(f':arrow_down: Downloading...\n```{video_stream}```', delete_after=3)

  video_stream.download(output_path=temp_path, filename=filename)  

  print('After download')

  try:
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    voice.play(discord.FFmpegPCMAudio(executable='C:/ffmpeg/ffmpeg.exe', source=temp_path + '\\' + filename + '.' + filetype))
    voice.source = discord.PCMVolumeTransformer(voice.source)
    voice.source.volume = 0.07
  except Exception as e:
    print(f'Couldn\'t play the song. I believe FFMPEG has not been installed correctly.\n{e}')
    await ctx.send(f'x: **CLIENT ERROR** An error occured on the system hosting this bot.\n{e}')

  print('After playing start')


@client.command(name='pausesong', aliases=['pause', 'resume'], help='Pauses or resumes a song.')
async def pause(ctx):
  voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
  if voice.is_playing():
    voice.pause()
  else:
    voice.resume()

@client.command(name='move', help='Move the voice client to another channel.')
async def move(ctx):
  channel = ctx.author.voice.channel
  try:
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    voice.pause()
    await asyncio.sleep(0.7) # The delays are because it crashes otherwise.
    await voice.move_to(channel)
    await asyncio.sleep(0.7) # I tried a lot and think that 0.7s is the best delay.
    voice.resume()
  except Exception as e:
    await ctx.send(f':x: **ERROR** Couldn\'t move the voice client to your channel. Please join a voice channel and try again. Error:\n{e}')
    return

@client.command(name='stopsong', aliases=['stop', 'xs'])
async def stopsong(ctx):
  voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
  voice.stop()

@client.command(name='songname', aliases=['musicname', 'sn'], help='What song is currently being played?')
async  def songname(ctx):
  try:
    await ctx.send(f'Currently playing:', embed=embed)
  except:
    await ctx.send('No song is currently playing.')

@client.command(name='clear', aliases=['cls'], help='Clears the last x messages from a channel.', usage='<amount>')
async def clear(ctx, amount : int):
  await ctx.channel.purge(limit=amount)
  await ctx.send(f':white_check_mark: I deleted **{amount}** messages.', delete_after=3)

# Run
try:
  client.run(token)
except:
  print('ERROR: Unable to run the client. Did you input a invalid token?')
  sys.exit(0)