# Operador lógico "not" que inverte a expressão, sendo assim:
# not True = False
# not false = True
# 0 => Avaliado como false

print(not True)  # False
print(not False)  # True

senha = input('Senha: ')

if not senha:
    print('Você não digitou a senha')
