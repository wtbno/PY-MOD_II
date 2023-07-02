entrada = input("Selecione E para entrar ou S para sair:").upper()
senha = input('Senha: ')

teste = "123456"

if entrada == 'E' and senha == teste:
    print("Bem vindo(a)!")
else:
    print("Sair")
# utilização do AND funciona quando há mais de uma condição e ambas são verdadeiras
