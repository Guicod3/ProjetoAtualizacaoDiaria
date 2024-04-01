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


#VerificarBOMDIABOATARDEOUBOANOITE
if horaAtual >= 4 and horaAtual < 12:
    saudacaoDoDia = 'Bom dia'
elif horaAtual >= 12 and horaAtual < 18:
    saudacaoDoDia = 'Boa tarde'
else:
    saudacaoDoDia = 'Boa noite'


#SAIDA
print('-------------------------------------------------------------------')
print('|                       ATUALIZAÇÕES DO DIA                       |')
print(f'|                 {diaSemana}, {dataFormatada}                 |')
print('-------------------------------------------------------------------')
print(f'\n                        {saudacaoDoDia}, usuário.                 ')
print('\n-------------------------------------------------------------------')
print('\n                      COTAÇÂO DAS MOEDAS HOJE                      ')
print(f'        Dólar: R${valorDolar:.2f} | Euro: R${valorEuro:.2f} | Bitcoin: R${valorBitcoin:.2f}')
print('\n-------------------------------------------------------------------')





