import requests

response = requests.get('http://www.omdbapi.com/?t=the matrix&apikey=35b13908')
print(response.json()['Title'])
print(2020-int(response.json()['Released'].split(' ')[2]))