temp = []
princ = []

while True: 
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))
    princ.append(temp[:])
    resp = str(input('Quer continuar? [S/N]'))
    if resp in 'Nn' :
        break
print('Os dados {princ}')