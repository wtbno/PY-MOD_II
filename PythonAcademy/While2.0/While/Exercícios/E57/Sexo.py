sexo = str(input('Insira seu sexo [M/F]: ')).strip().upper()[0]
# Com ese zero pega somente a primeira leta 'fatiamento'
while sexo not in 'Mm/Ff':
    sexo = str(input('Dados inválidos, insira novamente seu sexo: ')
               ).strip().upper()[0]
print('Dados registrado com sucesso!!!'.format(sexo))
