import os
palavraSecreta = 'tartaruga'

letrasCorretas = ''
asteristico = ''
tentativas = 0

while True:

    letraDigitada = input(
        'Tente advinhar a palavra secreta, selecione uma letra: ')
    tentativas += 1
    if len(letraDigitada) > 1:
        print('Selecione apenas uma letra')
        continue

    if letraDigitada in palavraSecreta:
        letrasCorretas += letraDigitada

    palavraFormada = ''
    for letraSecreta in palavraSecreta:
        if letraSecreta in letrasCorretas:
            palavraFormada += letraSecreta
        else:
            palavraFormada += '*'
    print('Palavra formada ', palavraFormada)

    if palavraFormada == palavraSecreta:
        os.system('clear')
        # Limpa o terminal
        print('Você acertou!')
        print('A palavra era:', palavraFormada)
        print('Tentativas:', tentativas)

        palavraSecreta = 'tartaruga'
        letrasCorretas = ''
