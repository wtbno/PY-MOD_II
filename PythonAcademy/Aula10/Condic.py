# if => se
# elif => se não se
# else => se não => sempre a última opção; Contrário de if; Sempre a última condição
# Uma condição depende da outra
# Quando identificado uma cond verdadeira, ele salta para solução do cod
# Pass => passar um trecho de código

'''entrada = input('Deseja entrar ou sair do sistema? ')

if entrada == "entrada":
    print('Você entrou no sistema!')
elif entrada == "sair":
    print('Você saiu do sistema!')
else:
    print('Opção inválida.')
print('Fora dos blocos.')'''


condicao1 = False
condicao2 = False
condicao3 = True
condicao4 = False

if condicao1:
    print('Código para condição 1')
elif condicao2:
    print('Código para condição 2')
elif condicao3:
    print('Código para condição 3')
elif condicao4:
    print('Código para condição 4')
else:
    print('Nenhuma condição satisfeita.')
print('Fim!')
