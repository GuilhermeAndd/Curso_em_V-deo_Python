#Variaveis nota_1 e nota_2 recebem as notas do aluno 
nota_1 = float(input('Qual a sua primeira nota? '))
nota_2 = float(input('Qual a sua segunda nota? '))
#Variavel que calcula a média do aluno
media = (nota_1 + nota_2) / 2 
#Exibição da média do aluno
print(f'A média entre {nota_1:.1f} e {nota_2:.1f} total é {media:.1f}')