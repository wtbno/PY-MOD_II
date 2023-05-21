salario = float(input('Qual o seu salário bruto R$: '))
porcent = float(input('Qual a porcentagem de aumento: '))
ajuste = salario + (salario * porcent / 100)
print('O seu salário era de R$ {:.2f} e com o ajuste de 15% passou para R$ {:.2f}' .format(
    salario, ajuste))
