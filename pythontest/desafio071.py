print('='*30)
print('{:^30}'.format('BANCO DA JG'))
print('='*30)
valor = int(input('Que valor você quer sacar? R$'))
total = valor
nota = 50
totalnota = 0
while True:
    if total >= nota:
        total -= nota
        totalnota += 1
    else:
        if totalnota > 0:
            print(f'Total de {totalnota} notas de R${nota}')
        if nota == 50:
            nota = 20
        elif nota == 20:
            nota = 10
        elif nota == 10:
            nota = 1
        totalnota = 0
        if total == 0:
            break
print('~'*30)
print('Nós do Banco JG agradecemos a preferência!')
print('~'*30)

