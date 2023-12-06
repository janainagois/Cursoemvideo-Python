#descobrindo fatorial
from math import factorial
n = int(input('Digite um número e descubra seu fatorial:'))
#a forma de fazer com módulo
#f = factorial(n)
#print(f'O fatorial de {n} é {f}')
#utilizando for
fatorial = 1
for f in range(1, n + 1):
    fatorial *= f
print(f'O fatorial de {n} é {fatorial}.')
#uilizando while
'''c = n
#começando multiplicação limpa
f = 1
print(f'Calculando {n}! = ', end='')
while c > 0:
    print(f'{c}', end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print(f'{f}')'''

