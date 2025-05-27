class Biblioteca:
    def __init__(self):
        self.livros = []  # Lista para armazenar os livros

    def adicionar_livro(self, titulo, autor, ano):
        livro = (titulo, autor, ano)  # Criando a tupla do livro
        self.livros.append(livro)  # Adicionando à lista

    def consultar_tupla(self, indice):
        if 0 <= indice < len(self.livros):
            return self.livros[indice]
        return "Livro não encontrado."

    def consultar_lista(self):
        return self.livros


# Criando a biblioteca
biblioteca = Biblioteca()

# Adicionando livros
biblioteca.adicionar_livro("Dom Quixote", "Miguel de Cervantes", 1605)
biblioteca.adicionar_livro("1984", "George Orwell", 1949)
biblioteca.adicionar_livro("O Pequeno Príncipe", "Antoine de Saint-Exupéry", 1943)

# Consultando um livro específico (por índice)
print("Consulta de um livro na tupla:", biblioteca.consultar_tupla(1))

# Consultando toda a coleção de livros
print("\nColeção completa de livros:")
for livro in biblioteca.consultar_lista():
    print(f"Título: {livro[0]}, Autor: {livro[1]}, Ano: {livro[2]}")
