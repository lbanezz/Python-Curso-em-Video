primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
décimo = primeiro + (10 - 1) * razão
for d in range(primeiro, décimo, razão):
        print('{}' .format(d), end=' -> ')
print('ACABOU')