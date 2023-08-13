import os


lista = []


while True:
    print('Selecione uma opção: ')
    opcao = input('[i]nserir, [a]pagar ou [l]istar: ')

    if opcao == 'i':
        os.system('clear')  # Limpa o terminal
        item = input('Insira o item desejado: ')  # Inserir novo item
        lista.append(item)  # Associa o novo item capturado no input a lista

    elif opcao == 'a':
        for indice, item in enumerate(lista):
            print(indice, item)
        indice_str = input('Selecione o item que deseja excluir: ')
        try:
            indice = int(indice_str)
            del lista[indice]
            # Tratando erros
        except ValueError:
            print('Selecione um número inteiro.')
        except IndexError:
            print('Índice inexistente')

    elif opcao == 'l':
        if len(lista) == 0:
            print('Lista vazia')
        for indice, item in enumerate(lista):
            print(indice, item)
    else:
        print('Insira uma opção válida')
