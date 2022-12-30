valor = int(input('Insira o valor que deseja converter: '))
print('=====' * 10)
print('[1] para binário')
print('[2] para octal')
print('[3] para hexadecimal')
opcao = str(input('Selecione a opção desejada: '))
if opcao == 1:
    sBin = str(bin(valor))
    print(sBin)
elif opcao == 2:
    sOct = str(oct(valor))
elif opcao == 3:
    sHex = str(hex(valor))
