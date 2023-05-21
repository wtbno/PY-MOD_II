ladoA = int(input('Primeiro valor: '))
ladob = int(input('Segundo valor: '))
ladoc = int(input('Terceiro valor: '))
if ladoA < ladob + ladoc and ladob < ladoA + ladoc and ladoc < ladoA + ladob:
    print('Os segmentos acima podem formar um triangulo')
else:
    print('Os segmentos informados não formam um triangulo')
