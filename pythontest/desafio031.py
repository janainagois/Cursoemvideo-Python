#calculando o valor da viagem
km = float(input('digite qual a distância em km até o seu destino?'))
p1 = km * 0.5
p2 = km * 0.45
if km <= 200:
    print(f'Sua passagem vai custar R${p1:.2f}')
else:
    print(f'Sua passagem vai custar R${p2:.2f}')



