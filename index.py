#ENTRADA DE DADOS
from datetime import datetime #calendário e horas atuais
import requests
import json
data = datetime.now()
dataFormatada = data.strftime('%d/%m/%Y %H:%M')

diaSemanaValorBase = datetime.weekday(data)#Mostrar dia da semana
diaSemanaTextoBase = ('Segunda-Feira', 'Terça-Feira', 'Quarta-Feira', 'Quinta-Feira', 'Sexta-Feira', 'Sábado', 'Domingo')
diaSemana = diaSemanaTextoBase[diaSemanaValorBase]

from newsdataapi import NewsDataApiClient #entrada do modulo de noticias e chave
key = 'pub_4134944160e86b1fb06065fdfed9e21969f24'
urlNews = NewsDataApiClient(apikey=key)


horaAtual = datetime.now().hour #Hora atual Int
saudacaoDoDia = ''

#APICOTACAO
urlCot = 'https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL'
responseCot = requests.get(urlCot)
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

#Módulo de noticias entrada
noticia = urlNews.news_api(country='br',category='politics', prioritydomain='top')
newsSports = urlNews.news_api(country='br',category='sports', prioritydomain='top')
newsWorld = urlNews.news_api(country='br',category='world', prioritydomain='top')


resultsPolitics = noticia['results']
resultsWorld = newsWorld['results']
resultsSports = newsSports['results']

#logica para erro de 0 resultados
if resultsPolitics == 0:
    newsPoliticsText = 'Sem resultados retornados na pesquisa'

elif resultsSports == 0:
    newsSportsText = 'Sem resultados retornados na pesquisa'

elif resultsWorld == 0:
    newsWorldText = 'Sem resultados retornados na pesquisa'

else:
    newsPoliticsText = (f'1 - {noticia['results'][0]['title']}\n2 - {noticia['results'][1]['title']}\n3 - {noticia['results'][2]['title']}')
    urlNewsPolitics = (f'1 - {noticia['results'][0]['link']}\n2 - {noticia['results'][1]['link']}\n3 - {noticia['results'][2]['link']}')

    newsSportsText = (f'1 - {newsSports['results'][0]['title']}\n2 - {newsSports['results'][1]['title']}\n3 - {newsSports['results'][2]['title']}')
    urlNewsSports = (f'1 - {newsSports['results'][0]['link']}\n2 - {newsSports['results'][1]['link']}\n3 - {newsSports['results'][2]['link']}')


    newsWorldText = (f'1 - {newsWorld['results'][0]['title']}\n2 - {newsWorld['results'][1]['title']}\n3 - {newsWorld['results'][2]['title']}')
    urlNewsWorld = (f'1 - {newsWorld['results'][0]['link']}\n2 - {newsWorld['results'][1]['link']}\n3 - {newsWorld['results'][2]['link']}')


#logica para erro de temp max e atual
if temperaturaAtual > TempMax:
    TempMax = temperaturaAtual

#VerificarBOMDIABOATARDEOUBOANOITE
if horaAtual >= 1 and horaAtual < 12:
    saudacaoDoDia = 'Bom dia'
elif horaAtual >= 12 and horaAtual < 18:
    saudacaoDoDia = 'Boa tarde'
else:
    saudacaoDoDia = 'Boa noite'

#logica do menu abaixo
def menuSelecao1(a):
    if a.isdigit() and int(a) <= 4 and int(a) > 0:
        a = int(a)
        if a == 1:
            link = noticia['results'][0]['link']
            print(f'Link: {link}')
            return menuSelecao1(input('\nDigite o número do tópico p/ ver seu link ou digite [4] p/ mais notícias:'))
        elif a == 2:
            link = newsSports['results'][0]['link']
            print(f'Link: {link}')
            return menuSelecao1(input('\nDigite o número do tópico p/ ver seu link ou digite [4] p/ mais notícias:'))
        elif a == 3:
            link = newsWorld['results'][0]['link']
            print(f'Link: {link}')
            return menuSelecao1(input('\nDigite o número do tópico p/ ver seu link ou digite [4] p/ mais notícias:'))
        elif a == 4: 
            textoSelecao = '1 - Política | 2 - Esporte | 3 - Mundo'
            print(textoSelecao)
            showCategory = menuSelecao2(input('\nEscolha a categoria de notícia: '))

    else:
        return print('[ERRO] Insira um valor válido'), menuSelecao1(input('\nDigite o número do tópico p/ ver seu link ou digite [4] p/ mais notícias: '))


def menuSelecao2(a):
    if a.isdigit() and int(a) <= 4 and int(a) > 0:
        a = int(a)
        if a == 1:
            print(newsPoliticsText)
            b = input('\nDigite o número da notícia para ver link e [4] p/ outra categoria: ')
            if b.isdigit() and int(b) <= 4 and int(b) > 0:
                b = int(b)
                if b == 1:
                    link = noticia['results'][0]['link']
                    print(f'Link: {link}')
                elif b == 2:
                    link = noticia['results'][1]['link']
                    print(f'Link: {link}')
                elif b == 3:
                    link = noticia['results'][2]['link']
                    print(f'Link: {link}')
                elif b == 4:
                    print('\n1 - Política | 2 - Esporte | 3 - Mundo')
                    menuSelecao2(input('\nEscolha a categoria de notícia: '))
            else:
                return print('[ERRO] Insira um valor válido'), menuSelecao2(input('\nEscolha a categoria de notícia: '))

        elif a == 2:
            print(newsSportsText)
            b = input('\nDigite o número da notícia para ver link e [4] p/ outra categoria: ')
            if b.isdigit() and int(b) <= 4 and int(b) > 0:
                b = int(b)
                if b == 1:
                    link = newsSports['results'][0]['link']
                    print(f'Link: {link}')
                elif b == 2:
                    link = newsSports['results'][1]['link']
                    print(f'Link: {link}')
                elif b == 3:
                    link = newsSports['results'][2]['link']
                    print(f'Link: {link}')
                elif b == 4:
                    print('\n1 - Política | 2 - Esporte | 3 - Mundo')
                    menuSelecao2(input('\nEscolha a categoria de notícia: '))
            else:
                return print('[ERRO] Insira um valor válido'), menuSelecao2(input('\nEscolha a categoria de notícia: '))
            
        elif a == 3:
            print(newsWorldText)
            b = input('\nDigite o número da notícia para ver link e [4] p/ outra categoria: ')
            if b.isdigit() and int(b) <= 4 and int(b) > 0:
                b = int(b)
                if b == 1:
                    link = newsWorld['results'][0]['link']
                    print(f'Link: {link}')
                elif b == 2:
                    link = newsWorld['results'][1]['link']
                    print(f'Link: {link}')
                elif b == 3:
                    link = newsWorld['results'][2]['link']
                    print(f'Link: {link}')
                elif b == 4:
                    print('\n1 - Política | 2 - Esporte | 3 - Mundo')
                    menuSelecao2(input('\nEscolha a categoria de notícia: '))
            else:
                return print('[ERRO] Insira um valor válido'), menuSelecao2(input('\nEscolha a categoria de notícia: '))
    else:
        return print('[ERRO] Insira um valor válido'), menuSelecao2(input('\nEscolha a categoria de notícia: '))





#SAIDA
print('-------------------------------------------------------------------')
print('|                       ATUALIZAÇÕES DO DIA                       |')
print(f'|                          {cidade}                          |')
print(f'|                  {diaSemana}, {dataFormatada}                 |')
print('-------------------------------------------------------------------')
print(f'\n                        {saudacaoDoDia}, usuário.                 ')
print('\n-------------------------------------------------------------------')
print('\n                      COTAÇÂO DAS MOEDAS HOJE                      ')
print(f'        Dólar: R${valorDolar:.2f} | Euro: R${valorEuro:.2f} | Bitcoin: R${valorBitcoin:.2f}')
print('\n-------------------------------------------------------------------')
print('\n                          TEMPERATURA ATUAL                        ')
print(f'                         {descricaoTempo}')
print(f'                    {temperaturaAtual}°C | Max: {TempMax}°C | Min: {TempMin}°C')
print(f'                     Chuva(mm): {quantidadeChuva} | Chuva %: {probChuva}')
print(f'                        Atualizado em: {ultAtualizacao}')
print('\n-------------------------------------------------------------------')
print('\n                          TOP 3 NOTÍCIAS DO DIA                      ')
print(f'\n1 - {noticia['results'][0]['title']}')
print(f'\n2 - {newsSports['results'][0]['title']}')
print(f'\n3 - {newsWorld['results'][0]['title']}')
showCategoryLink = menuSelecao1(input('\nDigite o número do tópico p/ ver seu link ou digite [4] p/ mais notícias: '))
print('\nSoftware feito por Guilherme Miranda.')
print('Repositório do Software: https://github.com/Guicod3/ProjetoAtualizacaoDiaria')
print('Linkedin do Criador: https://www.linkedin.com/in/guilhermemiranda12/')
print('\n-------------------------------------------------------------------')
input()

