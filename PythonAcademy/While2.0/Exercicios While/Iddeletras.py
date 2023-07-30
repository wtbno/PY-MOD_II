frase = "The Legend of Zelda: Ocarina of Time é um jogo eletrônico de ação e aventura."

i = 0
# Variável que é utilizada como um índice

qtdMaisApareceu = 0
letraMaisApareceu = ''

while i < len(frase):
    # Equando o índice for menor que o tamanho da var frase, retorne
    letra_atual = frase[i]
    # var letra que é igual a var frase utilizando a var índice

    if letra_atual == '':
        i += 1
        continue

    contador_letraAtual = frase.count(letra_atual)
    # está contando a var letra atual aparece
    print('Aqui inicia a contagem')

    if qtdMaisApareceu <= contador_letraAtual:
        # confere se a qtd que apareceu é menor que o contador atual
        qtdMaisApareceu = contador_letraAtual
        # aqui ocorre a modificação da ver qtdMaisApareceu de 0 para 3
        letraMaisApareceu = letra_atual
        # E a letraMaisApareceu passa a ser a letra_atual

    i += 1

    print(
        'A letra que apareceu mais vezes foi '
        f'"{letraMaisApareceu}" que apareceu '
        f'{qtdMaisApareceu}x'
    )
