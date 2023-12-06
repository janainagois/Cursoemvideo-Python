#calculando seno, cosseno e tangente a partir de um ângulo
from math import sin, cos, tan, radians
a = int(input(f'Digite o ângulo que você deseja:'))
b = radians(a)
print(f'O seno de {a} é {sin(b):.2f}\nO cosseno de {a} é {cos(b):.2f}\nA tangente de {a} é  {tan(b):.2f}')
