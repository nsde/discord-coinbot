# discord-coinbot
A coin system for Discord with an API.

Basically an updated and improved version of **https://github.com/nsde/SCD-Bot**.

*"Why didn't I just update the SCD-Repo?"*, you might ask.
> It's because the SCD-Bot was created for a gaming clan, but thgis one is a public bot.

*"Are you going to update the SCD-Repo anytime soon?"*

> I'm not sure yet, but probably no.

# Installation
Execute in root dir: `pip install -r requirements.txt` to install the needed libaries.
After that, create a file in "\config" called "token.txt". The content of the file has to be the bot token (see the section "Security" > "Token") for security information.

## Fix errors:
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


# Security note
This section will inform you about how you can safe your bot against black hat hackers/exploits etc.

## Permissions
Please go to the Discord Developer Portal `/applications/<application id>/bot` and scroll down to the section "Bot permissions". From there, tick all **needed and used** permissions. Do NOT tick "Administrator" - this will allow the bot to do almost everything on your server. And, do NOT tick unused permissions.

## Token
The bot token is secret! Everyone with access to the token can execute everything allowed to the bot (see "Permissions"). Therefore, remember to put the token.txt in the `.gitignore`, if you are using Git.