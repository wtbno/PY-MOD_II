from random import randint


computador = randint(1, 10)
print('Sou seu computador, e pensei em um número')
print('Será que você consegue advinhar?')
acertou = False
palpites = 0

while not acertou:
    jogador = int(input('Qual o seu palpite? '))
    if jogador == 0:
        print('Escolha um número de 1 à 10')
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador > computador:
            print('Menos')
        elif jogador < computador:
            print('Não, é mais')

if palpites <= 2:
    print('Parabéns')
if palpites >= 3:
    print('Você acertou com {} palpites, vamos tentar novamente?' .format(palpites))
