from random import randint
numeros = randint(1,10), randint(1,10), randint(1,10), 
randint(1,10), randint(1,10),
print('Os valores sorteados foram: ', end='')
for n in numeros: 
    print(f'Eu sortei o valor {n}')
print(f'O maior valor sorteado foi {max(numeros)}')
print(f'O maior valor sorteado foi {min(numeros)}')
