prova_1 = int(input('Insira a nota da sua primeira prova: '))
prova_2 = int(input('Insira a nota da sua segunda prova: '))
mediaFinal = (prova_1 + prova_2) / 2

if mediaFinal >= 7:
    print('Você foi aprovado, matéria finalizada')
elif mediaFinal <= 6:
    print('Você foi reprovado, entre em contato com a secretaria')
# Aplicar a ordem de precedencia
print('A sua média final é {:.1f}' .format(
    mediaFinal))
