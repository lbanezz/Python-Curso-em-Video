from random import randint
from time import sleep
computador = randint(0, 7) # Faz o computador "PENSAR"
print('-=- * 8')
print('Vou pensa em um número entre 0 e 7. Tenta advinhar...')
print('-=-' * 19)
jogador = int(input('Em que número eu pensei? ')) # Jogador tenta adivinhar
print('PROCESSANDO...')
sleep(2)
if jogador == computador:
    print('PARABENS! Você conseguiu vencer!')
else:
    print('Ganhei! Eu pensei no número {} e não no {} '.format(computador, jogador))