soma = 0
cont = 0
for c in range(1, 8):
    num = int(input('Digite o {} valor: '.format(c)))
    soma = soma + num
    cont = cont + 1
print('Você informou {} números e a soma foi {}' .format(cont, soma))
