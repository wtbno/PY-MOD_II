from time import sleep
# Sleep para ficar com efeito de loading
for contagem in range(10, 0, - 1):
    print('Contagem regressiva...')
    print(contagem)
    sleep(3)
print('Fim da contagem')
