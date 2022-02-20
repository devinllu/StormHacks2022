from discord.ext import commands
from dotenv import load_dotenv, find_dotenv
import os
import games

load_dotenv(find_dotenv())

API_TOKEN = os.environ.get('TOKEN')


bot = commands.Bot(command_prefix="!")

categories = ["mmorpg", "shooter", "strategy", "moba", "racing", "sports", "social", "sandbox", "open-world", "survival", "pvp", "pve", "pixel", "voxel", "zombie", "turn-based", "first-person", "third-Person", "top-down", "tank", "space", "sailing", "side-scroller", "superhero", "permadeath", "card", "battle-royale", "mmo", "mmofps", "mmotps", "3d", "2d", "anime", "fantasy", "sci-fi", "fighting", "action-rpg", "action", "military", "martial-arts", "flight", "low-spec", "tower-defense", "horror", "mmorts"]
platforms = ["pc", "browser", "all"]

@bot.event
async def on_ready():
    print(f'{bot.user} succesfully logged in!')

@bot.command(name='game_categories')
async def get_categories(ctx):
    await ctx.send(f'List of categories:\n{categories}')

@bot.command(name='game_platforms')
async def get_platforms(ctx):
    await ctx.send(f'List of platforms:\n{platforms}')

@bot.command(name='recommend_game')
async def recc_game(ctx, args1=None, args2=None):
    if args1 is not None and not isinstance(args1, str):
        await ctx.send(f'Sorry, {args1} is not a valid command!')
    
    if args2 is not None and not isinstance(args2, str):
        await ctx.send(f'Apologies, {args2} is not a valid command!')
    
    await ctx.send(f'Completed {args1} {args2}')

bot.run(API_TOKEN)