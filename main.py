from discord.ext import commands 
from discord import Embed, Color
import os

import games
import requests
from dotenv import load_dotenv, find_dotenv
from social import *

load_dotenv(find_dotenv())

API_TOKEN = os.environ.get('TOKEN')
TRIVIA_API = os.getenv('TRIVIA_API')


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
    embed = Embed(title='Commands', color=Color.dark_gold())
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
    embed = Embed(title="Trivia Categories", color=Color.dark_gold())
    embed.add_field(name='Filter By', value=stringified)
    # for i in range(len(arr)):
    #     embed.add_field(name=i+1, value=arr[i])
    await ctx.send(embed=embed)

@bot.event
async def on_message(message):
    category = ''
    if message.author == bot.user:
        return 

    if message.content == '!trivia music':
        category = 'music'

    if message.content == '!trivia language':
        category = 'language'

    if message.content == '!trivia artliterature':
        category = 'artliterature'

    if message.content == '!trivia sciencenature':
        category = 'sciencenature'

    if message.content == '!trivia general':
        category = 'general'

    if message.content == '!trivia fooddrink':
        category = 'fooddrink'
        
    if message.content == '!trivia peopleplaces':
        category = 'peopleplaces'

    if message.content == '!trivia geography':
        category = 'geography'

    if message.content == '!trivia historyholidays':
        category = 'historyholidays'

    if message.content== '!trivia entertainment':
        category = 'entertainment'

    if message.content == '!trivia toysgames':
        category = 'toysgames'

    if message.content == '!trivia mathematics':
        category = 'mathematics'
    
    if message.content == '!trivia religionmythology':
        category = 'religionmythology'

    if message.content == '!trivia sportsleisure':
        category = 'sportsleisure'

    if category != '':
    
        URL = 'https://api.api-ninjas.com/v1/trivia?category={}'.format(category)

        response = requests.get(URL, headers={'X-Api-Key': TRIVIA_API})
        if response.status_code == requests.codes.ok:
            # print(response.json()[0]['category'])
            data = response.json()
            await message.channel.send(f'{data[0]["question"]}' + '?')
        else:
            print("Error:", response.status_code, response.text)

    else:
        vals = message.content.split(' ')[0]

        if vals == '!trivia':
            await message.channel.send(f'Sorry, command {message.content} is not valid!')

bot.run(API_TOKEN)
