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
    await ctx.send(welcome_msg())


@client.command()
async def go(ctx):
    await ctx.send('Here is your question {}'.format(ctx.author.mention) + "\n**" + social_mode() + "**")



client.run(TOKEN)