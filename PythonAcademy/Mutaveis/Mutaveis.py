"""
Cuidados com dados mutáveis
= - copiado o valor (imutáveis)
= - aponta para o mesmo valor na memória (mutável)
"""
lista_a = ['Batata', 'Hamburger', 1, True, 1.2]
print(lista_a)  # =>
lista_b = lista_a.copy()

lista_a[0] = 'Suco'
print(lista_a)
print(lista_b)


"""
Vamos explicar o código passo a passo:

1. `lista_a = ['Batata', 'Hamburger', 1, True, 1.2]`: Aqui, criamos uma lista chamada `lista_a`, que contém diferentes tipos de elementos, como strings ('Batata' e 'Hamburger'), um inteiro (1), um booleano (True) e um número de ponto flutuante (1.2).

2. `print(lista_a)`: Imprimimos o conteúdo da lista `lista_a`. A saída será: `['Batata', 'Hamburger', 1, True, 1.2]`. 

3. `lista_b = lista_a.copy()`: Criamos uma cópia da lista `lista_a` e a atribuímos à variável `lista_b`. Isso é feito usando o método `copy()`, que cria uma cópia rasa (shallow copy) da lista, ou seja, os elementos em `lista_b` apontarão para os mesmos objetos da `lista_a`.

4. `lista_a[0] = 'Suco'`: Modificamos o primeiro elemento da lista `lista_a`, que inicialmente era 'Batata', para 'Suco'.

5. `print(lista_a)`: Imprimimos o conteúdo da lista `lista_a` após a modificação. A saída será: `['Suco', 'Hamburger', 1, True, 1.2]`. O primeiro elemento foi alterado para 'Suco'.

6. `print(lista_b)`: Imprimimos o conteúdo da lista `lista_b`. A saída será: `['Batata', 'Hamburger', 1, True, 1.2]`. Apesar de termos modificado `lista_a`, `lista_b` não foi afetada pela mudança, pois fizemos uma cópia rasa, ou seja, os elementos são compartilhados pelas duas listas.

Aqui está a explicação resumida:
- `lista_a` é uma lista com vários tipos de elementos.
- `lista_b` é uma cópia rasa de `lista_a`.
- Ao modificar `lista_a`, `lista_b` não é afetada porque as duas listas têm elementos compartilhados.
"""

"""
Em Python, o garbage collector trabalha automaticamente para identificar e recuperar memória que não é mais usada por objetos em execução no programa. Isso é especialmente útil para evitar que a memória seja esgotada e para garantir que recursos sejam liberados quando não estão mais sendo utilizados.

Embora seja possível modificar as configurações do garbage collector e forçar uma coleta de lixo manualmente usando o módulo gc (garbage collector), em geral, não é necessário interferir nesse processo, a menos que você esteja enfrentando problemas específicos de desempenho ou tenha requisitos muito específicos.
"""
