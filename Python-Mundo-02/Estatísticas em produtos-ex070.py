total = totmil = menor = cont = 0
barato = ''
while True:
    produto = str(input('Nome do Porduto: '))
    valor = float(input('Valor: R$'))
    cont += 1
    total += valor
    if valor > 1000:
        totmil += 1
    if cont == 1:
        menor = valor
    else:
        if valor < menor:
            menor = valor
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print('{:-^40}'.format('FIM DO PROGRAMA'))
print(f'O total da compra foi {valor:.2f}')
print(f'Temos {totmil} produtos cutando mais de R$1000.00')
print(f'O produto mais barato foi {barato} que custa R${menor:.2f}')