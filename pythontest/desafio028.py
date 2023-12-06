from random import randint
#fazer a máquina fingir que está pensando
from time import sleep
#computador x usuário descobrindo um número

#o computador vai sortear um número de 0 - 5
nm = randint(0,5)
#o usuário vai descobrir o número que o compuador 'pensou'
nu = int(input('O computador "pensou" um número entre (0 - 5).\nDigite qual você acha que foi:'))
#se o número que usuário digitou for igual ao do computador imprima você venceu
print('PROCESSANDO...')
sleep(3)
if nm == nu:
    print('Você venceu a máquina!')
#senão imprima você perdeu
else:
    print('Você perdeu!')