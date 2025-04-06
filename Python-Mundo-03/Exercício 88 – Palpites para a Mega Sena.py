from random import randint 
from time import sleep
lista = list()
jogos = list()
print('-' *  30)
print('      Joga na mega sena         ')
print('-' * 30)
quant = int(input('Quantos jogos você quer que eu sorteie? '))
tot = 1
while tot <= quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear
    tot += 1
print('-=' * 3, f'Sorteando {quant} jogos ', '-=' * 3)
for i, l in enumerate(jogos):
    sleep(2)
    print(f' Jogos {i}: {l} ')
print('-=' * 5, '< Boa sorte! >', '-=' * 5 )
