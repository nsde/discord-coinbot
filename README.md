# 🤖 NeoVision Discord-Bot
A Discord-Bot written in Python with features like coin/economy system, music, utilities and more!

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


# 🔒 Security note
This section will inform you about how you can safe your bot against black hat hackers/exploits etc.

## Permissions
Please go to the Discord Developer Portal `/applications/<application id>/bot` and scroll down to the section "Bot permissions". From there, tick all **needed and used** permissions. Do NOT tick "Administrator" - this will allow the bot to do almost everything on your server. And, do NOT tick unused permissions.

## Token
The bot token is secret! Everyone with access to the token can execute everything allowed to the bot (see "Permissions"). Therefore, remember to put the token.txt in the `.gitignore`, if you are using Git.


## ✔️ Features
### Tempchannels
Create channels (text or voice), that delete themselves after a specific amount of time inactivity.

This helpes the server being organised and clean.

**Syntax:**
- `t(emp)channel [text/voice] <inactivity-timeout>(s) (t) <channel-name>`.
  - **text/voice**: type of the channel
  - [Optional, if type=voice] **inactivity-timeout**: timeout in minutes
  - [Optional] **s**: measure the timeout in seconds, not a single argument, but directly after `inactivity-timeout`
  - [Optional] **t**: timeout even on activity
  - [Optional] **channel-name**: custom channel name 

 When creating a voice channel, if no *inactivity-timeout*-argument is given, I will delete itself when noone is in the channel. The inactivity timeout is measured in minutes, by default. But if there is the letter 's' at the end, it will count in seconds.

**Defaults:**
- `channel-name`: `<user>`-`<timeout>`(s)

**Examples:**
- `tchannel text 2` will create a text channel deleting itself after 2 minutes of no new message
- `tchannel voice 5` will create a voice channel deleting itself after 5 minutes when everybody left it.
- `tchannel voice` will create a voice channel deleting itself immediatly if everybody left it.a
- `tchannel text 10s` will create a voice channel 
