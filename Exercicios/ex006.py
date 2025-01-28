#Importação da biblioteca nativa math para calculos matemáticos
from math import sqrt
#Input de valores do número para realizar a operação proposta
n1 = int(input('Digite um número qualquer para saber qual o seu dobro, triplo e a sua raiz quadrada: '))
#Exibição do dobro, triplo e raiz quadrada do valor digitado
print(f'O dobro do seu número é: {n1*2}\nO triplo é: {n1*3}\nE a sua raiz quadrada é: {sqrt(n1)}')