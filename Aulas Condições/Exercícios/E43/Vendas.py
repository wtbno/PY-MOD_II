compras = float(input('Preço total das compras: R$ '))
print('-------------' * 10)
print('''Selecione a forma de pagamento:
[1] Dinheiro à vista
[2] Débito
[3] 2x crédito
[4] 3x crédito

''')
opcao = float(input('Qual é a opção? '))
if opcao == 1:
    total = compras - (compras * 10 / 100)
elif opcao == 2:
    total = compras - (compras * 10 / 100)
elif opcao == 3:
    total = compras
    parcela = total / 2
    print('Sua compra será parcelada em 2x no cartão sem juros de R${:.2f}' .format(
        parcela))
    print('Sua compra de R$ {:.2f} vai custar R$ {:.2f} no final' .format(
        compras, total))
elif opcao == 4:
    total = compras + (compras * 20 / 100)
    totparc = int(input('Quantas parcelas? '))
    parcela = total / totparc
    print('Sua compra será parcelada em {}x de R$ {:.2f}' .format(
        totparc, parcela))
    print('O valor será de R$ {:.2f} totalizando o valor final {:.2f}' .format(
        compras, total))
