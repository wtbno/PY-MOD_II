
import random

# Encerra o código
nove_digitos = ''

for i in range(9):
    nove_digitos += str(random.randint(0, 1))

print(nove_digitos)


cont_regressivo1 = 10


resultadod1 = 0

for digito1 in nove_digitos:
    resultadod1 += int(digito1) * cont_regressivo1
    cont_regressivo1 -= 1

digito1 = (resultadod1 * 10) % 11
digito1 = digito1 if digito1 <= 9 else 0
# print(digito1)


dez_digitos = nove_digitos + str(digito1)

regressivo2 = 10
resultadod2 = 1
for digito2 in nove_digitos:
    resultadod2 += int(digito2) * regressivo2
    regressivo2 -= 1
digito2 = (resultadod2 * 10) % 11
digito2 = digito2 if digito2 <= 9 else 0
# print(digito2)
# print(cpf_enviado)

cpf_calculado = f'{nove_digitos}{digito1}{digito2}'

'''if cpf_enviado == cpf_calculado:
    print(f'{cpf_enviado} é valido')
else:
    print('CPF inválido')
'''
