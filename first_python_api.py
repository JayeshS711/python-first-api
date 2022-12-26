import requests
response = requests.get('https://google.com/')
print(response)
if response:
    print('Request is successfully sent')
else:
    print('Request returned an error')