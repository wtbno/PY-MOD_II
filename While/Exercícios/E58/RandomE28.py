from random import randint
from time import sleep

tentativas = 0
computador = randint(0, 10)
print('-=-' * 20)
print('Vou pensar em um número de 0 à 10 tente advinhar')
print('-=-' * 20)
jogador = int(input('Em que número eu pensei? '))
print('PROCESSANDO . . .')
sleep(3)
while jogador != computador:
    print('Você errou!!!')
    continuar = str(input('Quer tentar novamente? [S/N] '))
    jogador = int(input('Em que número eu pensei? '))

    '''tentativas += continuar'''
print('Você ganhou, mas tentou {} vezes' .format(tentativas))
