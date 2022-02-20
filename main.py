from email import message
from xml.dom.minidom import Element
from discord.ext import commands 
from discord import Embed, Color
import discord
import os
from dotenv import load_dotenv
load_dotenv()
TOKEN = os.getenv('TOKEN')

bot = commands.Bot(command_prefix='!')

arr = ['artliterature', 'language',
    'sciencenature', 'general', 'fooddrink', 'peopleplaces',
    'geography', 'historyholidays', 'entertainment', 
    'toysgames', 'music', 'mathematics', 
    'religionmythology', 'sportsleisure']

@bot.event
async def on_ready():
    print (f'{bot.user} succesfully logged in!')

@bot.command(name="trivia_category")
async def get_categories(ctx):
    embed = Embed(title="Trivia Categories", color=Color.dark_gold())
    for i in range(len(arr)):
        embed.add_field(name=i+1, value=arr[i])
    await ctx.send(embed=embed)


bot.run(TOKEN)
