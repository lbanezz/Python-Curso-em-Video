lista_num = []
mai = 0
men = 0
for c in range(0, 5):
    lista_num.append(int(input(f'Digite um valor para a Posição {c}: ')))
    if c == 0:
        mai = men = lista_num [c]

    else:
        if lista_num [c] > mai:
            mai = lista_num [c]
        if lista_num[c] < men:
            men = lista_num[c]
        
print('=-' * 30)
print(f'Você digitou os valores {lista_num}')
print(f'O maior valor digitado foi {mai} nas posições ', end='')
for i, v in enumerate(lista_num):
    if lista_num[i] == mai:
        print(f'{i}...', end=' ')
print()
print(f'O menor valor digitado foi {men} nas posições ', end='')
for i, in enumerate(lista_num):
    if v == men:
        print(f'{i}...', end='')
print()
