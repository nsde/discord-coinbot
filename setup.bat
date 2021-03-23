@echo off
color 03
echo This programm will setup the bot for you. Press any key to start.
pause
echo Installing needed dependencies (packages) using pip...
color 0D
pip install -r requirements.txt
echo.
echo.
echo.
echo.
echo Installed.
color 03
echo.
echo Now, open the Discord developer portal, select an application or create one, go to the bot-tab and copy the token.
set /p token=Enter your Discord bot token and press enter:
echo %token%>config/token.txt
echo Done.
echo You can now press any key to close the setup process.
pause