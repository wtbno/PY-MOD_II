import emoji
from time import sleep
while True:

    num_1 = float(input("Insira o primeiro número: "))
    num_2 = float(input("Insira o segundo número: "))
    operacao = str(input(
        "Digite a operação desejada (+*-/): "))

    num_Validos = None
    num_1f = 0
    num_2f = 0
    try:
        num_1f = float(num_1)
        num_2f = float(num_2)
        num_Validos = True

    except:

        num_Validos = None

        if num_Validos is None:
            print('Um dos valores digitados é inválido')
            continue

        operadores = '+*-/'
        if operacao not in operadores:
            print('Operador inválido')
            continue
        if len(operacao) > 1:
            print('Selecione ape')
            continue
    print(emoji.emojize('Realizando operação :abacus:'))
    sleep(2)
    if operacao == '+':
        print(f'Resultado: {num_1 + num_2}')
    if operacao == '*':
        print(f'Resultado: {num_1 * num_2}')
    if operacao == '-':
        print(f'Resultado: {num_1 - num_2}')
    if operacao == '/':
        print(f'Resultado: {num_1 / num_2}')

    sair = input(
        'Digite [s]air para encerrar ou enter para continuar: ').lower().startswith('s')
    if sair is True:
        break
