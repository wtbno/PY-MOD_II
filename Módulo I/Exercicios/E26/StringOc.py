frase = str(input('Insira uma frase: ')).upper().strip()
print('A letra A aparece {} vezes na sua frase' .format(frase.count('A')))
print('A primeira letra A aparece na posição {}' .format(frase.find('A')+1))
print('A última letra A apareceu na posição {}' .format(frase.rfind('A')+1))
