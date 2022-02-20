from multiprocessing import Event
import os
import discord
import requests
from discord.ext import commands
from dotenv import load_dotenv

client = discord.Client()

load_dotenv()
# API KEY 
TRIVIA_API = os.getenv('TRIVIA_API')
TOKEN = os.getenv('TOKEN')

# choose = input('Enter category: ')
# category = choose
# api_url = 'https://api.api-ninjas.com/v1/trivia?category={}'.format(category)
# response = requests.get(api_url, headers={'X-Api-Key': TRIVIA_API})
# if response.status_code == requests.codes.ok:
#     # print(response.json()[0]['category'])
#     data = response.json()
#     print(data)
# else:
#     print("Error:", response.status_code, response.text)


# def getQuestion():
#     question = data[0]['question']
#     print(question + '?')

# getQuestion()

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_message(message):
    category = ''
    if message.author == bot.user:
        return 

    if message.content == 'music':
        category = 'music'

    if message.content == 'language':
        category = 'language'

    if message.content == 'artliterature':
        category = 'artliterature'

    if message.content == 'sciencenature':
        category = 'sciencenature'

    if message.content == 'general':
        category = 'general'

    if message.content == 'fooddrink':
        category = 'fooddrink'
        
    if message.content == 'peopleplaces':
        category = 'peopleplaces'

    if message.content == 'geography':
        category = 'geography'

    if message.content == 'historyholidays':
        category = 'historyholidays'

    if message.content== 'entertainment':
        category = 'entertainment'

    if message.content == 'toysgames':
        category = 'toysgames'

    if message.content == 'mathematics':
        category = 'mathematics'
    
    if message.content == 'religionmythology':
        category = 'religionmythology'

    if message.content == 'sportsleisure':
        category = 'sportsleisure'
    
    URL = 'https://api.api-ninjas.com/v1/trivia?category={}'.format(category)

    response = requests.get(URL, headers={'X-Api-Key': TRIVIA_API})
    if response.status_code == requests.codes.ok:
        # print(response.json()[0]['category'])
        data = response.json()
        await message.channel.send(f'{data[0]["question"]}' + '?')
    else:
        print("Error:", response.status_code, response.text)


bot.run(TOKEN)