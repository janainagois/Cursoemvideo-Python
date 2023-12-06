#computador joquenpô
import random
from time import sleep
#print('Quer jogar joquenpô com o computador?')
#jogador1 = str(input('Digite pedra, papel ou tesoura:'))
jogo = ['pedra', 'papel', 'tesoura']
jogador2 = random.choice(jogo)
#print(f'O computador colocou {jogador2}.')
'''if jogador1 == 'tesoura' and jogador2 == 'papel':
    print('Você venceu!')
elif jogador1 == 'papel' and jogador2 == 'tesoura':
    print('Você perdeu!')
elif jogador1 == 'papel' and jogador2 == 'pedra':
    print('Você venceu!')
elif jogador1 == 'pedra' and jogador2 == 'papel':
    print('você perdeu!')
elif jogador1 == 'pedra' and jogador2 == 'tesoura':
    print('Você ganhou!')
elif jogador1 == 'tesoura' and jogador2 == 'pedra':
    print('Você perdeu!')
else:
    print('Deu empate!')'''
#outra forma
'''if jogador1 == jogador2:
    print('Deu empate!')
if jogador1 == 'tesoura':
    if jogador2 == 'papel':
        print('Você venceu!')
    elif jogador2 == 'pedra':
        print('VocÊ perdeu!')
elif jogador1 == 'pedra:':
    if jogador2 == 'tesoura':
        print('Você venceu!')
    elif jogador2 == 'papel':
        print('Você perdeu!')
elif jogador1 == 'papel':
    if jogador2 == 'pedra':
        print('Você venceu!')
    elif jogador2 == 'tesoura':
        print('Você perdeu!')'''
#forma Guanabara
#itens == jogo
#computador == jogador2
print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input('Qual é a sua jogada?'))
print('JO')
sleep(1)
print('KEM')
sleep(1)
print('PO!!!')
sleep(1)
print('-=' * 11)
print(f'Computador jogou {jogador2}')
print(f'Você jogou {jogo[jogador]}')
print('-=' * 11)
if jogador2 == 'pedra':
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('VOCÊ GANHOU')
    elif jogador == 2:
        print('O COMPUTADOR GANHOU')
    else:
        print('JOGADA INVÁLIDA!')
elif jogador2 == 'papel':
    if jogador == 0:
        print('O COMPUTADOR GANHOU')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('VOCÊ GANHOU')
    else:
        print('JOGADA INVÁLIDA!')
elif jogador2 == 'tesoura':
    if jogador == 0:
        print('VOCÊ GANHOU')
    elif jogador == 1:
        print('O COMPUTADOR GANHOU')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('JOGADA INVÁLIDA!')


