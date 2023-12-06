#comparando peso
maior = 0
menor = 0
for p in range(1,6):
    peso = float(input(f'Digite o peso da {p}ª pessoa em Kg:'))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f'O maior peso lido é {maior:.2f}Kg.')
print(f'O menor peso lido é {menor:.2f}Kg.')
