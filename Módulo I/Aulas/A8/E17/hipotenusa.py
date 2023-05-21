from math import hypot
ca = float(input('Insira o cateto adjacente: '))
co = float(input('Insira o cateto oposto: '))
hipotenusa = hypot(ca, co)
# catetos = (ca ** 2 + co ** 2) ** (1/2) metodo matematico
print('A hipotenusa vai medir {:.2f} ' .format(hipotenusa))
