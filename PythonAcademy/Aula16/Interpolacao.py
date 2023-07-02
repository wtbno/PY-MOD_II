# Semelhante ao .format que coloca o % antes do valor de acordo com a lista abaixo
# %s  || %d e %i || %f
"""
Interpolação básica de strings
s - string
d e i - int
f - float
x e X - Hexadecimal (ABCDEF0123456789)
x => x
X => X
"""
nome = 'Bruno'
idade = 32
variavel = '%s, o preço é R$%.2f' % (nome, idade)
print(variavel)
print('O hexadecimal de %d é %08X' % (1500, 1500))

nome = "Bruno"
idade = 32
mensagem = "Olá, {}! Você tem {} anos.".format(nome, idade)
print(mensagem)
