import requests
urlTEMP = 'https://api.hgbrasil.com/weather?key=7d9fedb4&user_ip=remote'
tempRequest = requests.get(urlTEMP)
tempJson = tempRequest.json()
print(tempJson)

'city' cidade
'time' ultima atualziacao
'temp' temp atual
'description' resumo tempo limpo
'max'
'min'
'rain_probability'
'rain' em mm
'date'