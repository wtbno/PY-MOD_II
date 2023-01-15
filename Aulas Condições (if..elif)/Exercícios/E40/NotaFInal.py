prova1 = float(input('Insira a nota da sua primeira prova: '))
prova2 = float(input('Insira a nota da sua segunda prova: '))
media = (prova1 + prova2) / 2
if media >= 7.0:
    print('Você está aprovado!!! Sua média final é {}' .format(media))
elif media == 5.0 and 6.9:
    print('Você está de exame, sua média é {}!' .format(media))
else:
    print('Você foi reprovado neste semestre! Sua média final é {}' .format(media))
