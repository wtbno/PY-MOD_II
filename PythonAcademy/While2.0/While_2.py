qtd_linhas = 5
qtd_colunas = 5

linha = 1
while linha <= qtd_linhas:
    coluna = 1

    # criação de um while dentro de outro
    while coluna <= qtd_colunas:
        print(linha, coluna)
        coluna += 1
    linha += 1

print('Fim')
