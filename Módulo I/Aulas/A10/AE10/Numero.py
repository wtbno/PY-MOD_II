import random
import emoji
from time import sleep
aleatorio = random.randint(0, 100)  # Faz o PC escolher um número
print('-*-' * 20)
escolha = int(input('Pense em um número de 0 a 100: '))
print('-*-' * 20)
print(emoji.emojize('Processando . . . :robot:'))
sleep(3)
if aleatorio == escolha:
    print(emoji.emojize('Parabéns, você venceu {} :celebration:' .format(aleatorio)))
else:
    print(emoji.emojize('Número incorreto, eu venci!!! :star-struck:'))
print('O número escolhido foi: {}' .format(aleatorio))
