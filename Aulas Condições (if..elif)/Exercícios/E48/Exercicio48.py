cont = 0
soma = 0
for numero in range(1, 5001, 2):
    if numero % 3 == 0:
        cont = cont + 1
        soma = soma + numero
print('A soma de todos {} os valores solicitados é {} '.format(cont, soma))
