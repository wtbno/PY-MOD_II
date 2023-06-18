nome = str(input('Qual o seu nome? '))
altura = float(input('Insira sua altura: '))
peso = float(input('Agora coloque o seu peso: '))
imc = peso/(altura * altura)


# fstrings => não utiliza vírgulas
# resposta = f'{nome} tem {altura:.2f} de altura '
print('Olá {}, sua altura é {:.2f} seu índice de massa corpórea é: {:.2f} '.format(
    nome, altura, imc))


# imc...Ellipsis
