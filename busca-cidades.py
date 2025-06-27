# Lista pré-definida com 8 cidades
cidades = ["Curitiba", "São Paulo", "Rio de Janeiro", "Belo Horizonte", "Porto Alegre", "Fortaleza", "Manaus", "Recife"]

# Solicita ao usuário uma letra ou sequência de caracteres
busca = input("Digite uma letra ou sequência de caracteres para buscar nas cidades: ").lower()

# Filtra as cidades que contêm a sequência buscada (ignorando maiúsculas/minúsculas)
resultado = [cidade for cidade in cidades if busca in cidade.lower()]

# Exibe o resultado da busca
if resultado:
    print("Cidades encontradas:")
    for cidade in resultado:
        print("-", cidade)
else:
    print("Nenhuma cidade corresponde à busca.")
