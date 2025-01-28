from math import radians, sin, cos, tan
angulo = float(input('Digite um angulo para saber seu Seno, Cosseno e Tangente: '))
seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))
print(f'O Seno de {angulo} e {seno:.2f}\nO Cosseno de {angulo} e {cosseno:.2f}\ne a tangente de {angulo} e {tangente:.2f} ')