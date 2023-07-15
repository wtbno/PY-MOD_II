nome = str(input('Insira seu nome: '))
idade = int(input('Digite a sua idade: '))
if nome and idade:
    print('Seu nome é {}'.format(nome))
    print('Seu nome invertido é {}'.format(nome)[::-1])
    if '' in nome:
        print('Seu nome contém espaços')
    else:
        print('Seu nome não contem espaços')
    print(('Seu nome tem {} letras').format({len(nome)}))
    print('A primeira letra do seu nome é: {} '.format({nome[0]}))
    print('A última letra do seu nome é: {} '.format({nome[4]}))
else:
    print('Você não preencheu os campos acima.')
