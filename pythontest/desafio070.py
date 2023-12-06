print('~'*15)
print('LOJA J GÓIS')
print('~'*15)
pr = cmp = total = menor = cont = 0
barato = ' '
while True:
    p = str(input('Qual produto vai comprar? '))
    pr = float(input('Quanto custa? R$'))
    cont += 1
    total += pr
    if pr > 1000:
        cmp += 1
    if cont == 1 or pr < menor:
        menor = pr
        barato = p
    c = ' '
    while c not in 'SN':
        c = str(input('Quer continuar comprando?[S/N] ')).upper().strip()[0]
    if c == 'N':
        break
print('FIM DO PROGRAMA')
print(f'O total da compra foi {total:.2f}')
print(f'{cmp} dos seus produtos custam mais de R$1.000,00')
print(f'O produto mais barato foi {barato} que custa R${menor:.2f}')
