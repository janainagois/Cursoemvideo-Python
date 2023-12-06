#receber um número real e mostrar a parte inteira
from math import floor
num = float(input('Digite um número real:'))
print(f'A porcão inteira de {num} é {floor(num)}')

#outra forma de fazer é usando a função trunc() de math

'''mais uma forma de fazer
num = float(input('Digite um número real:'))
print(f'A porcão inteira de {num} é {int(num)}')'''
