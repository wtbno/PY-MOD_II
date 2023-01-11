valor = int(input('Insira o valor que deseja converter: '))
print('=====' * 10)

print('''Escolha uma opção para conversão: 
[1] para binário 
[2] para octal 
[3] para hexadecimal''')

opcao = int(input('Sua opção é '))
if opcao == 1:
    print("{} resultado desse valor em binário é: {} ".format(valor, bin(valor)))
elif opcao == 2:
    print("{} resultado desse valor em octal é: {} ".format(valor, oct(valor)))
elif opcao == 3:
    print("{} resultado desse valor em hexadecimal é: {} ".format(valor, hex(valor)))
