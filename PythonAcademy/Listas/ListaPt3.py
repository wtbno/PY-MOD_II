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
mercado = ['Batata', 'Cenoura', 'Mexerica', 'Banana', 'Maçã']
print(mercado)
mercado.append('Pão')
print(mercado)
mercado.pop()
print(mercado)
mercado.append('Ovos')
print(mercado)
del mercado[-1]
print(mercado)
mercado.insert(1, 'Requeijão')
# => esse método recebe dois argumentos, que são valores que são passados para os métodos
# => foi inserido um elemento na posição 1 sendo ele a str 'Requeijão'
print(mercado)
