# telegramShell
A Telegram Bot to execute Linux &amp; Windows OS commands remotely using Telegram Messenger.

## Requirement
`code` python3 -m pip install python-telegram-bot

## Setup
1. Search and select *@BotFather* in your Telegram Messenger App.
2. Type /help for a list of available commands.
3. Type /newbot and set a name and username for this bot. 
4. A API Token will be generated. Replace the 'YOUR_TELEGRAM_TOKEN' in telegramShell.py with the API Token generated in the app.
5. Click on the link of your new bot and Click on Start.
6. Send a message to your bot.
7. Visit https://api.telegram.org/botAPITOKEN/getUpdates on your browser and find the 'id' value and replace 'YOUR_TELEGRAM_USERID' in telegramShell.py
  
## Usage
Server:
`code` python3 telegramShell.py

Commands:
- /h - Help
- /s - Shell
- /q - Quit 

Example:
- /s ifconfig
- /s ipconfig
