print('{}'.format('LOJAS REIS'))
preço = float(input('Preço das comporas: R$ '))
print('''FORMAS DE PAGMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista no cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''' )
opção = int(input('Qual é a opção?  '))
if opção == 1:
    total = preço - (preço * 10 / 100)
elif opção == 2:
    total = preço - (preço * 5 / 100)
elif opção == 3:
    total = preço 
    parcela = total / 2
    print('Sua compra será parcelada em 2x de R${:.2f}' .format(parcela))
print('Sua compra de R${:.2f} vai cusatr R${:.2f} no final.' .format(preço, total))
