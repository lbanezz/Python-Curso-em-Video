from random import randint
computador = randint(0,1)
print('Sou seu computador... Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue advinhar qual foi? ')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual é seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mias... Tente mais uma vez.')
        elif jogador > computador:
            print('Menos... Tnte mais um avez.')   
print('Acertou com {} palpites'.format(palpites))