"""
Lista de listas e seus índices
"""
salas = [
    # 0        1
    ['Maria', 'Helena', ],  # 0
    # 0
    ['Elaine', ],  # 1
    # 0       1       2
    ['Luiz', 'João', 'Eduarda'],  # 2
]

# print(salas[1][0]) -> acessa o inídce 1 com o valor 0
# print(salas[0][1])
# print(salas[2][2])
# print(salas[2][3][1])
# print(salas[2][3][1]) -> acessar o valor 20

for sala in salas:  # para cada sala na lista salas
    print(f'A sala é {sala}')
    for aluno in sala:  # para cada aluno na sala
        print(aluno)
