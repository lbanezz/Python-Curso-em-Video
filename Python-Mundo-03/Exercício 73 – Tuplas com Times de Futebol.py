times = ("Atlético Mineiro","Flamengo","Palmeiras","São Paulo",
    "Corinthians","Internacional","Grêmio","Fluminense"
    "Santos","Athletico Paranaense","Ceará","Bahia",
    "Botafogo","Vasco da Gama","Cruzeiro"," Goiás")
print('-=' * 15)
print(f"Lista de time: {times} ")
print('-=' * 15)
print(f'Os 5 primeiros são {times[0:5]}')
print('-=' * 15)
print(f'Os 4 últimos são {times[-4:]}')
print('-=' * 15)
print(f'Times em ordem alfabética: {sorted(times)}')
print('-=' * 15)
print(f'O Chapecoense está na : {times.index('Vasco da gama')+1} posição')