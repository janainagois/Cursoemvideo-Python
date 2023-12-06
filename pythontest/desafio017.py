#calculando hipotenusa
from math import hypot
a = float(input('Digite a medida do cateto oposto:'))
b = float(input('Digite a medida do cateto adjacente:'))
print(f'A hipotenusa deste triângulo é {hypot(a,b):.2f}')

'''#outra forma de fazer
co = float(input('Comprimento do cateto oposto:'))
ca = float(input('Comprimento do cateto adjacente:'))
hi = (co ** 2 + ca ** 2) ** (1/2)
print(f'A hipotenusa vai medir {hi:.2f}')'''
