entrada = int(input('Digite a hora atual em números inteiro: '))
# isdigit checa se a entrada é só número


try:
    # Código que pode gerar uma exceção
    hora = int(entrada)

    if hora >= 0 and hora <= 11:
        print('Bom dia!')
    elif hora >= 12 and hora <= 17:
        print('Boa tarde!')
    elif hora >= 18 and hora <= 23:
        print('Boa noite')
    else:
        print('Horário incorreto')

except:
    # Código para lidar com a exceção
    print('Insira apenas números inteiros')


"""Explicação do fluxo de execução do try-except:

1.O código dentro do bloco try é executado normalmente.
2.Se ocorrer uma exceção dentro do bloco try, a execução é interrompida e o Python procura por um bloco except que corresponda ao tipo de exceção gerada.
3.Se uma correspondência é encontrada, o código dentro do bloco except é executado, permitindo que você trate a exceção de alguma maneira específica.
4.Se nenhuma correspondência é encontrada, o programa pára e uma mensagem de erro é exibida."""


# if horario in range(1, 11):
#     print('Bom dia!')
# elif horario in range(12, 17):
#     print('Boa tarde!')
# elif horario in range(18, 00):
#     print('Boa noite!')
