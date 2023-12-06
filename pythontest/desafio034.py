#calculando aumento de salários
'''sal = float(input('Digite o seu salário:'))
aum10 = sal * 10/100
aum15 = sal * 15/100
if sal > 1250.00:
    print(f'Você receberá R${aum10:.2f} de aumento!')
if sal <= 1250.00:
    print(f'Você receberá R${aum15:.2f} de aumento!')'''
#outra forma de fazer
sal = float(input('Digite seu salário:'))
if sal <= 1250:
    novo = sal + (sal * 15/100)
else:
    novo = sal + (sal * 10/100)
print(f'Seu novo salário é {novo}!')
