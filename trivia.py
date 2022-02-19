import os
import discord

import requests
from dotenv import load_dotenv

load_dotenv()
TRIVIA_API = os.getenv('TRIVIA_API')

choose = input('Enter category: ')
category = choose
api_url = 'https://api.api-ninjas.com/v1/trivia?category={}'.format(category)
response = requests.get(api_url, headers={'X-Api-Key': TRIVIA_API})
if response.status_code == requests.codes.ok:
    print(response.json()[0]['category'])
else:
    print("Error:", response.status_code, response.text)