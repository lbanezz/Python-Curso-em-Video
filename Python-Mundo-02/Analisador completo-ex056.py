somaidade = 0
médiaidade = 0
for p in range ('1, 5'):
    print('------- {}ª PESSOA -----'.format(p))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    somaidade += idade

médiaidade = somaidade/ 4
print('A média idade do grupo é de {} anos'.format(médiaidade))
