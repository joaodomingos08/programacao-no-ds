# 1. Lista de nomes de estudantes
estudantes = ["Carlos", "Ana", "Pedro", "Beatriz", "Mariana"]

# Use sort() para ordenar diretamente a lista original
estudantes.sort()
print("Estudantes ordenados:", estudantes)  # A lista original foi modificada

# 2. Lista de notas dos estudantes
notas = [88, 92, 78, 90, 85]

# Use sorted() para retornar uma nova lista ordenada
notas_ordenadas = sorted(notas)
print("Notas ordenadas:", notas_ordenadas)  # Uma nova lista ordenada foi criada

# Verifica lista original de notas
print("Lista original de notas:", notas)  # A lista original permanece inalterada
