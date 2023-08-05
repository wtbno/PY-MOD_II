from time import sleep
primValor = int(input('Insira o primeiro valor: '))
segValor = int(input('Insira o segundo valor: '))
opcao = ''
while opcao != 6:
    print('''
    [1] → Adição 
    [2] → Subtração
    [3] → Divisão
    [4] → Multiplicação
    [5] → Novos valores
    [6] → Encerrar programa
    ''')

    opcao = int(input('→ Selecione uma opção: '))

    if opcao == 1:
        Adição = primValor + segValor
        print('A soma de {} e {} é igual à: {}'.format(primValor, segValor, Adição))
    elif opcao == 2:
        Subtração = primValor - segValor
        print('A subtração de {} e {} é igual à: {}'.format(primValor, segValor, Subtração))
    elif opcao == 3:
        Divisão = primValor / segValor
        print('A divisão de {} e {} é igual à: {}'.format(primValor, segValor, Divisão))
    elif opcao == 4:
        Multiplicação = primValor * segValor
        print('A múltiplicação de {} e {} é igual à: {}'.format(primValor, segValor, Divisão))
    elif opcao == 5:
        print('Insira novos números')
        primValor = int(input('Insira o primeiro valor: '))
        segValor = int(input('Insira o segundo valor: '))
else:
    opcao == 6
print('Encerrando programa. . . ')
sleep(2)
print('Até logo.')
