# Sempre vai ter que ter um IF
# Pode se usar ELIF quantas vezes for necessário
# ELSE só se utiliza uma vez.

nome = str(input('Insira seu nome: '))
if nome == 'Bruno':
    print('Que bonito nome, {}' .format(nome))
    print('Bom dia, {}!!!' .format(nome))

elif nome == 'Shen':
    print('Que nome diferente {}' .format(nome))
    print('Bom dia, {}!!!' .format(nome))
else:
    print('Olá {}' .format(nome))
    print('Tenha um bom dia {}' .format(nome))
