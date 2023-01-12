from datetime import date
atual = date.today().year
nasc = int(input('Insira o ano de nascimento: '))
idade = atual - nasc
if idade == 18:
    print('Você nasceu em {} e sua idade atual é {} em {}' .format(
        nasc, idade, atual))
    print('Compareça a junta militar imediatamente!')
elif idade > 18:
    print('Sua idade atual é {} anos' .format(idade))
    print('Se não se alistou, compareça a junta militar')
elif idade < 18:
    print('Você não está apto para se alistar')
