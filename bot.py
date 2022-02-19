from discord.ext import commands
from dotenv import load_dotenv, find_dotenv
import os

load_dotenv(find_dotenv())

API_TOKEN = os.environ.get('TOKEN')


bot = commands.Bot(command_prefix="!")


@bot.event
async def on_ready():
    print(f'{bot.user} succesfully logged in!')

bot.run(API_TOKEN)