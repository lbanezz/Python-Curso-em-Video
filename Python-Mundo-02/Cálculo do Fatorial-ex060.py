from math import factorial
d = int(input('Digite um númeor para calcular seu Fatorial: '))
c = d
print('Calculando {}!'.format(d), end='')
while c > 0:
    print('{}  x '.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    c -= 1
#print('O fatorial de {} é {}' .format(n, f))