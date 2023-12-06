#carregando e executando um arquivo mp3 do computador

import pygame
#inicializar o mixer do pygame

pygame.mixer.init()

#carregar o arquivo mp3

pygame.mixer.music.load('musica.mp3')
pygame.mixer.music.play()
while pygame.mixer.music.get_busy():
    continue

'''a= str(input('usuário:'))
if a == 'jana':
    pygame.mixer.music.load('musica.mp3')
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        continue
else:
    print('Sem música')'''



