import requests
import random
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

TRIVIA_API = os.environ.get('TRIVIA_API')

arr = ['artliterature', 'language',
    'sciencenature', 'general', 'fooddrink', 'peopleplaces',
    'geography', 'historyholidays', 'entertainment', 
    'toysgames', 'music', 'mathematics', 
    'religionmythology', 'sportsleisure']

def trivia(content=None):
    TRIVIA_URL = 'https://api.api-ninjas.com/v1/trivia'
    print(TRIVIA_API)

    try:
        params = None
        if content and isinstance(content, str) and content.lower() in arr:
            params = {
                'category': content.lower()
            }

        response = requests.get(TRIVIA_URL, headers={'X-Api-Key': TRIVIA_API}, params=params)

        if response.status_code == requests.codes.ok:
            data = response.json()
            print(data[0]['question'])
        else:
            print("Error:", response.status_code, response.text)
    
    except Exception as e:
        print(e)
        


def main():
    trivia()

if __name__ == "__main__":
    main()