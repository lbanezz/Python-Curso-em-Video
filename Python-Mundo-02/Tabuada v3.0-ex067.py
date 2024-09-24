while True:
    d = int(input('Quer ver a tabuada de qual valor? '))
    if d < 0:
          break
    print('-' * 30)
    for c in range(1, 11):
            print(f'{d} x {c} = {d*c}')
    print('-' * 30)
print('PROGRAMA DA TABUADA ENCERRADO. Volte sempre!')