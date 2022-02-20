from email import message
from discord.ext import commands
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

@bot.command(name="category")
async def get_categories(ctx):
    await ctx.send(f'Select category:\n{arr}')


bot.run(TOKEN)
