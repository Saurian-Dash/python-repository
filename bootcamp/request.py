import requests

url = 'https://www.ycombinator.com/'

response = requests.get(url, headers={'Accept': 'application/json'})

print(response.text)