import numpy as np
import matplotlib.pyplot as plt

# Parâmetros da simulação
anos = 10
simulacoes = 10  # Ajuste esse valor para melhor visualização
retorno_medio = 0.07
desvio_padrao = 0.20
valor_inicial = 10000  # Valor inicial da carteira

# Simulação de Monte Carlo
trajetorias = np.zeros((simulacoes, anos + 1))
trajetorias[:, 0] = valor_inicial

for i in range(simulacoes):
    for j in range(1, anos + 1):
        crescimento = np.random.normal(retorno_medio, desvio_padrao)
        trajetorias[i, j] = trajetorias[i, j - 1] * (1 + crescimento)

# Plotando o gráfico
plt.figure(figsize=(10, 6))
for i in range(simulacoes):
    plt.plot(range(anos + 1), trajet
