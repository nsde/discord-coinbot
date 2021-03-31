'''A Discord-Bot written in Python with features like coin/economy system, music, memes, temporary channels, server-bridge, general moderation utilities and more!'''

import os
try:
  import colorama #pip install colorama | for colored text
except ImportError:
  os.system('pip install colorama')
  import colorama
print(colorama.Fore.MAGENTA)

'''Local imports'''
try:
  import padlet # self-made
except ImportError:
  print('Ignoring padlet module because of ImportError')

'''Regular imports'''
import io
import ast
import sys
import bs4 #pip install beautifulsoup4 | for web scrapers
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
import requests #pip install requests | for getting html of a website
import datetime
try:
  import pymongo #pip install pymongo | for the database
except ImportError:
  print('Ignoring pymongo module because of ImportError')
try:
  import meme_get #pip install meme_get | for meme-commands
except ImportError:
  os.system('pip install future')
  import meme_get
try:
  import mcstatus #pip install mcstatus | see "mojang"
except ImportError:
  print('Ignoring mcstatus module because of ImportError')
try:
  import wikipedia #pip install wikipedia | Wikipedia scraping
except ImportError:
  print('Ignoring wikipedia module because of ImportError')
import xmltodict #pip install xmltodict | The name says it.
try:
  import dateparser #pip install dateparser | Converts human readable text to datetime.datetime
except ImportError:
  print('Ignoring padlet module because of ImportError')
import langdetect #pip install langdetect | to detect langauges in a string
import skingrabber #pip install skingrabber | to render skins
import googlesearch #pip install google | to search something on the web
# import geizhalscrawler #pip install geizhalscrawler | for product data (price, etc.)
try:
  import deep_translator #pip install deep_translator | for translating-commands
except:
  print(colorama.Fore.RED + 'No internet connection.')
  print(colorama.Style.RESET_ALL)

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
  token = open(CWD + '/config/SECRET_token.txt').read()
except Exception as e:
  try:
    token = os.getenv('token')
  except:
    print(colorama.Fore.YELLOW + 'Token file not found. Creating one...')
    token = input(colorama.Fore.BLUE + 'Please type in the Discord bot token: ')
    open(CWD + '/config/SECRET_token.txt', 'w').write(token)    
finally:
  print(colorama.Style.RESET_ALL)

if not token:
  print(colorama.Style.RESET_ALL)
  print(colorama.Fore.YELLOW + 'Token file not found. Creating one...')
  token = input(colorama.Fore.BLUE + 'Please type in the Discord bot token: ')
  print(colorama.Style.RESET_ALL)
  open(CWD + '/config/SECRET_token.txt', 'w').write(token)    
else:
  print(colorama.Fore.GREEN + 'Token loaded. Length: ' + str(len(token)))
  print(colorama.Style.RESET_ALL)

with open(CWD + '/config/config.yml') as f:
  config = yaml.load(f, Loader=yaml.SafeLoader)

  def fixuml(x):
    '''Fix wrong coding of äüö (German language only)'''
    return x.replace('Ã¤','ä').replace('Ã¶','ö').replace('Ã¼', 'ü')

  # intents = discord.Intents().all()
  client = commands.Bot(command_prefix = config['main']['prefix'])

try:
  database = pymongo.MongoClient(open(CWD + '/config/SECRET_database.txt'))
except:
  try:
    database = pymongo.MongoClient(open(CWD + os.getenv('database')))
  except:
    print(f'''{colorama.Fore.RED}
Oops! There was an problem loading the MondoDB database.
Please set up a database and a cluster at 'mongodb.com', create a user, remember its password,
connect with the application 'Python' -> '3.6 or higher', replace the <password> in the string
with the user you just set up and copy the final string. Sorry - It's quite difficult to set up,
but it's needed for coin/economy/leveling & other systems to work!
    {colorama.Style.RESET_ALL}''')

    print(colorama.Fore.YELLOW)
    dbstring = input(colorama.Fore.BLUE + 'Please type in the database string or press enter to skip: ')
    open(CWD + '/config/SECRET_database.txt', 'w').write(dbstring)
    if dbstring:
      print('Please restart the program!')
    print(colorama.Style.RESET_ALL)

@client.event
async def on_ready():
  print(f'{colorama.Fore.GREEN}Ready. User: {client.user}{colorama.Style.RESET_ALL}.')
  # helpcmd = commands.HelpCommand
  await client.change_presence(activity=discord.Game(name='.help | visit bit.ly/nevi'))

@client.event
async def on_disconnect():
  print(f'{colorama.Fore.YELLOW}Disconnected.{colorama.Style.RESET_ALL}')

@client.event
async def on_reaction_add(reaction, user):
  pass

@client.event
async def on_reaction_remove(reaction, user):
  pass

@client.event
async def on_private_channel_create(channel):
  await channel.send('*Do **`.help`** for information about the DM system.*', delete_after=5)

# @client.event
# async def on_command_error(ctx, error):
#   error_msg = 'Unknown error.'
#   if isinstance(error, commands.CommandNotFound):
#     error_msg = 'This command does not exist. Use **`.info`** for information.'

# #   if isinstance(error, commands.MissingRequiredArgument):
# #     error_msg = 'Please follow the syntax.\nYou can use `.help <command>` for information.'
# #   if isinstance(error, commands.TooManyArguments):
# #     error_msg = 'You passed too many arguments. You can use `.help` for information'
# #   if isinstance(error, commands.Cooldown):
# #     error_msg = 'Please wait. You are on a cooldown.'
# #    if isinstance(error, commands.CommandError):
# #     error_msg = 'There was an error with this command.'
# #   if isinstance(error, commands.MessageNotFound):
# #     error_msg = 'I couldn\'t find this message.'
# #   if isinstance(error, commands.ChannelNotFound):
# #     error_msg = 'I couldn\'t find this channel.'
# #   if isinstance(error, commands.UserInputError):
# #     error_msg = 'I couldn\'t find this user.'
# #   if isinstance(error, commands.ChannelNotFound):
# #     error_msg = 'I couldn\'t find this channel.'
# #   if isinstance(error, commands.NoPrivateMessage):
# #     error_msg = 'Sorry, I can\'t send you private messages.\nLooks like you have disabled them.'
# #   if isinstance(error, commands.MissingPermissions):
# #     error_msg = 'Sorry, you don\'t have the role permissions for this.'
# #   if isinstance(error, commands.BotMissingPermissions):
# #     error_msg = 'Sorry, I don\'t have permissions to do this.'
# #   if isinstance(error, commands.ExtensionError):
# #     error_msg = 'I apologize, but I couldn\'t load the needed extension.'
# #   if isinstance(error, commands.CheckFailure):
# #     error_msg = 'Sorry, you don\'t have the permissions for this.'
# #   if isinstance(error, commands.BadArgument):
# #     error_msg = 'You gave an invalid agument. Please check if it\'s correct.'

#   if error_msg != 'Unknown error.':
#     await ctx.send(f':x: **ERROR** - {error_msg}')

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
    `.info`
    `.ping`
    `.help`

  **Links**
    [GitHub](https://bit.ly/nevi)
    [Readme](https://github.com/nsde/neovision/blob/main/README.md)
  ''')
  icon = ''
  embed.set_footer(text=f'Ping: {str(round(client.latency * 1000, 2))}ms', icon_url=icon)
  
  if not ctx.guild:
    await ctx.author.send(embed=embed)
    return
  await ctx.send(embed=embed)

@client.command(name='user', aliases=['member', 'userinfo', 'memberinfo'], help='Get information about an user.', usage='<user>')
async def user(ctx, *args):
  args = list(args)
  if isinstance(args, list):
    member = ' '.join(args)

  if not member:
    member = ctx.message.author
  else:
    for user in ctx.guild.members:
      if member.lower() in user.name.lower() or member.lower() in str(user.nick).lower():
        member = user
        break
   
  if isinstance(member, str):
    await ctx.send(':x: Member not (at leat in this guild) found.')
    return

  custom_status = '*[Not set]*'
  activity = '*[Empty]*'

  if member.activities:
    for member_activity in member.activities:
      if type(member_activity) is discord.CustomActivity:
        custom_status = member_activity.name
      elif type(member_activity) is discord.Activity:
        activity = member_activity.name
  
  nick = '*[Not set]*'
  if member.nick:
    nick = member.nick

  roles = []
  for role in member.roles:
    roles.append(role.mention)
  roles = ' '.join(x.mention for x in member.roles)

  status = member.status
  created = member.created_at.strftime('%A, %B %d, %Y at %H:%M %p %Z')
  joined = member.joined_at.strftime('%A, %B %d, %Y at %H:%M %p %Z')
  highest_role = member.top_role.mention

  status_icon = str(member.status).replace('dnd', ':no_entry:').replace('online', ':green_circle:').replace('idle', ':crescent_moon:').replace('offline', ':black_circle:')
  info = f'''
    **ID**
      {member.id}
    **Nickname**
      {nick}
    **Status**
      {status}
    **Custom Status**
      {custom_status}
    **Playing**
      {activity}
    **Created account**
      {created}
    **Joined guild**
      {joined}
    **Highest role**
      {highest_role}
    **Roles**
      {roles}
    '''
  embed = discord.Embed(title=f'{status_icon} {member.name}#{member.discriminator}', color=member.top_role.color, description=info)
  embed.set_thumbnail(url=member.avatar_url)
  await ctx.send(embed=embed)

@client.command(name='timer', help='Create a timer.', usage='<time> [s|m|h] (<message>)')
async def timer(ctx, time, unit, message='Time\'s up!'):
  time = int(time)
  oldtime = time # time without unit calculation to seconds
  if unit == 's':
    pass
  elif unit == 'm':
    time *= 60
  elif unit == 'h':
    time *= 3600
  else:
    await ctx.send(':x: **ERROR**: Invalid unit.\nUnit can be \'s\' for seconds, \'m\' for minutes or \'h\' for hours.')
    return
  if time > 10000:
    await ctx.send(':x: **ERROR**: Timer can\'t be longer than 10000 seconds.')
    return
  await ctx.send(f':white_check_mark: Creating a timer for **{oldtime}{unit}** with message \"**{message}**\"...\nYou will get mentioned/pinged.')
  await asyncio.sleep(time)
  await ctx.send(f'{ctx.author.mention} **{message}** (**{oldtime}{unit}** passed.)')

@client.command(name='translate', aliases=['tl'], help='Translate a text!', usage='<to_lang> <text>')
async def translate(ctx, *args):
  to_lang = args[0].lower()
  text = ' '.join(args[1:])
  translated = deep_translator.GoogleTranslator(source='auto', target=to_lang).translate(text)
  await ctx.send(translated)

@client.command(name='padlet', help='Get posts from a padlet.com-page.', usage='[<url>|<shortcut>] (<show_the_last_?_posts>)')
async def getpadlet(ctx, value, posts=10):
  shortcuts = {
    'ha': 'https://padlet.com/onlix/ha',
    '9a': 'https://padlet.com/bkessen/yb85s2hcioj2',
    '9b': 'https://padlet.com/petrakraayvanger/p2seaqfncyyi',
    'latein': 'https://padlet.com/kirstenlauschke/qea97sv1mlqi'
    } # shortcuts, so me and my friends don't have to write down the whole url
  
  if value in shortcuts.keys():
    url = shortcuts[value]
  else:
    url = value
  try:
    padlet_page = padlet.getpadlet(url, discord=True)
  except:
    await ctx.send(':x: **ERROR:** Couldn\'t load this Padlet. Please check the URL.')
    return

  embed = discord.Embed(title=padlet_page['title'], colour=discord.Colour(0x009fff), url=url, description=padlet_page['description'], timestamp=padlet_page['last_edit'])
  embed.set_thumbnail(url=padlet_page['icon'])
  embed.set_footer(text='Padlet created by: ' + padlet_page['author'] + ' | Last update: ')
  for post in padlet_page['posts'][-posts:]:
    title = post['title']
    if post['items']:
      if isinstance(post['items'], str):
        content = post['items'][:200]
      else:
        content = post['items'][:3]
    else:
      content = '*[Empty]*'
    print(title, content)
    embed.add_field(name=title, value=content, inline=False)
  await ctx.send(embed=embed)

@client.command(name='randomizer', aliases=['random', 'rd'], help='Random things!', usage='[thing|wiki|item]')
async def randomizer(ctx, *args):
  random_type = args[0]

  if random_type == 'thing' or random_type == 'item':
    request = requests.get('https://www.wikidata.org/wiki/Special:Random')
    soup = bs4.BeautifulSoup(request.text, 'html.parser')

    title = str(soup.find_all(class_='wikibase-title-label')[0]).split('>')[1].split('<')[0]
    if title == 'No label defined':
      title = '[No title avaiable]'
    
    info = str(soup.find_all(class_='wikibase-entitytermsview-heading-description')[0]).split('>')[1].split('<')[0]
    if info == 'No description defined':
      info = '[No description avaiable]'
    url = request.url
    footer = 'Thanks to WikiData and its contributors!'

  elif random_type == 'wiki':
    request = requests.get('https://en.wikipedia.org/wiki/Special:Random')
    soup = bs4.BeautifulSoup(request.text, 'html.parser')

    title = str(soup.find_all(class_='firstHeading')[0]).split('>')[1].split('<')[0]

    try:
      pic = 'https:' +str(soup.find_all(class_='image')[0]).split('src=\"')[1].split('\"')[0]
    except:
      pass    

    url = request.url
    try:
      info = wikipedia.page(title=url.split('/wiki/')[1]).summary[:500]
    except:
      info = '[No description avaiable]'
    footer = 'Thanks to Wikipedia and its contributors!'
    pass
  else:
    await ctx.send(':x: **ERROR:** This is not a valid random thing type. Use `.help randomizer` for usage help.')
    return

  embed = discord.Embed(title=title, colour=discord.Colour(0x009fff), description=info, url=url, )
  try:
    embed.set_thumbnail(url=pic)
  except:
    pass
  embed.set_footer(text=footer)
  await ctx.send(embed=embed)

@client.command(name='wiki', aliases=['wikipedia'], help='View a Wikipedia page.', usage='<page>')
async def wiki(ctx, *args):
  page = ' '.join(args)

  try:
    wikipage = wikipedia.page(wikipedia.search(page, results=10)[0])
  except:
    if wikipedia.search(page, results=10):
      await ctx.send(':x: **ERROR:** Sorry, I couldn\'t find any page with this title.\nMaybe you are looking for:\n**`' + '`**, **`'.join(list(wikipedia.search(page, results=10))) + '`**')
      return
    else:
      await ctx.send(':x: **ERROR:** Sorry, I couldn\'t find any page with this title.')

  title = wikipage.title
  url = wikipage.url

  try:
    for picture in wikipage.images:
      if picture.endswith('jpg') or picture.endswith('png'):
        pic = picture
        break
  except:
    pass    

  try:
    info = wikipedia.summary(title)[:500] + ' *[...]*'
  except:
    info = '[No description avaiable]'
  footer =  'Categories: ' + ', '.join(wikipage.categories[:3][:50])

  embed = discord.Embed(title=title, colour=discord.Colour(0x009fff), description=info, url=url)

  try:
    embed.set_thumbnail(url=pic)
  except:
    pass
  embed.set_footer(text=footer)
  await ctx.send(embed=embed)

@client.command(name='counting', aliases=['ct'], help='Get information about the counting system.')
async def counting(ctx):
  await ctx.send(
    f'''**__Counting Information__**
    *For help on how to setup a counting channel, see the wiki on the GitHub page.*
    ''')

@client.command(name='minecraft', aliases=['mc', 'minecraftinfo', 'mcinfo'], help='Get information about a player or server.', usage='<player|server>')
async def minecraft(ctx, value):
  value = value.lower()
  uuid = mojang.MojangAPI.get_uuid(value)

  if not uuid:
    server = mcstatus.MinecraftServer.lookup(f'{value}')
    try:
      status = server.status()
    except:
      await ctx.send(':x: **ERROR:** Invalid user/server.')
      return

    color = discord.Colour(0x009fff)

    # players = ' '.join(server.query().players.names)
    playercount = str(status.players.online) + ' players'
    
    if status.players.online == 0:
      color = discord.Colour(0xff0000)

    embed = discord.Embed(title=value, colour=color)
    embed.set_thumbnail(url='https://i.ibb.co/1GLrmKC/pack.png')
    embed.add_field(name='Ping', value=f'{status.latency}ms', inline=False)
    embed.add_field(name='Online', value=f'{playercount}')
    # embed.add_field(name='Players', value=f'{players}', inline=False)
    await ctx.send(embed=embed)

  else:
    skin = mojang.MojangAPI.get_profile(uuid).skin_url
    skinrender = skingrabber.skingrabber()
    skinrendered = skinrender.get_skin_rendered(user=value)

    drop = mojang.MojangAPI.get_drop_timestamp(value)

    if not drop:
      drop = 'Not dropping.'
    else:
      drop = drop - time.time()
      drop = f'Dropping in: {drop} Seconds'

    embed = discord.Embed(title=value, colour=discord.Colour(0x009fff))
    embed.set_thumbnail(url=skinrendered)
    embed.add_field(name='UUID', value=uuid, inline=False)
    await ctx.send(embed=embed)

coins_file = CWD + '/data/coins.txt'

@client.command(name='tictactoe', aliases=['ttt'], help='Play tic tac toe!')
async def dailycoins(ctx):
  content = '''
  :black_large_square::black_large_square::black_large_square:
  :black_large_square::blue_square::black_large_square:
  :black_large_square::black_large_square::black_large_square:
  '''
  embed = discord.Embed(title='TicTacToe', colour=discord.Colour(0x20b1d5), description=content)
  # embed.add_field(name='', value='', inline=True)
  await ctx.send(embed=embed)

def getcoins(user):
  for line in open(coins_file).readlines():
    if line.startswith(str(user.id)):
      return int(line.split()[1])
  open(coins_file, 'a').write(f'\n{user} 0')
  return 0

def setcoins(user, amount):
  for line in open(coins_file).readlines():
    if line.startswith(str(user.id)):
      open(coins_file, 'w').write(open(coins_file.read().replace(line, f'{user} {amount}')))
      return
  open(coins_file, 'a').write(f'\n{user} {amount}')

@client.command(name='dailycoins', aliases=['dcoins', 'dc', 'dailyrewards'], help='Economy command to get daily coins.')
async def dailycoins(ctx):
  dailycoins_file = CWD + '/data/dailycoins.txt'
  try:
    dailycoins_list = open(dailycoins_file).readlines()
  except:
    open(dailycoins_file).write('')
    dailycoins_list = open(dailycoins_file).readlines()

  if str(ctx.message.author.id) not in dailycoins_list:
    amount = random.randint(config['currency']['rarity_normal']['min'], config['currency']['rarity_normal']['max'])
    await ctx.send('**Here, enjoy your daily coins!**\n> +' + str(amount) + ' ' + config['currency']['symbols']['currency_normal'])
    dailycoins_list.append(str(ctx.message.author.id))
    print('\n'.join(dailycoins_list))
    open(dailycoins_file, 'w').write('\n'.join(dailycoins_list))
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

globals()['tempchannel_users'] = []

@client.command(name='tempcreate', aliases=['tcreate', 'tempc', 'tcc'], help='Creates a temporary channel.', usage='[v|t] <time>(s) (x)')
async def tempchannel(ctx, ctype=None, timeout=None, afk_timer=None):
  def getChannelName(ctx, timeout):
    return f'⏳│{ctx.message.author.display_name[:13].lower()}-{timeout}'
  
  cname = getChannelName(ctx=ctx, timeout=timeout)

  if not afk_timer:
    afk_timer = True
  else:
    afk_timer = False

  # await ctx.send(f'''
  # :wrench: Creating channel...
  # > **Type:** {ctype}
  # > **Timeout:** {timeout}
  # > **Channel name:** {cname}
  # ''', delete_after=3)

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

  if timeout > 600:
    await ctx.send(':x: **ERROR:** The maximum timeout is 600 seconds (10 minutes).')
    return

  if ctx.author.id in globals()['tempchannel_users']:
    await ctx.send(':x: **ERROR:** You can\'t create two tempchannels at once.')
    return

  category = ctx.channel.category

  if ctype[0] == 't':
    await ctx.send(f':white_check_mark: Created text channel ***#{cname}*** with timeout ***{timeout}***.')
    
    try:
      channel = await ctx.guild.create_text_channel(cname, category=category)
      globals()['tempchannel_users'].append(ctx.author.id)
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
      globals()['tempchannel_users'].append(ctx.author.id)
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
    
  if ctx.author.id in globals()['tempchannel_users']:
    user_num = 0
    for user in globals()['tempchannel_users']:
      if ctx.author.id == user:
        del globals()['tempchannel_users'][user_num]
      user_num += 1

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
    if ctx.message.author.display_name in channel.name:
      await channel.edit(user_limit=limit)
      await ctx.send(f'''
        :white_check_mark: New user limit for ***{channel.name}*** is **{limit}**.
        Keep in mind that users with certain permissions can bypass this restriction.''')
    else:
      await ctx.send('Lol, You little hacker, not this time!')
  else:
    await ctx.send(':x: **ERROR:** Please join a voice channel to change its userlimit and try again.')

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
  'Tt7bzxurJ1I', 'fC7oUOUEEi4', 'O91DT1pR1ew', 'bxqLsrlakK8', 'oHg5SJYRHA0'] # Rickrolls

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

  await ctx.send(f':arrow_down: **Downloading...**\n`{video_stream}`', delete_after=3)

  video_stream.download(output_path=temp_path, filename=filename)  

  try:
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    voice.play(discord.FFmpegPCMAudio(options='-loglevel panic', executable='C:/ffmpeg/ffmpeg.exe', source=temp_path + '/' + filename + '.' + filetype))
    voice.source = discord.PCMVolumeTransformer(voice.source)
    voice.source.volume = 0.1
  except Exception as e:
    print(f'Couldn\'t play the song. I believe FFMPEG has not been installed correctly.\n{e}')
    await ctx.send(f':x: **CLIENT ERROR** An error occured on the system hosting this bot.\nThis could be because the host system doesn\'t have FFMPEG installed correctly.\n`{e}`')

  print('After playing start')


@client.command(name='pausesong', aliases=['pause', 'resume', 'resumesong'], help='Pauses or resumes a song.')
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

@client.command(name='songname', aliases=['musicname', 'sn', 'mn'], help='What song is currently being played?')
async def songname(ctx):
  embed = globals()['embed']
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
  ['I\'m good, what about you? :+1:', 'fine', 'I\'m glad to hear that!'],
  ['I\'m good, what about you? :+1:', 'nice', 'I\'m glad to hear that!'],
  ['I\'m good, what about you? :+1:', 'great', 'I\'m glad to hear that!'],

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
async def clear(ctx, amount: int):
  await ctx.channel.purge(limit=amount)
  await ctx.send(f':white_check_mark: I deleted **{amount}** messages.', delete_after=3)

@client.command(name='anonymbox', aliases=['ab'], help='Information about the AnonymBox-System')
async def anonymbox(ctx, action=None):
  if action == 'setup':
    channel = ctx.channel
    text = f'Send anonym messages! Just DM the \'NeoVision\'-Bot with \'.anonymbox {channel.id} (message)\'. nv-anonymbox'
    try:
      await channel.edit(topic=text)
      await ctx.send(':white_check_mark: Changed the channel\'s description.')
    except:
      await ctx.send(f'''
Oops! I don\'t have the permission to edit the channel\'s description.\nYou can copy & paste this text then:
      ***{text}***''')
  else:
    await ctx.send(f'''
    **AnonymBox**
AnonymBox means that users can DM
me and an anonymous message will be
posted in an specific AnonomBox-channel.

To set up such one, do **`.ab setup`**.
    ''')

@client.event
async def on_message(message):
  '''Used for e.g. counting system, chatbot system & bridge system'''

  bridge_names = ['nv-bridge', '𝔫𝔳-𝔟𝔯𝔦𝔡𝔤𝔢', '𝖓𝖛-𝖇𝖗𝖎𝖉𝖌𝖊', '𝓷𝓿-𝓫𝓻𝓲𝓭𝓰𝓮', '𝓃𝓋-𝒷𝓇𝒾𝒹𝑔𝑒', '𝕟𝕧-𝕓𝕣𝕚𝕕𝕘𝕖', '𝘯𝘷-𝘣𝘳𝘪𝘥𝘨𝘦', '𝙣𝙫-𝙗𝙧𝙞𝙙𝙜𝙚', '𝚗𝚟-𝚋𝚛𝚒𝚍𝚐𝚎', '𝐧𝐯-𝐛𝐫𝐢𝐝𝐠𝐞', 'ᑎᐯ-ᗷᖇᎥᗪǤᗴ'] # channel names for bridges can be...
  chatbot_names = ['nv-chatbot', '𝔫𝔳-𝔠𝔥𝔞𝔱𝔟𝔬𝔱', '𝖓𝖛-𝖈𝖍𝖆𝖙𝖇𝖔𝖙', '𝓷𝓿-𝓬𝓱𝓪𝓽𝓫𝓸𝓽', '𝓃𝓋-𝒸𝒽𝒶𝓉𝒷𝑜𝓉', '𝕟𝕧-𝕔𝕙𝕒𝕥𝕓𝕠𝕥', '𝘯𝘷-𝘤𝘩𝘢𝘵𝘣𝘰𝘵', '𝙣𝙫-𝙘𝙝𝙖𝙩𝙗𝙤𝙩', '𝚗𝚟-𝚌𝚑𝚊𝚝𝚋𝚘𝚝', '𝐧𝐯-𝐜𝐡𝐚𝐭𝐛𝐨𝐭', 'ᑎᐯ-ᑕᕼᗩ丅ᗷᗝ丅']
  counting_names = ['nv-counting', 'nv-count']
  anonymbox_names = ['nv-anonymbox']

  if not message.author.bot:
    if not isinstance(message.channel, discord.DMChannel):
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
                          return
    else:
      if message.content.startswith('.anonymbox '):
        channel_id = message.content.split()[1]
        text = ' '.join(message.content.split()[2:])
        channel = client.get_channel(int(channel_id))
        for name in anonymbox_names:
          if name in channel.topic:
            await channel.send(text)
        return
      elif message.content.startswith('.support '):
          text = ' '.join(message.content.split()[1:])
          support_users = [657900196189044736] # Supporter IDs that can help the users
          if not message.author.id in support_users: # So supporters don't get spammed by their own messages lmao
            for user_id in support_users:
              user = await client.fetch_user(user_id)
              await user.send(f'**[{message.author.id}] {message.author}** » {message.content}')
              return

      elif message.content.startswith('.help '):
        await channel.trigger_typing()
        await asyncio.sleep(1)
        await channel.send('Hello there! :wave:')

        await channel.trigger_typing()
        await asyncio.sleep(1.5)
        await channel.send('Please keep in mind that commands don\'t work in here.')

        await channel.trigger_typing()
        await asyncio.sleep(2.5)
        await channel.trigger_typing() 
        await channel.send('But you can write me for help & support!')

        await asyncio.sleep(2)
        await channel.send('Don\'t worry, the messages will be redirected to a human ;)')

        await channel.trigger_typing()
        await asyncio.sleep(3)
        await channel.send('Bye! <3')

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
              if 'r1(' in message.channel.topic:
                if not int(message.content) % 500:
                  worked = False
                  try:
                    reward1_role_id = int(message.channel.topic.split('r1(')[1].split(')')[0])
                    worked = True
                  except:
                    pass
                  if worked:
                    role = discord.utils.get(message.author.guild.roles, id=reward1_role_id)
                    await message.author.add_roles(role)
                    await message.add_reaction('🎉')
                    await message.add_reaction('🟡')
                    return
              if 'r2(' in message.channel.topic:
                worked = False
                try:
                  reward2_role_id = int(message.channel.topic.split('r2(')[1].split(')')[0])
                  worked = True
                except:
                  pass
                if worked:
                  for i in range(3, 10):
                    i = int(i*'1')
                    if int(message.content) % i == 0:
                      role = discord.utils.get(message.author.guild.roles, id=reward2_role_id)
                      await message.author.add_roles(role)
                      await message.add_reaction('🎉')
                      await message.add_reaction('⚪')
                      return

            msg_count += 1
  await client.process_commands(message)
  
try:
  client.run(token)
except:
  print(colorama.Fore.RED + 'Unable to run the client. Please check your bot token.')
  sys.exit(-1)
  pass
finally:
  print(colorama.Style.RESET_ALL)