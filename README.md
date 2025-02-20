# archivist
A bot for the Dorkcord server, with commands requested by users or dreamt up by the server owner.

Primary dependencies necessary for function:
- [Pycord](https://github.com/Pycord-Development/pycord) - a [discord.py](https://github.com/Rapptz/discord.py) fork for interacting with the Discord API
- [dotenv](https://pypi.org/project/python-dotenv/) - a python .env manager for hiding important information (guild id, token)
- [markovify](https://github.com/jsvine/markovify) - generates markov chains for the primary command

In order for the bot to function on your device, you must install all of the above dependencies, as well as create a .env file.

The .env file should look like below. Your bot's token can be found [like this.](https://github.com/reactiflux/discord-irc/wiki/Creating-a-discord-bot-&-getting-a-token#fetching-your-bots-token) Server ID can be found by right clicking server in developer mode, then pressing the "Copy ID" popup.
```
TOKEN=[Your Token]
GUILD_ID=[ID of the server the bot is being operated on]
```
Once the .env file is set up, install dependencies in Pipfile with:
```
pipenv install [dependency]
```
Confirm all dependencies are usable with
```
pipenv sync
```
Once it's ready to go, run the bot with
```
pipenv run python3 bot.py
```
The current primary feature of the bot is a Markov chain message generator by scraping the entire server's message history. This feature is provided largely by code from [wid-bot](https://github.com/ericpretzel/wid-bot). 

Please note that this bot does not have any audio features, but rather requires install of audioop-lts due to issues with py-cord.