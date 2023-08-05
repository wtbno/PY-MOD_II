"""
Listas em Python
Tipo list - Mutável => lista de coisas semelhante o array do JS
Mutável, ou seja, o conteúdo desta lista pode ser alterada
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis: append, insert, pop, del, clear, extend, +
lista = [] => lista vazia 
"""
#        +01234
#        -54321
string = 'ABCDE'  # 5 caracteres (len)
# print(bool([]))  # falsy
# print(lista, type(lista))

#        0    1      2              3    4
#       -5   -4     -3             -2   -1
lista = [123, True, 'Bruno Alves',  1.2, []]
# => modificação da str da lista de 'Bruno Alves' para 'Camila'
lista[-3] = 'Camila '
print(lista)
print(lista[2], type(lista[2]))
