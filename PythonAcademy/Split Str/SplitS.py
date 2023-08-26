"""
split e join com list e str
split - divide uma string (list)
join - une uma string
"""
frase = '   Olha só que   , coisa interessante          '
# -> especificando para realizar a quebra na vírgula
lista_frases_cruas = frase.split(',')
# rstrip para cortar espaço da direita e lstrip da esquerda
lista_frases = []
for i, frase in enumerate(lista_frases_cruas):
    lista_frases.append(lista_frases_cruas[i].strip())

# print(lista_frases_cruas)
# print(lista_frases)
frases_unidas = ', '.join(lista_frases)
# join é um método, que pode ser utilizado somente com iteráveis.
print(lista_frases_cruas)
print(frases_unidas)
