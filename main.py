from discord.ext import commands 
from discord import Embed, Color
import os

import games
import requests
from dotenv import load_dotenv, find_dotenv
from social import *
import time

load_dotenv(find_dotenv())

API_TOKEN = os.environ.get('TOKEN')
TRIVIA_API = os.environ.get('TRIVIA_API')


bot = commands.Bot(command_prefix="!")

categories = ["mmorpg", "shooter", "strategy", "moba", "racing", "sports", "social", "sandbox", "open-world", "survival", "pvp", "pve", "pixel", "voxel", "zombie", "turn-based", "first-person", "third-Person", "top-down", "tank", "space", "sailing", "side-scroller", "superhero", "permadeath", "card", "battle-royale", "mmo", "mmofps", "mmotps", "3d", "2d", "anime", "fantasy", "sci-fi", "fighting", "action-rpg", "action", "military", "martial-arts", "flight", "low-spec", "tower-defense", "horror", "mmorts"]
platforms = ["pc", "browser", "all"]

arr = ['artliterature', 'language',
    'sciencenature', 'general', 'fooddrink', 'peopleplaces',
    'geography', 'historyholidays', 'entertainment', 
    'toysgames', 'music', 'mathematics', 
    'religionmythology', 'sportsleisure']

@bot.event
async def on_ready():
    print(f'{bot.user} succesfully logged in!')

@bot.command()
async def commands(ctx):
    game_commands = '!game_categories\n!game_platforms\n!recommend_game'
    social_commands = '!social\n!go'
    trivia_commands = '!trivia_categories\n!trivia'
    embed = Embed(title='Commands', color=Color.blue())
    embed.add_field(name='Game Commands', value=game_commands)
    embed.add_field(name='Social Commands', value=social_commands)
    embed.add_field(name='Trivia Commands', value=trivia_commands)
    await ctx.send(embed=embed)

@bot.command(name='game_categories')
async def get_categories(ctx):
    stringified = '\n'.join(categories)
    embed = Embed(title='Game Categories')
    embed.add_field(name='Filter By', value=stringified)
    await ctx.send(embed=embed)

@bot.command(name='game_platforms')
async def get_platforms(ctx):
    stringified = '\n'.join(platforms)
    embed = Embed(title='Game Platforms')
    embed.add_field(name='Filter By', value=stringified)
    await ctx.send(embed=embed)

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

@bot.command(name="trivia_categories")
async def get_categories(ctx):
    stringified = '\n'.join(arr)
    embed = Embed(title="Trivia Categories", color=Color.blue())
    embed.add_field(name='Filter By', value=stringified)
    # for i in range(len(arr)):
    #     embed.add_field(name=i+1, value=arr[i])
    await ctx.send(embed=embed)

@bot.command()
async def trivia(ctx, content):
    TRIVIA_URL = 'https://api.api-ninjas.com/v1/trivia'

    try:
        params = None
        if content and isinstance(content, str):
            content = content.lower()

            if content in arr:
                params = {
                    'category': content.lower()
                }
            else:
                raise Exception(f'Sorry, input argument {content} is not valid')

        response = requests.get(TRIVIA_URL, headers={'X-Api-Key': TRIVIA_API}, params=params)

        if response.status_code == requests.codes.ok:
            data = response.json()
            question = Embed(title='Question', description=f'{data[0]["question"]}')
            await ctx.send(embed=question)
            time.sleep(5)
            answer = Embed(title='Answer', description=f'||{data[0]["answer"]}||')
            await ctx.send(embed=answer)
        else:
            await ctx.send(f"Error: {response.status_code} {response.text}")
    
    except Exception as e:
        print(e)
        await ctx.send(f'Sorry, the input commands you provided were incorrect')

bot.run(API_TOKEN)
