import requests
urlTEMP = 'https://api.hgbrasil.com/weather?key=7d9fedb4&user_ip=remote'
tempRequest = requests.get(urlTEMP)
tempJson = tempRequest.json()

teste = tempJson["results"]['temp']
print(teste)