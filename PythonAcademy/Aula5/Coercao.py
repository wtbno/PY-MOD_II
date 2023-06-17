# conversão de tipos, coerção
# type convertion, typecasting, coercion
# é o ato de converter um tipo em outro
#  tipos imutáveis e primitivos:
# str, int, float, bool
print(int('1'), type(int('1')))
print(type(float('1') + 1))
print(bool(' '))
# Converter int para str
print(str(11) + 'b')
# Coerção:
print((int('1') + 1))

# Uma str vazia é considerada false
# A execução da função é realizada de dentro para fora
# Tipagem dinâmica e forte => print('1' + 1) não é possível realizar essa operação, não sendo possível juntar uma str e um int, a menos que tenha uma  conversão => print(type(int('1') + 1))
