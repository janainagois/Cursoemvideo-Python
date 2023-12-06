#soma de números específicos a partir de números dados
s = 0
cont = 0
for c in range(1,7):
    n = int(input(f'Digite o {c}º valor:'))
    if n%2==0:
        s += n
        cont += 1
print(f'Você informou {cont} números pares e a soma dos valores é {s}')
