"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis:
    append, insert, pop, del, clear, extend, +
Create Read Update   Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)

"""


lista = [10, 20, 30, 40]


numero = lista[2]
print(numero)
numero = lista[2] = 400
print(numero)

del lista[3]
""" 
=> exclui um item da lista, e ao excluir um item da lista, altera todo seu indice,
ao excluir um indice da lista, isso acarretará uma reorganização desses items, o que pode
gera um custo de processamento do programa como um todo
Para reduzir os danos, é interessante a remoção apenas do final da lista
"""
print(lista)


"""
=> Método append é utilizado para adicionar um elemento ao final de uma lista.
=> Ao adicionar um elemento ao final da lista, essa lista aumenta seu tamanho em 1
"""

lista.append(890)
lista.append(782)
print(lista)
lista.pop()
# .pop() remove o último item da lista
print(lista)
lista.append('Batata')
print(lista)
lista.append('Cenoura')
lista.append('Pepino')
lista.append('Chuchu')
print(lista)
# remover um item de acordo com seu índice <-
lista.pop(0)
print(lista)
