import os
import sys

import discord
from discord.ext import commands
from dotenv import load_dotenv
from social import *

load_dotenv()
TOKEN = os.getenv('TOKEN')

client = discord.Client()
client = commands.Bot(command_prefix="!")

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')


@client.command()
async def social(ctx): # The name of the function is the name of the command
    # print(arg) # this is the text that follows the command
    # await ctx.send(int(arg) ** 2) # ctx.send sends text in chat
    # channel = discord.utils.get(ctx.guild.channels, name=given_name)

    await ctx.send(social_mode())

client.run(TOKEN)