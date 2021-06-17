# How to host this bot
**PLEASE DO NOT JUST DOWNLOAD THE CODE AND RUN IT WITHOUT KNOWING WHAT YOU'RE DOING. MAKE SURE TO READ THIS WHOLE PAGE.**

***

###  🍴 This guide will teach you how to make and host your own version/fork of this bot.

# 🔨 Installation
1. Install **Python 3.7.9** with **pip**. If asked so, also deactivate the Path-length limit. Those things are more important than you might think.

2. Execute in root dir: `pip install -r requirements.txt` to install the needed libaries.

3. Follow the steps in ***apis.md*** to set up the APIs. 

4. [This is experimental and this may be changed later] Finally, go to https://github.com/BtbN/FFmpeg-Builds/releases download `ffmpeg-n(VERSION)-win64-gpl-(VERSION).zip`, unzip it, and paste `/bin/ffmpeg.exe` to `C:/ffmpeg/ffmpeg.exe`.

5. Before running the `src/bot.py`, make sure to check and update (if neccessary) its constants (about in line 100), this step is optional, but some variables, such as `OWNERS` are recommended to be changed. Read the variable line's comments for more info.

## ⛔ Fix errors & problems
### General ImportErrors
1. Make sure you are using the exact correct Python version for the program, you can view it at the first step of *Installation*.
2. Check if pip is installed correctly.

### API Problems
There are a lot of APIs NeoVision is using, but don't worry, you don't need to use all of them. The cool thing is: I'll try my best to make it so that the program is working perfectly fine, even without the APIs. Of course, the commands and features using a specific API you didn't set up won't work, which shouldn't be a big problem.

See ***apis.md*** for further information on this topic.

### MultiDict
If you get "ERROR: Could not build wheels for multidict, yarl which use PEP 517 and cannot be installed directly":
- __(not recommended)__ Downgrade to Python 3.8.6 
- __(not recommended)__ Download the "cp39" (for Python 3.9)-Versions of:

    - **lfd.uci.edu/~gohlke/pythonlibs/#yarl**
    - **lfd.uci.edu/~gohlke/pythonlibs/#multidict**

    Remember to choose the right `win_amd64`/`win32`-Version.

    And do `pip install `**FILENAME** (e.g `yarl-1.6.3-cp39-cp39-win_amd64.whl --force-reinstall` in the directory you downloaded the files for **both the two files**. 

    Then try `pip install discord.py` or `pip install discord` again.

- __(recommended/best way)__ install **https://visualstudio.microsoft.com/visual-cpp-build-tools/** (this worked for me)

- alternatively, see: https://stackoverflow.com/a/64861883

Run the setup.bat or start.bat (see *usage*) and follow the instructions.

## 🛠️ Usage
Try running the bot from the root directory (meaning not "src"). If you are running on windows, I added a start.bat and setup.bat, they are self-explainitory.

# 🔒 Security note
This section will inform you about how you can safe your bot against black hat hackers/exploits etc.

## Permissions
Please go to the Discord Developer Portal `/applications/<application id>/bot` and scroll down to the section "Bot permissions". From there, tick all **needed and used** permissions. Do NOT tick "Administrator" - this will allow the bot to do almost everything on your server. And, do NOT tick unused permissions.

## Token
The bot token is secret! Everyone with access to the token can execute everything allowed to the bot (see "Permissions"). Therefore, remember to put the token.txt in the `.gitignore`, if you are using Git.
