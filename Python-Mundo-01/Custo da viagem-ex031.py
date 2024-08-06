distância = float(input('Qual é a distância da sua viagem?'))
print('Você está preste a começar uma viagem de {}Km.')
preço = distância * 0.50 if distância <= 200 else distância * 0.45
print('E o preço da sua passagem será de {:.2f}' .format(preço))