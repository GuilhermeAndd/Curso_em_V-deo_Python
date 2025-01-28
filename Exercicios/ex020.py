from random import shuffle

alunos = []

for i in range (4):
    nome = str(input(f'Digite o nome do {i+1}º aluno: '))
    alunos.append(nome)

shuffle(alunos)

print("A ordem de apresentação será: ")
for i, aluno in enumerate(alunos):
    print(f'{i+1}º - {aluno}')