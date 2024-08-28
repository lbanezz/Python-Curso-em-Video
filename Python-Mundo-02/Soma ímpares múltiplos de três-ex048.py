soma = 0
cont = 0
for d in range(1,501, 2):
    if d % 3 == 0:
        cont = cont + 1
        soma = soma + d
print('A soma de todos os valores solicitados é {}'.format(cont, soma))
