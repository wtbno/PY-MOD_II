import emoji

nome = 'Bruno'

indice = 0
novo_nome = ''
while indice < len(nome):
    letra = nome[indice]
    novo_nome += emoji.emojize(f' {letra} :thumbs_up:')
    indice += 1

print(novo_nome)

# print('O nome digitado foi: ' + nome)
# print(tamanho)

# while nome == 'Bruno':

#     print(nome)

#     if nome == "Bruno":
#         print(emoji.emojize(f'Olá {nome} :thumbs_up:'))
#     if nome == 'Bruno':
#         print(emoji.emojize(
#             f'{nome[0]} :video_game: {nome[1]} :video_game: {nome[2]} :video_game: {nome[3]} :video_game: {nome[4]}'))
#     print(nome + " *" * 10)
#     break


"""
Essa diferença ocorre devido ao escopo das variáveis em Python.

No primeiro caso, a variável `letra` é declarada dentro do laço while. Quando uma variável é declarada dentro de um bloco de código, como o laço while, ela tem um escopo local, o que significa que só existe dentro desse bloco. Isso quer dizer que cada vez que o laço itera, uma nova variável `letra` é criada e só pode ser acessada dentro daquele loop específico. Isso é útil em situações em que você precisa de uma variável temporária para armazenar algum valor que será utilizado somente dentro do loop e não precisa ser acessado fora dele.

Por outro lado, a variável `novo_nome` é declarada fora do laço while. Isso significa que ela tem um escopo global, e pode ser acessada em todo o código após sua declaração. Dessa forma, quando o laço while itera, o valor da variável `novo_nome` é atualizado, pois ela foi declarada fora do loop e seu valor persiste em todas as iterações.

Em resumo, a variável `letra` precisa ser declarada dentro do laço while porque é uma variável temporária que só é relevante dentro de cada iteração do loop. Já a variável `novo_nome` é declarada fora do laço para que seu valor seja mantido e atualizado em cada iteração, e possa ser impressa corretamente no final do programa."""
