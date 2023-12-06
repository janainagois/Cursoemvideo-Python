#comaparando mais de uma característica
somaidade = 0
maioridadehomem = 0
totmulher20 = 0
nomevelho = ''
for c in range(1,5):
    print(f'------ {c}ª PESSOA ------')
    nome = str(input('Nome:')).strip()
    idade = int(input('Idade:'))
    sexo = input('Sexo[M/F]:').strip()
    somaidade += idade
    if c == 1 and sexo == 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1
média = somaidade/4
print(f'A média de idade do grupo é {média} anos')
print(f'O homem mais velho é {maioridadehomem} e o nome dele é {nomevelho}')
print(f'Ao todo são {totmulher20} mulheres com menos de 20 anos')
