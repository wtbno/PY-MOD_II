numeros = range(10)
# Seleciona números em um range

print(numeros[5])


# No For não é necessário o uso de índice, porque já é identificado autom.
# For é um iteravél finito


for numero in numeros:
    print(numero)


"""
O iterador é criado a partir da sequência fornecida após a palavra-chave "in". Isso pode ser uma lista, uma string, uma tupla ou qualquer outro objeto iterável.

O iterador avança para o primeiro elemento da sequência.

O bloco de código dentro do "for" é executado para o elemento atual.

O iterador avança para o próximo elemento da sequência.

Os passos 3 e 4 são repetidos até que todos os elementos da sequência tenham sido percorridos.

O loop "for" termina quando não há mais elementos a serem iterados.
    """
