soma = 0
cont = 0
for d in range(1, 7):
    num = int(input('Digite o {} valor: '.format(d)))
    soma  += num
    cont += 1
print('Você informou {} números e a soma foi {}' .format(cont, soma))
