from random import randint
import emoji
print(emoji.emojize('Vamos jogar jokenpo :video_game:'))

itens = ('Pedra', 'Papel', 'Tesoura')
maquina = randint(0, 2)  # randomização de um item
print('''Selecione uma das opções abaixo: 
[0] Pedra
[1] Papel
[2] Tesoura 
  ''')
jogador = int(input('Qual sua escolha? '))
print('O computador escolheu {}' .format(itens[maquina]))
print('A sua escolha foi {}' .format(itens[jogador]))
if maquina == 0:
    if jogador == 0:
        print('Empate')

    elif jogador == 1:
        print('Você venceu!')
    elif jogador == 2:
        print(emoji.emojize('O computador venceu! '))
    else:
        print('Jogada inválida')
elif maquina == 1:
    if jogador == 0:
        print(emoji.emojize('O computador venceu! '))
    elif jogador == 1:
        print('Empatou!')
    elif jogador == 2:
        print('Você venceu!')
    else:
        print('Jogada inválida')
elif maquina == 2:
    if jogador == 0:
        print('Você venceu!')
    elif jogador == 1:
        print(emoji.emojize('O computador venceu! '))
    elif jogador == 2:
        print('Empate!')
    else:
        print('Jogada inválida')
