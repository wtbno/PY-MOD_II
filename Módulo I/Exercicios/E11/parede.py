altura = float(input('Insira a altura da parede em metros: '))
largura = float(input('Insira a largura da parede em metros: '))
area = altura * largura
tinta = area/2
print('Sua parede tem a dimensão de  {} x {} e sua area  é de {} m² ' .format(altura, largura,
                                                                              area))
print('Para pintar essa parede será necessário {}l de tinta' .format(tinta))
