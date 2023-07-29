"""
While (Enquanto) executa uma ação enquanto uma ação for verdadeira
Break dentro de um laço, procura o while mais próximo para sair deste laço
Sempre que o while ver o break, a condição é finalizada
Além do break, pode fazer com que a condição se torne falsa

= += -= *= 
/= => divisão 
//= => divisão inteira
 **= %= 
"""

contador = 0

while contador <= 100:
    # continue aqui pode gerar um laço infinito
    contador += 1
    # contador = contador + 1
    if contador >= 10 and contador <= 50:
        print('Não vou mostrar os números', contador)
    if contador == 87:
        print('Não vou exibir o 87')
    print(contador)

    if contador == 90:
        print('Será encerrado por um break')
        break


print('Fim')
