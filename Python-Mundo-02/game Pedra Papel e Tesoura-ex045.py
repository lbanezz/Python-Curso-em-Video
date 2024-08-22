from random import randint
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0,2)
print('''Suas opções:
[ 0 ] PEDRA 
[ 1 ] PAPEL
[ 2 ] TESOURA ''')
jogador = int(input('Qual é a sua jogada? '))
print('Computador jogou {}' .format(itens[computador]))
print('Jogador jogou {}' .format(itens[jogador]))