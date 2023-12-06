#fazendo a progressão aritimética
from time import sleep
pt = int(input('Digite o primeiro termo da PA:'))
rz = int(input('Digite a razão da PA:'))
pa = pt
print('Calculando os dez primeiros termos da PA...')
sleep(3)
for m in range(10):
    print(pa, end=' ->')
    pa += rz
'''forma Guanabara
pt = int(input('Digite o primeiro termo da PA:'))
rz = int(input('Digite a razão da PA:'))
décimo = pt + (10 - 1) * rz 
print('Calculando os dez primeiros termos da PA...')
for c in range(pt, décimo + rz, rz):
    print(f'{c}, end=' ->'')
print('ACABOU')'''

