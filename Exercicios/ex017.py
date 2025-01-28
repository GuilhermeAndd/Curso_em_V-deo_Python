from math import hypot
# Entrada dos dados
cat_op = float(input('Digite o comprimento do cateto oposto: '))
cat_adj = float(input('Digite o comprimento do cateto adjacente: '))
# Cálculo da hipotenusa utilizando o teorema de Pitágoras
hipotenusa = hypot(cat_op,cat_adj)
# Saída do resultado
print(f'A hipotenusa mede o total de: {hipotenusa:.2f}')
