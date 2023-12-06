#calculando maior e menor
n1 = int(input('Digite um número:'))
n2 = int(input('Digite outro número:'))
n3 = int(input('Digite mais um número:'))
'''if n1 > n2:
    if n1 > n3:
        print(f'{n1} é o maior!')
if n2 > n1:
    if n2 > n3:
        print(f'{n2} é o maior!')
if n3 > n1:
    if n3 > n2:
        print(f'{n3} é o maior')
if n1 < n2:
    if n1 < n3:
        print(f'{n1} é o menor!')
if n2 < n1:
    if n2 < n3:
        print(f'{n2} é o menor!')
if n3 < n1:
    if n3 < n2:
        print(f'{n3} é o menor')'''
#outra forma de fazer
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
print(f'O maior número é {maior} e o menor número é {menor} ')



