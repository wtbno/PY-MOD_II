numero = int(input('Insira um número inteiro: ').isdigit())


if numero != int:
    print('Esse não é um número inteiro')
if numero % 2 == 0:
    print('O valor {} é um número par'.format(numero))

else:
    print('O valor {} é um número ímpar'.format(numero))
