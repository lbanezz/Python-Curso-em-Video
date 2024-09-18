d = s = 0
while d != 999:
    d = int(input('Digite um número: '))
    if d == 999:
        break
    s += d
print('A soma vale {}'.format(s))
