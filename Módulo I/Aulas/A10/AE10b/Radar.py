velocidade = int(input('Velocidade capturada: '))
if velocidade >= 80:
    print('A velocidade atingida foi de {}km' .format(velocidade))
    print('Você ultrapassou o limite de velocidade, será multado em R$ 700.00')
else:
    print('Você está dentro dos limites de velocidade.')
