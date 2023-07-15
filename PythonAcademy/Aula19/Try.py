"""
Intro ao try/except
Try => para tentar executar um código
Except => ocorreu algum erro ao tentar executar o código
"""

# Fail fast => captura o erro rapidamente.
try:
    num = float(input('vou dobrar o número que você digitar: ').isdigit)
    multiplicado = (num * 2)
    print('O número digitado foi {:.2f} e o dobro dele é {:.2f}'.format(
        num, multiplicado))
except:
    print('Isso não é um número')
