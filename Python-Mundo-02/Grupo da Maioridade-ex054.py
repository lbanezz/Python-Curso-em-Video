from datetime import date
ano_atual = date.today().year
for pess in range(1, 8):
    nasc = int(input('Em que ano a pessoa nasceu? '))
idade = ano_atual - nasc
if idade >= 21:
    print('Essa pessoa é maior')
else:
    print('Essa pessoa é menor')