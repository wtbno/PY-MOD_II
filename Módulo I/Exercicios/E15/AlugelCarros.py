locDias = int(input('Por quantos dias o veículo ficou alugado? '))
kmRodados = float(input('Quantos KM o veículo percorreu? '))
calcDiaria = locDias * 60
calcKm = kmRodados * 0.15
valorTotal = calcDiaria + calcKm
print('O valor da locação é de R$ {:.2f} e o valor correspondente aos kilometros radodos é de R$ {:.2f}, totalizando R$ {:.2f}' .format(
    calcDiaria, calcKm, valorTotal))
