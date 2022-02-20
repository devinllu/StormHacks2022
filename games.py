import requests
import random

URL = "https://www.freetogame.com/api/games"

def recommend_game(platform=None, category=None):

    if platform is not None and category is not None:
        params1 = {
            'platform': platform
        }

        cat = requests.get(URL, params=params1).json()

        filtered = [x for x in cat if x['genre'].lower() == category]

        n = len(filtered)
        idx = random.randint(0, n - 1)
        
        return filtered[idx]
    
    
    params = {
        'category': category,
        'platform': platform
    }
    print(params)

    req = requests.get(URL, params=params)

    if req.status_code == 200:

        data = req.json()
        n = len(data)
        idx = random.randint(0, n - 1)

        return data[idx]

    return 'Sorry, there was an error processing the request'


def main():
    game = recommend_game(category='shooter', platform='browser')
    print(game.keys())

if __name__ == "__main__":
    main()