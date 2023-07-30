"""
Iterável -> str, range, etc (__iter__)
Iterador -> quem sabe entregar um valor por vez
next -> me entregue o próximo valor
iter -> me entregue seu iterador

Qundo solicitado o FOR é iniciado o método __iter__ que solicita um outro obj que irá
executar a função de iterar na str ou no número
Quando utilizamos um método estamos solicitando uma ação
Um método utiliza parênteses ()
"""
# for letra in texto
texto = iter('Bruno')  # iterável

# iteratador = iter(texto)  # iterator

# while True:
#     try:
#         letra = next(iteratador)
#         print(letra)
#     except StopIteration:
#         break

for letra in texto:
    print(letra)
