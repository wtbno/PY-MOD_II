import pygame
from time import sleep
import emoji
# Sleep para ficar com efeito de loading


for contagem in range(10, 0, - 1):

    print(emoji.emojize('WARNING, MISSILE ATTACK CONFIRM! :fire:'))
    print(contagem)
    sleep(1)

print('ROCKET!!!')
pygame.init()
pygame.mixer.music.load('nuclear.mp3')
pygame.mixer.music.play(loops=0, start=0.0)
input()
pygame.event.wait()
