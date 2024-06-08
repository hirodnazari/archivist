# archivist
A bot for the Dorkcord server, meant to archive events and people as well as other miscellaneous functions.

Primary dependencies necessary for function:
- [Pycord](https://github.com/Pycord-Development/pycord) - a [discord.py](https://github.com/Rapptz/discord.py) fork for interacting with the Discord API
- [dotenv](https://pypi.org/project/python-dotenv/) - a python .env manager for hiding important information (guild id, token)
- [markovify](https://github.com/jsvine/markovify) - generates markov chains for the primary command

In order for the bot to function on your device, you must install all of the above dependencies, as well as create a .env file. This file must contain 2 lines:
```
TOKEN=[Your Token]
GUILD_ID=[ID of the server the bot is being operated on]
```

Once the .env file is set up, create a pipenv environment for the bot. If it does not work at this stage, check path config or install dependencies within the virtual environment.

The current primary feature of the bot is a Markov chain message generator by  scraping the entire server's message history. This feature is provided largely by code from [wid-bot](https://github.com/ericpretzel/wid-bot). 
