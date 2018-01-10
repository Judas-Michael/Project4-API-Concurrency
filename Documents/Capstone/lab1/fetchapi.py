import requests

key = '  '

base_url = 'http://www.omdb.com'

movie = input('what movie?')

params = { 'apikey' : key, 't' : movie}
data = requests.get(base_url, params ).json()

print(data)

print ('rating for movie')
print(data['ratings'][0]['value'])

