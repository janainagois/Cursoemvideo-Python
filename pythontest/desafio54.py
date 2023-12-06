#contando idades
from datetime import date
ano = date.today().year

maior_idade = 0
menor_idade = 0

for c in range(1,8):
    nascimento = int(input(f'Digite em que ano a {c}ª pessoa nasceu:'))
    idade = ano - nascimento
    if idade >= 21:
            maior_idade += 1
    else:
            menor_idade += 1
print(f'Quantidade de pessoas que atingiram a maior idade: {maior_idade}')
print(f'Quantidade de pessoas que não atingiram a maior idade: {menor_idade}')


