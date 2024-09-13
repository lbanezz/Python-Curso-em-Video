from math import factorial
d = int(input('Digite um númeor para calcular seu Fatorial: '))
c = d
f = 1 
print('Calculando {}! = '.format(d), end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= d
    c -= 1
print('{}'.format(f))