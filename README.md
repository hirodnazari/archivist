# archivist
A bot for the good ones server, meant to archive events and people as well as any miscellaneous functions.

Primary dependencies necessary for function:
- [Pycord](https://github.com/Pycord-Development/pycord) - a [discord.py](https://github.com/Rapptz/discord.py) fork for interacting with the Discord API
- [dotenv](https://pypi.org/project/python-dotenv/) - a python .env manager for hiding important information (guild id, token)
- [markovify](https://github.com/jsvine/markovify) - generates markov chains for the primary command

The current primary feature of the bot is a Markov chain generation through scraping the entire server's messages. This feature is provided largely by code from [wid-bot](https://github.com/ericpretzel/wid-bot). 
