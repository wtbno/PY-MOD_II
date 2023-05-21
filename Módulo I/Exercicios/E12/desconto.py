preco = float(input('Insira o preço do produto: R$ '))
desconto = preco - (preco * 5 / 100)
segDesconto = preco - (preco * 10 / 100)
tercDesconto = preco - (preco * 30 / 100)

print('O produto custava R$ {:.2f} e com desconto ficou por R$ {}' .format(
    preco, desconto))
print('O produto custava R$ {:.2f} e com 10% de desconto ficou por R$ {} ' .format(
    preco, segDesconto))
print('O produto custava R$ {:.2f} e com 30% de desconto ficou por R$ {} ' .format(
    preco, tercDesconto))
