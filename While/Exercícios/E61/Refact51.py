primeiro = int(input('Insira o primeiro valor: '))
razao = int(input('Insira o valor da razao: '))
termo = primeiro
cont = 1
while cont <= 1000:
    print('{}'.format(termo),  end='→ ')
    termo += razao
    razao += 1
    cont += 1
print('Fim')
