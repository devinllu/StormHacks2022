import os
import discord
import requests
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
# API KEY 
TRIVIA_API = os.getenv('TRIVIA_API')
TOKEN = os.getenv('TOKEN')
# help = 'help'
# bot = commands.Bot(command_prefix="!trivia")


# @bot.event
# async def on_ready():
#     print('Trivia')
#     await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name='!trivia'))

# @client.event
# async def on_message(msg):
#     if msg.author == bot.user:
#         return 

#     if msg.content == 'category':
#         await msg.channel.send()


choose = input('Enter category: ')
category = choose
api_url = 'https://api.api-ninjas.com/v1/trivia?category={}'.format(category)
response = requests.get(api_url, headers={'X-Api-Key': TRIVIA_API})
if response.status_code == requests.codes.ok:
    # print(response.json()[0]['category'])
    data = response.json()
    print(data)
else:
    print("Error:", response.status_code, response.text)


def getQuestion():
    question = data[0]['question']
    print(question + '?')

getQuestion()

