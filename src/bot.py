'''Imports of self-made modules'''
import padlet

'''Regular imports'''
import os
import io
import ast
import sys
import yaml #pip install pyyaml | for config files
import time
import gtts #pip install gtts | for text to speech
import string
import pytube #pip install pytube | for downloading YouTube videos and reading their data
import random
import shutil
import socket
import mojang #pip install mojang | API for Minecraft
#pip install PyNaCl | for voicechannel support
import discord #pip install discord | for bot-system
import asyncio
import requests #pip install requests | 
import datetime
try:
  import colorama #pip install colorama | for colored text
except:
  os.system('pip install colorama')
  import colorama
try:
  import meme_get #pip install meme_get | for gags/jokes-commands
except:
  os.system('pip install future')
  import meme_get
import xmltodict #pip install xmltodict | The name says it.
import langdetect #pip install langdetect | to detect langauges in a string
import skingrabber #pip install skingrabber | to render skins
import googlesearch #pip install google | to search something on the web
import geizhalscrawler #pip install geizhalscrawler | for product data (price, etc.)
import deep_translator #pip install deep_translator | for translating-commands

'''Imports with abbrevations'''
import youtubesearchpython as ysp #pip install youtube-search-python | for YouTube-Search

'''From-Imports'''
from discord.ext import commands #pip install discord.py | For an advanced version of the "normal" discord libary
from PIL import Image, ImageFilter #pip install pillow | for image modification | sorry for importing in this that way, but see https://stackoverflow.com/questions/11911480/python-pil-has-no-attribute-image

'''Constants'''
VERSION = '0.0.1'
CWD = os.getcwd().replace('\\', '/')
if CWD.split('/')[-1] == 'src':
  CWD = '/'.join(CWD.split('/')[:-1])

chatbot_history = ['']

temp_path = CWD + '/temp'
try:
  shutil.rmtree(temp_path)
except Exception as e:
  pass
finally:
  os.mkdir(temp_path)

try:
  token = open(CWD + '/config/token.txt').read()
  if token == '':
    print('ERROR - Token (config/token.txt) is empty.')
    sys.exit(-1)
  else:
    print('Token loaded. Length: ' + str(len(token)))
except Exception as e:
  try:
    token = os.getenv('token')
  except:
    print(colorama.Fore.YELLOW + 'Token file not found. Creating one...')
    token = input(colorama.Fore.BLUE + 'Please type in the Discord bot token: ')
    open(CWD + '/config/token.txt', 'w').write(token)    
finally:
  print(colorama.Style.RESET_ALL)

with open(CWD + '/config/config.yml') as f:
  config = yaml.load(f, Loader=yaml.SafeLoader)

  def fixuml(x):
    '''Fix wrong coding of äüö (German language only)'''
    return x.replace('Ã¤','ä').replace('Ã¶','ö').replace('Ã¼', 'ü')

  client = commands.Bot(command_prefix = config['main']['prefix'])

@client.event
async def on_ready():
  print(f'\nLogged in as {client.user}\n')
  helpcmd = commands.HelpCommand
  await client.change_presence(activity=discord.Game(name='.help | visit bit.ly/nevi'))

@client.event
async def on_command_error(ctx, error):
  error_msg = 'Unknown error.'
  if isinstance(error, commands.CommandNotFound):
    error_msg = 'This command does not exist. Use **`.info`** for information.'

#   if isinstance(error, commands.MissingRequiredArgument):
#     error_msg = 'Please follow the syntax.\nYou can use `.help <command>` for information.'
#   if isinstance(error, commands.TooManyArguments):
#     error_msg = 'You passed too many arguments. You can use `.help` for information'
#   if isinstance(error, commands.Cooldown):
#     error_msg = 'Please wait. You are on a cooldown.'
#    if isinstance(error, commands.CommandError):
#     error_msg = 'There was an error with this command.'
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

  if error_msg != 'Unknown error.':
    await ctx.send(f':x: **ERROR** - {error_msg}')

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
    await ctx.send('> :loud_sound: **Audio latency:** *[inactive]*')
  if socket.gethostname().count('-') != 4:
    await ctx.send(f'> :gear: Private computer name: {socket.gethostname()}')
  else:
    await ctx.send(f'> :gear: Heroku computer name: {socket.gethostname()}')

@client.command(name='info', help='Information, useful commands & links for this bot.')
async def info(ctx):
  embed = discord.Embed(title='NeoVision Bot Info', color=discord.Colour(0x0094FF), description='''
  **Useful Commands**
    `.commands`
    `.ping`
    `.help`

  **Links**
    [GitHub](https://bit.ly/nevi)
    [Readme](https://github.com/nsde/neovision/blob/main/README.md)
  ''')
  icon = ''
  embed.set_footer(text=f'Ping: {str(round(client.latency * 1000, 2))}ms', icon_url=icon)
  
  await ctx.send(embed=embed)

@client.command(name='user', help='Get information about an user.')
async def user(ctx):
  user = ctx.message.author
  mention = ctx.message.author.mention
  msg_id = ctx.message.author.id
  await ctx.send('''
  user
  ''')
  await ctx.send(mention)
  await ctx.send(msg_id)
  await ctx.send(member.avatar_url)

@client.command(name='terminate', help='Stops the bot (administrator only)')
@commands.has_permissions(administrator=True)
async def quit(ctx):
  await ctx.send('Terminating Bot...')
  await client.close()
  exit()

@client.command(name='translate', aliases=['tl'], help='Translate a text!', usage='<to_lang> <text>')
async def translate(ctx, *args):
  to_lang = args[0].lower()
  text = ' '.join(args[1:])
  translated = deep_translator.GoogleTranslator(source='auto', target=to_lang).translate(text)
  await ctx.send(translated)

@client.command(name='price', aliases=['bestprice'], help='Get price information about a product on the internet.', usage='<country_code> <product>')
async def price(ctx, *args):
  await ctx.send('*Please wait...*', delete_after=3)

  country = args[0].lower()
  countries = ['at', 'eu', 'de', 'uk', 'pl']
  country_list = '` or `'.join(countries)
  if not country in countries:
    await ctx.send(
      f':x: **ERROR** Invalid country code argument. Country code can be: `{country_list}`')
    return

  product = ' '.join(args[1:])

  query = 'site:geizhals.eu ' + product

  try:
    for result in googlesearch.search(query, tld=country.lower(), num=1, stop=1, pause=2):
      url = result
  except:
    await ctx.send(':x: **ERROR** Sorry, there was an error while searching for the product. Try another country or product name.')
    return

  try:
    obj = geizhalscrawler.Geizhals(url, country.upper())
  except:
    await ctx.send(':x: **ERROR** Sorry, the bot is being **rate-limited**. ¯\_(ツ)_/¯\nThis means we have to wait...\nIn the meanwhile, listen to this instead:\n*[https://youtu.be/BezpUnoZObw]*')
    return
  product = obj.parse()

  embed = discord.Embed(title=f'**__{product.name[:100]}__**', colour=discord.Colour(0x2a5aff))
  icon = 'https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fs3-eu-west-1.amazonaws.com%2Ftpd%2Flogos%2F46d31a8a000064000500a7c8%2F0x0.png&f=1&nofb=1'
  embed.set_footer(text='Data without guarantee. Country: ' + country.upper(), icon_url=icon)
  embed.add_field(name=f'__URL__', value=url, inline=False)
  try:
    embed.add_field(name=f'__Lowest price__', value=str(product.prices[0]) + product.price_currency , inline=True)
    embed.add_field(name=f'__AVG price__', value=str(round(sum(product.prices)/len(product.prices), 2)) + product.price_currency, inline=True)
  except:
    embed.add_field(name=f'__Error__', value='Price not avaiable', inline=True)
  await ctx.send(embed=embed)

@client.command(name='padlet', help='Get posts from a padlet.com-page.', usage='<url>')
async def getpadlet(ctx, url=None):
  if not url:
    url = 'https://padlet.com/onlix/ha' # my Homework-Padlet
  padlet_posts = padlet.getpadlet(url, discord=True)

  posts = []
  for post in padlet_posts['posts']:
    posts.append(post['title'] + post['items'])

  title = padlet_posts['title']
  posts = '\n'.join(posts[-4:])
  await ctx.send(f'**__{title}__**{posts}')

@client.command(name='counting', aliases=['ct'], help='Get information about the counting system.')
async def counting(ctx):
  await ctx.send(
    f'''**__Counting Information__**
    *For help on how to setup a counting channel, see the docs and the readme on the GitHub page.*
    ''')

@client.command(name='minecraft', aliases=['mc', 'minecraftinfo', 'mcinfo'], help='Get information about a player.', usage='<playername>')
async def minecraft(ctx, name):
  uuid = mojang.MojangAPI.get_uuid(name)
  if not uuid:
    await ctx.send(':x: Invalid user.')
    return
  else:
    skin = mojang.MojangAPI.get_profile(uuid).skin_url

  skinrender = skingrabber.skingrabber()
  skinrendered = skinrender.get_skin_rendered(user=name)

  drop = mojang.MojangAPI.get_drop_timestamp(name)

  if not drop:
    drop = 'Not dropping.'
  else:
    drop = drop - time.time()
    drop = f'Dropping in: {drop} Seconds'

  embed = discord.Embed(title=name, colour=discord.Colour(0x009fff))
  embed.set_thumbnail(url=skinrendered)
  embed.add_field(name='UUID', value=uuid, inline=False)
  await ctx.send(embed=embed)

def getcoins(user):
  for line in open(CWD + '/data/coins.txt').readlines():
    if line.startswith(str(user.id)):
      return int(line.split()[1])
  open(CWD + '/data/coins.txt', 'a').write(f'\n{user} 0')
  return 0

def setcoins(user, amount):
  for line in open(CWD + '/data/coins.txt').readlines():
    if line.startswith(str(user.id)):
      open(CWD + '/data/coins.txt', 'w').write(open(CWD + '/data/coins.txt').read().replace(line, f'{user} {amount}'))
      return
  open(CWD + '/data/coins.txt', 'a').write(f'\n{user} {amount}')

@client.command(name='dailycoins', aliases=['dcoins', 'dc', 'dailyrewards'], help='Economy command to get daily coins.')
async def dailycoins(ctx):
  try:
    dailycoins_list = open(CWD + '/data/dailycoins.txt').readlines()
  except:
    open(CWD + '/data/dailycoins.txt', 'w').write('')
    dailycoins_list = open(CWD + '/data/dailycoins.txt').readlines()

  if str(ctx.message.author.id) not in dailycoins_list:
    amount = random.randint(config['currency']['rarity_normal']['min'], config['currency']['rarity_normal']['max'])
    await ctx.send('**Here, enjoy your daily coins!**\n> +' + str(amount) + ' ' + config['currency']['symbols']['currency_normal'])
    dailycoins_list.append(str(ctx.message.author.id))
    print('\n'.join(dailycoins_list))
    open(CWD + '/data/dailycoins.txt', 'w').write('\n'.join(dailycoins_list))
    setcoins(user=ctx.author, amount=getcoins(ctx.message.author) + amount)
  else:
    await ctx.send(':x: Sorry, I can\'t give you daily coins because you already claimed them today.')

@client.command(name='balance', aliases=['bal'], help='Get a user\'s account balance.')
async def balance(ctx, user:discord.Member=None):
  if not user:
    user = ctx.author
  
  await ctx.send(f'Account balance of  \'{user}\': {getcoins(user)}')

@client.command(name='meme', help='Shows a random meme. Specify "load count" to a high number to get more unique memes.', usage='(<load_count>)')
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

@client.command(name='image', aliases=['picture', 'img', 'pic'], help='Create a funny image of an user (you by default).', usage='<style> (<user>)')
async def image(ctx, style, user:discord.Member=None):
  if not user:
    user = ctx.author
  
  styles = {
    'business': [103, 310, 43],
    'rip': [151, 284, 378], # Thank you for the pictures: https://pixabay.com/photos/waterfall-water-river-silent-5138793/ and https://pixabay.com/photos/tombstone-grave-cemetery-gravestone-3385623/
    'wanted': [204, 156, 320], # Thank you for the pictures: https://pixabay.com/illustrations/wanted-poster-wanted-poster-west-1081663/
    'future': [290, 96, 312],
    'confusing': [290, 96, 312],
    }

  # Syntax: {'style_name': [resize_size, top_left_x, top_left_y]}. All 3 values represent the location of the profile-picture-square

  try:
    template = Image.open(f'{CWD}/data/images/{style}.png')
  except:
    style_list = ', '.join(styles.keys())
    await ctx.send(f':x: There is no such image template. Avaiable style templates: {style_list}.')
    return
  profile_pic = user.avatar_url_as(size=256)
  profile_pic_bytes = io.BytesIO(await profile_pic.read())
  profile_pic = Image.open(profile_pic_bytes)

  profile_pic = profile_pic.resize((styles[style][0], styles[style][0]))
  template.paste(profile_pic, (styles[style][1], styles[style][2]))

  filepath = f'{CWD}/temp/{user.id}.png'
  template.save(filepath)

  await ctx.send(file=discord.File(filepath))

@client.command(name='texttospeech', aliases=['tts', 'text2speech', 't2s'], help='Reads text in a voice channel.', usage='([en|de|fr]:) <text>')
async def texttospeech(ctx, *args):
  text = ' '.join(args)
  if not text:
    await ctx.send('There is no text...')
    return

  if args[0] in ['en:', 'de:', 'fr:']:
    lang = args[0].split(':')[0]
    text = ' '.join(args[1:])
  else:
    try:
      lang = langdetect.detect(text)
      if not lang in ['en', 'de', 'fr']:
        raise Exception
    except:
      lang = 'en'
    
  tts = gtts.gTTS(text, lang=lang)
  tts.save(f'{CWD}/temp/tts.mp3')
  
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

  try:
    await channel.connect()
  except:
    pass

  voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
  voice.play(discord.FFmpegPCMAudio(executable='C:/ffmpeg/ffmpeg.exe', source=f'{CWD}/temp/tts.mp3'))
  voice.source = discord.PCMVolumeTransformer(voice.source)
  voice.source.volume = 0.1


@client.command(name='tempcreate', aliases=['tcreate', 'tempc', 'tcc'], help='Creates a temporary channel.', usage='[v|t] <time>(s) (x)')
async def tempchannel(ctx, ctype=None, timeout=None, afk_timer=None):
  def getChannelName(ctx, timeout):
    return f'⏳│{ctx.message.author.display_name[:13].lower()}-{timeout}'
  
  cname = getChannelName(ctx=ctx, timeout=timeout)

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
            if timeout-difference <= 3:
              cname = getChannelName(ctx=ctx, timeout='❗')
              await channel.edit(name=cname)
              await channel.send(':warn: 3 seconds left!')
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
          if timeout-timer <= 3:
            cname = getChannelName(ctx=ctx, timeout='❗')
            await channel.edit(name=cname)
        else:
          timer = 0
    else:
      await asyncio.sleep(timeout)
    await channel.delete()
  else:
    await ctx.send(':x: **ERROR:** No channel type argument is given. Channel type can only be `t(ext)` or `v(oice)`.')
    return

@client.command(name='templimit', aliases=['tul', 'tempul', 'tcul'], help='Edits a voice channel\'s user limit.', usage='<limit>')
async def templimit(ctx, limit=None):
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

@client.command(name='playsong', aliases=['play', 'psong', 'ps'], help='Search and play song on YouTube.', usage='<search>')
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

  easteregg_videos = ['dQw4w9WgXcQ', 'ub82Xb1C8os', 'iik25wqIuFo', 'YddwkMJG1Jo',
  '8ybW48rKBME', 'dRV6NaciZVk', 'QB7ACr7pUuE', 'll-mQPDCn-U', 'ehSiEHFY5v4', '-51AfyMqnpI',
  'Tt7bzxurJ1I', 'fC7oUOUEEi4', 'O91DT1pR1ew', 'bxqLsrlakK8', 'oHg5SJYRHA0']

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

  filetype = 'webm'
  filename = video_id

  song_there = os.path.isfile(CWD + '/temp/' + filename + '.' + filetype)
  try:
      if song_there:
          os.remove(CWD + '/temp/' + filename + '.' + filetype)
  except PermissionError:
      await ctx.send(':x: **ERROR** Wait for the current playing music to end or use the \'stop\' command')
      return


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
  
  try:
    await channel.connect()
  except:
    pass

  # Download

  video_stream = pytube.YouTube(url).streams.filter(file_extension=filetype, only_audio=True).first()

  await ctx.send(f':arrow_down: Downloading...\n```{video_stream}```', delete_after=3)

  video_stream.download(output_path=temp_path, filename=filename)  

  try:
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    voice.play(discord.FFmpegPCMAudio(options='-loglevel panic', executable='C:/ffmpeg/ffmpeg.exe', source=temp_path + '/' + filename + '.' + filetype))
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

@client.command(name='stopsong', aliases=['stop', 'xs'], help='Stops a song without leaving.')
async def stopsong(ctx):
  voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
  voice.stop()

@client.command(name='songname', aliases=['musicname', 'sn'], help='What song is currently being played?')
async  def songname(ctx):
  try:
    await ctx.send(f'Currently playing:', embed=embed)
  except:
    await ctx.send('No song is currently playing.')

@client.command(name='blockabl', help='Get information about blockabl.')
async def blockabl():
  pass
 
chatbot_phrases = {
  'hi': 'Hello! :wink:',
  'hey': 'Hey! What\'s up? :wave:',
  'hello': 'Hi :wave:',
  'how are you': 'I\'m good, what about you? :+1:',
  'what are you doing': 'I\'m chatting with you! :joy:',
  'thank': 'You\'re welcome. :blush:',
  'lmao': ':sweat_smile:',
  'xd': ':grin:',
  'lol': ':laughing:',
}

context_phrases = [
  ['I\'m good, what about you? :+1:', 'good', 'I\'m glad to hear that!'],
]

intelligent_phrases = {
  'wiki': 'Wikipedia Search'
}

@client.command(name='chatbot', aliases=['cb'], help='Get information about the chatbot.', usage='[info|phrases]')
async def chatbot(ctx, *args):
  if len(args) == 0:
    await ctx.send(':x: Please give `info` or `phrases` as an argument.')
    return

  if args[0] == 'info':
    await ctx.send('''
    *Do **`.chatbot phrases`** to see all different input-possibilities.*

    **Normal Phrases (NP)**\n> NPs react every single time with pretty much the same thing, no matter the situation and context.

    **Context-Dependent Phrases (CDP)**\n> CDPs can react different at each situation. They can check the last messages and think of what to say now.

    **Intelligent Phrases (IP)**\n> IPs can react with a scientific solution to a question. For example, they can calculate or search something on the internet.
    ''')

  cdp_list = []
  for i in context_phrases:
    cdp_list.append(i[0])

  if args[0] == 'phrases':
    await ctx.send(
      f'''
      __**ChatBot**__
      *Do **`.chatbot info`** to see what the difference between the phrases are.*

      __Normal Phrases__
      `{'`, `'.join(chatbot_phrases.keys())}`

      __Context-Dependent Phrases__
      `{'`, `'.join(cdp_list)}`

      __Intelligent Phrases__
      `{'`, `'.join(intelligent_phrases.keys())}`
      ''')

@client.command(name='clear', aliases=['cls'], help='Clears the last x messages from a channel.', usage='<amount>')
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount : int):
  await ctx.channel.purge(limit=amount)
  await ctx.send(f':white_check_mark: I deleted **{amount}** messages.', delete_after=3)

@client.event
async def on_message(message):
  bridge_names = ['nv-bridge', '𝔫𝔳-𝔟𝔯𝔦𝔡𝔤𝔢', '𝖓𝖛-𝖇𝖗𝖎𝖉𝖌𝖊', '𝓷𝓿-𝓫𝓻𝓲𝓭𝓰𝓮', '𝓃𝓋-𝒷𝓇𝒾𝒹𝑔𝑒', '𝕟𝕧-𝕓𝕣𝕚𝕕𝕘𝕖', '𝘯𝘷-𝘣𝘳𝘪𝘥𝘨𝘦', '𝙣𝙫-𝙗𝙧𝙞𝙙𝙜𝙚', '𝚗𝚟-𝚋𝚛𝚒𝚍𝚐𝚎', '𝐧𝐯-𝐛𝐫𝐢𝐝𝐠𝐞', 'ᑎᐯ-ᗷᖇᎥᗪǤᗴ'] # channel names for bridges can be...
  chatbot_names = ['nv-chatbot', '𝔫𝔳-𝔠𝔥𝔞𝔱𝔟𝔬𝔱', '𝖓𝖛-𝖈𝖍𝖆𝖙𝖇𝖔𝖙', '𝓷𝓿-𝓬𝓱𝓪𝓽𝓫𝓸𝓽', '𝓃𝓋-𝒸𝒽𝒶𝓉𝒷𝑜𝓉', '𝕟𝕧-𝕔𝕙𝕒𝕥𝕓𝕠𝕥', '𝘯𝘷-𝘤𝘩𝘢𝘵𝘣𝘰𝘵', '𝙣𝙫-𝙘𝙝𝙖𝙩𝙗𝙤𝙩', '𝚗𝚟-𝚌𝚑𝚊𝚝𝚋𝚘𝚝', '𝐧𝐯-𝐜𝐡𝐚𝐭𝐛𝐨𝐭', 'ᑎᐯ-ᑕᕼᗩ丅ᗷᗝ丅']
  counting_names = ['nv-counting']
  if not message.author.bot:
    for bridge_name in bridge_names:
      if message.channel.topic:
        if bridge_name in message.channel.topic:
          for guild in client.guilds:
            for textchannel in guild.text_channels:
              for bridge_name in bridge_names:
                if textchannel.topic:
                  if bridge_name in textchannel.topic:
                    if message.channel.id != textchannel.id:
                      if textchannel.topic.split('-')[-1] == message.channel.topic.split('-')[-1]:
                        await textchannel.send(f'**[{message.guild.name}] {message.author}** » {message.content}')

    for chatbot_name in chatbot_names:
      if message.channel.topic:
        if chatbot_name in message.channel.topic:

          response = chatbot_history[-1]

          phrase_num = 0
          for phrase in context_phrases:
            if response == phrase[0]:
              if phrase[1] in message.content.lower():
                response = phrase[2]
                await message.channel.send(response)
                chatbot_history.append(response)
                break
            phrase_num += 1

          for phrase in chatbot_phrases.keys():
            if phrase in message.content.lower():
              response = chatbot_phrases[phrase]
              await message.channel.send(response)
              chatbot_history.append(response)
              break
      
    for counting_name in counting_names:
      if message.channel.topic:
        if counting_name in message.channel.topic:
          msg_count = 0
          async for h_message in message.channel.history(limit=2):
            if msg_count == 1:
              if message.author.id == h_message.author.id:
                await message.delete()
              try:
                if int(h_message.content) + 1 != int(message.content):
                  try:
                    await message.delete()
                  except:
                    pass
              except:
                try:
                  await message.delete()
                except:
                  pass
              gold_reqs = [100, 200, 500, 900, 1000]
              iron_reqs = [69, 111, 420, 333, 555, 777, 999]              
              if int(message.content) in gold_reqs:
                role = discord.utils.get(message.author.guild.roles, id=799603986163826708) # Gold
                await message.author.add_roles(role)
                await message.add_reaction('🎉')
                await message.add_reaction('🟡')
              elif int(message.content) in iron_reqs:
                role = discord.utils.get(message.author.guild.roles, id=799603845982060574) # Iron
                await message.author.add_roles(role)
                await message.add_reaction('🎉')
                await message.add_reaction('⚪')
            msg_count += 1
  await client.process_commands(message)
  
try:
  client.run(token)
except:
  print(colorama.Fore.RED + 'Unable to run the client. Please check your bot token.')
  sys.exit(-1)
finally:
  print(colorama.Style.RESET_ALL)
