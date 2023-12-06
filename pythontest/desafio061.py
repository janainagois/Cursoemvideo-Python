#refazendo o desafio 51 (PA)
pt = int(input('Digite o primeiro termo da PA:'))
rz = int(input('Digite a razão da PA:'))
termo = pt
cont = 1
while cont <= 10:
    print(f'{termo} -->', end=' ')
    termo += rz
    cont += 1
print('FIM')
