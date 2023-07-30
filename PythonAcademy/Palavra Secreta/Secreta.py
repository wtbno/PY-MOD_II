
palavraSecreta = 'tartaruga'
asteristico = ''
letrasCorretas = ''

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
        print('Você acertou!')
