soma = 0
cont = 0
for c in range(1, 8):
    num = int(input('Digite o {} valor: '.format(c)))
    if num % 2 == 0:
        # Se o número for par verifica se a divisão é igual a 0
        soma += num
        cont += 1
print('Você informou {} números pares e a soma foi {}' .format(cont, soma))
