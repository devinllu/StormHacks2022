import requests
import random

URL = "https://www.freetogame.com/api/games"

def recommend_game(platform=None, category=None):

    params = {
        'platform': platform,
        'category': category
    }

    req = requests.get(URL, params=params)

    data = req.json()
    n = len(data)
    idx = random.randint(0, n - 1)

    return data[idx]


def main():
    game = recommend_game(category='shooter')
    print(game)

if __name__ == "__main__":
    main()