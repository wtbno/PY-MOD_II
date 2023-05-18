numero = int(input('Insira um número: '))
tot = 0
for c in range(1, numero + 1):
    if numero % c == 0:
        print('\033[33m', end='')
        tot += 1
    else:
        print('\033[31m', end='')
    print('{} '.format(c), end='')
print('\nO número {} foi divisivel {} vezes' .format(numero, tot))
if tot == 2:
    print('Esse número é primo')
else:
    print('O número inserido não é primo')
# O end='' serve para ele não pular de linha
# '\033[33m' alterar cores do texto
