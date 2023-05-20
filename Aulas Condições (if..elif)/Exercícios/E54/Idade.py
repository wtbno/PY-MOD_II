from datetime import date
dataAtual = date.today().year
totalMaior = 0
totalMenor = 0
for pessoa in range(1, 5):
    dataNasc = int(input('Em qual ano  {}° pessoa nasceu? '.format(pessoa)))
    idade = dataAtual - dataNasc
    if idade >= 18:
        totalMaior += 1

    else:
        totalMenor += 1
print('Ao todo tivemos {} pessoas maior de idade' .format(totalMaior))
print('E também tivemos {} pessoas menor de idade' .format(totalMenor))


# print('A idade atual é {}' .format(idadeAtual))
