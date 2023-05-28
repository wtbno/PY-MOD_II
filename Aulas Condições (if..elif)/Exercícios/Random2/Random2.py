from random import randint
from time import sleep

computador = randint(0, 10)
resposta = 0
tentativas = ''
print('Sou seu computador, advinhe o número que escolhi ')
print('Qual seu palpite? ')
jogador = int(input())
while resposta < computador:
    print('Errado, é mais')
    print('Tentar novamente? [S/N] ')
