pt = int(input('Digite o primeiro termo da PA:'))
rz = int(input('Digite a razão da PA:'))
termo = pt
cont = 1
total = 0
mais = 10
print('Mostrando os 10 primeiros termos:')
while mais != 0:
    total += mais
    while cont <= total:
        print(f'{termo} -->', end=' ')
        termo += rz
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais?'))
print(f'Progressão finalizada com {total} termos mostrados!')






