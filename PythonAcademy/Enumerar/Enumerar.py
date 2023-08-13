pedido = ['Batata', 'Hamburger', 'Suco', 'Milk-Shake']


pedido.append('Sorvete')

print(pedido)

# pedidoEnum = enumerate(pedido)

# Ao utilizar o enumerate, não precisar ser diretamente utilizado em uma var
# utilizando o enumerate diretamente no laço for
# for item in enumerate:
#    print(item)

print(pedido)


# => (0, 'Batata')
# => (Tupla), índice, 'valor'

"""
A diferença entre as duas formas de impressão está na utilização da função enumerate() em cada uma delas.

Vamos analisar o código linha por linha:

Primeiro exemplo:

"""
for indice, items in enumerate(pedido):
    print(indice, items)

"""
Neste exemplo, a função enumerate() é usada para iterar sobre a lista pedido. A função enumerate() retorna um objeto iterável que gera tuplas contendo um índice e o valor correspondente em cada iteração. A variável indice recebe o índice e a variável items recebe o valor do item atual da lista pedido. O comando print() é utilizado para imprimir o índice e o item correspondente na mesma linha.
"""

for item in enumerate(pedido):
    print(item)
