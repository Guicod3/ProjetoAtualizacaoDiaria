from datetime import datetime #calendário e horas atuais
data = datetime.now()
dataFormatada = data.strftime('%d/%m/%Y %H:%M')

diaSemanaValorBase = datetime.weekday(data)#Mostrar dia da semana
diaSemanaTextoBase = ('Segunda-Feira', 'Terça-Feira', 'Quarta-Feira', 'Quinta-Feira', 'Sexta-Feira', 'Sábado', 'Domingo')
diaSemana = diaSemanaTextoBase[diaSemanaValorBase]

print('ATUALIZAÇÕES DO DIA')
print(f'\n{diaSemana}, {dataFormatada}')


