"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0

Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7
"""

cpf_enviado = '674.184.860-65' \
    .replace('.', '')\
    .replace('-', '')\
    .replace(' ', '')

nove_digitos = cpf_enviado[:9]
"""
Nesta linha, você está criando uma nova variável chamada nove_digitos. Você está usando a técnica de "slicing" para pegar os primeiros 9 caracteres da string cpf e atribuí-los a essa variável. Portanto, nove_digitos agora contém os primeiros nove dígitos do CPF, que são '005988001'.

Em Python, o termo "slicing" refere-se à técnica de extrair partes específicas de uma sequência, como uma string, lista ou tupla, criando uma nova sequência contendo os elementos desejados. O operador de slice em Python é o [:]. Ele permite que você especifique um intervalo de índices para extrair um subconjunto dos elementos da sequência original.
"""


print(nove_digitos)

# => realização da multiplicação regressiva

cont_regressivo1 = 10


resultadod1 = 0

for digito1 in nove_digitos:
    resultadod1 += int(digito1) * cont_regressivo1
    cont_regressivo1 -= 1

digito1 = (resultadod1 * 10) % 11
digito1 = digito1 if digito1 <= 9 else 0
print(digito1)


dez_digitos = nove_digitos + str(digito1)

regressivo2 = 10
resultadod2 = 1
for digito2 in nove_digitos:
    resultadod2 += int(digito2) * regressivo2
    regressivo2 -= 1
digito2 = (resultadod2 * 10) % 11
digito2 = digito2 if digito2 <= 9 else 0
print(digito2)
print(cpf_enviado)

cpf_calculado = f'{nove_digitos}{digito1}{digito2}'

if cpf_enviado == cpf_calculado:
    print(f'{cpf_enviado} é valido')
else:
    print('CPF inválido')
