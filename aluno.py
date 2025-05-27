# Criando uma lista para armazenar os alunos
alunos = []

# Solicitando nome e nota de três alunos
for i in range(3):
    nome = input(f"Informe o nome do aluno {i+1}: ")
    nota = float(input(f"Informe a nota do aluno {i+1}: "))
    alunos.append((nome, nota))

# Ordenando a lista pela nota, do maior para o menor
alunos.sort(key=lambda x: x[1], reverse=True)

# Exibindo os alunos ordenados
print("\nLista de alunos ordenada por nota:")
for aluno in alunos:
    print(f"Nome: {aluno[0]}, Nota: {aluno[1]}")
