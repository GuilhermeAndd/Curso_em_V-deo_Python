import random

def sortear_aluno():
  """Sorteia um aluno dentre os nomes fornecidos."""

  alunos = []
  while True:
    nome = input("Digite o nome do aluno (ou 'sair' para finalizar): ")
    if nome.lower() == 'sair':
      break
    alunos.append(nome)

  if not alunos:
    print("Nenhum aluno foi adicionado.")
    return

  aluno_sorteado = random.choice(alunos)
  print(f"O aluno sorteado para apagar o quadro é: {aluno_sorteado}")

# Chamando a função para iniciar o sorteio
sortear_aluno()