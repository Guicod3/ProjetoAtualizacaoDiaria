#ENTRADA DE DADOS
from datetime import datetime #calendário e horas atuais
import requests
import json
data = datetime.now()
dataFormatada = data.strftime('%d/%m/%Y %H:%M')

diaSemanaValorBase = datetime.weekday(data)#Mostrar dia da semana
diaSemanaTextoBase = ('Segunda-Feira', 'Terça-Feira', 'Quarta-Feira', 'Quinta-Feira', 'Sexta-Feira', 'Sábado', 'Domingo')
diaSemana = diaSemanaTextoBase[diaSemanaValorBase]

horaAtual = datetime.now().hour #Hora atual Int
saudacaoDoDia = ''

#APICOTACAO
url = 'https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL'
responseCot = requests.get(url)
if responseCot.status_code == 200:
    cotacaoJson = responseCot.json()
    valorDolar = float(cotacaoJson["USDBRL"]['bid'])
    valorEuro = float(cotacaoJson["EURBRL"]['bid'])
    valorBitcoin = float(cotacaoJson["BTCBRL"]['bid'])
else:
    print('[ERRO] Falha na Comunicação API(COTAÇÃO)')


#API DE TEMPO E LOCAL
import requests
urlTEMP = 'https://api.hgbrasil.com/weather?key=7d9fedb4&user_ip=remote'
tempRequest = requests.get(urlTEMP)
if tempRequest.status_code == 200:
    tempJson = tempRequest.json()
    temperaturaAtual = tempJson["results"]['temp']#1
    ultAtualizacao = tempJson["results"]['time']#ultimo
    descricaoTempo = tempJson["results"]['description']#2
    cidade = tempJson["results"]['city'] #ok
    quantidadeChuva = tempJson["results"]['rain']#5
    TempMax = tempJson["results"]['forecast'][0]['max']#3
    TempMin = tempJson["results"]['forecast'][0]['min']#4
    probChuva = tempJson["results"]['forecast'][0]['rain_probability']#6
else:
    print('[ERRO] Falha na Comunicação API(Tempo)')

#logica para erro de temp max e atual
if temperaturaAtual > TempMax:
    TempMax = temperaturaAtual

#VerificarBOMDIABOATARDEOUBOANOITE
if horaAtual > 24 and horaAtual < 12:
    saudacaoDoDia = 'Bom dia'
elif horaAtual >= 12 and horaAtual < 18:
    saudacaoDoDia = 'Boa tarde'
else:
    saudacaoDoDia = 'Boa noite'


#SAIDA
print('-------------------------------------------------------------------')
print('|                       ATUALIZAÇÕES DO DIA                       |')
print(f'|                    {cidade}                    |')
print(f'|                  {diaSemana}, {dataFormatada}                 |')
print('-------------------------------------------------------------------')
print(f'\n                        {saudacaoDoDia}, usuário.                 ')
print('\n-------------------------------------------------------------------')
print('\n                      COTAÇÂO DAS MOEDAS HOJE                      ')
print(f'        Dólar: R${valorDolar:.2f} | Euro: R${valorEuro:.2f} | Bitcoin: R${valorBitcoin:.2f}')
print('\n-------------------------------------------------------------------')
print('\n                          TEMPERATURA ATUAL                        ')
print(f'                        {descricaoTempo}')
print(f'                    {temperaturaAtual}°C | Max: {TempMax}°C | Min: {TempMin}°C')
print(f'                     Chuva(mm): {quantidadeChuva} | Chuva %: {probChuva}')
print(f'                        Atualizado em: {ultAtualizacao}')
print('\n-------------------------------------------------------------------')


