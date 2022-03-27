import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.environ['TOKEN']

GUILD_ID = int(os.environ['GUILD_ID'])