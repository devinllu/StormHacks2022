from email import message
from discord.ext import commands
import discord

bot = commands.Bot(command_prefix='!')

arr = ['artliterature', 'language',
    'sciencenature', 'general', 'fooddrink', 'peopleplaces',
    'geography', 'historyholidays', 'entertainment', 
    'toysgames', 'music', 'mathematics', 
    'religionmythology', 'sportsleisure']

@bot.event
async def on_ready():
    print (f'{bot.user} succesfully logged in!')

@bot.commands(name="category")
async def get_categories(ctx):
    await ctx.send(f'Select category:\n{arr}')

