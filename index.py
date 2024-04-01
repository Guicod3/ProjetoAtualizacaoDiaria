#ENTRADA DE DADOS
from datetime import datetime #calendário e horas atuais
import requests from requests
import json
data = datetime.now()
dataFormatada = data.strftime('%d/%m/%Y %H:%M')

diaSemanaValorBase = datetime.weekday(data)#Mostrar dia da semana
diaSemanaTextoBase = ('Segunda-Feira', 'Terça-Feira', 'Quarta-Feira', 'Quinta-Feira', 'Sexta-Feira', 'Sábado', 'Domingo')
diaSemana = diaSemanaTextoBase[diaSemanaValorBase]

horaAtual = datetime.now().hour #Hora atual Int
saudacaoDoDia = ''

#APICOTACAO
chaveCotacao = https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL
responseCot = get(chaveCotacao)



#COMPILAÇãO E LOGICA
if horaAtual >= 4 and horaAtual < 12:
    saudacaoDoDia = 'Bom dia!'
elif horaAtual >= 12 and horaAtual < 18:
    saudacaoDoDia = 'Boa tarde!'
else:
    saudacaoDoDia = 'Boa noite!'


#SAIDA
print('ATUALIZAÇÕES DO DIA')
print(f'\n{saudacaoDoDia}, usuário.')
print(f'\n{diaSemana}, {dataFormatada}')




