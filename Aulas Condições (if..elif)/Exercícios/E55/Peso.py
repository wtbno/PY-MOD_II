
maior = 0
menor = 0
for pessoa in range(1, 5):
    peso = float(input('Peso da {}° pessoa: '.format(pessoa)))
    if pessoa == 1:
        # leitura da primeira pessoa ocorrência
        maior = pessoa
        menor = pessoa
    else:
        # se não for a primeira pessoa, verifico a ocorrência
        if peso > maior:
            # se o peso for maior que o maior registrado atualmente
            maior = peso
            # o último peso inserido torna-se o maior peso
        if peso < menor:
            meno = peso
print('O maior peso registrado foi {} '.format(maior))
