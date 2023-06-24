a = 'A'
b = 'B'
c = 99.167895
# Parâmetro nomeado => que se refere ao nome da variável
string = 'a={} b={} c={:.2f}'

# string = 'a={0} b={1} c={2:.2f}' => Essa forma atual como índice

formato = string.format(a, b, c)

# format por exemplo é um método

print(formato)

# Quando uma função está dentro de um obj, essa função passa a se chamar método
# objetos possuí métodos dentro dele, ou seja, um objeto tem ações que pode realizar alguma função, e essas ações são denominadas de métodos.
