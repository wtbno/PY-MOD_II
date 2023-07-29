while True:
    operacao = str(input(
        "Digite a operação desejada (soma, subt, div, mult): ")).lower()
    num_1 = int(input("Insira o primeiro número: "))
    num_2 = int(input("Insira o segundo número: "))

    if operacao == "soma":
        resultado = int(num_1) + int(num_2)
    elif operacao == "subt":
        resultado = int(num_1) - int(num_2)
    elif operacao == "div":
        resultado = int(num_1) / int(num_2)
    elif operacao == "mult":
        resultado = int(num_1) * int(num_2)
    else:
        resultado = "Operação indisponível"

    print("O resultado da operação é: " + str(resultado))

    # if sair is True:
    #     break


# ordem de precedência
# 1 ()
# 2 **
# 3 * / // %
# 4 + -
