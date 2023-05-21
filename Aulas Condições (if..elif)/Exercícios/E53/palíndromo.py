texto = str(input('Insira seu texto: ')).strip().upper()
# strip remove espaços em branco antes e após; upper torna o texto maiúsculo
palavras = texto.split()
# separa o txt em palavras
junto = ''.join(palavras)
# remove os espaços
inverso = junto[::-1]
# for letra in range(len(junto) - 1, -1, -1):
#   inverso += junto[letra]
#   print(junto, inverso)
if inverso == junto:
    print('Essa palavra é um palíndromo')
else:
    print('Essa palavra não é um palíndromo')
