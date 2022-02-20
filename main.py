import os

from discord import Embed, Color

import games
from discord.ext import commands
from dotenv import load_dotenv, find_dotenv
from social import *

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
    try:
        game = None

        if args1 and args2:
            args1 = args1.lower()
            args2 = args2.lower()

            if args1 in categories:
                if args2 in platforms:
                    game = games.recommend_game(platform=args2, category=args1)

            elif args1 in platforms:
                if args2 in categories:
                    game = games.recommend_game(platform=args1, category=args2)


        elif args1 and args2 is None:
            args1 = args1.lower()

            if args1 in categories:
                game = games.recommend_game(category=args1)

            elif args1 in platforms:
                game = games.recommend_game(platform=args1)

        elif args2 and args1 is None:
            args2 = args2.lower()

            if args2 in categories:
                game = games.recommend_game(category=args2)

            elif args2 in platforms:
                game = games.recommend_game(platform=args2)

        elif args1 is None and args2 is None:
            game = games.recommend_game()


        if game:
            print(f'genre: {game["genre"]} platform: {game["platform"]}')
            embed = Embed(title=game['title'], url=game['game_url'], description=game['short_description'], color=Color.blue())
            await ctx.send(embed=embed)
        else:
            await ctx.send(f'Sorry, there is no game with the specified category and platform!')

    except Exception as e:
        print(e)
        await ctx.send(f'Sorry, the input commands you provided were incorrect')

@bot.command()
async def social(ctx): # The name of the function is the name of the command
    await ctx.send(welcome_msg())


@bot.command()
async def go(ctx):
    await ctx.send('Here is your question {}'.format(ctx.author.mention) + "\n**" + social_mode() + "**")


bot.run(API_TOKEN)