"""
Introdução ao empacotamento e desempacotamento

=> 
"""


# pedido1, pedido2, pedido3, pedido4 = [
#    'Batata', 'Hamburger', 'Suco', 'Milk-Shake']
# pedido1, pedido2, pedido3, pedido4 = pedido


# => Empacotamento de outras variáveis que não serão utilizadas
# Criar uma var e não utilizar não é uma boa prática
# Para isso pode utilizar *_ sinalizando que não será utilizável
pedido1, *resto = [
    'Batata', 'Hamburger', 'Suco', 'Milk-Shake']


print(pedido1)
print(*resto)
