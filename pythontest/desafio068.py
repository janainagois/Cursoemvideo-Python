import random
n = v = s = 0
print('~'*30)
print('Vamos jogar par ou ímpar?')
print('~'*30)
while True:
    n = int(input('Digite um número:'))
    pc = random.randint(0, 11)
    s = n + pc
    a = ' '
    while a not in 'PI':
        a = str(input('Par ou ímpar?[P/I]:')).upper().strip()[0]
    print(f'Você jogou {n} e o computador jogou {pc}. Total de {s}')
    if a == 'P':
        if s % 2 == 0:
            print('Você venceu!')
            v += 1
        else:
            print('Você perdeu!')
            break
    elif a == 'I':
        if s % 2 == 1:
            print('Você venceu!')
            v += 1
        else:
            print('Você perdeu!')
            break
    print('Vamos jogar novamente...')
print(f'GAME OVER! Você venceu {v} vezes')
