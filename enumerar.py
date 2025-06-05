# Solicita ao usuário que forneça uma lista de nomes
nomes = input("Digite os nomes separados por vírgula: ").split(',')

# Itera sobre a lista usando enumerate e exibe os índices e nomes
for indice, nome in enumerate(nomes):
    print(f"{indice}: {nome.strip()}")
