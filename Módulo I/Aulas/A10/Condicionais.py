#If = V = Simples
#Else = F = Composta
glicemia = float(input('Qual o valor da sua glicemia? '))
if glicemia >= 120.0:
    print('Sua glicemia está acima do normal, procure um médico!')

elif glicemia <= 70:
    print('Sua glicemia está baixa, procure ajuda médica!!!')

else:
    print('Sua glicemia está normal')
