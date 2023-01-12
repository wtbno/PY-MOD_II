
print('Bem vindo a copa EBJJ')
print('[=====]' * 10)
idade = int(input('Insira sua idade atual: '))
if idade == 0 and 9:
    print('Você tem {} anos, sua categoria é a mirim' .format(idade))
elif idade == 10 and 14:
    print('Você tem {} anos, sua categoria é a infantil' .format(idade))
elif idade == 15 and 19:
    print('Você tem {} anos, sua categoria é a junior' .format(idade))
elif idade == 20 and 25:
    print('Você tem {} anos, sua categoria é a adulto' .format(idade))
else:
    print('Você tem {} anos, sua categoria é a master' .format(idade))
