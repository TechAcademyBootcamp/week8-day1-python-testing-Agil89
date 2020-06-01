import requests


link = input('ENter the link: ')

response = requests.get(link)

print(response.status_code)

if response.status_code == 200:
    print('200 success')
else:
    print('404 not found')

