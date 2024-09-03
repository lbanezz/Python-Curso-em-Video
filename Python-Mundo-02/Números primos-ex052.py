núm = int(input('Digite um número: '))
tot = 0 
for d in range(1, núm + 1):
    if núm % d == 0:
        print('\033[36m', end='')
        tot += 1
    else:
        print('\033[31m', end='')
    print('{}' .format(d), end='')
print('\n\033 [m O número {} foi divisível {} vezes' .format(núm, tot))
if tot == 2:
    print('E por isso ele É PRIMO!')
else:
    print('E por isso ele NÃO É PRIMO!')