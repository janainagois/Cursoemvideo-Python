#melhorando o desafio 028
from random import randint
nm = randint(0,10)
palpite = 0
acertou = False
print('O computador "pensou" um número entre (0 - 10).')
palpite = 0
while not acertou:
    jogador = int(input('Qual é seu palpite?'))
    palpite += 1
    if jogador == nm:
        acertou = True
    else:
        if jogador < nm:
            print('Ainda não, é maior. Tente novamente!')
        elif jogador > nm:
            print('Ainda não, é menor. Tente novamente!')
print(f'Você venceu após {palpite} tentativas.')

