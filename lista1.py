# Solicita ao usuário um número inteiro positivo n
n = int(input("Digite um número inteiro positivo: "))

# Cria uma lista para armazenar os n números inteiros
lista = []

# Lê n números inteiros e adiciona à lista
for _ in range(n):
    num = int(input("Digite um número inteiro: "))
    lista.append(num)

# Solicita ao usuário um número inteiro x
x = int(input("Digite um número inteiro para verificar se está na lista: "))

# Verifica se x pertence à lista e exibe o resultado
if x in lista:
    print("O número", x, "pertence à lista.")
else:
    print("O número", x, "não pertence à lista.")
