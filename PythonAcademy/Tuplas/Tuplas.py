"""
Uma lista imutável

=> mais efeciente que a lista
=> Ao criar uma tupla não utiliza os []
"""


pedidos = 'Batata', 'Hamburger', 'Suco', 'Milk-Shake'
# pedido = tuple(pedido) => converte uma lista pra tupla
# pedido = list(pedido) => converte uma tupla para uma lista
# pedidos[2] = 'Refrigerante' => Não é possível alterar
print(pedidos)
