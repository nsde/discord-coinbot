@echo off
color 03
set /p token=Enter your discord bot token and press enter:
echo %token%>config/token.txt
echo Done.