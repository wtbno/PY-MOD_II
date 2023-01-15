peso = float(input('Insira o seu peso kg: '))
altura = float(input('Agora insira sua altura: '))
imc = peso / (altura*altura)
if imc < 18.5:
    print('Estado de magreza, procure um médico.')
elif 18.6 <= imc < 24.9:
    print('Seu IMC é {:.2f}}, e se encontra no valor normal! ' .format(imc))
elif 25 <= imc < 29.9:
    print('Seu IMC é {:.2f}, você pode estar em sobrepeso! ' .format(imc))
elif 30 <= imc < 34.9:
    print('Seu IMC é {:.2f}, risco de obsidade grau I! ' .format(imc))
elif 35 <= imc < 39.9:
    print('Seu IMC é {:.2f}, risco de obsidade grau II! ' .format(imc))
# else:
#     print('Seu IMC é {:.2f}, risco de obsidade grau III! ' .format(imc))
