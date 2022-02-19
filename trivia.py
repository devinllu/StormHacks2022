import requests

choose = input('Enter category: ')
category = choose
api_url = 'https://api.api-ninjas.com/v1/trivia?category={}'.format(category)
response = requests.get(api_url, headers={'X-Api-Key': 'GTFcyQ5xs0/j6KG7rV3jzg==WJ13oCWtAGfufGYY'})
if response.status_code == requests.codes.ok:
    print(response.json())
else:
    print("Error:", response.status_code, response.text)