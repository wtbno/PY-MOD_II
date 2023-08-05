lista = ['Batata', 'Hamburger', 'Suco', 'Milk-Shake']
indices = range(len(lista))
# Na stg tem letra por letra, e na lista tem valor por valor
print(indices)

for indice in indices:
    print(indice, lista[indice], type(lista[indice]))
