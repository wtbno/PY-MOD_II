precoCasa = float(input('Qual o valor da casa que você deseja comprar R$: '))
salario = float(input('Certo, agora me informe qual a sua renda R$: '))
pagamento = int(input('Insira em quantos anos você pretente pagar: '))
if precoCasa < (salario * 30 / 100):
    print('O valor da casa excede 30% da sua renda, sua proposta foi negada')
elif precoCasa / pagamento:
    print('Sua prestações serão pagas durante {} anos' .format(pagamento))
else:
    print('Até mais!')
