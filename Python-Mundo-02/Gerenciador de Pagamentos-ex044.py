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
elif opção == 4:
    total = preço + (preço * 20 / 100)
    totalparc = int(input('Quantas parcelas?  '))
    parcela = total / totalparc
    print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS' .format(totalparc, parcela))
else:
    total = preço
    print('OPÇÃO INVALIDA de pagamento. Tente novamente!')
print('Sua compra de R${:.2f} vai custa R${:.2f} no final.' .format(preço, total))
