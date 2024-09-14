núm = cont = soma = 0
núm = int(input('Digite um número [999 para parar]: '))
while núm != 999:
    núm = int(input('Digite um número [999 para parar]: '))
    soma += núm
    cont += 1
    núm = int(input('Dite um número [999 para parar]: '))
print('Você digitou {} números e as soma entre eles foi {}.' .format(cont - 1, soma - 999))