nome = str(input('Qual é seu nome?'))
if nome == 'David':
    print('Que nome top!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Geraldo':
        print('Seu nome é bem popular no Brasil.')
elif nome in 'Ana Clara Jéssica Julia':
     print('Belo nome feminino')
else:
    print('Seu nome é bom normal ')
    print('Tenha um bom dia, {}'.format(nome))

