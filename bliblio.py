class Livro:
    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    def __str__(self):
        return f"Livro: {self.titulo}\nAutor: {self.autor}\nNúmero de páginas: {self.paginas}"

# Solicitando informações ao usuário
titulo = input("Digite o título do livro: ")
autor = input("Digite o autor do livro: ")
paginas = input("Digite o número de páginas do livro: ")

# Criando uma instância da classe Livro
livro = Livro(titulo, autor, paginas)

# Exibindo a descrição do livro
print("\nDescrição do livro:")
print(livro)
