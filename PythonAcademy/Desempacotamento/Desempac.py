# Desempacotamento em chamadas
# de métodos e funções

string = 'ABCD'
lista = ['Banana', 'Abacate', 'Laranja']
tupla = 'Python', 'é', ' legal'
salas = [
    # 0        1
    ['Maria', 'Helena', ],  # 0
    # 0
    ['Elaine', ],  # 1
    # 0       1       2
    ['Luiz', 'João', 'Eduarda', ],  # 2
]


# p, b, *_, ap, u = lista
# print(p, u, ap)

"""
-> Em Python, o uso de *_ é uma convenção comumente usada para indicar variáveis que você não pretende usar ou que não são relevantes em uma determinada parte do código. O *_ é conhecido como "variável descartável" ou "wildcard" e é usado para indicar que os valores não serão usados ou acessados posteriormente.
"""

print(*lista, end='\n')
print(*string, sep='\n')
print(*tupla)
