somaIdade = 0
mediaIdade = 0
maiorIdadeHomem = 0
nomeVelho = ''
totMulher = 0
nomeMulher = ''
for pessoa in range(1, 4):
    print('→ {}ª Pessoa'.format(pessoa))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    somaIdade += idade
    if pessoa == 1 and sexo in 'Mm':
        maiorIdadeHomem = idade
        nomeVelho = nome
    if sexo in 'Mm' and idade > maiorIdadeHomem:
        maiorIdadeHomem = idade
        nomeVelho = nome
    if sexo in 'Ff' and idade < 20:
        totMulher += 1

mediaIdade = somaIdade / 3
print('A média de idade do grupo é {} anos: '.format(mediaIdade))
print('O homen mais velho tem {} anos e se chama {}' .format(
    maiorIdadeHomem, nomeVelho))
print('Ao todo são {} com mais de 20 anos' .format(totMulher))
