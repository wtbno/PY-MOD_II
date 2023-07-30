import emoji
texto = 'Python'
novoTexto = ''

# for => iteração abaixo realizada pelo for

for letra in texto:
    novoTexto += (emoji.emojize(f':sparkles:{letra}'))
    print(letra)
    # Para cada letra na var texto, exiba a letra
print(novoTexto)

# Var letra é criada


# texto = 'Python'

# i = 0

# tamanhoString = len(texto)

# # while true é utilizado em repetições infinitas quando não se sabe a quantidade de repetições a serem realizadas

# while i < tamanhoString:
#     print(texto[i], i)

#     i += 1
# print('Fim da leitura do texto')
