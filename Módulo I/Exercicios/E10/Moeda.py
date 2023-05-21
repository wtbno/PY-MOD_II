from tkinter import *
real = float(input('Quanto dinheiro você possui na carteira? R$ '))
dolares = real / 5.31
euro = real / 5.63
yene = real / 25.34
print('Com R$ {:.2f} você pode comprar U$ {:.2f}' .format(
    real, dolares))
print('Com R$ {:.2f} você pode comprar € {:.2f}' .format(real, euro))
print('Com R$ {:.2f} você pode comprar ¥ {:.2f}' .format(real, yene))


janela = Tk()


janela.mainloop
