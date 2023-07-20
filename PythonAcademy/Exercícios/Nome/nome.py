nome = input('Insira seu nome: ')
tamanho = len(nome)

if tamanho <= 4:
    print('Seu nome é curto')
elif tamanho == 5:
    print('Seu nome é um tamanho normal')
else:
    print('Seu nome é longo')
