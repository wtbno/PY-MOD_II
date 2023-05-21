import emoji

salario = float(input('Insira seu salário: R$ '))

if salario <= 1250:
    ajuste = salario + (salario * 15 / 100)
    print(emoji.emojize(
        'O seu salário com ajuste é de {:.2f} ' .format(ajuste)))
if salario >= 1250:
    ajuste2 = salario + (salario * 10 / 100)
    print('O seu salário com ajuste é de {:.2f}' .format(ajuste2))
