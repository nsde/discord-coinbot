# 🤖 NeoVision Discord-Bot
A Discord-Bot written in Python with features like coin/economy system, music, memes, temporary channels, server-bridge utilities and more!

[![huntr](https://cdn.huntr.dev/huntr_security_badge.svg)](https://huntr.dev)

## ℹ️ Information
This is basically an updated and improved version of **https://github.com/nsde/SCD-Bot**.

*"Why didn't I just update the SCD-Repo?"*, you might ask.
> It's because the SCD-Bot was created for a gaming clan, but thgis one is a public bot.

*"Are you going to update the SCD-Repo anytime soon?"*

> I'm not sure yet, but probably no.

# 🔨 Installation
1. Execute in root dir: `pip install -r requirements.txt` to install the needed libaries.
2  After that, create a file in "\config" called "token.txt". The content of the file has to be the bot token (see the section "Security" > "Token") for security information.
3. Go to https://github.com/BtbN/FFmpeg-Builds/releases download `ffmpeg-n(VERSION)-win64-gpl-(VERSION).zip` and paste `/bin/ffmpeg.exe` to `C:/ffmpeg/ffmpeg.exe`.

## ⛔ Fix errors:
If you get "ERROR: Could not build wheels for multidict, yarl which use PEP 517 and cannot be installed directly":
- __(not recommended)__ Downgrade to Python 3.8.6 
- __(not recommended)__ Download the "cp39" (for Python 3.9)-Versions of:

    -**lfd.uci.edu/~gohlke/pythonlibs/#yarl**

    -**lfd.uci.edu/~gohlke/pythonlibs/#multidict**

    remember to choose the right win_amd64/win32-Version.

    And do `pip install `**FILENAME** (e.g *yarl-1.6.3-cp39-cp39-win_amd64.whl*)` --force-reinstall` in the directory you downloaded the files for **both the two files**. 

    Then try `pip install discord.py` or `pip install discord` again.

- __(recommended/best way)__ install **https://visualstudio.microsoft.com/visual-cpp-build-tools/** (this worked for me)

- alternatively, see: https://stackoverflow.com/a/64861883

Run the "main"-python file in /src and follow the instructions and you are *good to go*!

## 🛠️ Usage
Try running the bot from the root directory (meaning not "src"). If you are running on windows, I added a start.bat and setup.bat, they are self-explainitory.

# 🔒 Security note
This section will inform you about how you can safe your bot against black hat hackers/exploits etc.

## Permissions
Please go to the Discord Developer Portal `/applications/<application id>/bot` and scroll down to the section "Bot permissions". From there, tick all **needed and used** permissions. Do NOT tick "Administrator" - this will allow the bot to do almost everything on your server. And, do NOT tick unused permissions.

## Token
The bot token is secret! Everyone with access to the token can execute everything allowed to the bot (see "Permissions"). Therefore, remember to put the token.txt in the `.gitignore`, if you are using Git.

## ✔️ Features
Sorry if they aren't up to date. Keep in mind you can always use the command **`.help`** to get information about other commands. Use **`.command`**

### Tempchannels
Create channels (text or voice) deleting themselves after a specific amount of time of user inactivity.

Inactivity means:
- no user being in a **voice** channel
- no message written in a **text** channel

### Syntax:
- `[tempcreate|tcc|tempc|tcreate] [t(ext)|v(oice)] <timeout>(s) (x)`
  Create a temporary channel. 
  > The channel name will be '⌛|<your_name>-<timeout>' by default.
  
  
  - **type**: 't' or 'text' for a text channel, 'v' or 'voice' for a **voice** channel
  - **timeout**: timeout in minutes (or append a 's' for seconds)
  - [Optional] **s**: measure the timeout in seconds, appended directly after `<timeout>`
  - [Optional] **x**: ignore user inactivity / force deleting the channel after time passed

### Examples
- `tcc t 2`: a two-minute text channel
- `tcc t 2 x`: a two-minute text channel deleting itself even after user activity  
- `tcc v 10s`: a ten-second voice channel 


## Music Bot
Play music from YouTube.

### Syntax
- `[playsong|play|psong|ps] <search_query>`
  Search and play a video on YouTube.
  > Make sure to join a channel before executing the command.
  
  
  - **search_query**: search for a video

- `[stopsong|stop|xs]`
  Stop a song.

- `move`
  Move the bot to your channel.
