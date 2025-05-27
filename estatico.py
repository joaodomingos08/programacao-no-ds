class Calculadora:
    @staticmethod
    def soma(a, b):
        return a + b

    @staticmethod
    def subtracao(a, b):
        return a - b

# Exemplo de uso
print("Soma:", Calculadora.soma(10, 5))
print("Subtração:", Calculadora.subtracao(10, 5))
