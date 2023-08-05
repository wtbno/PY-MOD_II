"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis:
    append - Adiciona um item ao final
    insert - Adiciona um item no índice escolhido
    pop - Remove do final ou do índice escolhido
    del - apaga um índice
    clear - limpa a lista
    extend - estende a lista
    + - concatena listas
Create Read Update   Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)
"""
lista_a = [32, 52, 99]
lista_b = ['Carro', 'Luz', 'Academia']
lista_c = lista_a + lista_b  # => extendendo a lista de uma forma
print(lista_c)
lista_d = lista_a.extend(lista_b)
# O método extend não retornada nada, pois está executando uma ação diretamente na var lista_a
# Ou seja, não posso pegar o valor da lista_a e jogar na lista_b, retornando então o none
print(lista_d)
