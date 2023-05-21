distancia = int(input('Insira a distância aproximada da sua viagem: '))
ViagPadrao = distancia * 0.50
ViagLonga = distancia * 0.45
if distancia >= 200:
    print('O valor da sua viagem é de R$ {:.2f}' .format(ViagPadrao))
else:
    print('O valor da sua viagem é de R$ {:.2f}' .format(ViagLonga))
