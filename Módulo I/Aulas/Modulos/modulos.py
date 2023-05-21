#Importando bliotecas

import emoji
from math import sqrt, ceil

# import math
# import bebida => generalista
# from math import ceil
# from bebida import cafe => especifico


numero = int(input('Insira um número: '))
raiz = sqrt(numero)
print('A raiz de {} é igual a {}' .format(numero, ceil(raiz)))
print(emoji.emojize('Python is :thumbs_up:'))