""" while/else """
string = 'Valor qualquer'

i = 0
while i < len(string):
    letra = string[i]

    if letra == ' ':
        break

    print(letra)
    i += 1
else:
    print('Não encontrei um espaço na string.')
print('Fora do while.')


"""
Nesse código, o "i" é uma variável que serve como um índice para percorrer os caracteres da string 'Valor qualquer'. Vamos analisar o código passo a passo:

1. `string = 'Valor qualquer'`: Aqui, definimos uma string chamada 'Valor qualquer'.

2. `i = 0`: Inicializamos a variável "i" com o valor 0. Isso será usado para acessar os caracteres da string um por um, começando do primeiro caractere (índice 0).

3. `while i < len(string):`: Este é o início do loop "while". Enquanto o valor de "i" for menor que o comprimento da string (len(string)), o loop continuará executando.

4. `letra = string[i]`: Aqui, obtemos o caractere atual da string 'Valor qualquer' usando o valor do índice "i" e atribuímos à variável "letra".

5. `if letra == ' ':`: Verificamos se o caractere atual é um espaço em branco. Se for, o loop será interrompido com a instrução `break`.

6. `print(letra)`: Se o caractere não for um espaço em branco, imprimimos o caractere atual (letra).

7. `i += 1`: Incrementamos o valor de "i" em 1 para passar para o próximo caractere da string na próxima iteração do loop.

8. `else:`: Se o loop "while" for concluído sem encontrar um espaço em branco, o bloco "else" será executado.

9. `print('Não encontrei um espaço na string.')`: Neste bloco "else", exibimos a mensagem "Não encontrei um espaço na string.".

10. `print('Fora do while.')`: Finalmente, independente do resultado do loop, esta linha será executada, imprimindo "Fora do while.".

Resumidamente, o código percorre cada caractere da string 'Valor qualquer' e imprime cada caractere até que encontre um espaço em branco. Se o loop terminar sem encontrar um espaço em branco, ele imprimirá a mensagem "Não encontrei um espaço na string." e, em seguida, imprimirá "Fora do while.".
"""
